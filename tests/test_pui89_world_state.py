import unittest
from pui89_world_state import summarise_world_state, validate_observation

def obs(identifier, value, timestamp="2026-10-31T10:00:00Z", **extra):
    record = {"observation_id":identifier,"entity_id":"entity-1","attribute":"hazard_level","value":value,
              "observed_at":timestamp,"source_id":"sensor-1","modality":"environmental","evidence_kind":"observed","quality":"valid"}
    record.update(extra)
    return record

class WorldStateTests(unittest.TestCase):
    def test_valid_observation(self): self.assertEqual(validate_observation(obs("o1","high")), [])
    def test_rejects_timezone_free_timestamp(self):
        self.assertTrue(any("timezone" in x for x in validate_observation(obs("o1","high","2026-10-31T10:00:00"))))
    def test_preserves_conflict_without_resolving(self):
        state=summarise_world_state([obs("o1","high"),obs("o2","low")],now="2026-10-31T10:01:00Z",max_age_seconds=600)["states"][0]
        self.assertTrue(state["conflict"]); self.assertIsNone(state["resolution"])
        self.assertEqual(state["action"],"REQUEST_HUMAN_REVIEW"); self.assertEqual(set(state["distinct_values"]),{"high","low"})
    def test_marks_old_observation_stale(self):
        state=summarise_world_state([obs("o1","high","2026-10-31T09:00:00Z")],now="2026-10-31T10:00:00Z",max_age_seconds=30)["states"][0]
        self.assertEqual(state["status"],"STALE"); self.assertEqual(state["action"],"SAFE_HOLD")
    def test_rejects_invalid_record_and_never_enables_actuation(self):
        result=summarise_world_state([{"entity_id":"missing"}],now="2026-10-31T10:01:00Z",max_age_seconds=600)
        self.assertEqual(len(result["rejected_observations"]),1); self.assertFalse(result["physical_actuation_permitted"])
        self.assertTrue(result["simulation_only"])
    def test_future_observation_is_stale(self):
        state=summarise_world_state([obs("o1","high","2026-10-31T11:00:00Z")],now="2026-10-31T10:00:00Z",max_age_seconds=600)["states"][0]
        self.assertEqual(state["status"],"STALE")

if __name__ == "__main__": unittest.main()
