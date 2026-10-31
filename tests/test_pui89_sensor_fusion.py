import unittest
from datetime import datetime, timedelta

from tools.pui89_sensor_fusion import assess_observations

NOW = "2026-10-31T12:00:00Z"

def obs(oid, modality, value="clear", age=10, quality="GOOD", attribute="hazard"):
    now = datetime.fromisoformat(NOW.replace("Z", "+00:00"))
    return {"observation_id": oid, "attribute": attribute, "value": value,
            "observed_at": (now - timedelta(seconds=age)).isoformat(),
            "source_id": "test-source", "modality": modality, "quality": quality}

class SensorFusionTests(unittest.TestCase):
    def assess(self, items, required=("camera", "lidar")):
        return assess_observations(items, required_modalities=list(required),
                                   now=NOW, max_age_seconds=60)

    def test_complete_agreement(self):
        self.assertEqual(self.assess([obs("1", "camera"), obs("2", "lidar")])["decision"], "CONTINUE")

    def test_missing_modality(self):
        self.assertEqual(self.assess([obs("1", "camera")])["decision"], "REQUEST_EVIDENCE")

    def test_conflict_escalates(self):
        result = self.assess([obs("1", "camera"), obs("2", "lidar", "blocked")])
        self.assertEqual(result["decision"], "REQUEST_HUMAN_REVIEW")
        self.assertEqual(len(result["conflicts"]), 1)

    def test_stale_evidence_holds(self):
        self.assertEqual(self.assess([obs("1", "camera", age=120), obs("2", "lidar")])["decision"], "SAFE_HOLD")

    def test_degraded_quality_holds(self):
        self.assertEqual(self.assess([obs("1", "camera", quality="DEGRADED"), obs("2", "lidar")])["decision"], "SAFE_HOLD")

    def test_duplicate_ids_hold(self):
        self.assertEqual(self.assess([obs("same", "camera"), obs("same", "lidar")])["decision"], "SAFE_HOLD")

    def test_naive_timestamp_rejected(self):
        item = obs("1", "camera")
        item["observed_at"] = "2026-10-31T11:59:00"
        result = self.assess([item, obs("2", "lidar")])
        self.assertEqual(result["rejected_observations"][0]["reason"], "invalid_timestamp")

    def test_no_actuation_or_calibration_claim(self):
        result = self.assess([obs("1", "camera"), obs("2", "lidar")])
        self.assertFalse(result["physical_actuation_permitted"])
        self.assertFalse(result["probabilities_calibrated"])

if __name__ == "__main__":
    unittest.main()
