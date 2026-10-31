import copy
import unittest

from pui89_hf_registry import load_registry, validate_registry


class HuggingFaceRegistryTests(unittest.TestCase):
    def setUp(self):
        self.registry = load_registry()

    def test_committed_registry_is_valid(self):
        self.assertEqual(validate_registry(self.registry), [])

    def test_registry_contains_three_project_relevant_candidates(self):
        resources = self.registry["resources"]
        self.assertEqual(len(resources), 3)
        self.assertTrue(any("SmolVLM" in item["id"] for item in resources))
        self.assertTrue(any("smolvla" in item["id"] for item in resources))

    def test_downloads_and_external_execution_remain_disabled(self):
        policy = self.registry["policy"]
        boolean_safety_controls = (
            "network_access", "automatic_downloads", "package_installation",
            "paid_inference", "hardware_actuation",
        )
        self.assertTrue(all(policy[key] is False for key in boolean_safety_controls))
        self.assertEqual(policy["default_approval"], "NOT_APPROVED")
        self.assertTrue(all(item["download"] == "DISABLED" for item in self.registry["resources"]))
        self.assertTrue(all(item["approval"] == "NOT_APPROVED" for item in self.registry["resources"]))

    def test_duplicate_resource_ids_are_rejected(self):
        data = copy.deepcopy(self.registry)
        data["resources"].append(copy.deepcopy(data["resources"][0]))
        self.assertTrue(any("duplicated" in error for error in validate_registry(data)))

    def test_non_https_source_is_rejected(self):
        data = copy.deepcopy(self.registry)
        data["resources"][0]["source_url"] = "http://example.invalid/model"
        self.assertTrue(any("HTTPS" in error for error in validate_registry(data)))

    def test_approval_requires_completed_licence_and_resource_reviews(self):
        data = copy.deepcopy(self.registry)
        data["resources"][0]["approval"] = "APPROVED_FOR_OFFLINE_EVALUATION"
        self.assertTrue(any("licence review" in error for error in validate_registry(data)))
        self.assertTrue(any("resource testing" in error for error in validate_registry(data)))

    def test_reviewed_licence_requires_evidence(self):
        data = copy.deepcopy(self.registry)
        item = data["resources"][0]
        item["license_review"] = {"status": "REVIEWED", "license": None,
                                  "reviewed_on": None, "review_evidence_url": None}
        self.assertTrue(any("required for REVIEWED" in error for error in validate_registry(data)))

    def test_unsafe_policy_change_is_rejected(self):
        data = copy.deepcopy(self.registry)
        data["policy"]["automatic_downloads"] = True
        self.assertTrue(any("automatic_downloads must be false" in error
                            for error in validate_registry(data)))

    def test_unknown_resource_state_is_rejected(self):
        data = copy.deepcopy(self.registry)
        data["resources"][0]["resource_review"]["status"] = "READY"
        self.assertTrue(any("resource_review.status" in error for error in validate_registry(data)))


if __name__ == "__main__":
    unittest.main()
