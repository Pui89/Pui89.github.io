"""Dependency-light, proposal-only Coconut Harvest AI grasp workflow.

This module is a software reference implementation for synthetic tests.
It does not connect to motors, actuators, cutters, ROS, or a simulator.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class GraspState(str, Enum):
    IDLE = "IDLE"
    TARGET_CHECK = "TARGET_CHECK"
    APPROACH = "APPROACH"
    PRE_CONTACT = "PRE_CONTACT"
    CONTACT_SEARCH = "CONTACT_SEARCH"
    GRASP_VERIFY = "GRASP_VERIFY"
    HOLD = "HOLD"
    RELEASE = "RELEASE"
    SAFE_STOP = "SAFE_STOP"


@dataclass(frozen=True)
class Observation:
    source: str
    timestamp: float
    frame_id: str
    target_valid: bool = False
    target_confidence: float = 0.0
    contact: Optional[bool] = None
    normal_force: Optional[float] = None
    slip_score: Optional[float] = None
    sensor_valid: bool = True
    obstacle_in_path: bool = False
    emergency_stop: bool = False


@dataclass(frozen=True)
class WorldState:
    state: GraspState
    target_accepted: bool
    contact_detected: bool
    grasp_stable: bool
    uncertainty: tuple[str, ...] = ()


@dataclass(frozen=True)
class ActionProposal:
    action: str
    reason: str
    requires_human_approval: bool = True
    executable: bool = False


@dataclass(frozen=True)
class FailureReport:
    code: str
    reason: str
    safe_state: GraspState
    human_review_required: bool = True


@dataclass(frozen=True)
class StepResult:
    world_state: WorldState
    proposal: ActionProposal
    failure: Optional[FailureReport] = None


class GraspWorkflow:
    """Fail-closed state machine that emits proposals, never actuator commands."""

    def __init__(
        self,
        *,
        expected_frame: str = "world",
        max_observation_age: float = 0.5,
        minimum_confidence: float = 0.7,
        synthetic_slip_limit: float = 0.6,
    ) -> None:
        if max_observation_age <= 0:
            raise ValueError("max_observation_age must be positive")
        if not 0.0 <= minimum_confidence <= 1.0:
            raise ValueError("minimum_confidence must be within [0, 1]")
        if not 0.0 <= synthetic_slip_limit <= 1.0:
            raise ValueError("synthetic_slip_limit must be within [0, 1]")
        self.expected_frame = expected_frame
        self.max_observation_age = max_observation_age
        self.minimum_confidence = minimum_confidence
        self.synthetic_slip_limit = synthetic_slip_limit
        self.state = GraspState.IDLE
        self.target_accepted = False
        self.contact_detected = False
        self.grasp_stable = False

    def _result(
        self,
        action: str,
        reason: str,
        *,
        uncertainty: tuple[str, ...] = (),
        failure: Optional[FailureReport] = None,
    ) -> StepResult:
        return StepResult(
            world_state=WorldState(
                state=self.state,
                target_accepted=self.target_accepted,
                contact_detected=self.contact_detected,
                grasp_stable=self.grasp_stable,
                uncertainty=uncertainty,
            ),
            proposal=ActionProposal(action=action, reason=reason),
            failure=failure,
        )

    def _stop(self, code: str, reason: str) -> StepResult:
        self.state = GraspState.SAFE_STOP
        self.grasp_stable = False
        return self._result(
            "NO_MOTION",
            reason,
            uncertainty=(code,),
            failure=FailureReport(code, reason, GraspState.SAFE_STOP),
        )

    def step(self, observation: Observation, *, now: float) -> StepResult:
        """Consume one observation and return a non-executable proposal."""
        if self.state == GraspState.SAFE_STOP:
            return self._result("NO_MOTION", "Reset requires human review.")

        if observation.emergency_stop:
            return self._stop("E_STOP", "Emergency-stop input received.")

        if not observation.source or not observation.frame_id:
            return self._stop("INVALID_PROVENANCE", "Source and frame_id are required.")
        if observation.timestamp > now:
            return self._stop("FUTURE_TIMESTAMP", "Observation timestamp is in the future.")
        age = now - observation.timestamp
        if age > self.max_observation_age:
            return self._stop("STALE_OBSERVATION", "Observation is too old.")
        if observation.frame_id != self.expected_frame:
            return self._stop("FRAME_MISMATCH", "Observation frame does not match the configured frame.")
        if not observation.sensor_valid:
            return self._stop("SENSOR_INVALID", "Sensor validity flag is false.")

        if self.state in (GraspState.IDLE, GraspState.TARGET_CHECK):
            self.state = GraspState.TARGET_CHECK
            if not observation.target_valid or not 0.0 <= observation.target_confidence <= 1.0:
                return self._stop("TARGET_INVALID", "Target validity or confidence is invalid.")
            if observation.target_confidence < self.minimum_confidence:
                return self._stop("TARGET_UNCERTAIN", "Target confidence is below the configured test threshold.")
            self.target_accepted = True
            self.state = GraspState.APPROACH
            if observation.obstacle_in_path:
                return self._stop("PATH_BLOCKED", "Obstacle detected in the proposed approach path.")
            return self._result("PROPOSE_APPROACH", "Target accepted; propose collision-checked approach.")

        if self.state == GraspState.APPROACH:
            if observation.obstacle_in_path:
                return self._stop("PATH_BLOCKED", "Obstacle detected during approach.")
            self.state = GraspState.PRE_CONTACT
            return self._result("PROPOSE_PRE_CONTACT", "Approach observation accepted.")

        if self.state == GraspState.PRE_CONTACT:
            self.state = GraspState.CONTACT_SEARCH
            return self._result("PROPOSE_BOUNDED_CLOSE", "Begin bounded contact search in the test model.")

        if self.state == GraspState.CONTACT_SEARCH:
            if observation.contact is None:
                return self._stop("CONTACT_UNKNOWN", "Contact signal is missing.")
            if not observation.contact:
                self.state = GraspState.RELEASE
                return self._result("PROPOSE_OPEN_AND_RETREAT", "No contact detected; abort grasp.")
            self.contact_detected = True
            self.state = GraspState.GRASP_VERIFY
            return self._result("PROPOSE_VERIFY_GRASP", "Contact detected; verify synthetic grasp stability.")

        if self.state == GraspState.GRASP_VERIFY:
            if observation.normal_force is None or observation.slip_score is None:
                return self._stop("TACTILE_INCOMPLETE", "Force or slip signal is missing.")
            if observation.normal_force < 0:
                return self._stop("FORCE_INVALID", "Normal-force estimate cannot be negative.")
            if not 0.0 <= observation.slip_score <= 1.0:
                return self._stop("SLIP_INVALID", "Slip score must be within [0, 1].")
            if observation.slip_score > self.synthetic_slip_limit:
                self.state = GraspState.RELEASE
                return self._result("PROPOSE_OPEN_AND_RETREAT", "Slip exceeds the synthetic test threshold.")
            self.grasp_stable = True
            self.state = GraspState.HOLD
            return self._result("PROPOSE_BOUNDED_HOLD", "Synthetic grasp checks passed; hold remains proposal-only.")

        if self.state == GraspState.HOLD:
            if observation.slip_score is None or not 0.0 <= observation.slip_score <= 1.0:
                return self._stop("SLIP_UNKNOWN", "Slip state is missing or invalid during hold.")
            if observation.slip_score > self.synthetic_slip_limit:
                self.grasp_stable = False
                self.state = GraspState.RELEASE
                return self._result("PROPOSE_OPEN_AND_RETREAT", "Slip detected during hold.")
            return self._result("PROPOSE_MAINTAIN_HOLD", "No synthetic slip trigger; continue monitoring.")

        if self.state == GraspState.RELEASE:
            self.grasp_stable = False
            self.contact_detected = False
            self.target_accepted = False
            self.state = GraspState.IDLE
            return self._result("PROPOSE_RELEASE_COMPLETE", "Release cycle completed in software state only.")

        return self._stop("UNHANDLED_STATE", "State is not supported; fail closed.")

    def reset_after_human_review(self) -> None:
        """Reset software state only; this is not a physical safety reset."""
        self.state = GraspState.IDLE
        self.target_accepted = False
        self.contact_detected = False
        self.grasp_stable = False
