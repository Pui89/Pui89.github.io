# PUI89 Common Hardware & Safety Standard

**Status:** Proposed common engineering standard  
**Applies to:** All seven PUI89 AI and robotics projects  
**Version:** 0.1.0  
**Last updated:** 8 November 2026  
**Implementation boundary:** Documentation standard only. This document does not certify, procure, build, or validate hardware.

## 1. Purpose

Establish a reusable, evidence-led baseline for selecting, integrating, testing, and maintaining materials and hardware across the PUI89 portfolio. Shared requirements are a starting point; each project must add domain-specific hazards, operating limits, and acceptance tests.

The standard is designed for a zero-cost planning and software-development phase. It does not authorise purchases, paid services, subscriptions, cloud compute, hardware operation, or physical testing.

## 2. Evidence and maturity labels

Every hardware or safety statement in project documentation must use the most accurate status:

| Status | Meaning |
|---|---|
| Proposed | A candidate design, material, component, or requirement |
| Specified | A measurable requirement and acceptance method have been written |
| Implemented | The relevant design or software control exists |
| Bench-tested | A physical component was tested under recorded bench conditions |
| Integrated-tested | Components were tested together under recorded conditions |
| Field-validated | Evidence supports performance in the stated real operating environment |
| Certified | A named, applicable certification has been issued by an authorised body |
| Unknown / Not tested | Evidence is absent, incomplete, or not yet reviewed |

Do not use “waterproof”, “fireproof”, “shockproof”, “safe”, “certified”, “autonomous”, or a numeric protection rating as a verified claim without appropriate test evidence and, where applicable, certification.

## 3. Common hardware architecture

Each project should document the following layers, even when a layer is not yet selected or implemented.

### 3.1 Structure and materials

Record:
- Candidate material and grade, supplier/manufacturer data source, and revision.
- Intended structural role, load direction, estimated load cases, and safety factor rationale.
- Mass, dimensions, joining method, corrosion/UV/chemical exposure, wear, repairability, and end-of-life considerations.
- Relevant failure modes: fracture, fatigue, buckling, deformation, sharp edges, pinch points, loose fasteners, and component detachment.

Material selection must be based on the actual environment and load cases. “Titanium”, aluminium, stainless steel, engineering polymers, composites, and elastomers are candidate families—not blanket recommendations or proof of suitability.

### 3.2 Power and electrical safety

Document:
- Power source chemistry and exact cell/pack specification, if selected.
- Battery Management System (BMS) functions and documented limits.
- Over-current, short-circuit, over-charge, over-discharge, reverse-polarity, and thermal protection as applicable.
- Fuse or protective-device ratings, wiring gauge, connector ratings, insulation, strain relief, and enclosure.
- Charging method, isolation, service access, emergency power isolation, and safe storage procedure.
- Measured voltage/current/temperature limits and test conditions before operational claims.

Do not design or recommend an improvised battery pack as ready for use. Battery assembly, charging, high-current testing, and mains-voltage work require competent supervision and appropriate equipment.

### 3.3 Compute and control

For each compute/control unit, record:
- Exact board or device, processor, memory, storage, interfaces, and documented operating limits.
- Power draw and thermal envelope from authoritative specifications or measurements.
- Boot/recovery behaviour, watchdog strategy, logging, software version, and update/rollback method.
- Separation between high-level AI proposals and safety-critical control.
- Offline behaviour and what happens when compute, communication, or time synchronisation fails.

An AI model or general-purpose computer must not be the sole safety controller for a physical platform.

### 3.4 Sensors and evidence quality

For every sensor, record:
- Modality, model, serial/revision where available, range, field of view, resolution, sampling rate, and environmental limits.
- Calibration method/date, timestamp source, coordinate frame, mounting position, and known blind spots.
- Data provenance, licence/permission, retention, privacy, and access controls.
- Missing, stale, noisy, occluded, saturated, out-of-range, and conflicting observation handling.

Sensor presence does not establish measurement accuracy. RGB imagery alone cannot establish chemical identity, internal structure, or other properties outside the sensor's validated capability.

### 3.5 Environmental protection

Assess separately:
- Water ingress, immersion, rain, spray, condensation, humidity, and drainage.
- Dust and particulate ingress.
- Temperature extremes, thermal cycling, sunlight/UV, and ventilation.
- Corrosion, chemicals, cleaning agents, and biological contamination.
- Vibration, impact, drop, abrasion, and transport loads.
- Fire exposure, ignition sources, battery thermal events, smoke, and safe isolation.

Select enclosure materials, seals, connectors, vents, coatings, and drainage only after defining the exposure profile. An IP rating applies only to the tested configuration and conditions; it does not prove fire resistance, corrosion resistance, or suitability for immersion beyond its rating.

Fire safety must prioritise prevention, separation of energy sources, appropriate electrical protection, thermal monitoring where justified, safe isolation, and a documented emergency response. Do not describe a robot as fire-resistant or fireproof without a relevant test standard and independent evidence.

## 4. Common safety requirements

Every project must define and test, as applicable:

1. **Human authority:** a person can stop, disable, or override the system through a clearly documented method.
2. **Safe state:** loss of power, communication, localisation, sensor confidence, or controller health leads to a defined safe response.
3. **Bounded operation:** speed, force, reach, temperature, current, payload, water depth, and operating area have explicit limits where relevant.
4. **Uncertainty handling:** unknown, stale, missing, or conflicting inputs cannot silently become a confident action.
5. **No unauthorised actuation:** AI outputs are proposals until validated gates and required human approval are satisfied.
6. **Emergency isolation:** power isolation and recovery procedures are documented and accessible.
7. **Mechanical safety:** guards, covers, cable routing, pinch-point controls, stability, and emergency access are reviewed.
8. **Privacy and security:** collect only necessary data, protect credentials, restrict access, and document data handling.
9. **Failure reporting:** record fault, context, timestamp, affected component, safe response, and recovery steps.
10. **Maintenance:** define inspection intervals and replacement criteria based on manufacturer guidance and actual use.

