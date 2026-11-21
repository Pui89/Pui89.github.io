# PUI89 World-Class Engineering Standard v1.0

**Version:** 1.0  
**Effective date:** 15 November 2026  
**Applies to:** Seven PUI89 products, PUI89 Shared AI Core, PTI, simulation and shared engineering infrastructure  
**Status:** Adopted portfolio engineering standard — effective 15 November 2026  
**Implementation principle:** Open-source-first, evidence-led, safety-first, modular and cost-conscious

## 1. Purpose and governing principles

This standard defines the common engineering gates required to move a PUI89 concept through requirements, architecture, simulation, prototype, verification and release review. It supplements—not replaces—the PUI89 Simple, Safe & Professional Engineering Standard, common hardware safety standard, development-stage standard, shared technology standard and product-specific requirements.

World-class means independently understandable, traceable, reproducible and testable engineering. It does not mean claiming advanced capability before evidence exists.

The following principles are mandatory:
- Requirements before features; evidence before claims; safety before performance.
- Separate shared platform capabilities from product-specific implementation.
- Prefer the simplest architecture that meets a documented requirement.
- Prefer open-source and inspectable tools with clear provenance and compatible licences.
- Design for low compute, low memory, low power, maintainability and repairability.
- Preserve human authority over consequential decisions and physical actions.
- Distinguish proposed, implemented, simulated, bench-tested, field-tested and validated capability.
- No paid service, subscription, metered API/cloud/GPU, purchase, supplier commitment, installation or download without explicit approval.
- Protect default branches; use reviewable feature branches and pull requests; do not merge or deploy without explicit approval.

## 2. Portfolio system architecture

Every product shall document:
1. Mission, users, operating environment and intended use.
2. System boundary, assumptions, exclusions and misuse cases.
3. Functional and non-functional requirements with unique IDs.
4. Hardware, software, data, human and external-system interfaces.
5. Data flow, control flow, trust boundaries and failure paths.
6. Resource budgets: compute, memory, storage, power, bandwidth, thermal envelope and cost.
7. Safety constraints, operating envelope and human-approval points.
8. Verification method and acceptance criteria for each critical requirement.

### Shared AI Core

The Shared AI Core is a common platform, not an eighth product. It should support heterogeneous compute orchestration across CPU, GPU, NPU and MCU; model sizing and quantisation; memory-aware scheduling; sensor and power-aware operation; edge inference; health monitoring; and graceful fallback.

No single processor, accelerator, model or sensor stack is assumed to fit every product. Every adapter must declare capabilities, resource requirements, supported data types, failure modes and test evidence. If an accelerator is unavailable or unhealthy, the system must fall back only to a verified safe mode; it must not silently change safety behavior.

### Shared data contracts

Use versioned, documented contracts for:
- **Observation:** source, modality, timestamp, units, frame/reference, quality, provenance and validity.
- **WorldState:** fused state, source references, uncertainty, freshness and conflicts.
- **ActionProposal:** proposed task/action, rationale, preconditions, limits, confidence/uncertainty and required human approval.
- **FailureReport:** fault code, severity, affected subsystem, evidence, safe-state transition, recovery conditions and unresolved risks.

Contracts must be schema-validated, versioned and backward-compatibility tested. Model output is never itself an actuator permission.

## 3. Perception & Task Intelligence (PTI)

Each product shall define its applicable PTI modules rather than claiming every module is deployed:
- Input-quality and provenance checks.
- Detection, classification, segmentation, tracking and spatial/depth estimation where supported.
- Scene/context understanding and sensor fusion.
- Change, anomaly and event detection.
- Confidence, uncertainty, out-of-distribution and abstention behavior.
- Task assessment, bounded proposals, human review and evidence logging.

Every evaluation must identify dataset source and licence, class definitions, label guidance, split method, sample counts, environment, hardware, software/model versions and evaluation date. Prevent leakage between training, validation and test sets.

Report task-appropriate metrics, including per-class precision, recall, F1, confusion matrix and confidence intervals where sample size permits. For safety-relevant systems, also report missed-hazard and false-safe rates, latency, stale-input rejection, abstention behavior and failure cases. Do not publish a single aggregate score without class-level and limitation context.

