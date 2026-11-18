"""Dependency-light, proposal-only structural/environmental monitoring rules.

This module consumes already-processed, timestamped measurements. It does not
read sensors, process raw accelerometer streams or images, diagnose structures,
predict earthquakes, or control hardware. Thresholds are site/asset configured.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Optional, Tuple


class Severity(str, Enum):
    NORMAL = "normal"
    CAUTION = "caution"
    WARNING = "warning"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Measurement:
    value: float
    unit: str
    observed_at: datetime
    source_id: str
    calibrated: bool = False
    quality_ok: bool = True


@dataclass(frozen=True)
class CrackChange:
    """Calibrated crack-width observation; image-derived values need human review."""
    width_mm: float
    delta_mm: float
    observed_at: datetime
    source_id: str
    calibrated_scale: bool
    human_reviewed: bool = False
    quality_ok: bool = True


@dataclass(frozen=True)
class MonitoringLimits:
    # Vibration acceleration RMS in m/s^2; define per installed asset.
    vibration_caution_m_s2: Optional[float] = None
    vibration_warning_m_s2: Optional[float] = None
    vibration_critical_m_s2: Optional[float] = None
    # Relative humidity in %RH; site-specific indoor monitoring limits.
    humidity_caution_pct: Optional[float] = None
    humidity_warning_pct: Optional[float] = None
    # Crack width and growth limits in mm; require qualified review.
    crack_width_warning_mm: Optional[float] = None
    crack_growth_warning_mm: Optional[float] = None
    max_age_seconds: int = 300


@dataclass(frozen=True)
class Alert:
    domain: str
    severity: Severity
    message: str
    source_id: Optional[str] = None


def _fresh(timestamp: datetime, now: datetime, max_age: int) -> bool:
    if timestamp.tzinfo is None or now.tzinfo is None:
        return False
    age = (now - timestamp).total_seconds()
    return 0 <= age <= max_age


def evaluate_measurement(
    domain: str,
    measurement: Optional[Measurement],
    now: datetime,
    limits: MonitoringLimits,
) -> Alert:
    if measurement is None:
        return Alert(domain, Severity.UNKNOWN, "Measurement missing.")
    if not _fresh(measurement.observed_at, now, limits.max_age_seconds):
        return Alert(domain, Severity.UNKNOWN, "Measurement is stale or timestamp is invalid.", measurement.source_id)
    if not measurement.quality_ok or not measurement.calibrated:
        return Alert(domain, Severity.UNKNOWN, "Sensor quality or calibration is not verified.", measurement.source_id)

    value = measurement.value
    if domain == "vibration":
        if measurement.unit != "m/s^2 RMS" or value < 0:
            return Alert(domain, Severity.UNKNOWN, "Expected non-negative m/s^2 RMS vibration measurement.", measurement.source_id)
        bands = (
            (limits.vibration_critical_m_s2, Severity.CRITICAL),
            (limits.vibration_warning_m_s2, Severity.WARNING),
            (limits.vibration_caution_m_s2, Severity.CAUTION),
        )
    elif domain == "humidity":
        if measurement.unit != "%RH" or not 0 <= value <= 100:
            return Alert(domain, Severity.UNKNOWN, "Expected relative humidity in %RH from 0 to 100.", measurement.source_id)
        bands = (
            (limits.humidity_warning_pct, Severity.WARNING),
            (limits.humidity_caution_pct, Severity.CAUTION),
        )
    else:
        return Alert(domain, Severity.UNKNOWN, "Unsupported measurement domain.", measurement.source_id)

    for threshold, severity in bands:
        if threshold is not None and value >= threshold:
            return Alert(domain, severity, f"{domain} measurement reached a configured site-specific limit.", measurement.source_id)
    return Alert(domain, Severity.NORMAL, f"{domain} measurement is within configured limits.", measurement.source_id)


def evaluate_crack_change(
    observation: Optional[CrackChange],
    now: datetime,
    limits: MonitoringLimits,
) -> Alert:
    if observation is None:
        return Alert("crack", Severity.UNKNOWN, "Crack observation missing.")
    if not _fresh(observation.observed_at, now, limits.max_age_seconds):
        return Alert("crack", Severity.UNKNOWN, "Crack observation is stale or timestamp is invalid.", observation.source_id)
    if not observation.quality_ok or not observation.calibrated_scale or not observation.human_reviewed:
        return Alert("crack", Severity.UNKNOWN, "Crack measurement needs image/scale quality checks and human review.", observation.source_id)
    if observation.width_mm < 0:
        return Alert("crack", Severity.UNKNOWN, "Crack width cannot be negative.", observation.source_id)

    if limits.crack_width_warning_mm is not None and observation.width_mm >= limits.crack_width_warning_mm:
        return Alert("crack", Severity.WARNING, "Crack width reached a configured review limit.", observation.source_id)
    if limits.crack_growth_warning_mm is not None and observation.delta_mm >= limits.crack_growth_warning_mm:
        return Alert("crack", Severity.WARNING, "Crack growth reached a configured review limit.", observation.source_id)
    return Alert("crack", Severity.NORMAL, "Crack measurement is within configured review limits.", observation.source_id)


def assess_monitoring(
    vibration: Optional[Measurement],
    humidity: Optional[Measurement],
    crack: Optional[CrackChange],
    now: datetime,
    limits: MonitoringLimits,
) -> Tuple[Alert, ...]:
    """Return advisory indicators only; UNKNOWN is not equivalent to NORMAL."""
    return (
        evaluate_measurement("vibration", vibration, now, limits),
        evaluate_measurement("humidity", humidity, now, limits),
        evaluate_crack_change(crack, now, limits),
    )
