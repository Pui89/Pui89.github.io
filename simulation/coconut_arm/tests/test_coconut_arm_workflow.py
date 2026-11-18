"""Standard-library tests for the proposal-only grasp workflow."""
import unittest

from coconut_arm_workflow import GraspState, GraspWorkflow, Observation


def obs(**kwargs):
    values = {
        "source": "synthetic-test",
        "timestamp": 10.0,
        "frame_id": "world",
    }
    values.update(kwargs)
    return Observation(**values)


class GraspWorkflowTests(unittest.TestCase):
    def test_valid_target_starts_proposal_only_approach(self):
        workflow = GraspWorkflow()
        result = workflow.step(
            obs(target_valid=True, target_confidence=0.9), now=10.1
        )
        self.assertEqual(result.world_state.state, GraspState.APPROACH)
        self.assertEqual(result.proposal.action, "PROPOSE_APPROACH")
        self.assertFalse(result.proposal.executable)

    def test_stale_observation_fails_closed(self):
        workflow = GraspWorkflow(max_observation_age=0.5)
        result = workflow.step(
            obs(target_valid=True, target_confidence=0.9), now=11.0
        )
        self.assertEqual(result.world_state.state, GraspState.SAFE_STOP)
        self.assertEqual(result.failure.code, "STALE_OBSERVATION")

    def test_wrong_frame_fails_closed(self):
        workflow = GraspWorkflow()
        result = workflow.step(
            obs(frame_id="camera", target_valid=True, target_confidence=0.9),
            now=10.1,
        )
        self.assertEqual(result.failure.code, "FRAME_MISMATCH")

    def test_emergency_stop_fails_closed(self):
        workflow = GraspWorkflow()
        result = workflow.step(obs(emergency_stop=True), now=10.1)
        self.assertEqual(result.world_state.state, GraspState.SAFE_STOP)
        self.assertEqual(result.failure.code, "E_STOP")
        self.assertEqual(result.proposal.action, "NO_MOTION")

    def test_obstacle_blocks_approach(self):
        workflow = GraspWorkflow()
        result = workflow.step(
            obs(target_valid=True, target_confidence=0.9, obstacle_in_path=True),
            now=10.1,
        )
        self.assertEqual(result.failure.code, "PATH_BLOCKED")

    def test_missing_contact_signal_fails_closed(self):
        workflow = GraspWorkflow()
        workflow.step(obs(target_valid=True, target_confidence=0.9), now=10.1)
        workflow.step(obs(), now=10.1)
        workflow.step(obs(), now=10.1)
        result = workflow.step(obs(contact=None), now=10.1)
        self.assertEqual(result.failure.code, "CONTACT_UNKNOWN")

    def test_stable_synthetic_grasp_enters_hold(self):
        workflow = GraspWorkflow()
        workflow.step(obs(target_valid=True, target_confidence=0.9), now=10.1)
        workflow.step(obs(), now=10.1)
        workflow.step(obs(), now=10.1)
        workflow.step(obs(contact=True), now=10.1)
        result = workflow.step(
            obs(normal_force=1.0, slip_score=0.1), now=10.1
        )
        self.assertEqual(result.world_state.state, GraspState.HOLD)
        self.assertTrue(result.world_state.grasp_stable)
        self.assertFalse(result.proposal.executable)

    def test_slip_during_hold_requests_release(self):
        workflow = GraspWorkflow()
        workflow.step(obs(target_valid=True, target_confidence=0.9), now=10.1)
        workflow.step(obs(), now=10.1)
        workflow.step(obs(), now=10.1)
        workflow.step(obs(contact=True), now=10.1)
        workflow.step(obs(normal_force=1.0, slip_score=0.1), now=10.1)
        result = workflow.step(obs(slip_score=0.9), now=10.1)
        self.assertEqual(result.world_state.state, GraspState.RELEASE)
        self.assertEqual(result.proposal.action, "PROPOSE_OPEN_AND_RETREAT")

    def test_safe_stop_requires_explicit_software_review_reset(self):
        workflow = GraspWorkflow()
        workflow.step(obs(emergency_stop=True), now=10.1)
        blocked = workflow.step(
            obs(target_valid=True, target_confidence=0.9), now=10.1
        )
        self.assertEqual(blocked.world_state.state, GraspState.SAFE_STOP)
        workflow.reset_after_human_review()
        self.assertEqual(workflow.state, GraspState.IDLE)


if __name__ == "__main__":
    unittest.main()
