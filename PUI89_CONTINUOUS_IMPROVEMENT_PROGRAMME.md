# PUI89 Continuous Improvement & Intelligence Programme

**Status:** approved strategic direction; implementation is staged and evidence-gated.  
**Scope:** Coconut Harvest AI, Extreme Flood Rescue AI, Multimodal Narcotics Screening AI, the proposed HOMEGUARD AI project, and the shared PUI89 AI Core.

> **North star:** Intelligent Systems. Verifiable Decisions. Safer Outcomes.

PUI89 should continuously discover where its systems can improve, produce testable recommendations, and preserve evidence that each approved change works. Automation may inspect, report, create isolated proposals and run checks. It must not silently alter safety-critical behaviour, merge consequential changes, operate hardware, or convert an unverified claim into a verified result.

## 1. Shared intelligence capability catalogue

The following capabilities form a common vocabulary and architecture. They are not a claim that every capability is already implemented.

1. **Evidence Integrity** — detect missing, contradictory, unreliable or incomplete evidence.
2. **Loss Intelligence** — detect assets, quantities, records or observations that appear to be lost or missing.
3. **Change Intelligence** — compare current observations with previous observations and established baselines.
4. **Deterioration Intelligence** — identify supported trends that indicate worsening condition.
5. **Predictive Intelligence** — estimate possible future states, with uncertainty and validation limits.
6. **Decision Intelligence** — recommend checks or actions while preserving human authority.
7. **World Model Intelligence** — represent entities, components, states, relationships and time.
8. **Root Cause Intelligence** — rank plausible causes and show the evidence for and against each; do not present correlation as causation.
9. **Spatial Intelligence** — locate observations and understand affected areas and connected components.
10. **Adaptive Intelligence** — adjust monitoring priorities to context within approved, bounded policies; never silently relax safety limits.
11. **What-If Intelligence** — evaluate hypothetical scenarios in simulation or analytical models.
12. **Prevention & Recovery Intelligence** — track unresolved issues, maintenance, repair evidence and recurrence.
13. **Trust & Sensor Intelligence** — monitor calibration status, data quality, sensor health, drift and provenance.
14. **Impact Intelligence** — estimate potential consequences and prioritize review without overstating certainty.
15. **Relationship Intelligence** — identify dependencies and possible cascading effects between systems.
16. **Hidden Pattern Intelligence** — identify unusual combinations or sequences that merit investigation.
17. **Active Investigation Intelligence** — recommend the next observation or measurement that could reduce uncertainty.
18. **Confidence Calibration Intelligence** — compare stated confidence with observed performance on suitable evaluation data.
19. **Resilience Intelligence** — test missing data, sensor failure, communication loss, corrupted inputs and simultaneous faults.
20. **Knowledge Evolution Intelligence** — preserve verified lessons, decisions, failures and regression cases across versions.
21. **Continuous Improvement Intelligence** — discover, rank, propose, validate and document upgrades.

The six foundational intelligence functions (1–6) are the decision lifecycle. The remaining capabilities strengthen context, diagnosis, prediction, resilience and learning.

## 2. Shared PUI89 AI Core architecture

Use reusable contracts and project adapters rather than forcing every project into one monolithic model.

- **Observation & Evidence Layer:** source, timestamp, location/context, units, freshness, quality, calibration, hash/reference and explicit unknown/missing state.
- **World Model & Memory:** current, historical, predicted and verified states must remain distinguishable.
- **Integrity & Trust Engine:** validate schemas, provenance fields, time ordering, missingness, contradictions, stale values and sensor-health flags.
- **Change, Loss & Deterioration Engine:** compare observations with an appropriate baseline and distinguish real change from data gaps or sensor faults.
- **Reasoning & Investigation Layer:** show candidate explanations, counter-evidence, uncertainty and the next useful measurement.
- **Prediction & What-If Layer:** produce bounded forecasts and scenario results with assumptions, model/version and limitations.
- **Decision & Safety Guardian:** return a recommendation, abstention, request for evidence or human-review state. No direct actuation.
- **Intelligence Assurance:** attach evidence references, software/configuration version, checks, uncertainty, reviewer status and decision history.
- **Continuous Improvement Engine:** create prioritized engineering proposals and regression tests from observed failures.
- **Reporting Layer:** machine-readable JSON plus a human-readable daily/weekly engineering summary.

