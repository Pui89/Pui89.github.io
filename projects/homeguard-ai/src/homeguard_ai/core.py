"""Transparent, deterministic evaluation of sensor observations.

This module intentionally uses baseline statistics and explicit quality gates.
It is not a trained AI model and does not diagnose a physical hazard.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from math import isfinite, sqrt
from typing import Any, Iterable


VALID_QUALITY = {"VALID", "DEGRADED", "INVALID", "MISSING"}
VALID_CALIBRATION = {"CURRENT", "EXPIRED", "UNKNOWN", "NOT_APPLICABLE"}


@dataclass(frozen=True)
class SensorObservation:
    observation_id: str
    sensor_id: str
    domain: str
    metric: str
    value: float
    unit: str
    timestamp: str
    location: str
    quality: str = "VALID"
    calibration: str = "UNKNOWN"
    uncertainty: float | None = None

    def validate(self) -> None:
        if not self.observation_id or not self.sensor_id or not self.metric:
            raise ValueError("observation_id, sensor_id and metric are required")
        if not isfinite(self.value):
            raise ValueError("observation value must be finite")
        if self.quality not in VALID_QUALITY:
            raise ValueError(f"unsupported quality status: {self.quality}")
        if self.calibration not in VALID_CALIBRATION:
            raise ValueError(f"unsupported calibration status: {self.calibration}")
        parsed = datetime.fromisoformat(self.timestamp.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("timestamp must include a timezone")
        if self.uncertainty is not None and (
            not isfinite(self.uncertainty) or self.uncertainty < 0
        ):
            raise ValueError("uncertainty must be a finite non-negative value")


@dataclass(frozen=True)
class Baseline:
    metric: str
    mean: float
    standard_deviation: float
    unit: str
    sample_count: int
    period_start: str
    period_end: str

    def validate(self) -> None:
        if not isfinite(self.mean) or not isfinite(self.standard_deviation):
            raise ValueError("baseline statistics must be finite")
        if self.standard_deviation < 0 or self.sample_count < 1:
            raise ValueError("baseline spread and sample count are invalid")
        for stamp in (self.period_start, self.period_end):
            parsed = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                raise ValueError("baseline timestamps must include a timezone")


def evaluate_observations(
    observations: Iterable[SensorObservation],
    baselines: dict[str, Baseline],
    *,
    threshold_z: float = 3.0,
) -> dict[str, Any]:
    """Return an auditable report; never convert missing/poor evidence to normal."""
    if not isfinite(threshold_z) or threshold_z <= 0:
        raise ValueError("threshold_z must be positive and finite")

    findings: list[dict[str, Any]] = []
    accepted = 0
    excluded = 0

    for observation in observations:
        observation.validate()
        baseline = baselines.get(observation.metric)
        if baseline is None:
            excluded += 1
            findings.append({
                "finding_id": f"HG-{observation.observation_id}",
                "status": "INSUFFICIENT_BASELINE",
                "severity": "UNASSESSED",
                "summary": "No matching baseline is available.",
                "evidence_ids": [observation.observation_id],
                "limitations": ["A missing baseline is not evidence of normality."],
            })
            continue

        baseline.validate()
        if observation.quality != "VALID":
            excluded += 1
            findings.append({
                "finding_id": f"HG-{observation.observation_id}",
                "status": "DATA_QUALITY_REVIEW",
                "severity": "UNASSESSED",
                "summary": "Observation excluded because its quality is not VALID.",
                "evidence_ids": [observation.observation_id],
                "limitations": [f"Input quality is {observation.quality}."],
            })
            continue
        if observation.calibration not in {"CURRENT", "NOT_APPLICABLE"}:
            excluded += 1
            findings.append({
                "finding_id": f"HG-{observation.observation_id}",
                "status": "CALIBRATION_REVIEW",
                "severity": "UNASSESSED",
                "summary": "Observation excluded because calibration is not confirmed current.",
                "evidence_ids": [observation.observation_id],
                "limitations": [f"Calibration status is {observation.calibration}."],
            })
            continue
        if observation.unit != baseline.unit:
            excluded += 1
            findings.append({
                "finding_id": f"HG-{observation.observation_id}",
                "status": "UNIT_MISMATCH",
                "severity": "UNASSESSED",
                "summary": "Observation and baseline units do not match.",
                "evidence_ids": [observation.observation_id],
                "limitations": ["No automatic unit conversion is performed."],
            })
            continue

        accepted += 1
        delta = observation.value - baseline.mean
        if baseline.standard_deviation == 0:
            z_score = 0.0 if delta == 0 else float("inf")
        else:
            z_score = delta / baseline.standard_deviation

        if abs(z_score) >= threshold_z:
            findings.append({
                "finding_id": f"HG-{observation.observation_id}",
                "status": "DEVIATION_DETECTED",
                "severity": "REVIEW_REQUIRED",
                "summary": f"{observation.metric} deviates from its configured baseline.",
                "evidence_ids": [observation.observation_id],
                "measurement": {
                    "value": observation.value,
                    "unit": observation.unit,
                    "baseline_mean": baseline.mean,
                    "baseline_standard_deviation": baseline.standard_deviation,
                    "z_score": z_score if isfinite(z_score) else None,
                    "direction": "ABOVE" if delta > 0 else "BELOW",
                },
                "limitations": [
                    "A statistical deviation is not proof of a physical hazard or its cause.",
                    "Thresholds require domain-specific calibration and validation.",
                ],
            })

    return {
        "schema_version": "0.1.0",
        "system": {
            "name": "HOMEGUARD AI",
            "software_version": "0.1.0",
            "execution_mode": "DETERMINISTIC_BASELINE_DEMONSTRATOR",
            "model_status": "NO_TRAINED_MODEL",
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "assessment": {
            "status": ("INSUFFICIENT_EVIDENCE" if accepted == 0 else "REVIEW_REQUIRED" if findings else "NO_DEVIATION_IN_EVALUATED_INPUTS"),
            "observations_received": accepted + excluded,
            "observations_evaluated": accepted,
            "observations_excluded": excluded,
            "findings_count": len(findings),
            "threshold_z": threshold_z,
        },
        "findings": findings,
        "safety_notice": (
            "Decision support only. Not a certified alarm, diagnosis, engineering "
            "assessment or authorization for automatic control."
        ),
    }


def observation_to_dict(observation: SensorObservation) -> dict[str, Any]:
    """Stable serialization helper for future adapters."""
    return asdict(observation)