## 4. Robotics, mobility and physical systems

Before physical testing, document:
- Mechanical drawings, materials, load paths, tolerances and service access.
- Electrical architecture, wiring protection, connectors, grounding and isolation.
- Battery chemistry, BMS, fusing, thermal monitoring, charging and emergency isolation.
- Sensor placement, calibration, field of view, environmental limits and failure detection.
- Actuator limits, interlocks, emergency stop, safe state and loss-of-control behavior.
- Human, bystander, animal, environmental and property hazards.
- Maintenance, inspection, repair, replacement and end-of-life considerations.

Physical actuation remains disabled in software tests and simulations unless a separately approved controlled test plan exists. Never treat a software mock-up or simulation as proof of physical safety.

For road vehicles, driver/rider control of steering, throttle and braking remains human-controlled. Driver/rider-facing AI is advisory unless a separately approved safety case and applicable regulatory process authorize a different design.

## 5. Simulation and digital twin

Use a staged workflow: **model → simulate → inspect failures → revise → bench test → controlled prototype test → field evaluation**.

Select tools by task and resource constraints; potential open-source options include SimPy for process/discrete-event models, OR-Tools for routing/scheduling optimization, and ROS 2 with Gazebo for robotics simulation. Tool selection requires licence, provenance, compatibility and resource review.

Every simulation record must include:
- Simulator and version, model/configuration and scenario ID.
- Initial conditions, environment parameters, random seed where applicable.
- Sensor/physics assumptions, simplifications and known model gaps.
- Test objective, expected result, observed result and logs.
- Failure cases, repeatability and comparison with any available real measurements.

Simulation results are labelled **Simulation-only**. They do not establish real-world range, buoyancy, waterproofing, structural strength, navigation safety, battery safety or field performance.

## 6. Safety, security, privacy and resilience

Apply hazard analysis proportionate to risk. Identify hazards, hazardous situations, severity, likelihood, mitigations, residual risk, owner and verification evidence. Use independent safety controls outside model-generated outputs.

Required design behaviors:
- Unknown, stale, conflicting, malformed or out-of-scope input → abstain, warn or safe hold.
- Sensor degradation or loss → detect, report and enter a defined safe state.
- Communication loss → product-specific safe behavior; never assume connectivity.
- Power or thermal fault → controlled shutdown/isolation as designed.
- Emergency stop → independent, accessible and tested where physical actuation exists.
- Recovery → explicit preconditions and human authorization where needed.

Security controls include least privilege, dependency/licence review, input validation, secret hygiene, auditability, backup/version history and documented recovery. Do not expose credentials, private footage, internal network settings or sensitive operational security details in public READMEs or websites.

Collect only necessary data. Record source, lawful basis/consent where applicable, licence, access, retention and deletion policy. Human review is required for consequential or uncertain outputs.

## 7. Hardware traceability and cost engineering

Every candidate component record should include:
- Functional category and physical position.
- Manufacturer, brand, exact model/part number and specification.
- Country of manufacture and country of origin evidence (do not infer from brand nationality).
- Supplier, source link, quote status, stock and lead time.
- Unit price, currency, price date, tax status, shipping and warranty.
- Compatibility, interfaces, dimensions, power, environmental rating and integration risks.

Mark unknown values **UNVERIFIED**. Distinguish supplier quote, observed listing price, historical price and planning estimate. Calculate Thai landed cost with dated assumptions for freight, insurance, customs duty, VAT, brokerage, local delivery and fabrication. Avoid double counting shared equipment.

Report separately:
1. One-off prototype cost.
2. Shared tools/equipment allocation.
3. Low-volume production estimate.
4. Potential commercial unit cost.

No cost figure is a quotation or purchase authorization unless explicitly supported as such.

## 8. Verification and validation

Maintain a requirements traceability matrix linking each requirement to:
- Design element and implementation reference.
- Hazard/risk control where applicable.
- Test ID, method, environment and acceptance criteria.
- Result, logs, measured data and reviewer.
- Defect, corrective action and retest result.