Each project adapter must preserve domain-specific units, hazards, privacy rules and validation criteria. Cross-project dashboards must not combine incomparable performance metrics into a single score.

## 3. Project-specific intelligence

### Coconut Harvest AI
Prioritize fruit/tree identity, four maturity classes, source and annotation provenance, height/reach uncertainty, harvest-readiness evidence, safe operating envelope, worker/animal proximity and post-harvest verification. Unknown or conflicting readiness, reach, stability or approval must result in abstention / safe hold. No cut or actuator command is authorized by this programme.

### Extreme Flood Rescue AI
Prioritize victim-location uncertainty, water depth/current/flow evidence, stale or conflicting sensors, communications loss, platform-specific mobility limits, energy/return planning and scenario resilience. Ground, boat and aerial concepts require separate evidence. Simulation does not establish flood physics, buoyancy, depth capability or rescue performance.

### Multimodal Narcotics Screening AI
Prioritize modality provenance, calibration, time alignment, missing/conflicting signals, false-positive/false-negative evaluation, privacy and authorized human review. An AI score or RGB image is not proof of chemical identity or wrongdoing. No autonomous search, accusation, detention or enforcement decision.

### HOMEGUARD AI (proposed project)
Prioritize building/floor/room world model; daily condition comparison; water, electrical, fire/smoke, earthquake/vibration and structural-health monitoring; sensor trust; root-cause investigation; long-term deterioration; post-event review; maintenance verification. Certified alarms and qualified professionals remain authoritative. AI cannot certify structural safety or autonomously operate building electrical systems. Simulated three-floor building demonstration is the first proposed milestone; no physical building monitoring is claimed until sensors and a pilot are validated.

## 4. Daily intelligence report contract

A daily report should answer:

1. What changed since the last valid observation?
2. What is missing, stale or contradictory?
3. What appears lost or has reduced unexpectedly?
4. What is deteriorating relative to a documented baseline?
5. What might happen next, and with what uncertainty?
6. What should be checked, by whom, and what evidence would resolve the issue?

Every finding must include a status such as OBSERVED, INFERRED, PREDICTED, UNKNOWN, MISSING, CONFLICTED or NOT_RUN; a time window; source/evidence references; severity rationale; uncertainty; and recommended verification. Do not create a new incident every day for an unchanged unresolved issue: carry its incident ID forward and record whether it is new, ongoing, resolved or recurring.

No live daily report is possible until valid project data or sensors are connected. Synthetic examples must be labelled **ILLUSTRATIVE / SIMULATION-ONLY**.

## 5. Continuous improvement automation

### Event-driven checks
Run lightweight checks on pull requests and relevant pushes:
- syntax, formatting and dependency-free unit tests where available;
- schema, timestamp, provenance, missing/stale/conflicting-input tests;
- regression and deterministic scenario tests;
- security/dependency/licence checks already configured;
- evidence-report consistency and artifact validation;
- documentation/status consistency checks.

### Weekly engineering review
Produce a report of:
- current workflow outcomes and test failures;
- new issues, unresolved defects and regressions;
- missing evidence and NOT_RUN gates;
- dependency, licence and security changes;
- proposed improvements ranked by safety impact, evidence, feasibility, cost, risk and cross-project reuse;
- next recommended task and the reason it is highest value.

### Monthly architecture review
Review shared contracts, project adapters, benchmark quality, uncertainty calibration, technical debt, security/privacy, reproducibility, cost and grant/partner demonstration readiness.

