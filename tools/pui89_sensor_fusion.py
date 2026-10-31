"""Deterministic, fail-closed sensor evidence assessment (simulation only)."""
from __future__ import annotations
from datetime import datetime, timezone
from typing import Any

VALID_QUALITY = {"GOOD", "DEGRADED", "INVALID"}

def _parse_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("observed_at must include a timezone")
    return parsed.astimezone(timezone.utc)

def assess_observations(observations: list[dict[str, Any]], *,
                        required_modalities: list[str], now: str,
                        max_age_seconds: int) -> dict[str, Any]:
    """Check evidence coverage, freshness, quality and disagreement.

    Values are compared as supplied. No voting, averaging or inference occurs.
    """
    if max_age_seconds < 0:
        raise ValueError("max_age_seconds must be non-negative")
    current = _parse_time(now)
    if not required_modalities:
        raise ValueError("required_modalities must not be empty")
    accepted, rejected, seen_ids = [], [], set()
    for index, item in enumerate(observations):
        required = ("observation_id", "attribute", "value", "observed_at",
                    "source_id", "modality", "quality")
        if not isinstance(item, dict) or any(k not in item for k in required):
            rejected.append({"index": str(index), "reason": "missing_required_field"})
            continue
        oid = str(item["observation_id"])
        if not oid or oid in seen_ids:
            rejected.append({"index": str(index), "reason": "empty_or_duplicate_observation_id"})
            continue
        seen_ids.add(oid)
        if item["quality"] not in VALID_QUALITY:
            rejected.append({"index": str(index), "reason": "invalid_quality"})
            continue
        try:
            observed = _parse_time(str(item["observed_at"]))
        except (TypeError, ValueError):
            rejected.append({"index": str(index), "reason": "invalid_timestamp"})
            continue
        age = (current - observed).total_seconds()
        if age < 0:
            rejected.append({"index": str(index), "reason": "future_observation"})
            continue
        if age > max_age_seconds:
            rejected.append({"index": str(index), "reason": "stale_observation"})
            continue
        if item["quality"] != "GOOD":
            rejected.append({"index": str(index), "reason": "quality_not_good"})
            continue
        accepted.append(dict(item))
    present = {str(x["modality"]) for x in accepted}
    missing = sorted(set(required_modalities) - present)
    conflicts = []
    attributes = sorted({str(x["attribute"]) for x in accepted})
    for attribute in attributes:
        values = {}
        for item in accepted:
            if str(item["attribute"]) == attribute:
                modality = str(item["modality"])
                if modality in values and values[modality] != item["value"]:
                    conflicts.append({"attribute": attribute, "modality": modality,
                                      "reason": "intra_modality_disagreement"})
                values[modality] = item["value"]
        if len({str(v) for v in values.values()}) > 1:
            conflicts.append({"attribute": attribute,
                              "reason": "cross_modality_disagreement"})
    if any(x["reason"] in {"future_observation", "stale_observation"} for x in rejected):
        decision = "SAFE_HOLD"
    elif conflicts:
        decision = "REQUEST_HUMAN_REVIEW"
    elif missing:
        decision = "REQUEST_EVIDENCE"
    elif rejected:
        decision = "SAFE_HOLD"
    else:
        decision = "CONTINUE"
    return {
        "decision": decision,
        "accepted_observation_count": len(accepted),
        "rejected_observations": rejected,
        "missing_modalities": missing,
        "conflicts": conflicts,
        "accepted_observations": accepted,
        "simulation_only": True,
        "physical_actuation_permitted": False,
        "probabilities_calibrated": False,
    }
