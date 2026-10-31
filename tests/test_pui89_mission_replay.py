import unittest
from pui89_mission_replay import replay_mission, validate_event

def event(seq, kind="NOTE", **extra):
    item = {"event_id":f"e{seq}","mission_id":"m1","sequence":seq,
            "timestamp":f"2026-10-31T10:00:{seq:02d}Z","event_type":kind,
            "source":"test-fixture","summary":f"event {seq}","evidence_refs":[]}
    item.update(extra)
    return item

class MissionReplayTests(unittest.TestCase):
    def test_valid_event(self):
        self.assertEqual(validate_event(event(1)), [])
    def test_replay_is_sequence_ordered(self):
        result=replay_mission([event(2),event(1)])
        self.assertEqual([x["sequence"] for x in result["timeline"]],[1,2])
    def test_detects_sequence_gaps(self):
        self.assertEqual(replay_mission([event(1),event(3)])["sequence_gaps"],[2])
    def test_rejects_duplicate_ids(self):
        result=replay_mission([event(1),event(1,summary="duplicate")])
        self.assertEqual(result["accepted_event_count"],1)
        self.assertEqual(result["rejected_event_count"],1)
    def test_counts_faults_and_review_requests(self):
        result=replay_mission([event(1,"FAULT_DETECTED"),event(2,"HUMAN_REVIEW_REQUESTED")])
        self.assertEqual(result["fault_count"],1)
        self.assertEqual(result["human_review_request_count"],1)
    def test_stop_is_terminal(self):
        result=replay_mission([event(1,"MISSION_STOPPED"),event(2)])
        self.assertEqual(result["terminal_state"],"STOPPED")
    def test_rejects_timezone_free_timestamp(self):
        self.assertTrue(any("timezone" in x for x in validate_event(event(1,timestamp="2026-10-31T10:00:00"))))
    def test_rejects_mixed_mission(self):
        result=replay_mission([event(1),event(2,mission_id="other")],mission_id="m1")
        self.assertEqual(result["accepted_event_count"],1)
        self.assertEqual(result["rejected_event_count"],1)
    def test_never_authorises_actuation(self):
        result=replay_mission([event(1)])
        self.assertTrue(result["simulation_only"])
        self.assertFalse(result["physical_actuation_permitted"])

if __name__ == "__main__": unittest.main()
