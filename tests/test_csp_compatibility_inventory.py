import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "audit_csp_compatibility.py"
SPEC = importlib.util.spec_from_file_location("csp_inventory", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class CspInventoryTests(unittest.TestCase):
    def test_inline_executable_script_gets_sha256_fingerprint(self):
        parser = MODULE.InventoryParser()
        parser.feed('<script>window.pui89 = true;</script>')
        self.assertEqual(len(parser.inline_scripts), 1)
        self.assertTrue(parser.inline_scripts[0]["sha256_csp"].startswith("sha256-"))
        self.assertNotIn("window.pui89", str(parser.inline_scripts))

    def test_json_script_is_not_counted_as_executable(self):
        parser = MODULE.InventoryParser()
        parser.feed('<script type="application/ld+json">{"name":"PUI89"}</script>')
        self.assertEqual(parser.inline_scripts, [])

    def test_inline_handlers_styles_and_javascript_urls_are_counted(self):
        parser = MODULE.InventoryParser()
        parser.feed('<button onclick="go()" style="color:red">Go</button><a href="javascript:go()">x</a>')
        self.assertEqual(parser.event_handlers["onclick"], 1)
        self.assertEqual(parser.style_attributes, 1)
        self.assertEqual(len(parser.javascript_urls), 1)

    def test_external_script_origin_and_sri_are_counted(self):
        parser = MODULE.InventoryParser()
        parser.feed('<script src="https://cdn.example.test/app.js" integrity="sha384-abc" crossorigin="anonymous"></script>')
        self.assertEqual(parser.external_scripts, ["https://cdn.example.test/app.js"])
        self.assertEqual(parser.sri_attributes, 1)
        self.assertEqual(MODULE.origin(parser.external_scripts[0]), "https://cdn.example.test")

    def test_csp_meta_and_nonce_are_counted(self):
        parser = MODULE.InventoryParser()
        parser.feed('<meta http-equiv="Content-Security-Policy" content="default-src self"><script nonce="abc">run()</script>')
        self.assertEqual(parser.csp_meta, 1)
        self.assertEqual(parser.nonce_attributes, 1)


if __name__ == "__main__":
    unittest.main()
