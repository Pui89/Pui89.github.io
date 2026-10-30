import unittest
from tools.pui89_long_horizon import evaluate_sequence, build_report

class LongHorizonTests(unittest.TestCase):
    def test_missing_evidence_enters_safe_hold(self):
        r = evaluate_sequence([{"confidence": .9}, {"confidence": .9, "faults": ["missing_evidence"]}])
        self.assertEqual(r["final_state"], "SAFE_HOLD")

    def test_conflict_requests_human_review(self):
        r = evaluate_sequence([{"confidence": .95, "faults": ["conflicting_evidence"]}])
        self.assertEqual(r["final_state"], "REQUEST_HUMAN_REVIEW")

    def test_uncertainty_carries_forward(self):
        r = evaluate_sequence([{"confidence": .9}, {"confidence": .4}, {"confidence": 1.0}])
        self.assertEqual(r["trace"][-1]["uncertainty"], .6)
        self.assertTrue(r["uncertainty_increased"])

    def test_hold_requires_explicit_recovery(self):
        r = evaluate_sequence([
            {"faults": ["stale_sensor"]},
            {"confidence": 1.0},
            {"confidence": 1.0, "recovery": True, "fresh_evidence": True,
             "consistent_evidence": True, "operator_approved": True}
        ])
        self.assertEqual(r["trace"][1]["state"], "SAFE_HOLD")
        self.assertEqual(r["final_state"], "CONTINUE")

    def test_stop_is_latched(self):
        r = evaluate_sequence([{"faults": ["safety_critical_failure"]}, {"confidence": 1.0}])
        self.assertEqual(r["final_state"], "STOPPED")

    def test_invalid_confidence_is_fail_safe(self):
        r = evaluate_sequence([{"confidence": float("nan")}])
        self.assertEqual(r["final_state"], "SAFE_HOLD")
        self.assertEqual(r["failure_count"], 1)

    def test_report_is_transparent_about_synthetic_scope(self):
        report = build_report([{"id": "s1", "steps": [{"confidence": .9}],
                                "expected_final_state": "CONTINUE"}], "abc123")
        self.assertEqual(report["status"], "PASS")
        self.assertIn("not trained-model evaluation", report["limitations"][0])

    def test_empty_scenario_set_fails(self):
        self.assertEqual(build_report([])["status"], "FAIL")

if __name__ == "__main__":
    unittest.main()
