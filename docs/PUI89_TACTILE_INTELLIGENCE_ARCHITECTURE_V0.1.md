# PUI89 Tactile Intelligence Architecture v0.1

**Status:** Proposed architecture / design specification  
**Scope:** Shared AI Core capability for contact, touch, pressure, force, slip, vibration and haptic interaction  
**Evidence boundary:** This document defines a proposed architecture. It does not claim that tactile sensors, robotic hands, grippers, haptic interfaces or product integrations have been built, purchased, tested or validated.

## 1. Purpose

PUI89 Tactile Intelligence extends perception beyond cameras and other non-contact sensors. It gives a system a structured way to interpret what happens at a contact surface: whether contact occurred, where pressure is distributed, whether an object is moving relative to a gripper, whether a surface is vibrating, and whether a human has touched an interface.

The goal is not to add a sensor to every product. The goal is to provide reusable interfaces so each product can adopt only the contact-sensing capabilities justified by its task, safety case, environment and cost.

**Design principle:** Vision estimates what is in view; tactile sensing measures what is happening at the point of contact. Neither modality should be treated as a substitute for the other.

## 2. Capability taxonomy

| Capability | What it can observe | Potential PUI89 use |
|---|---|---|
| Contact / touch detection | Contact presence, location and onset | Touch interfaces, bump/contact detection, object handling |
| Pressure distribution | Relative or calibrated pressure across an area | Gentle grasping, load distribution, touch panels |
| Normal force | Force perpendicular to a surface | Grip-force estimation, button or handle interaction |
| Shear force | Tangential force parallel to a surface | Detecting lateral load and early slip |
| Slip / micro-slip detection | Relative motion or vibration at a contact patch | Detecting an object beginning to slide |
| Vibration / texture cues | Contact vibration and surface-pattern signals | Grip stability and material interaction research |
| Proximity before contact | Near-field approach without physical contact | Pre-touch awareness where suitable sensors exist |
| Temperature at contact | Sensor-surface temperature | Thermal context; not a substitute for a certified temperature-safety system |
| Haptic feedback | Vibration or other controlled feedback to a human | Alerts and interface feedback; output only through bounded, reviewed controls |
| Handle / seat / control touch | Touch, grip or pressure on a user interface | Rider/operator intent and interaction-state awareness |

Not every sensor measures every capability. A capacitive tactile array, resistive array, piezoresistive element, force-sensitive resistor, load cell, six-axis force/torque sensor, piezoelectric sensor, optical tactile sensor, proximity sensor and temperature sensor have different operating principles, calibration needs, bandwidth, environmental limits and licensing or integration costs.

## 3. Shared AI Core architecture

### 3.1 Data flow

1. **Sensor layer:** a selected tactile or contact sensor produces raw readings.
2. **Acquisition layer:** a device adapter timestamps readings, checks ranges and reports device health.
3. **Signal-conditioning layer:** documented filtering, baseline compensation, calibration and sensor-health checks are applied.
4. **Feature layer:** contact maps, pressure summaries, force estimates, vibration features or slip indicators are calculated where supported.
5. **Perception layer:** tactile observations are aligned with camera, depth, inertial, audio and other authorised observations.
6. **WorldState:** the system records contact state, confidence, uncertainty, stale data and conflicting evidence.
7. **Safety gate:** deterministic, product-specific limits and independent safety controls decide whether a proposed response is permitted.
8. **Human-facing output / bounded controller interface:** the system may present an advisory or a bounded proposal. An AI model must not directly command safety-critical actuators.

### 3.2 Proposed shared data objects

These extend, rather than replace, the existing Shared AI Core contracts.

