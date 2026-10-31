import tempfile
import unittest
from pathlib import Path

from pui89_resource_preflight import classify_resources, collect_report


class ResourcePreflightTests(unittest.TestCase):
    def test_memory_guidance_boundaries(self):
        self.assertEqual(classify_resources(2.0, 20.0)["memory_guidance"], "LOW")
        self.assertEqual(classify_resources(6.0, 20.0)["memory_guidance"], "LIMITED")
        self.assertEqual(classify_resources(8.0, 20.0)["memory_guidance"], "LOCAL_LIGHTWEIGHT_WORKLOADS")

    def test_disk_guidance_boundaries(self):
        self.assertEqual(classify_resources(8.0, 2.0)["disk_guidance"], "LOW")
        self.assertEqual(classify_resources(8.0, 10.0)["disk_guidance"], "LIMITED")
        self.assertEqual(classify_resources(8.0, 20.0)["disk_guidance"], "BASIC_HEADROOM")

    def test_unknown_values_are_explicit(self):
        self.assertEqual(classify_resources(None, None),
                         {"memory_guidance": "UNKNOWN", "disk_guidance": "UNKNOWN"})

    def test_report_is_read_only_and_marks_limitations(self):
        with tempfile.TemporaryDirectory() as directory:
            report = collect_report(Path(directory))
        self.assertEqual(report["report_type"], "pui89_read_only_resource_preflight")
        self.assertFalse(report["network_access_used"])
        self.assertFalse(report["packages_installed"])
        self.assertFalse(report["models_downloaded"])
        self.assertFalse(report["paid_services_used"])
        self.assertFalse(report["hardware_actuation_permitted"])
        self.assertIn("torch", report["optional_packages_installed"])
        self.assertTrue(report["limitations"])


if __name__ == "__main__":
    unittest.main()
