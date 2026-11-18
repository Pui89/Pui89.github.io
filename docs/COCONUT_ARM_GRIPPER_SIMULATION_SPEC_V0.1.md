# PUI89 Coconut Harvest AI — Arm and Gripper Simulation Specification v0.1

**Status:** Specified / proposed simulation work  
**Scope:** CPU-friendly, simulation-first design for a stationary robotic arm, compliant gripper and tactile sensing workflow.  
**Evidence boundary:** This document is a specification. No simulator has been installed or run, no robot or end-effector has been built, and no harvesting performance or safety capability is claimed.

## 1. Objective

Create a small, reproducible simulation that tests the manipulation sequence before any physical hardware is considered:

1. Detect or receive a target pose for a coconut-like test object.
2. Check target confidence, freshness and coordinate-frame validity.
3. Plan a collision-aware arm approach.
4. Close a compliant gripper under bounded force assumptions.
5. Detect contact and estimate grasp stability from synthetic tactile signals.
6. Detect slip or an uncertain grasp and respond conservatively.
7. Release safely or stop and request human review.

The first milestone is a **stationary bench-top arm/gripper simulation**. It does not include locomotion, stairs, self-righting, tree climbing, or an operational cutter.

## 2. Simulation boundary and non-goals

### Included
- One fixed-base arm model with a simple end-effector.
- A small set of synthetic coconut-shaped objects with varied pose and size.
- A simplified compliant-grasp abstraction.
- Synthetic normal-force and slip/tangential-motion signals.
- Obstacles, target pose error, sensor noise, delayed or missing observations.
- Deterministic state-machine behaviour and recorded test outcomes.

### Excluded
- Real-world dynamics claims or simulator-to-reality equivalence.
- Cutting, blade contact, branch detachment, or a live harvesting sequence.
- A mobile base, quadruped, tree-climbing mechanism or human interaction.
- Autonomous decisions by an LLM/VLM/VLA.
- Claims about payload, torque, reach, speed, grip force, battery life or farm readiness.

## 3. Candidate open-source toolchain

| Layer | Candidate | Initial use | Adoption gate |
|---|---|---|---|
| Robot description | URDF / Xacro | Describe links, joints, frames and collision geometry | Validate model structure and licence |
| Manipulation planning | MoveIt 2 | Kinematic planning and collision checking | Confirm ROS 2 distribution and resource fit |
| Robot middleware | ROS 2 | Message and node boundaries | Start with a minimal local setup |
| Physics simulation | MuJoCo | Fixed-base arm, object and contact experiments | Check version, licence, CPU/RAM use and model fidelity |
| Geometry and vision utilities | OpenCV / Open3D | Optional synthetic image and depth processing | Add only if the test requires them |
| Tests | Python standard library / pytest | Deterministic scenario and contract tests | Prefer dependency-light tests first |

**Selection rule:** Do not install or download any package, model, asset or simulator until separately approved. Confirm upstream provenance, licence, maintenance, hardware requirements and non-Chinese-origin status before adoption. The first design should remain understandable without a large model or GPU.

## 4. Logical architecture

`Synthetic Scene` → `Target Observation` → `WorldState` → `Grasp State Machine` → `Action Proposal` → `Independent Safety Gate`

Feedback path:

`Joint State + Contact/Tactile Signals` → `Grasp Monitor` → `WorldState Update`

### Required data records

- **Observation:** source, timestamp, frame ID, value, units, quality, uncertainty and validity.
- **WorldState:** target pose estimate, pose age, object identity hypothesis, contact state, grasp state and unresolved conflicts.
- **ActionProposal:** proposed arm waypoint or gripper command, preconditions, limits, expiry and reason. It is not permission to execute.
- **FailureReport:** failure code, triggering evidence, safe state, recovery suggestion and whether human review is required.

All records should be versioned and validated. Unknown, stale, malformed or conflicting inputs must not be treated as valid.

## 5. Grasp state machine

| State | Entry condition | Permitted behaviour | Safe exit |
|---|---|---|---|
| IDLE | System initialised | No motion proposal | Remain idle |
| TARGET_CHECK | Candidate target received | Validate pose, frame, age and confidence | Reject or request new observation |
| APPROACH | Target passes checks | Move through collision-checked waypoints | Stop on collision, timeout or stale target |
| PRE_CONTACT | End-effector near target | Reduce speed in the model; prepare contact monitoring | Stop if geometry is inconsistent |
| CONTACT_SEARCH | Controlled closing begins | Monitor synthetic contact and force bounds | Open/retreat if limits or sensor validity fail |
| GRASP_VERIFY | Contact detected | Check force stability and slip indicators | Accept only if all criteria pass |
| HOLD | Stable grasp hypothesis | Maintain bounded simulated hold | Stop/release if slip or sensor fault appears |
| RELEASE | Release requested and safe | Open gripper in simulation | Return to IDLE |
| SAFE_STOP | Any critical fault | No new motion proposal; simulated actuator state goes to defined safe condition | Human-reviewed reset only |