**Scheduling rule:** reuse existing workflows first. Before adding or changing cron schedules, runners, artifact retention or external services, verify the repository/account cost implications. No paid APIs, subscriptions, cloud GPUs, large runners, model downloads or automatic dataset downloads. If cost or licence is uncertain, leave the capability disabled and mark it NOT_APPROVED.

## 6. Upgrade proposal and release gates

Every automated upgrade proposal must include:
- problem statement and evidence reference;
- expected benefit and affected projects;
- scope and files to change;
- risk and rollback plan;
- cost, dependency and licence review;
- tests and acceptance criteria;
- known limitations and claims it does not support.

Required sequence:

1. Discover and record the baseline.
2. Rank opportunities; avoid adding features without demonstrated value.
3. Create a dedicated branch and isolated pull request.
4. Run relevant tests and security/evidence checks.
5. Inspect failures; never hide or relabel failed checks as passed.
6. Require human review for safety-critical logic, data/model changes, privacy changes, releases and hardware-related interfaces.
7. Merge only after approval and passing required checks.
8. Record the commit, test results, artifacts, reviewer and rollback path.
9. Add a regression test for each confirmed software defect.

No bot may auto-merge safety-critical changes, change thresholds or decision policies without review, approve training data, download model weights, spend money, expose private data, or issue physical commands.

## 7. Evidence and status vocabulary

Use these labels consistently:

- PROPOSED — planned, not implemented.
- IMPLEMENTED — code or workflow exists.
- TESTED — a named test ran; include command, commit and result.
- SIMULATION-ONLY — synthetic or simulated result, not field evidence.
- MEASURED — reproducible measurement on a documented evaluation set.
- VERIFIED — independently reviewable evidence supports the specific claim.
- NOT_RUN — no relevant check was run.
- NOT_VALIDATED — real-world capability is not established.
- NOT_APPROVED — blocked by cost, licence, safety or human approval.

A green workflow badge proves only that the configured workflow completed successfully. It does not prove AI accuracy, sensor truth, physical safety, certification or field readiness.

## 8. Staged implementation roadmap

### Stage A — consolidate what already exists
Inventory the three current repositories' shared-core contracts, evidence benchmark, world-state validation, provenance guards, regression tests and GitHub Actions. Reuse working components; do not duplicate them. Publish a dated baseline and gaps.

### Stage B — common reporting contract
Define and test the daily/weekly JSON report schema, status vocabulary, evidence references, incident continuity and cross-project adapter contract using standard-library tooling first.

### Stage C — improvement intelligence
Generate a deterministic improvement report from repository evidence: failed checks, NOT_RUN items, unresolved issues, stale documentation and prioritized recommendations. The first version should be rule-based and auditable, not dependent on a paid or downloaded LLM.

### Stage D — HOMEGUARD demonstration
Build a clearly labelled synthetic three-floor building dataset and demonstration for sensor quality, time-series baselines, FFT/PSD features, missing data, change detection and daily intelligence reporting. Validate against known synthetic signals. This is not a real building assessment.

### Stage E — validated pilots
Only after suitable sensors, calibration, privacy/legal review, qualified partners and a documented pilot plan are available, evaluate real measurements. Keep engineering judgement and emergency systems authoritative.

## 9. Immediate next actions

1. Audit existing workflows and shared-core implementations in the three repositories; preserve working automation.
2. Create a dated cross-project baseline and identify genuine gaps rather than reimplementing existing checks.
3. Define the shared daily/weekly intelligence report schema and tests.
4. Build the HOMEGUARD synthetic three-floor demonstration.
5. Generate the first weekly engineering improvement report.
6. Prepare concise, evidence-backed technical demonstrations for grant and strategic-partner discussions.

**Success is not the number of features or AI models. Success is measurable improvement in evidence quality, reliability, safety, reproducibility and useful outcomes.**