- `TactileObservation`: sensor identity and provenance, timestamp, contact location, measured channels, units, calibration version, quality flags, uncertainty and operating conditions.
- `ContactState`: no-contact / contact / unknown, contact region, pressure or force summary where calibrated, confidence and freshness.
- `SlipEvent`: candidate slip onset, direction if measurable, supporting signal window, confidence, detection latency and false-alarm status.
- `GraspState`: object/effector association, contact points, force distribution, stability estimate and explicit unknown fields.
- `HapticProposal`: proposed human-interface feedback pattern, reason, limits and expiry. It is not an actuator command.
- `TactileFailureReport`: saturation, drift, broken channel, calibration expiry, sensor detachment, communication loss, implausible readings or unresolved disagreement.

Every observation must preserve raw-source references or a documented digest, units, timestamps, calibration state and uncertainty. Missing or uncalibrated measurements must not be represented as precise force values.

## 4. Product applicability

The following are proposed use cases, not implemented product features.

| Product | Priority | Tactile / contact opportunities | Boundary |
|---|---|---|---|
| **Coconut Harvest AI** | High research priority | Gripper contact map, pressure distribution, normal/shear force, slip detection and tool-contact sensing during controlled handling | Requires a suitable gripper and real crop trials. Do not claim bruise reduction or safe harvest until independently measured |
| **AI HOME** | High, if manipulation is in scope | Soft bumper/contact strips, touch-sensitive user interface, handle/contact sensing, and tactile gripper feedback if a manipulator is specified | A touch panel is not a robotic hand. Human-contact safety requires separate design and validation |
| **AI NOMAD** | Medium / task-dependent | Handle grip and touch, body bump/contact sensing, wheel or mechanism contact diagnostics; future gripper sensing only if a manipulator is formally added | Do not assume NOMAD has a manipulator or object-grasping capability |
| **PUI89 Sentinel** | Medium / task-dependent | Protective bumper/contact sensing, foot/terrain contact where applicable, and controlled sample/object handling only if a dedicated mechanism is specified | Tactile sensing does not identify narcotics or replace RGB/X-ray/chemical inspection and human review |
| **PUI89 AI Global SUV** | Low, interface-focused | Steering-wheel/driver-control touch or grip-state sensing, seat occupancy/contact interfaces and haptic alerts where authorised | Advisory-only. No steering, throttle, braking, restraint or other safety-critical control path |
| **PUI89 AI Step-Through Scooter** | Low, interface-focused | Handlebar grip/touch, switch interaction, seat occupancy and bounded haptic warnings | Rider remains in control. No autonomous throttle, steering or braking; do not infer rider intent from one sensor alone |

The initial engineering demonstrator should be a **bench-top tactile test fixture**, followed by a Coconut Harvest AI gripper study only after the mechanical end-effector and test protocol are specified. This avoids implying that a physical harvesting robot already exists.

## 5. Hardware-neutral design

PUI89 should not depend on one chip or supplier. Evaluate sensor technologies against the actual task:

- Capacitive arrays: potentially useful for distributed touch and pressure-related signal patterns; sensitive to electrode design, grounding, moisture, parasitics and calibration.
- Resistive / piezoresistive arrays and force-sensitive resistors: accessible options for contact and relative force experiments; often require calibration and can exhibit drift, hysteresis and non-linearity.
- Load cells and force/torque sensors: useful for calibrated force measurement when installed correctly; require mechanical integration and appropriate ranges.
- Piezoelectric sensors: useful for dynamic changes and vibration; generally not a direct measurement of sustained static force.
- Optical tactile sensors: can provide rich contact-surface information but may require cameras, lighting, mechanical packaging and greater compute.
- Proximity and temperature sensors: complementary modalities, not substitutes for tactile force or slip sensing.

The Microchip ATFCD52 may be evaluated as one candidate capacitive-sensor interface. Its published headline specifications are not proof of a complete tactile system or of suitability for a PUI89 product. Before adoption, verify the current datasheet, channel configuration, evaluation-board availability, software/toolchain, licence, supply, price, provenance, power, host interface and integration requirements. No purchase or download is authorised by this architecture.

## 6. Safety and failure handling

