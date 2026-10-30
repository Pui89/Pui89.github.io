import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "pui89_report.py"
sys.path.insert(0, str(SCRIPT.parent))
from pui89_report import validate_report


def valid_report():
    return {
        "schema_version": "1.0.0",
        "project": {"id": "coconut-harvest-ai", "name": "Coconut Harvest AI"},
        "run": {
            "kind": "unit_test",
            "started_at": "2026-10-30T00:00:00+00:00",
            "commit": "abcdef0123456789",
        },
        "status": "PASS",
        "summary": {
            "tests_total": 3, "passed": 3, "failed": 0, "skipped": 0, "blocked": 0
        },
        "failures": [],
        "blockers": [],
        "claims": {
            "software_checks_only": True,
            "ai_performance_measured": False,
            "simulation_executed": False,
            "hardware_validated": False,
        },
    }


class Pui89ReportContractTests(unittest.TestCase):
    def test_accepts_valid_minimal_report(self):
        self.assertEqual(validate_report(valid_report()), [])

    def test_rejects_missing_required_field(self):
        report = valid_report()
        del report["claims"]
        self.assertTrue(any("missing required fields" in e for e in validate_report(report)))

    def test_rejects_invalid_status_and_commit(self):
        report = valid_report()
        report["status"] = "GREEN"
        report["run"]["commit"] = "not-a-sha"
        errors = validate_report(report)
        self.assertTrue(any("status is invalid" in e for e in errors))
        self.assertTrue(any("run.commit" in e for e in errors))

    def test_rejects_negative_test_counts(self):
        report = valid_report()
        report["summary"]["failed"] = -1
        self.assertTrue(any("summary.failed" in e for e in validate_report(report)))

    def test_rejects_inconsistent_test_totals(self):
        report = valid_report()
        report["summary"]["tests_total"] = 4
        self.assertTrue(any("tests_total must equal" in e for e in validate_report(report)))

    def test_rejects_pass_status_with_blocked_checks(self):
        report = valid_report()
        report["summary"]["blocked"] = 1
        self.assertTrue(any("PASS status cannot" in e for e in validate_report(report)))

    def test_rejects_invalid_repository_uri(self):
        report = valid_report()
        report["project"]["repository"] = "Pui89/example"
        self.assertTrue(any("project.repository" in e for e in validate_report(report)))

    def test_rejects_invalid_timestamp(self):
        report = valid_report()
        report["run"]["started_at"] = "not-a-date"
        self.assertTrue(any("ISO 8601" in e for e in validate_report(report)))

    def test_rejects_failure_without_reason(self):
        report = valid_report()
        report["failures"] = [{
            "id": "F-1", "severity": "medium", "category": "unknown",
            "message": "", "reproducible": False
        }]
        self.assertTrue(any("failures[0].message" in e for e in validate_report(report)))

    def test_cli_writes_valid_json_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.json"
            proc = subprocess.run([
                sys.executable, str(SCRIPT),
                "--project-id", "pui89-shared-core",
                "--project-name", "PUI89 Shared Core",
                "--repository", "https://github.com/Pui89/Pui89.github.io",
                "--kind", "unit_test", "--status", "PASS",
                "--commit", "abcdef0123456789",
                "--tests-total", "2", "--passed", "2",
                "--software-checks-only", "--output", str(output)
            ], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(validate_report(report), [])
            self.assertEqual(report["summary"]["passed"], 2)


if __name__ == "__main__":
    unittest.main()
