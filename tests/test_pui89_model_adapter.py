import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from pui89_model_adapter import run_mock_adapter

def sample_request():
    return {
        "project_id": "coconut_harvest", "request_id": "mock-001",
        "timestamp": "2026-11-01T00:00:00Z", "task": "check adapter envelope",
        "evidence": [{
            "source_id": "fixture-1", "source_type": "test_fixture",
            "source_ref": "synthetic://fixture-1", "timestamp": "2026-11-01T00:00:00Z",
            "evidence_kind": "synthetic", "modality": "simulation", "lineage": ["unit-test"]
        }],
        "mock_observations": [{"kind": "fixture_ping", "value": "present"}]
    }

class ModelAdapterTests(unittest.TestCase):
    def test_valid_request_is_mock_only(self):
        r = run_mock_adapter(sample_request(), now="2026-11-01T00:00:01Z")
        self.assertEqual(r["status"], "MOCK_OBSERVATION_ONLY")
        self.assertFalse(r["adapter"]["inference_performed"])
        self.assertEqual(r["adapter"]["mode"], "MOCK")
        self.assertFalse(r["physical_actuation_permitted"])
        self.assertEqual(r["proposed_actions"], [])
    def test_missing_provenance_is_rejected(self):
        q = sample_request(); q["evidence"][0].pop("source_ref")
        r = run_mock_adapter(q, now="2026-11-01T00:00:01Z")
        self.assertEqual(r["status"], "REJECTED")
        self.assertEqual(r["policy_result"]["action"], "SAFE_HOLD")
    def test_non_synthetic_evidence_is_rejected(self):
        q = sample_request(); q["evidence"][0]["evidence_kind"] = "observed"
        self.assertEqual(run_mock_adapter(q, now="2026-11-01T00:00:01Z")["status"], "REJECTED")
    def test_stale_evidence_requests_more(self):
        r = run_mock_adapter(sample_request(), now="2026-11-01T02:00:00Z", max_evidence_age_seconds=60)
        self.assertEqual(r["policy_result"]["action"], "REQUEST_EVIDENCE")
    def test_future_evidence_requests_more(self):
        r = run_mock_adapter(sample_request(), now="2026-10-31T23:59:00Z", max_evidence_age_seconds=60)
        self.assertEqual(r["policy_result"]["action"], "REQUEST_EVIDENCE")
    def test_unknown_project_is_rejected(self):
        q = sample_request(); q["project_id"] = "unknown_project"
        self.assertEqual(run_mock_adapter(q, now="2026-11-01T00:00:01Z")["status"], "REJECTED")
    def test_hardware_command_is_rejected(self):
        q = sample_request(); q["robot_command"] = {"move": "forward"}
        r = run_mock_adapter(q, now="2026-11-01T00:00:01Z")
        self.assertEqual(r["status"], "REJECTED")
        self.assertFalse(r["policy_result"]["physical_actuation_permitted"])
    def test_invalid_timestamp_is_rejected(self):
        q = sample_request(); q["timestamp"] = "not-a-time"
        self.assertEqual(run_mock_adapter(q, now="2026-11-01T00:00:01Z")["status"], "REJECTED")

if __name__ == "__main__":
    unittest.main()
