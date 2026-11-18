"""Dependency-light flood resilience reference logic.

Software-only reference implementation. No sensor drivers, network access,
actuator interfaces, vehicle controls, battery controls, or hardware commands.
All values supplied to this module are observations, not proof of physical safety.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import math
from typing import Iterable, Optional


class Quality(str, Enum):
    VALID = "valid"
    INVALID = "invalid"
    UNCALIBRATED = "uncalibrated"
    CONFLICTING = "conflicting"


class MeasurementKind(str, Enum):
    WATER_DEPTH = "water_depth"
    LEAK_DETECTED = "leak_detected"
    ELECTRONICS_TEMPERATURE = "electronics_temperature"
    BATTERY_TEMPERATURE = "battery_temperature"
    EMERGENCY_STOP = "emergency_stop"
    SENSOR_HEALTH = "sensor_health"


class RiskLevel(str, Enum):
    UNKNOWN = "unknown"
    NORMAL = "normal"
    CAUTION = "caution"
    RESTRICT = "restrict"
    CRITICAL = "critical"


class Response(str, Enum):
    MONITOR = "monitor"
    WARN_OPERATOR = "warn_operator"
    RESTRICT_OPERATION = "restrict_operation"
    REQUEST_SAFE_STOP = "request_safe_stop"
    HUMAN_REVIEW_REQUIRED = "human_review_required"


@dataclass(frozen=True)
class Observation:
    sensor_id: str
    kind: MeasurementKind
    value: float
    unit: str
    timestamp_s: float
    quality: Quality = Quality.VALID
    calibration_id: Optional[str] = None


@dataclass(frozen=True)
class ProductEnvelope:
    """Product-specific software envelope; not a certified safe operating limit."""
    product_id: str
    max_test_depth_cm: float = 0.0
    caution_depth_cm: float = 0.0
    max_observation_age_s: float = 2.0
    max_electronics_temp_c: Optional[float] = None
    max_battery_temp_c: Optional[float] = None


@dataclass(frozen=True)
class Assessment:
    risk: RiskLevel
    response: Response
    reasons: tuple[str, ...]
    evidence_status: str = "synthetic_or_unverified_observations"


def _fresh_valid(
    observation: Observation,
    now_s: float,
    max_age_s: float,
    expected_unit: str,
) -> bool:
    if observation.quality is not Quality.VALID:
        return False
    if not observation.sensor_id.strip():
        return False
    if not math.isfinite(observation.value) or not math.isfinite(observation.timestamp_s):
        return False
    age = now_s - observation.timestamp_s
    if age < 0 or age > max_age_s:
        return False
    return observation.unit == expected_unit


def assess_flood_risk(
    observations: Iterable[Observation],
    envelope: ProductEnvelope,
    now_s: float,
) -> Assessment:
    """Conservative, advisory-only assessment; never issues actuator commands."""
    items = tuple(observations)
    reasons: list[str] = []

    if not envelope.product_id.strip() or envelope.max_test_depth_cm < 0:
        return Assessment(RiskLevel.UNKNOWN, Response.HUMAN_REVIEW_REQUIRED,
                          ("invalid_product_envelope",))

    depths = [o for o in items if o.kind is MeasurementKind.WATER_DEPTH]
    if len(depths) < 1:
        return Assessment(RiskLevel.UNKNOWN, Response.RESTRICT_OPERATION,
                          ("water_depth_missing",))

    valid_depths = [
        o for o in depths
        if _fresh_valid(o, now_s, envelope.max_observation_age_s, "cm")
        and o.value >= 0
    ]
    if len(valid_depths) != len(depths) or not valid_depths:
        return Assessment(RiskLevel.UNKNOWN, Response.RESTRICT_OPERATION,
                          ("water_depth_invalid_stale_or_untrusted",))

    values = [o.value for o in valid_depths]
    if max(values) - min(values) > 5.0:
        return Assessment(RiskLevel.UNKNOWN, Response.RESTRICT_OPERATION,
                          ("water_depth_sensors_disagree",))
    depth_cm = max(values)

    critical_kinds = {
        MeasurementKind.LEAK_DETECTED: ("bool", "internal_leak_detected"),
        MeasurementKind.EMERGENCY_STOP: ("bool", "emergency_stop_asserted"),
    }
    for kind, (unit, reason) in critical_kinds.items():
        for obs in (o for o in items if o.kind is kind):
            if not _fresh_valid(obs, now_s, envelope.max_observation_age_s, unit):
                return Assessment(RiskLevel.UNKNOWN, Response.REQUEST_SAFE_STOP,
                                  (f"{kind.value}_signal_untrusted",))
            if obs.value not in (0.0, 1.0):
                return Assessment(RiskLevel.UNKNOWN, Response.REQUEST_SAFE_STOP,
                                  (f"{kind.value}_signal_invalid",))
            if obs.value == 1.0:
                return Assessment(RiskLevel.CRITICAL, Response.REQUEST_SAFE_STOP,
                                  (reason,))

    for kind, maximum, label in (
        (MeasurementKind.ELECTRONICS_TEMPERATURE,
         envelope.max_electronics_temp_c, "electronics_over_temperature"),
        (MeasurementKind.BATTERY_TEMPERATURE,
         envelope.max_battery_temp_c, "battery_over_temperature"),
    ):
        relevant = [o for o in items if o.kind is kind]
        if maximum is None and relevant:
            return Assessment(RiskLevel.UNKNOWN, Response.HUMAN_REVIEW_REQUIRED,
                              (f"{kind.value}_limit_not_configured",))
        for obs in relevant:
            if not _fresh_valid(obs, now_s, envelope.max_observation_age_s, "C"):
                return Assessment(RiskLevel.UNKNOWN, Response.REQUEST_SAFE_STOP,
                                  (f"{kind.value}_untrusted",))
            if obs.value >= maximum:
                return Assessment(RiskLevel.CRITICAL, Response.REQUEST_SAFE_STOP,
                                  (label,))

    health = [o for o in items if o.kind is MeasurementKind.SENSOR_HEALTH]
    for obs in health:
        if not _fresh_valid(obs, now_s, envelope.max_observation_age_s, "bool") or obs.value != 1.0:
            return Assessment(RiskLevel.UNKNOWN, Response.RESTRICT_OPERATION,
                              ("sensor_health_not_confirmed",))

    if depth_cm > envelope.max_test_depth_cm:
        reasons.append("depth_exceeds_configured_test_envelope")
        return Assessment(RiskLevel.RESTRICT, Response.RESTRICT_OPERATION, tuple(reasons))
    if depth_cm > envelope.caution_depth_cm:
        reasons.append("depth_exceeds_caution_threshold")
        return Assessment(RiskLevel.CAUTION, Response.WARN_OPERATOR, tuple(reasons))

    reasons.append("within_configured_software_envelope_only")
    return Assessment(RiskLevel.NORMAL, Response.MONITOR, tuple(reasons))


def synthetic_depth_observation(depth_cm: float, now_s: float = 100.0) -> Observation:
    """Clearly synthetic fixture helper for tests and examples only."""
    return Observation(
        sensor_id="synthetic-depth-fixture",
        kind=MeasurementKind.WATER_DEPTH,
        value=depth_cm,
        unit="cm",
        timestamp_s=now_s,
        quality=Quality.VALID,
        calibration_id="synthetic-not-calibrated",
    )
