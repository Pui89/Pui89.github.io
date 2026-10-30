import unittest
from pui89_adaptive_orchestrator import evaluate

NOW = "2026-10-31T00:00:00+00:00"

def evidence(sid="e1", timestamp=NOW):
    return {"source_id": sid, "source_type": "fixture", "source_ref": "synthetic",
            "timestamp": timestamp, "evidence_kind": "synthetic",
            "modality": "test", "lineage": ["fixture"]}

def message(agent="a", value="ready", sid="e1"):
    return {"agent_id": agent, "task_id": "t1", "timestamp": NOW,
            "source_ids": [sid], "observations": [],
            "claims": [{"claim_id": agent + "-c", "claim_key": "state",
                        "value": value, "evidence_ids": [sid]}],
            "confidence": 0.5, "uncertainty": ["synthetic"],
            "limitations": ["not validated"], "status": "PROPOSED",
            "requested_action": "CONTINUE"}

class Tests(unittest.TestCase):
    def test_continue_is_simulation_only(self):
        result = evaluate([message()], {"e1": evidence()}, now=NOW,
                          required_claim_keys=("state",))
        self.assertEqual(result["action"], "CONTINUE")
        self.assertTrue(result["simulation_only"])
        self.assertFalse(result["physical_actuation_permitted"])

    def test_stop_precedence(self):
        result = evaluate([{"status": "STOPPED", "requested_action": "STOP"}],
                          {}, now=NOW)
        self.assertEqual(result["action"], "STOP")

    def test_invalid_provenance_holds(self):
        result = evaluate([message(sid="unknown")], {"e1": evidence()}, now=NOW)
        self.assertEqual(result["action"], "SAFE_HOLD")

    def test_missing_required_claim_requests_evidence(self):
        result = evaluate([message()], {"e1": evidence()}, now=NOW,
                          required_claim_keys=("state", "position"))
        self.assertEqual(result["action"], "REQUEST_EVIDENCE")

    def test_stale_evidence_requests_evidence(self):
        old = evidence(timestamp="2026-10-30T00:00:00+00:00")
        result = evaluate([message()], {"e1": old}, now=NOW)
        self.assertEqual(result["action"], "REQUEST_EVIDENCE")

    def test_disagreement_escalates_without_resolution(self):
        result = evaluate([message(), message(agent="b", value="blocked")],
                          {"e1": evidence()}, now=NOW)
        self.assertEqual(result["action"], "REQUEST_SPECIALIST_VERIFICATION")
        self.assertIsNone(result["disagreements"][0]["resolution"])

    def test_human_review_escalates(self):
        msg = message()
        msg["status"] = "HUMAN_REVIEW"
        result = evaluate([msg], {"e1": evidence()}, now=NOW)
        self.assertEqual(result["action"], "REQUEST_HUMAN_REVIEW")

    def test_future_evidence_is_rejected(self):
        future = evidence(timestamp="2026-11-01T00:00:00+00:00")
        result = evaluate([message()], {"e1": future}, now=NOW)
        self.assertEqual(result["action"], "REQUEST_EVIDENCE")

    def test_invalid_threshold_rejected(self):
        with self.assertRaises(ValueError):
            evaluate([], {}, now=NOW, min_evidence_per_claim=0)

if __name__ == "__main__":
    unittest.main()
