# PUI89 Coconut Harvest AI — Physical AI Architecture v0.1

**Decision status:** Founder-selected research direction  
**Mobility strategy:** Separate mobility and tree-climbing configurations sharing PUI89 AI software  
**First harvesting mechanism:** Robotic arm + tactile gripper + guarded cutter  
**Development stage:** Architecture and simulation planning only  
**Evidence boundary:** No physical robot, arm, gripper, cutter, tree-climber, quadruped, field trial, or validated harvesting capability is claimed to exist.

## 1. Founder-approved direction

Coconut Harvest AI will not be forced into one machine that must walk, climb a tree, grasp fruit and cut stems. The software architecture is shared, but the mechanical platforms are separate:

1. **Ground mobility research configuration:** a mobile base selected later for the farm terrain and payload. A quadruped is a candidate for rough ground, slopes and stairs; tracked or wheeled platforms remain alternatives. Self-righting and stair climbing are research objectives, not current capabilities.
2. **Tree-climbing research configuration:** a dedicated trunk-climbing mechanism with its own attachment, traction, fall-arrest and recovery design. It is not assumed to be a quadruped.
3. **Harvesting manipulation configuration:** the first manipulation path is an arm, compliant gripper, tactile/force sensing and guarded cutting-tool concept. Start with a stationary bench rig; integrate a mobile base only after the manipulation task is repeatable and safe.

All configurations may reuse perception, task planning, evidence, device adapters and safety interfaces. They do not automatically share actuators, mechanical dimensions or safety limits.

## 2. System architecture

### 2.1 High-level flow

`Sensors → Device adapters → Time alignment & quality checks → Perception → WorldState → Task planner → ActionProposal → Independent safety gate → Bounded controller → Actuators`

The system separates:
- **Perception:** estimates coconut bunches, individual fruit, stems, obstacles, tree geometry, arm pose and contact.
- **WorldState:** records estimates, timestamps, source provenance, uncertainty, occlusion, stale inputs and disagreements.
- **Task intelligence:** selects a reviewable sequence such as approach, inspect, position, contact, stabilise, cut, release and verify.
- **ActionProposal:** describes a bounded intended action; it is not permission to execute.
- **Safety gate:** checks operating envelope, interlocks, tool state, force/torque limits, collision zones and human approval.
- **Low-level control:** deterministic joint, motor, force and emergency-stop controls. General-purpose AI/LLMs do not issue raw torque, motor or cutter commands.

### 2.2 Shared software modules

| Module | Responsibility | First implementation style |
|---|---|---|
| Perception | Detect fruit, bunches, stem candidates, trunk, ground, stairs and obstacles | Classical CV + task-specific compact vision model |
| Geometry | Estimate 3D target pose and reachability | Depth/stereo geometry, calibration and uncertainty |
| State estimation | Fuse IMU, encoders, contact and visual observations | ROS 2 state estimation; explicit sensor health |
| Mobility intelligence | Posture, terrain, foothold and recovery state | Separate controller package per base type |
| Manipulation intelligence | Reach, align, approach, contact, grasp and retreat | MoveIt 2 planning + bounded joint/Cartesian controllers |
| Tactile intelligence | Contact, pressure distribution, force and slip evidence | Sensor adapter + calibrated signal processing |
| Harvest task planner | Sequence and verify task steps | Finite-state machine / behaviour tree; human approval gates |
| Safety supervisor | Limits, interlocks, safe-stop, watchdog and E-stop | Independent deterministic MCU/controller |
| Evidence recorder | Log source, calibration, task, outcome and failures | Local structured logs; privacy and retention controls |

## 3. Mechanical configurations

### 3.1 First build: stationary arm-and-gripper bench rig

**This is the recommended first physical engineering milestone**, subject to later explicit hardware and spending approval.

Proposed assembly:
- Rigid benchtop frame and guarded work envelope.
- One research arm with adequate reach and payload determined from measured task requirements.
- Joint encoders and a controller with documented limits.
- Wrist-mounted force/torque sensing if the selected arm supports it and calibration can be established.
- Replaceable compliant gripper fingers and replaceable contact pads.
- Tactile sensing on selected contact surfaces; do not begin with full-hand tactile skin.
- RGB camera and, if needed, depth camera for object pose.
- Guarded, non-powered cutter mock-up for initial reach and clearance trials.
- Physical E-stop, mechanical stops, interlocks and a separate safe controller.
- Test objects first; real coconut material only after the fixture, protocol and hazard review are approved.