Use layered testing:
- Static analysis, formatting and schema validation.
- Unit and interface/contract tests.
- Integration and regression tests.
- Fault injection and recovery tests.
- Simulation scenario tests.
- Bench and controlled physical tests.
- Domain-specific field evaluation and independent review where appropriate.

A test is **Pass** only when its stated acceptance criteria are met and evidence is retained. Unrun, blocked, partial or inconclusive tests must not be labelled passed. Failed tests require an issue, risk assessment and corrective-action record.

## 9. Product maturity and release gates

| Gate | Name | Minimum evidence |
|---|---|---|
| G0 | Defined | Mission, users, requirements, constraints, hazards and acceptance criteria |
| G1 | Architected | System architecture, interfaces, resource budgets, BOM strategy and risk controls |
| G2 | Simulated | Reproducible scenarios, logs, limitations and test results |
| G3 | Bench integrated | Identified components, integration record, bench tests and safety review |
| G4 | Prototype tested | Controlled test plan, measured results, failures, corrective actions and retests |
| G5 | Validated / release review | Domain-appropriate evidence, regulatory review, service plan, traceability and independent review |

A gate is not passed by documentation completeness alone. Physical, safety, regulatory and commercial claims require evidence appropriate to the claim. Certification may only be claimed when a recognized certification has actually been granted.

## 10. Documentation and public communication

Each product README and bilingual product page must provide:
- Product purpose and intended users.
- Current development stage and evidence status.
- Product-specific architecture and capabilities, clearly marked as proposed or implemented.
- Main safety boundaries and human-control responsibilities.
- Test evidence and known limitations.
- BOM/cost status and sourcing verification state.
- Links to the shared standard and relevant product evidence.

English and Thai content must communicate equivalent meaning. Keep public content concise; do not publish confidential engineering, personal data or sensitive security details. Concept renders must be labelled as concepts, not real product photographs.

## 11. Change control and continuous improvement

Every engineering change must include rationale, affected requirements, safety/security/privacy/licence/cost impact, tests, evidence, rollback/recovery plan and reviewer. Use small pull requests. Do not write directly to protected default branches, merge, deploy, purchase, contact suppliers or alter billing/security settings without explicit authorization.

Review this standard at least quarterly and after a serious incident, major architecture change or material change in applicable regulation. Record version, owner, review date, approved deviations and corrective actions.

## 12. Product-specific validation boundaries

- **Coconut Harvest AI:** four maturity classes—young green, mature green, yellow and brown. The 0–30 m range is a design challenge only until independently measured and validated. Harvesting actuation requires separate hazard and controlled-test approval.
- **PUI89 Sentinel:** quadruped inspection robot dog. Do not describe it as a narcotics-screening product. Validate locomotion, stability, perception, safe stop and environmental limits separately.
- **AI HOME:** indoor four-wheel assistant; target payload 8 kg, maximum target 10 kg. These are design targets until measured and verified.
- **AI NOMAD:** distinct outdoor/mobile four-wheel assistant with dog-inspired compact form and handle; target 8–10 kg, maximum target 10 kg. Do not conflate it with HOME.
- **PUI89 AI Global SUV:** driver-first advisory intelligence; no autonomous steering, throttle or braking claim.
- **PUI89 AI Step-Through Scooter:** rider-controlled two-wheel step-through concept; no autonomous steering, throttle or braking claim. Payload, flood-depth, battery safety, roadworthiness and certification remain unvalidated unless supported by evidence.

## 13. Approval checklist

- [ ] Product requirements and acceptance criteria are traceable.
- [ ] Architecture, interfaces and resource budgets are documented.
- [ ] PTI/data/model provenance and evaluation plan are recorded.
- [ ] Safety hazards, safe states and human approvals are documented.
- [ ] Security, privacy, licence and origin checks are complete.
- [ ] BOM and cost assumptions are traceable; unknowns are marked.
- [ ] Simulation/test records are reproducible and limitations are explicit.
- [ ] Failures, corrective actions and retests are recorded.
- [ ] English and Thai public descriptions are equivalent.
- [ ] Changes are in a reviewable branch with rollback/recovery path.
- [ ] No unsupported implementation, validation, certification or commercial claim is made.

**Status note:** This document defines a proposed engineering standard. It does not certify any PUI89 product or establish that any gate has been passed.