The simulation must not equate a successful grasp classification with permission to cut or harvest.

## 6. Synthetic tactile and failure signals

Use dimensionless or explicitly labelled synthetic units until a sensor and calibration method are selected.

Candidate signals:
- Contact present / absent.
- Normal-force estimate and rate of change.
- Tangential movement or shear proxy.
- Slip likelihood proxy.
- Sensor saturation, dropout, delay and disagreement.
- Gripper position and closing rate.

Do not invent physical force thresholds. Parameter values in early tests must be labelled **synthetic test parameters**, not engineering limits.

## 7. Minimum scenario suite

| ID | Scenario | Expected result |
|---|---|---|
| S01 | Valid target, clear approach | Reach pre-contact state without collision |
| S02 | Target pose outside workspace | Reject target; no approach |
| S03 | Stale target observation | Stop before contact and request a fresh observation |
| S04 | Invalid coordinate frame | Reject observation |
| S05 | Obstacle intersects planned path | Planner rejects or replans; no collision accepted |
| S06 | No contact detected during close | Abort grasp and open/retreat |
| S07 | Contact signal appears | Enter grasp verification |
| S08 | Stable synthetic contact | Enter HOLD only when all checks pass |
| S09 | Slip proxy rises during HOLD | Release or enter SAFE_STOP according to configured test policy |
| S10 | Tactile sensor dropout | Fail closed; do not claim stable grasp |
| S11 | Conflicting force and position signals | Mark state uncertain; stop and request review |
| S12 | Emergency-stop input | Immediately suppress new proposals and enter SAFE_STOP |
| S13 | Repeated identical scenario and seed | Same deterministic result |
| S14 | Malformed or missing field | Reject record with a structured FailureReport |

## 8. Test and evidence requirements

For every run, record:
- Scenario ID and version.
- Simulator and model version, when used.
- Configuration and random seed.
- Input observations and synthetic-signal parameters.
- State transitions and proposed actions.
- Collision/contact events.
- FailureReport and final state.
- Test result and known limitations.

Initial software metrics:
- Scenario pass/fail count.
- Unsafe transition count (target: zero in the defined test suite).
- Invalid-input rejection count.
- Stale-data rejection count.
- Deterministic replay agreement.
- Collision-check outcomes.

These are software/simulation test results only. They are not real-world grasp success rates, harvesting rates, force accuracy or safety certification.

## 9. Validation gates

- **G0 — Requirements:** object envelope, arm workspace and test assumptions are documented.
- **G1 — Data contracts:** Observation, WorldState, ActionProposal and FailureReport validation tests pass.
- **G2 — State machine:** all transitions and prohibited transitions are unit-tested.
- **G3 — Kinematic model:** frames, joint limits and collision geometry are reviewed.
- **G4 — Simulation scenarios:** minimum scenario suite executes reproducibly.
- **G5 — Manipulation review:** assumptions, contact model limitations and failure cases are independently reviewed.
- **G6 — Physical rig proposal:** only after G0–G5 review; requires separate founder approval before any purchase, installation or construction.
- **G7 — Controlled physical tests:** separate safety plan, guarding, E-stop, supervision and measured acceptance criteria required.
- **G8 — Cutting-tool research:** separate hazard analysis and guarded mock-up; not part of this v0.1 simulation.

A gate is not passed by documentation alone. Attach test logs and review evidence.

## 10. Safety principles

- No LLM, VLM or VLA directly commands joint torque, motor current or a cutter.
- A deterministic controller and independent safety layer own motion limits and stop behaviour.
- Missing, stale, contradictory or low-quality observations trigger conservative behaviour.
- A simulated E-stop is a test input, not a substitute for a physical E-stop.
- No blade, cutting, tree-climbing or human-proximity operation is authorised by this specification.
- Human review is required before progressing from simulation to physical work.

## 11. Immediate implementation order

1. Define dependency-light Python data contracts and validation tests.
2. Implement the deterministic grasp state machine without a simulator.
3. Add synthetic tactile signal generators and fault injection.
4. Add deterministic scenario tests and structured run logs.
5. Only after review, select and approve a simulator/toolchain.
6. Build the minimal fixed-base arm model and connect the state machine.
7. Review evidence and limitations before proposing a physical bench rig.

## 12. Current status

| Item | Status |
|---|---|
| Arm-first harvesting direction | Founder-selected |
| Stationary rig as first physical milestone | Proposed; not authorised for construction |
| Simulation specification | Documented in this file |
| Python contracts and tests | Not implemented |
| Simulator installed or run | No |
| Robot, arm, gripper or cutter built | No |
| Physical harvesting validation | Not performed |

**Next engineering deliverable:** dependency-light Python contracts, state-machine tests and synthetic fault-injection scenarios. Keep simulator adoption as a later, separately reviewed step.