The first rig should prove camera-to-arm calibration, reachability, controlled contact, grasp stability, slip detection, release and safe-stop behaviour. Cutting begins as a guarded mock-up and then a separately reviewed controlled test. Do not start with a live blade beside people.

### 3.2 Ground mobility configuration — later research track

Possible alternatives:
- **Quadruped:** useful research candidate for uneven terrain, slopes, steps, posture control and self-righting. High mechanical/control complexity and fall risk; not the first harvesting prototype.
- **Tracked base:** potentially stable and practical for farm ground, but needs a defined ramp/step envelope and turning space.
- **Wheeled base:** simplest and often lowest complexity on prepared paths; limited by obstacles, mud and uneven terrain.

Before selecting, measure terrain, path width, slope, step height, mud/water exposure, payload, travel distance, recovery needs and operator access. Do not claim stairs or hill-climbing until the exact envelope has been tested.

### 3.3 Tree-climbing configuration — separate future research track

A dedicated trunk-climber needs:
- Tree-diameter and taper envelope.
- Multiple independently monitored contact/traction points.
- Mechanical retention and a secondary fall-arrest concept.
- Slip and attachment-state sensing.
- Branch, leaf, bunch and trunk-clearance perception.
- Power and communications strategy during ascent.
- Controlled descent, jam recovery and emergency retrieval.
- A safe exclusion zone and ground operator procedure.

Tree climbing is a high-consequence mechanical problem. No person should be under an experimental climber. Do not test at height until ground-level load, slip, retention, fault-injection and recovery tests pass and a qualified safety review approves the procedure.

## 4. Component selection framework

No brand, part number, purchase quantity or specification is frozen in v0.1. Select components only after requirements and compatibility are documented.

| Subsystem | Candidate component class | Selection criteria |
|---|---|---|
| Arm | 4–6 degree-of-freedom research arm, or a simpler 3–4 DOF rig for initial reach tests | Reach, payload, repeatability, joint limits, documented interface, safe speed and maintainability |
| End effector | Two- or three-finger compliant gripper; replaceable soft pads | Fruit geometry, contact area, cleanability, grip range and fail-safe release |
| Wrist sensing | 6-axis force/torque sensor or calibrated load-cell arrangement | Range, overload protection, calibration, bandwidth and mounting |
| Fingertip sensing | Small tactile array or discrete force sensors | Contact coverage, drift, moisture tolerance, replaceability and data interface |
| Vision | RGB camera; depth/stereo only if 3D geometry requires it | Resolution, working distance, outdoor lighting, calibration and open drivers |
| Arm feedback | Joint encoders and current/temperature telemetry | Accuracy, health monitoring and accessible data |
| Compute | CPU-first host for perception and planning; MCU for real-time I/O and safety | RAM, supported OS, interfaces, power, thermal envelope and offline operation |
| Power | Approved supply for bench rig; later battery + BMS for mobile platforms | Peak current, fusing, isolation, protection and measured duty cycle |
| Cutter | Guarded cutter concept with position/state sensing and physical interlock | Stem properties, cutting force measured in tests, guarding, jam detection and safe release |
| Safety | E-stop, watchdog, interlocks, limit switches, hard stops and independent controller | Fail-safe behaviour, diagnostic coverage and reviewable wiring |

Do not select arm torque, gripper force, cutter force, battery capacity or payload by guesswork. Measure representative coconuts, bunch geometry, stem dimensions and tool forces under a controlled fixture before sizing components.

## 5. Open-source-first software and simulation stack

The following are candidate tools, not a declaration that they have been installed or approved for a particular device. Verify supported versions, licences, platform requirements and non-Chinese provenance before adoption.

| Need | Candidate | Intended use |
|---|---|---|
| Robot middleware | ROS 2 | Nodes, messages, lifecycle, device integration and diagnostics |
| Arm motion planning | MoveIt 2 | Kinematics, collision checking, planning scene and trajectory planning |
| Low-level interfaces | ros2_control | Hardware abstractions and controller interfaces |
| Manipulator simulation | MuJoCo | Contact, grasping, dynamics and controlled manipulation experiments |
| Integrated robot simulation | Gazebo | Sensor and robot integration scenarios; later, when needed |
| Geometry and vision | OpenCV + Open3D | Image processing, calibration, point clouds and geometric estimation |
| Robot model | URDF / Xacro | Mechanical links, joints, frames, collision and inertial descriptions |
| State / task logic | ROS 2 lifecycle nodes + finite-state machine or behaviour tree | Inspectable task sequence and recovery states |
| Test automation | pytest + ROS 2 launch/testing tools | Unit, integration, fault and regression tests |
| Data analysis | Python, NumPy and Matplotlib | Calibration, metrics and evidence reports |

