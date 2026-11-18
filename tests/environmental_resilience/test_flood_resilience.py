import unittest

from flood_resilience import (
    MeasurementKind, Observation, ProductEnvelope, Quality, Response, RiskLevel,
    assess_flood_risk, synthetic_depth_observation,
)


class FloodResilienceTests(unittest.TestCase):
    def setUp(self):
        self.envelope = ProductEnvelope(
            product_id="test-fixture",
            max_test_depth_cm=20.0,
            caution_depth_cm=10.0,
            max_observation_age_s=2.0,
            max_electronics_temp_c=70.0,
            max_battery_temp_c=55.0,
        )

    def test_depth_below_caution_is_monitor_only(self):
        result = assess_flood_risk([synthetic_depth_observation(5)], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.NORMAL)
        self.assertEqual(result.response, Response.MONITOR)

    def test_depth_above_caution_warns(self):
        result = assess_flood_risk([synthetic_depth_observation(15)], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.CAUTION)
        self.assertEqual(result.response, Response.WARN_OPERATOR)

    def test_20cm_is_within_configured_test_envelope_not_validation(self):
        result = assess_flood_risk([synthetic_depth_observation(20)], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.CAUTION)
        self.assertIn("within_configured_software_envelope_only", result.reasons)

    def test_depth_above_envelope_restricts(self):
        result = assess_flood_risk([synthetic_depth_observation(20.1)], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.RESTRICT)
        self.assertEqual(result.response, Response.RESTRICT_OPERATION)

    def test_missing_depth_fails_closed(self):
        result = assess_flood_risk([], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.UNKNOWN)
        self.assertEqual(result.response, Response.RESTRICT_OPERATION)

    def test_stale_depth_fails_closed(self):
        obs = synthetic_depth_observation(5, now_s=90)
        result = assess_flood_risk([obs], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.UNKNOWN)

    def test_invalid_quality_fails_closed(self):
        obs = Observation("depth", MeasurementKind.WATER_DEPTH, 5, "cm", 100,
                          Quality.UNCALIBRATED)
        result = assess_flood_risk([obs], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.UNKNOWN)

    def test_disagreeing_depth_sensors_fail_closed(self):
        a = synthetic_depth_observation(5)
        b = Observation("depth-2", MeasurementKind.WATER_DEPTH, 12, "cm", 100)
        result = assess_flood_risk([a, b], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.UNKNOWN)
        self.assertIn("water_depth_sensors_disagree", result.reasons)

    def test_leak_requests_safe_stop(self):
        items = [
            synthetic_depth_observation(5),
            Observation("leak", MeasurementKind.LEAK_DETECTED, 1, "bool", 100),
        ]
        result = assess_flood_risk(items, self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.CRITICAL)
        self.assertEqual(result.response, Response.REQUEST_SAFE_STOP)

    def test_emergency_stop_requests_safe_stop(self):
        items = [
            synthetic_depth_observation(5),
            Observation("estop", MeasurementKind.EMERGENCY_STOP, 1, "bool", 100),
        ]
        result = assess_flood_risk(items, self.envelope, 100)
        self.assertEqual(result.response, Response.REQUEST_SAFE_STOP)

    def test_battery_over_temperature_requests_safe_stop(self):
        items = [
            synthetic_depth_observation(5),
            Observation("battery-temp", MeasurementKind.BATTERY_TEMPERATURE, 55, "C", 100),
        ]
        result = assess_flood_risk(items, self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.CRITICAL)

    def test_unconfigured_temperature_limit_requires_review(self):
        envelope = ProductEnvelope("no-temp-limit", max_test_depth_cm=20)
        items = [
            synthetic_depth_observation(5),
            Observation("battery-temp", MeasurementKind.BATTERY_TEMPERATURE, 30, "C", 100),
        ]
        result = assess_flood_risk(items, envelope, 100)
        self.assertEqual(result.response, Response.HUMAN_REVIEW_REQUIRED)

    def test_sensor_health_failure_restricts(self):
        items = [
            synthetic_depth_observation(5),
            Observation("sensor-health", MeasurementKind.SENSOR_HEALTH, 0, "bool", 100),
        ]
        result = assess_flood_risk(items, self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.UNKNOWN)
        self.assertEqual(result.response, Response.RESTRICT_OPERATION)

    def test_unit_mismatch_fails_closed(self):
        obs = Observation("depth", MeasurementKind.WATER_DEPTH, 0.05, "m", 100)
        result = assess_flood_risk([obs], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.UNKNOWN)

    def test_future_timestamp_fails_closed(self):
        obs = synthetic_depth_observation(5, now_s=101)
        result = assess_flood_risk([obs], self.envelope, 100)
        self.assertEqual(result.risk, RiskLevel.UNKNOWN)


if __name__ == "__main__":
    unittest.main()
