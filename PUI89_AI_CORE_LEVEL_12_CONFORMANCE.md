# PUI89 AI Core — Level 12 Cross-Project Conformance

**Version:** 1.0  
**Date:** 6 November 2026  
**Status:** Engineering specification and rollout gate; implementation is not yet certified across all seven projects.  
**Cost boundary:** zero-cost, dependency-light, offline-first. No paid APIs, subscriptions, cloud GPUs, metered inference, automatic model downloads, or unapproved packages.

## 1. Level 12 objective

Move PUI89 from several project-local AI foundations toward one consistent, versioned intelligence contract. Every project must describe observations, world state, proposed decisions and failures in compatible machine-readable forms, while retaining its own sensors, units, hazards, model choices and safety case.

**This is a conformance milestone, not a new-model milestone.** Do not add larger models or new dependencies until the project adapters pass the shared contract and evidence tests.

## 2. Portfolio scope

The first rollout covers these seven repositories:

1. [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI)
2. [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI)
3. [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI)
4. [PUI89 AI HOME](https://github.com/Pui89/AI-HOME)
5. [PUI89 AI NOMAD](https://github.com/Pui89/AI-NOMAD)
6. [PUI89 AI Robot Car](https://github.com/Pui89/ai-robot-car)
7. [PUI89 AI Robot Motorcycle — EasyRide](https://github.com/Pui89/ai-robot-motorcycle)

The portfolio website is the documentation and status surface, not the canonical runtime library. No standalone shared-core repository is currently recorded in this rollout. Until a separately reviewed core package exists, project adapters must declare their local implementation and contract version rather than pretending that they import one central runtime.

## 3. Canonical contracts

All seven adapters must support these four top-level records:

### Observation
Required fields:
- `schema_version`, `observation_id`, `project_id`, `scenario_id`
- `source_id`, `modality`, `observed_at`
- `quality_status`, `provenance_ref`, `evidence_ref`

Optional fields must be explicitly absent/null or populated with typed values; never replace missing evidence with a fabricated default. Preserve raw value, unit, location/context, sensor ID, received time, calibration state, uncertainty and content hash when applicable.

### WorldState
Required fields:
- `schema_version`, `world_state_id`, `project_id`, `created_at`
- `observations`, `known`, `unknown`, `conflicts`, `stale_items`

A derived state must retain references to the observations that support it. Do not collapse observed, inferred, predicted and human-confirmed facts into one category.

### ActionProposal
Required fields:
- `schema_version`, `proposal_id`, `project_id`, `created_at`
- `proposal_type`, `rationale`, `preconditions`, `risk_level`
- `confidence`, `evidence_refs`, `approval_state`, `execution_mode`

For the current PUI89 stage, `execution_mode` must be `SIMULATION_ONLY` or `ADVISORY_ONLY`. Proposals are records for review, not commands. They must not contain executable motor, steering, braking, cutter, valve, lock, alarm or building-control instructions.

### FailureReport
Required fields:
- `schema_version`, `failure_id`, `project_id`, `occurred_at`
- `failure_category`, `severity`, `expected`, `observed`
- `safe_state`, `evidence_refs`, `recovery_status`

A failure must remain visible in reports and benchmark artifacts. Do not suppress, relabel or silently retry away a failed safety check.

## 4. Shared invariants and fail-closed behaviour

Every project must test the same invariant set:

1. Missing, blank, whitespace-only or non-string source identifiers do not pass provenance validation.
2. Missing, malformed, Boolean, non-finite or timezone-ambiguous timestamps do not pass timestamp validation.
3. Missing, malformed or conflicting required evidence returns `UNKNOWN`, `ABSTAIN` or `REQUEST_HUMAN_REVIEW` as appropriate.
4. Stale, duplicated, frozen, out-of-range or uncalibrated observations are explicitly flagged.
5. Confidence is not treated as evidence quality or probability calibration unless its method and evaluation are recorded.
6. Conflicting observations remain visible; the system must not silently choose the most convenient value.
7. Every derived claim links to evidence references and the software/model/configuration identity that produced it.
8. Any proposal without required preconditions or human approval remains non-executable.
9. Any hardware-actuation claim in a simulation record fails validation.
10. Reports distinguish `NOT_RUN`, `NOT_CONNECTED`, `UNKNOWN`, `PASS` and `FAIL`; a missing test is never a pass.
11. Model outputs are candidate observations, not ground truth; preserve checkpoint ID/revision, prompt/configuration, raw output and post-processing version.
12. If model origin, publisher/control, licence, hosting path or provenance is unclear, mark `NOT_APPROVED`.

## 5. Model integration boundary

The current Hugging Face integration documentation in six project repositories describes opt-in local adapters for:
- `google/owlv2-base-patch16-ensemble` — open-vocabulary object proposals, not a project-trained detector.
- `Intel/dpt-hybrid-midas` — relative monocular depth only, not calibrated metric distance.

These are documented adapters, not proof of downloaded weights, installed dependencies, successful inference or benchmarked accuracy. The motorcycle repository's matching integration document was not found during this review and is **NOT CONFIRMED**.

Rules for every future model:
- Non-Chinese origin only, with publisher/control and hosting path checked.
- Verify model-card terms, weight licence, code licence, dependencies, security, provenance, size and hardware fit.
- No hosted inference, paid API, cloud GPU, subscription, automatic download or package installation.
- Existing local cache only unless the user explicitly approves a specific download.
- Wrap outputs in the Observation contract; attach source, timestamp, model revision, configuration, confidence method and uncertainty.
- Keep the deterministic safety gate independent from model and agent output.
- No VLM/VLA or agent may control physical hardware or make enforcement, emergency, medical, structural or road-safety decisions.

## 6. Domain adapters

| Project | Domain-specific evidence to preserve | Required boundary |
|---|---|---|
| Coconut | tree/source identity, four maturity labels, image provenance, bounding boxes, reachability evidence | no harvest action; no maturity or 0–30 m claim without held-out evidence |
| Flood Rescue | platform ID, water/terrain modality, depth/current units, localization quality, communication state | ground/boat/aerial results remain separate; no rescue or depth capability claim from generic vision |
| Screening | modality, sensor physics, calibration, sample provenance, reviewer authority | RGB/object proposals cannot establish chemical identity, guilt or enforcement action |
| HOME | building/floor/room, sensor placement, calibration, time-series baseline | not a certified fire/electrical/structural alarm or diagnosis |
| NOMAD | terrain, localization, gait/sensor state, battery reserve, owner-supervision state | no autonomous roaming, unsafe terrain entry or physical locomotion claim |
| AI Car | road-scene source, weather/visibility, vehicle-health evidence, driver advisory context | driver retains control; no steering/braking/throttle authority or road-certified ADAS claim |
| AI Motorcycle | rider-facing context, road/obstacle observations, vehicle-health evidence, alert burden | rider retains control; no autonomous riding or physical actuation |

## 7. Conformance test pack

The first shared test pack should use only Python standard library and synthetic fixtures. It must cover:
- valid minimal records for all four contracts;
- missing and malformed required fields;
- blank/non-string provenance and invalid timestamps;
- stale, duplicated, conflicting and out-of-range observations;
- uncertainty preservation and abstention;
- missing evidence references and invalid hashes;
- advisory/simulation-only proposal enforcement;
- failure-report retention and safe-state consistency;
- model identity/revision/licence metadata presence;
- no network calls, weight downloads, package installs or hardware access.

Each project reports its own test count and commit SHA. Do not sum test counts into a single PUI89 score. A passing contract suite verifies software behaviour only, not model accuracy, sensor truth, physical safety or product readiness.

## 8. Rollout order and acceptance gates

1. **Inventory:** record the actual contract files, test commands, workflows and model adapters in each repository.
2. **Baseline:** run existing free local checks and capture the exact commit, command and outcome; do not change project behaviour during baseline collection.
3. **Conformance:** implement the shared invariant test pack in each project using existing dependencies only.
4. **Model-output alignment:** adapt each model wrapper to emit the same Observation metadata and preserve raw outputs; do not download weights.
5. **Fault and regression testing:** inject missing, stale, conflicting and malformed evidence; preserve all failures in reports.
6. **Cross-project snapshot:** publish per-project PASS / FAIL / NOT_RUN / NOT_CONFIRMED with commit and workflow evidence.
7. **Model evaluation:** only after the conformance gate, select one small, licensed, non-Chinese checkpoint for a single project-specific offline test on a reviewed dataset.

Acceptance requires all seven repositories to publish the contract version, a reproducible test command, a machine-readable result, a commit SHA and explicit limitations. No automatic merge or release is permitted.

## 9. What Level 12 does not claim

Level 12 does not mean a single shared runtime has already been deployed, all seven repositories are conformant, any model has been downloaded or run, or any robot/vehicle has been built, field-tested, certified or made autonomous. It is the next controlled engineering gate toward those future capabilities.

**PUI89 — Intelligent Systems. Verifiable Decisions. Safer Outcomes.**