Start with one simulator for the first question. MuJoCo is a reasonable first choice for arm contact and gripper experiments; add Gazebo only when ROS-integrated sensor and environment simulation materially helps. Avoid running multiple simulators in parallel without a clear test need.

## 6. Model strategy — small, specialised and auditable

A model is selected per task, not as one general robot brain.

| Task | Initial candidate | Notes and constraints |
|---|---|---|
| Coconut / bunch detection | Compact MobileNet-based detector or classifier; compare a compact detector architecture after dataset review | Train/evaluate on rights-cleared, human-labelled coconut images; do not assume a pretrained model recognises local cultivars or maturity reliably |
| Maturity classification | MobileNetV3 or EfficientNet-Lite classifer baseline | Use the four defined classes: young green, mature green, yellow and brown; report per-class precision, recall, F1 and confusion matrix |
| Segmentation | Lightweight DeepLab-style segmentation baseline if fruit/stem boundaries are required | Only add if bounding boxes are insufficient; segmentation labels cost more to create |
| 3D target pose | Geometric RGB-D/stereo estimation first | Prefer measurable geometry and uncertainty over a large vision-language model |
| Arm motion | MoveIt 2 planning + deterministic controllers | A learned policy is not required for the first arm demonstrator |
| Grasp / slip | Signal processing and calibrated thresholds first; small CNN/temporal model only if it beats the baseline | Evaluate false alarms, missed slips, latency, drift and object damage |
| Task reasoning | Finite-state machine / behaviour tree first; optional small local language model for operator-facing explanations later | LLM may explain or propose; never directly control joints, cutter or safety interlocks |
| Locomotion | Classical balance, state estimation and model-predictive / whole-body control research | Separate mobility platform track; reinforcement learning only in simulation after a reliable baseline exists |

**Model governance:** every candidate must pass a provenance and licence review covering model weights, architecture, training data, backbone, dependencies, intended use and commercial restrictions. Do not import model weights or datasets automatically. Prefer CPU-capable, local inference. Do not use Chinese-origin models or dependencies under the PUI89 provenance rule. If a candidate's origin or licence is unclear, reject or hold it pending review.

## 7. Data and evidence plan

### 7.1 Dataset sequence

1. Confirm image and video rights and provenance before collection or reuse.
2. Create a data register with source, consent/licence, date, location granularity, device, conditions and allowed uses.
3. Define annotation instructions and class definitions before labelling.
4. Use trained human reviewers for labels; retain disagreements and adjudication records.
5. Split by tree, location, capture session or source—not random near-duplicate frames—to reduce leakage.
6. Keep a held-out test set untouched until model selection is complete.
7. Store images, labels, model versions and evaluation outputs with access and retention controls.

### 7.2 Minimum evaluation

- Detection: precision, recall, F1, per-class AP where appropriate, missed fruit and false detections.
- Maturity: per-class precision/recall/F1, confusion matrix and reviewer agreement.
- Geometry: position/orientation error against a documented reference and uncertainty.
- Grasp: successful stable holds, drops, slip-detection latency, false alarms, force-estimation error where calibrated and object damage.
- Cutting: stem cut success, incomplete cuts, unintended contact, tool jams, cut time and damage to fruit/bunch/tree.
- System: task completion, recovery, safe stops, sensor faults, compute latency, power and thermal behaviour.

Always report test count, environment, object variety, camera setup, operating range and limitations. Do not publish a single headline score without its protocol.

## 8. Staged simulation and validation gates