- A tactile reading is an observation, not permission to move an actuator.
- Keep motor current limits, force limits, speed limits, emergency stop and safe-stop behaviour in an independent deterministic safety layer.
- Define product-specific maximum force, contact area, speed and allowable duration only from engineering requirements and validated tests; do not invent universal limits.
- On sensor loss, saturation, drift, calibration expiry, stale data or conflicting modalities, mark the state unknown and enter the product's documented safe response.
- Do not increase grip force automatically just because slip is suspected. The response must be bounded by a validated policy and mechanical limits.
- Human contact, pinch points, crush hazards, fragile objects, wet environments and outdoor contamination require separate hazard analysis.
- Haptic alerts must be distinguishable, bounded and non-distracting. They must not replace visual/audible safety warnings where those are required.
- Keep private human touch, occupancy and interaction data to the minimum needed; define retention and access controls before collection.

## 7. Validation plan

Progress through evidence gates. Do not skip directly from a sensor datasheet to a product capability claim.

| Gate | Work | Evidence required |
|---|---|---|
| G0 — Requirements | Define target object, contact task, environment, hazards and measurable acceptance criteria | Approved test specification and hazard review |
| G1 — Sensor bench test | Read channels, timestamps, ranges, noise, drift, saturation and disconnect behaviour | Reproducible raw logs and test report |
| G2 — Calibration | Compare sensor output against an appropriate reference instrument over the intended range | Calibration procedure, uncertainty and calibration record |
| G3 — Contact / slip fixtures | Test known contact locations, loads and controlled slip events | Confusion matrix, latency distribution, false alarms and missed detections |
| G4 — Multimodal integration | Align tactile readings with camera/depth and system state | Timestamp and synchronisation tests; missing/stale/conflict tests |
| G5 — Controlled product trial | Test with representative objects and documented operating limits | Repeatable protocol, damage/quality inspection where relevant, failure log |
| G6 — Field validation | Test only after design, safety and controlled trials pass | Defined operating envelope, independent review and retained evidence |

For grasping and slip experiments, report at minimum: detection precision/recall, false alarms, missed slips, detection latency, force-estimation error where calibrated, repeatability, sensor drift, channel failures and object damage outcomes. Report sample size and test conditions. Do not publish a single accuracy number without its method and limitations.

## 8. Open-source-first implementation sequence

1. Specify language-neutral schemas and synthetic fixtures before choosing hardware.
2. Build deterministic parsers, unit checks, timestamp checks and failure-state tests using the existing Shared AI Core conventions.
3. Use synthetic data only to test software plumbing; label it synthetic and never present it as sensor measurements.
4. Compare openly documented sensor options and licences. Prefer local/offline tooling and CPU-capable tests.
5. Prototype on a bench only after hardware, cost, provenance and safety review.
6. Keep each device integration behind a small adapter so products can change suppliers without changing shared contracts.

No paid API, subscription, cloud GPU, automatic download, purchase or hardware order is required for the specification phase.

## 9. Initial scope decision

**Recommended first slice:** define the `TactileObservation`, `ContactState`, `SlipEvent` and `TactileFailureReport` schemas; create synthetic edge-case fixtures; and write a sensor evaluation checklist. Do not begin actuator control, purchase the ATFCD52, or claim physical performance in this phase.

**Success for this phase:** a reviewer can understand the sensor provenance, units, calibration, uncertainty, contact/slip state, failure behaviour and evidence gate without relying on a specific chip vendor.

## 10. Glossary

- **Tactile sensing:** sensing information at a physical contact surface.
- **Normal force:** force perpendicular to the contact surface.
- **Shear force:** force parallel to the contact surface.
- **Slip:** relative movement between two surfaces that are in contact.
- **Micro-slip:** small local slip that may precede visible object movement.
- **Haptics:** controlled feedback intended to be felt by a person.
- **Calibration:** establishing the relationship between sensor output and a reference measurement under stated conditions.
- **Safe state:** a product-specific state defined by its hazard analysis; it must not be guessed by a general AI model.
