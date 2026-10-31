"""Dependency-free PUI89 world-state record validation and summarisation."""
from __future__ import annotations
from datetime import datetime, timezone
from typing import Any, Iterable

VALID_MODALITIES = {"rgb", "depth", "lidar", "thermal", "audio", "chemical_sensor", "environmental", "operator", "simulation", "other"}
VALID_EVIDENCE = {"observed", "inferred", "synthetic", "derived", "unknown"}
VALID_QUALITY = {"valid", "degraded", "stale", "missing", "conflicting", "unknown"}

def _parse_timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip(): return None
    try: parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError: return None
    if parsed.tzinfo is None or parsed.utcoffset() is None: return None
    return parsed.astimezone(timezone.utc)

def validate_observation(record: Any) -> list[str]:
    if not isinstance(record, dict): return ["observation must be an object"]
    errors = []
    required = ("observation_id", "entity_id", "attribute", "value", "observed_at", "source_id", "modality", "evidence_kind", "quality")
    for key in required:
        if key not in record: errors.append(f"missing required field: {key}")
    for key in ("observation_id", "entity_id", "attribute", "source_id"):
        if key in record and (not isinstance(record[key], str) or not record[key].strip()): errors.append(f"{key} must be a non-empty string")
    if "observed_at" in record and _parse_timestamp(record["observed_at"]) is None: errors.append("observed_at must be an ISO-8601 timestamp with timezone")
    if "modality" in record and record["modality"] not in VALID_MODALITIES: errors.append("unsupported modality")
    if "evidence_kind" in record and record["evidence_kind"] not in VALID_EVIDENCE: errors.append("unsupported evidence_kind")
    if "quality" in record and record["quality"] not in VALID_QUALITY: errors.append("unsupported quality")
    if "confidence" in record:
        value = record["confidence"]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 1 or value != value or value in (float("inf"), float("-inf")):
            errors.append("confidence must be a finite number between 0 and 1")
    if "limitations" in record and not (isinstance(record["limitations"], list) and all(isinstance(x, str) for x in record["limitations"])):
        errors.append("limitations must be a list of strings")
    return errors

def summarise_world_state(observations: Iterable[dict[str, Any]], *, now: str, max_age_seconds: float) -> dict[str, Any]:
    current = _parse_timestamp(now)
    if current is None: raise ValueError("now must be an ISO-8601 timestamp with timezone")
    if isinstance(max_age_seconds, bool) or not isinstance(max_age_seconds, (int, float)) or max_age_seconds < 0:
        raise ValueError("max_age_seconds must be a non-negative number")
    groups = {}
    rejected = []
    for item in observations:
        errors = validate_observation(item)
        if errors: rejected.append({"observation": item, "errors": errors}); continue
        groups.setdefault((item["entity_id"], item["attribute"]), []).append(item)
    states = []
    for (entity_id, attribute), records in sorted(groups.items()):
        records = sorted(records, key=lambda x: (x["observed_at"], x["observation_id"]))
        stale_ids = []
        values = []
        for item in records:
            stamp = _parse_timestamp(item["observed_at"])
            age = (current - stamp).total_seconds()
            if age > max_age_seconds or age < 0 or item["quality"] == "stale": stale_ids.append(item["observation_id"])
            if item["quality"] not in {"missing", "unknown"} and item["evidence_kind"] != "unknown" and item["value"] not in values:
                values.append(item["value"])
        conflict = len(values) > 1 or any(x["quality"] == "conflicting" for x in records)
        states.append({
            "entity_id": entity_id, "attribute": attribute,
            "observation_ids": [x["observation_id"] for x in records],
            "distinct_values": values, "conflict": conflict,
            "stale_observation_ids": stale_ids,
            "status": "CONFLICT" if conflict else ("STALE" if stale_ids else "OBSERVED"),
            "resolution": None,
            "action": "REQUEST_HUMAN_REVIEW" if conflict else ("SAFE_HOLD" if stale_ids else "NO_ACTION")
        })
    return {
        "schema_version": "1.0", "simulation_only": True,
        "physical_actuation_permitted": False, "states": states,
        "rejected_observations": rejected,
        "limitations": [
            "Deterministic record organiser, not a perception model.",
            "Conflicting values are preserved, not averaged or automatically resolved.",
            "Freshness uses caller-supplied timestamps and age limit.",
            "Confidence is not calibrated; no physical action is authorised."
        ]
    }