| Gate | Work | Pass evidence / stop condition |
|---|---|---|
| C0 — Requirements | Measure target fruit, bunch and stem geometry; define operating context, human roles and hazards | Approved requirements, test protocol and hazard register |
| C1 — Perception baseline | Rights-cleared dataset, human labels, CPU baseline | Held-out evaluation and documented failure cases |
| C2 — Arm digital model | URDF, frames, joint limits, collision geometry and calibrated camera model | Kinematic checks, reachability and collision tests |
| C3 — Bench manipulation | Simulate approach, contact, grasp, slip, release and retreat | Repeatable tests, fault cases and bounded trajectories |
| C4 — Physical bench rig | Only after explicit approval and hardware review | Calibration, E-stop, safe-stop, repeatability and fault-injection evidence |
| C5 — Guarded cutting mock-up | Verify alignment, clearance, interlocks and tool-state sensing without an exposed live blade | Independent safety review and recorded tests |
| C6 — Controlled cutting | Limited, supervised trials on representative stems in a controlled exclusion zone | Cut quality, damage, jam, force and emergency-response evidence |
| C7 — Mobile-base integration | Integrate the proven arm with a selected ground platform | Payload, stability, vibration, power, braking/stop and terrain validation |
| C8 — Tree-climber research | Separate bench retention and slip tests, then staged low-height trials only after approval | Retention, fall-arrest, fault recovery and independent safety evidence |
| C9 — Farm validation | Supervised field trials within a declared operating envelope | Repeatability, reliability, crop impact, operator safety and maintenance evidence |

Do not combine C7 and C8 into a single first prototype. A tree climber and a ground mobile base have different mechanical safety cases.

## 9. Safety architecture and prohibited shortcuts

- Use a physical emergency stop and independent deterministic safety controller.
- Define safe states for loss of power, communications, camera, depth, encoder, tactile sensor, controller heartbeat and unexpected contact.
- Enforce joint, speed, force, torque, workspace and tool limits below the validated mechanical limits.
- Use collision geometry and keep-out zones; never treat a vision model's confidence as a safety-rated obstacle detector.
- Keep the cutter disabled by default. Require physical guarding, interlocks, tool-state feedback, human-authorised test mode and a clear exclusion zone.
- No autonomous cutting near people, no person beneath an experimental tree-climber, and no operation over public areas.
- A fall-recovery controller must not attempt to stand up if the robot is entangled, damaged, near a person, or on an unverified surface.
- On uncertain state, stale data, sensor disagreement or failed checks, stop or enter the documented safe state.
- Never let an LLM or VLA model bypass safety checks or send direct motor/cutter commands.
- Keep a manual recovery procedure and an operator-controlled safe stop available.

## 10. Open-source-first and approval controls

- No paid API, subscription, cloud GPU, metered inference or recurring service without explicit approval.
- No package, model, dataset, firmware or large dependency download or installation without explicit approval.
- No hardware purchase, supplier commitment or external test arrangement without explicit approval.
- Prefer open-source tools with clear licences, local/offline operation and modest CPU/RAM requirements.
- Review software licence, model-weight licence, dataset rights, dependency tree, provenance, security, maintenance and hardware needs before adoption.
- Keep experiments reproducible and preserve raw evidence, calibration records, configuration, code revision and test conditions.
- Use protected branches and reviewable PRs; no default-branch writes or automatic merges.

## 11. Immediate next actions — documentation and simulation only

1. Freeze the separate-platform decision and arm-first harvesting mechanism in the project requirements.
2. Write a measurement sheet for coconut bunch, fruit, stem, reach, approach direction and representative object mass; do not invent values.
3. Define the arm/gripper test tasks and hazard analysis.
4. Create a minimal URDF/Xacro arm and gripper model with placeholder dimensions explicitly marked as assumptions.
5. Create MuJoCo scenes for approach, contact, grasp, slip, release and guarded cutter mock-up.
6. Define perception labels and a rights-cleared dataset plan.
7. Define Shared AI Core interfaces for target pose, grasp state, tactile observation, action proposal and failure report.
8. Review the simulation and documentation before seeking approval for any hardware.

**Immediate deliverable:** a repeatable, CPU-friendly simulated arm-and-gripper workflow with explicit assumptions and failure cases. This is a software/simulation milestone, not a physical harvesting prototype.

## 12. Glossary

- **Ground mobility configuration:** a robot base that moves over farm terrain.
- **Tree-climbing configuration:** a dedicated mechanism that attaches to and ascends a tree trunk.
- **End effector:** the tool mounted at the end of a robotic arm, such as a gripper or cutter.
- **Tactile sensing:** sensing at the physical contact surface.
- **Force/torque sensing:** measurement of loads applied to a sensor in defined axes.
- **WorldState:** the structured current estimate of known, unknown, stale and conflicting conditions.
- **ActionProposal:** a bounded suggested action awaiting safety checks and required approval.
- **Operating envelope:** the explicitly validated range of conditions in which a system is allowed to operate.