These are design requirements. Their existence in this document does not establish that any project currently implements them.

## 5. Verification and acceptance evidence

Before a physical system is described as tested, create a test record containing:

- Test ID, date, operator, location, and risk review.
- Hardware identity, revisions, assembly configuration, and software commit.
- Test objective, setup, instruments and calibration status.
- Environmental conditions and operating limits.
- Procedure, expected result, measured result, pass/fail criteria, and deviations.
- Photos/logs/data where appropriate, with privacy safeguards.
- Failures, corrective action, retest result, and reviewer.

Use a staged sequence:
1. Requirements and hazard review.
2. Documentation and design review.
3. Offline software/unit tests using fixtures.
4. Simulation or mock-interface tests where applicable.
5. Supervised low-energy bench tests.
6. Integrated tests in a controlled area.
7. Domain-specific field trials after risk review.
8. Independent review or certification where required.

Do not skip stages based on a successful unit test or simulation. A software test does not validate material strength, water ingress, fire behaviour, braking, stability, buoyancy, or physical safety.

## 6. Shared software contracts

Hardware-facing software should use the shared PUI89 contracts and preserve provenance and uncertainty:

- **Observation:** sensor identity, modality, timestamp, coordinate frame, quality, calibration reference, provenance, and uncertainty.
- **WorldState:** timestamped state estimate, observed facts, unknowns, stale data, conflicts, hazards, and source references.
- **ActionProposal:** intended action, preconditions, limits, expected effects, confidence/uncertainty, expiry, and required approvals.
- **FailureReport:** fault category, component, context, detection time, safe-state response, evidence, and recovery status.

All action proposals must pass project-specific safety gates. A contract is an interface, not proof that an actuator or safety mechanism is reliable.

## 7. Portfolio-specific adaptation

| Project | Hardware focus | Additional safety and verification focus |
|---|---|---|
| Coconut Harvest AI | Structure, guarded cutting mechanism, arm, gripper/basket, cameras, depth/localisation sensors, battery and BMS | Falling fruit, cutter guarding, worker/animal exclusion, reach/load limits, branch interaction, safe stop and harvest verification |
| Extreme Flood Rescue AI | Buoyant hull, propulsion, optional ground mobility, sealed electronics, communication and navigation sensors | Stability, buoyancy, ingress, current, entanglement, rescue-load limits, loss of communication, recovery and human rescue-team coordination |
| Multimodal Narcotics Screening AI / Sentinel | RGB and only authorised, suitable, separately validated inspection sensors; mobile platform is a concept | Sensor provenance/calibration, false positives/negatives, human review, lawful use, privacy, no autonomous accusation or enforcement |
| AI HOME | Indoor mobile base, environmental sensors, electrical monitoring interfaces, battery and charging | Mains isolation, trip/fall hazards, indoor navigation, alarms, privacy, false alarm handling and safe unattended behaviour |
| AI NOMAD | Portable enclosure, wheels/handle, removable power system, location and environmental sensors | Transport/drop exposure, weather limits, battery handling, offline operation, location privacy and safe mobility |
| AI Robot Car | Research chassis, steering/braking/drive interfaces, perception and localisation sensors | Closed-course testing, emergency stop, speed/area limits, fail-safe braking and separation from public roads until legally authorised and validated |
| AI Motorcycle Robotics | Two-wheel platform, frame, tyres, braking, lighting, battery/engine interfaces and advisory sensors | Human-controlled steering/throttle/braking, stability, rider visibility, weather limits and no AI actuation of safety-critical controls |

This table describes research priorities, not confirmed component selections or completed hardware.

## 8. Zero-cost and resource governance

- Prefer documentation, standard-library checks, existing repository automation, and offline simulation/mock tests.
- Do not introduce paid APIs, subscriptions, cloud GPUs, hosted inference, or recurring services without explicit approval.
- Do not automatically download model weights, datasets, large dependencies, or firmware.
- Check licence, provenance, security, disk/RAM/CPU requirements, and maintenance status before adoption.
- Check current GitHub plan quotas and workflow usage; do not assume all automation is unlimited or permanently free.
- Record optional hardware as a future feasibility requirement, not as an implied purchase commitment.

## 9. Required project README disclosure

Each project README should link to this common standard and state:
- Which requirements apply to that project.
- Which controls are implemented and tested, with evidence links.
- Which hardware is proposed, selected, built, or tested.
- Known gaps and operating restrictions.
- What evidence is still required before the next maturity stage.

Do not copy the entire standard into every project. Link to this document and maintain a concise project-specific adaptation.

## 10. Review and change control

Changes to this standard should be reviewed for:
- Safety impact across all seven projects.
- Compatibility with existing software contracts.
- New costs, dependencies, licences, or external service commitments.
- Testability and measurable acceptance criteria.
- Clear distinction between proposed requirements and verified evidence.

Record the reason, author, date, affected projects, and migration needs for each material change.

---

**Current status:** Proposed common standard. No physical hardware, materials, enclosure, battery, sensor, water-resistance, fire-resistance, or safety certification is validated by publication of this document.
