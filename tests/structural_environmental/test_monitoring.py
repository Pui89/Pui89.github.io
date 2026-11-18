import unittest
from datetime import datetime, timezone, timedelta

from shared_ai_core.structural_environmental.monitoring import (
    CrackChange,
    Measurement,
    MonitoringLimits,
    Severity,
    assess_monitoring,
    evaluate_crack_change,
    evaluate_measurement,
)


class StructuralEnvironmentalMonitoringTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 11, 18, 12, 0, tzinfo=timezone.utc)
        self.limits = MonitoringLimits(
            vibration_caution_m_s2=0.5,
            vibration_warning_m_s2=1.0,
            vibration_critical_m_s2=2.0,
            humidity_caution_pct=65.0,
            humidity_warning_pct=80.0,
            crack_width_warning_mm=2.0,
            crack_growth_warning_mm=0.3,
            max_age_seconds=300,
        )

    def measurement(self, value, unit, **kwargs):
        return Measurement(
            value=value, unit=unit, observed_at=kwargs.get("observed_at", self.now),
            source_id="sensor-1", calibrated=kwargs.get("calibrated", True),
            quality_ok=kwargs.get("quality_ok", True),
        )

    def test_vibration_critical_uses_configured_limit(self):
        alert = evaluate_measurement("vibration", self.measurement(2.2, "m/s^2 RMS"), self.now, self.limits)
        self.assertEqual(alert.severity, Severity.CRITICAL)

    def test_humidity_warning_uses_configured_limit(self):
        alert = evaluate_measurement("humidity", self.measurement(82, "%RH"), self.now, self.limits)
        self.assertEqual(alert.severity, Severity.WARNING)

    def test_stale_measurement_is_unknown(self):
        old = self.measurement(0.1, "m/s^2 RMS", observed_at=self.now - timedelta(minutes=10))
        alert = evaluate_measurement("vibration", old, self.now, self.limits)
        self.assertEqual(alert.severity, Severity.UNKNOWN)

    def test_uncalibrated_sensor_is_unknown(self):
        item = self.measurement(0.1, "m/s^2 RMS", calibrated=False)
        self.assertEqual(evaluate_measurement("vibration", item, self.now, self.limits).severity, Severity.UNKNOWN)

    def test_wrong_units_are_unknown(self):
        item = self.measurement(0.1, "g")
        self.assertEqual(evaluate_measurement("vibration", item, self.now, self.limits).severity, Severity.UNKNOWN)

    def test_unreviewed_crack_image_is_unknown(self):
        crack = CrackChange(0.5, 0.1, self.now, "camera-1", True, False, True)
        self.assertEqual(evaluate_crack_change(crack, self.now, self.limits).severity, Severity.UNKNOWN)

    def test_crack_growth_triggers_warning_after_review(self):
        crack = CrackChange(0.8, 0.4, self.now, "gauge-1", True, True, True)
        self.assertEqual(evaluate_crack_change(crack, self.now, self.limits).severity, Severity.WARNING)

    def test_missing_channels_remain_unknown(self):
        alerts = assess_monitoring(None, None, None, self.now, self.limits)
        self.assertTrue(all(a.severity == Severity.UNKNOWN for a in alerts))

    def test_no_limits_produce_unknown_not_false_reassurance(self):
        no_limits = MonitoringLimits()
        item = self.measurement(0.01, "m/s^2 RMS")
        self.assertEqual(evaluate_measurement("vibration", item, self.now, no_limits).severity, Severity.UNKNOWN)
        crack = CrackChange(0.1, 0.0, self.now, "gauge-1", True, True, True)
        self.assertEqual(evaluate_crack_change(crack, self.now, no_limits).severity, Severity.UNKNOWN)


if __name__ == "__main__":
    unittest.main()
