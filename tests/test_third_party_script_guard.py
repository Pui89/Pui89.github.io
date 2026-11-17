import importlib.util
import json
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_third_party_scripts.py"
SPEC = importlib.util.spec_from_file_location("pui89_script_guard", SCRIPT)
GUARD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(GUARD)


class ThirdPartyScriptGuardTests(unittest.TestCase):
    def test_parser_finds_external_and_inline_scripts(self):
        parser = GUARD.ScriptParser()
        parser.feed('<script src="https://cdn.example/app.js"></script><script>eval("x")</script>')
        self.assertEqual(parser.scripts[0]["src"], "https://cdn.example/app.js")
        self.assertIn('eval("x")', parser.scripts[1]["_inline"])

    def test_dynamic_execution_patterns_are_reported(self):
        warnings = []
        count = GUARD.inspect_dynamic_script_patterns(
            'const s=document.createElement("script"); eval("x"); import("remote")',
            "fixture.js",
            warnings,
        )
        self.assertEqual(count, 3)
        self.assertEqual(len(warnings), 3)

    def test_clean_source_has_no_dynamic_pattern_findings(self):
        warnings = []
        count = GUARD.inspect_dynamic_script_patterns(
            'const total = 1 + 2; console.log(total);',
            "clean.js",
            warnings,
        )
        self.assertEqual(count, 0)
        self.assertEqual(warnings, [])

    def test_allowlist_requires_exact_https_url_and_sri_hash(self):
        expiry = (date.today() + timedelta(days=30)).isoformat()
        entry = [{
            "url": "https://cdn.example/app.js",
            "owner": "web-maintainer",
            "purpose": "approved static widget",
            "reviewed_on": date.today().isoformat(),
            "expires_on": expiry,
            "integrity": "sha384-" + "A" * 64,
        }]
        with tempfile.TemporaryDirectory() as tmp:
            allowlist_path = Path(tmp) / "allowlist.json"
            allowlist_path.write_text(json.dumps(entry), encoding="utf-8")
            original = GUARD.ALLOWLIST_PATH
            GUARD.ALLOWLIST_PATH = allowlist_path
            try:
                result = GUARD.load_allowlist()
                self.assertIn("https://cdn.example/app.js", result)
            finally:
                GUARD.ALLOWLIST_PATH = original

    def test_allowlist_rejects_missing_sri_hash(self):
        entry = [{
            "url": "https://cdn.example/app.js",
            "owner": "web-maintainer",
            "purpose": "approved static widget",
            "reviewed_on": date.today().isoformat(),
            "expires_on": (date.today() + timedelta(days=30)).isoformat(),
        }]
        with tempfile.TemporaryDirectory() as tmp:
            allowlist_path = Path(tmp) / "allowlist.json"
            allowlist_path.write_text(json.dumps(entry), encoding="utf-8")
            original = GUARD.ALLOWLIST_PATH
            GUARD.ALLOWLIST_PATH = allowlist_path
            try:
                with self.assertRaises(ValueError):
                    GUARD.load_allowlist()
            finally:
                GUARD.ALLOWLIST_PATH = original


if __name__ == "__main__":
    unittest.main()
