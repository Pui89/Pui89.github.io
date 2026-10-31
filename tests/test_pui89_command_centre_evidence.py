"""Contract checks for cross-project evidence benchmark visibility."""
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "tools" / "pui89_command_centre.py"


class EvidenceCommandCentreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def test_all_three_simulation_workflows_are_recognised(self):
        for name in (
            "coconut simulation evaluation",
            "flood rescue ai simulation evaluation",
            "multimodal narcotics screening ai simulation evaluation",
        ):
            with self.subTest(name=name):
                self.assertIn(name, self.source.lower())

    def test_evidence_benchmark_safeguard_is_reported(self):
        self.assertIn("Evidence benchmark + report integrity", self.source)

    def test_unknown_status_is_not_claimed_as_pass(self):
        self.assertIn("not_seen_in_recent_runs", self.source)
        self.assertIn("unknown, not failed or passed", self.source)

    def test_real_world_validation_is_explicitly_limited(self):
        self.assertIn("does not validate real-world robot performance", self.source)

    def test_dashboard_is_read_only(self):
        self.assertIn("read-only public GitHub status summary", self.source)
        self.assertIn("does not change project repositories", self.source)


if __name__ == "__main__":
    unittest.main()
