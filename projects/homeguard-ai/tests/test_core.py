from datetime import datetime, timezone

import pytest

from homeguard_ai.core import Baseline, SensorObservation, evaluate_observations
from homeguard_ai.simulator import build_demo


def baseline():
    stamp = datetime.now(timezone.utc).isoformat()
    return Baseline("temperature_c", 25.0, 1.0, "degC", 30, stamp, stamp)


def observation(**overrides):
    values = dict(
        observation_id="OBS-1", sensor_id="S-1", domain="THERMAL",
        metric="temperature_c", value=31.0, unit="degC",
        timestamp=datetime.now(timezone.utc).isoformat(),
        location="SIM/FLOOR-1", quality="VALID", calibration="CURRENT",
    )
    values.update(overrides)
    return SensorObservation(**values)


def test_detects_baseline_deviation_with_evidence_link():
    report = evaluate_observations([observation()], {"temperature_c": baseline()})
    assert report["assessment"]["findings_count"] == 1
    finding = report["findings"][0]
    assert finding["status"] == "DEVIATION_DETECTED"
    assert finding["evidence_ids"] == ["OBS-1"]
    assert "not proof" in finding["limitations"][0]


def test_invalid_quality_is_not_treated_as_normal():
    report = evaluate_observations(
        [observation(quality="INVALID")], {"temperature_c": baseline()}
    )
    assert report["assessment"]["observations_excluded"] == 1
    assert report["findings"][0]["status"] == "DATA_QUALITY_REVIEW"


def test_unknown_calibration_is_excluded():
    report = evaluate_observations(
        [observation(calibration="UNKNOWN")], {"temperature_c": baseline()}
    )
    assert report["findings"][0]["status"] == "CALIBRATION_REVIEW"


def test_unit_mismatch_is_excluded():
    report = evaluate_observations(
        [observation(unit="F")], {"temperature_c": baseline()}
    )
    assert report["findings"][0]["status"] == "UNIT_MISMATCH"


def test_missing_baseline_is_explicit_not_normal():
    report = evaluate_observations([observation()], {})
    assert report["findings"][0]["status"] == "INSUFFICIENT_BASELINE"


def test_rejects_timezone_naive_timestamp():
    with pytest.raises(ValueError):
        observation(timestamp="2026-01-01T12:00:00").validate()


def test_simulator_is_repeatable_except_report_timestamp():
    first = build_demo(89)
    second = build_demo(89)
    assert first["findings"] == second["findings"]
    assert first["system"]["data_status"] == "SIMULATION_ONLY"
    assert first["assessment"]["floors_simulated"] == [
        "FLOOR-01", "FLOOR-02", "FLOOR-03"
    ]


def test_no_automatic_actuation_or_diagnostic_claims():
    report = build_demo()
    assert "automatic control" in report["safety_notice"]
    assert report["system"]["model_status"] == "NO_TRAINED_MODEL"
