# PUI89 — Engineering Quality Dashboard

**Purpose:** track software verification across exactly six active PUI89 products. Shared AI Core is infrastructure, not a seventh product. This dashboard distinguishes implemented checks from results that still need to be observed or measured.


## Execution status

The historical run records later in this file are dated snapshots and must not be treated as current status. Verify the exact repository, commit and workflow run before citing a pass. Missing or stale evidence is Unknown.

## Current project comparison — six active products

| Product | Engineering focus | Current evidence boundary | Highest-priority gap |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | Four-class coconut maturity perception and harvesting workflow | Software/evaluation preparation; no current held-out real-image accuracy claim | Rights-cleared dataset, human-reviewed labels, leakage-safe split, CPU Precision/Recall/F1 and failure cases |
| [PUI89 Sentinel](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot) | Four-legged all-terrain exploration and inspection robot | Concept and requirements; no physical mobility or field validation claim | Define first supervised inspection mission and operating envelope before hardware selection |
| [PUI89 AI HOME](https://github.com/Pui89/AI-Home-Safety-Robot) | Indoor four-wheel home assistant | Complete mass target 8 kg; maximum 10 kg including battery and installed hardware | Verify design mass budget and later measure complete prototype |
| [PUI89 AI NOMAD](https://github.com/Pui89/AI-Mobile-Assistant-Robot) | Ground-use four-wheel mobile assistant robot | Not luggage or airline baggage; physical mobility unvalidated | Define supervised mobility tasks, terrain limits and safe-stop requirements |
| [PUI89 AI Global SUV](https://github.com/Pui89/PUI89-AI-Global-SUV) | Human-driver vehicle concept and advisory AI | No autonomous steering, throttle or braking claim | Road, weather and flood-risk warning evidence |
| [PUI89 AI Step-Through Scooter](https://github.com/Pui89/AI-Step-Through-Scooter) | Rider-first two-wheel step-through scooter | AI remains advisory; no water-wading or waterproof capability claim | Road-water/flood-risk warnings; unknown water means do not enter |

## Automated verification

- [Run combined quality report](https://github.com/Pui89/Pui89.github.io/actions/workflows/pui89-combined-quality-report.yml)
- [Coconut Harvest AI Actions](https://github.com/Pui89/Coconut-Harvest-AI/actions)
- Sentinel's current scope is a four-legged inspection robot dog; no physical prototype, validated mobility, integrated sensors or field performance is claimed. Previous software-workflow results are not carried forward.
- [Portfolio verification Actions](https://github.com/Pui89/Pui89.github.io/actions)

Open the newest combined workflow run. Check its conclusion and download the `pui89-combined-quality-report` artifact. The Markdown/JSON report gives each project's status; each `pui89-*-tests.txt` file contains the full unittest output, including tracebacks and failed test names. A report that says `review_required` or a project that says `failed` must remain visible and be fixed, not rewritten as a pass.

## Coconut Harvest AI — first measurable baseline

The evaluator already in the repository is `tools/evaluate_coconut_detections.py`. It compares manually reviewed ground-truth bounding boxes with predictions exported by an actual detector. It reports counts, precision, recall and F1 at declared IoU/score thresholds; it is a single-threshold box evaluator, **not mAP**, and does not run a model.

After rights review, annotation QA, and a source/tree/session-separated held-out split are complete, run:

```bash
python tools/evaluate_coconut_detections.py --ground-truth path/to/heldout_ground_truth.csv --predictions path/to/real_detector_predictions.csv --iou 0.50 --score 0.25 --output evaluation.json
```

Required ground-truth columns: `image_id,xmin,ymin,xmax,ymax,class`.
Required prediction columns: `image_id,xmin,ymin,xmax,ymax,class,score`.

Use actual model predictions and the same pixel coordinate system as the ground-truth boxes. Record the dataset/manifest SHA-256, code commit, detector/checkpoint and its hash, split policy, number of held-out images/scenes, environment and thresholds. Do not use the same images to tune and report final performance.

**Baseline status: NOT RUN / NOT MEASURED in this dashboard.** No reviewed held-out ground-truth CSV and corresponding real detector prediction CSV have been established as available evidence for this run. Empty, invented or synthetic predictions must not be reported as model accuracy. The existing evaluator's unit tests validate the metric code only; they are not a performance benchmark.

## Status definitions

- **Implemented:** code or documented test exists in the repository.
- **Passed:** the relevant automated run has completed successfully and its result is visible.
- **Measured:** a reproducible experiment reports the method, configuration, data/scenario count, environment and result.
- **Validated in the real world:** independent evidence supports the claim under the stated operating conditions.

These labels are not interchangeable. A passing unit test is not proof of model accuracy, safety certification, or a working physical robot.

## Open-source-first and safety limits

- No paid model API, cloud GPU, or automatic large-model download is required by the combined unit-test workflow.
- GitHub-hosted runner usage depends on repository visibility and account allowances; monitor usage and avoid adding paid services.
- No robot hardware is actuated by these checks.
- Do not publish accuracy, precision/recall, latency, flood depth capability, chemical-identification capability, or harvesting success without appropriate measured evidence.
- Sentinel's current scope is a four-legged inspection robot dog; no physical prototype, validated mobility, integrated sensors or field performance is claimed. Previous software-workflow results are not carried forward.

## Next engineering sequence

1. Observe the triggered combined workflow and publish its actual per-project results, including failures.
2. Fix any genuine shared-test failures before adding new model dependencies.
3. For Coconut Harvest AI, complete dataset provenance, annotation QA and leakage-safe split; then run the detector evaluator against actual held-out predictions.
- Sentinel's current scope is a four-legged inspection robot dog; no physical prototype, validated mobility, integrated sensors or field performance is claimed. Previous software-workflow results are not carried forward.
6. Add VLMs, mock VLA interfaces and robotics simulation only after the software tests are stable; preflight licence, resource use and cost before optional installs.


## New engineering gates added

- [Shared engineering charter](https://github.com/Pui89/Pui89.github.io/blob/main/PUI89_ENGINEERING_CHARTER.md): evidence labels, experiment metadata, safety principles and merge checklist.
- [Coconut dataset preflight validator](https://github.com/Pui89/Coconut-Harvest-AI/blob/main/tools/validate_coconut_dataset.py): dependency-free checks for manifest fields, duplicate image IDs, annotation box validity, optional image file/hash checks, and source/tree/session split leakage.
- [Coconut safety and validation gates](https://github.com/Pui89/Coconut-Harvest-AI/blob/main/docs/PUI89_SAFETY_AND_VALIDATION_GATES.md).
- Sentinel's current scope is a four-legged inspection robot dog; no physical prototype, validated mobility, integrated sensors or field performance is claimed. Previous software-workflow results are not carried forward.

The Coconut validator and its new unit tests have been added to the combined workflow. Their result remains **not verified until the next Actions run completes**. The validator's PASS_PREFLIGHT status is not a detector benchmark; it deliberately emits no accuracy metrics.

- [Experiment record JSON Schema](https://github.com/Pui89/Pui89.github.io/blob/main/schemas/pui89-experiment-record.schema.json): a common structure for reproducible run metadata and explicit status labels.
- Sentinel's current scope is a four-legged inspection robot dog; no physical prototype, validated mobility, integrated sensors or field performance is claimed. Previous software-workflow results are not carried forward.


## Historical evidence only — 29 October 2026 (not current active-product status)

| Project | Verified software checks in combined run | AI/model performance | Simulation / physical status | Next gate |
|---|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | 13 shared-core + 5 evaluator + 4 dataset-preflight tests passed in selected run; lightweight main checks pass | Real detector accuracy **NOT MEASURED** | Preflight tests used synthetic fixtures; physical harvesting **not validated** | Run full dependency-backed suite; validate real dataset and held-out predictions |
| [All-Terrain Inspection Robot Dog](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot) | PUI89 Sentinel quadruped inspection concept; concept and engineering requirements only | No physical prototype, validated mobility, integrated sensor suite or field performance is established | Define mission, operating envelope, hazard analysis, candidate components and validation plan |
| [All-Terrain Inspection Robot Dog](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot) | PUI89 Sentinel quadruped inspection concept; concept and engineering requirements only | No physical prototype, validated mobility, integrated sensor suite or field performance is established | Define mission, operating envelope, hazard analysis, candidate components and validation plan |

**Interpretation:** 52 passing tests in the combined run means the selected software test scopes passed. It does not mean 52 AI capability tests, a trained model benchmark, or physical robot validation. Earlier broad project test runs exposed optional-dependency/import errors and remain a separate unresolved test-infrastructure task.


## Master roadmap: unfinished work, current checks, fixes and future levels

See the [PUI89 Master Roadmap](PUI89_MASTER_ROADMAP.md) for each project's:
- verified work and test results;
- work currently identified for checking (not implied background execution);
- unresolved defects and blockers;
- ordered next process;
- next upgrade level and longer-term future;
- definition-of-done checklist.

The immediate priority is to verify the newest CI run, repair broad-suite test-environment/import failures transparently, then run the Coconut dataset preflight against reviewed real data. Model benchmarks, flood simulations and sensor tests remain unmeasured until actually run.


## Latest Coconut simulation-only run (29 October 2026)

The [Coconut Simulation Evaluation run 40881372992](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881372992) completed successfully: **7/7 configured simulation scenarios passed, 9/9 steps passed, 0 reported scenario failures**. The run recorded hardware_actuation=false and explicitly labels the result simulation-only, not real-world detector or robot validation. [Download the simulation report artifact](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881372992/artifacts/12901050654).

This is a separate simulation result and must not be added to the 52 software unit-test count or interpreted as model accuracy.


## Latest per-project lightweight verification — 29 October 2026

The newest checked default-branch lightweight verification runs completed successfully:

| Project | Run | Result in the emitted report | Explicit limit |
|---|---|---|---|
| Coconut Harvest AI | [40881602888](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881602888) | Python 3.11.17 compile checks: 0 errors; observability smoke: PASS; reported failure count: 0 | Full dependency-backed unit tests were not run in this lightweight preflight |
- Sentinel's current scope is a four-legged inspection robot dog; no physical prototype, validated mobility, integrated sensors or field performance is claimed. Previous software-workflow results are not carried forward.

Artifacts:
- [Coconut lightweight report](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881602888/artifacts/12901395117)
- Sentinel's current scope is a four-legged inspection robot dog; no physical prototype, validated mobility, integrated sensors or field performance is claimed. Previous software-workflow results are not carried forward.

The recent lightweight checks pass, but they do **not** close the previously recorded broad-suite import/optional-dependency repair task because they deliberately do not discover or execute the full dependency-backed test suites. Continue to report that work as unfinished until a dedicated broad-suite run proves otherwise.


## New shared reporting standard — 30 October 2026

- [PUI89 Verification and Failure Report Standard](PUI89_FAILURE_REPORT_STANDARD.md) defines common PASS / FAIL / BLOCKED / NOT_RUN / PARTIAL statuses and requires explicit scope and evidence limitations.
- [Machine-readable JSON Schema](schemas/pui89-failure-report.schema.json) defines a consistent structure for run metadata, test counts, failure records, blockers, measured metrics, and claims about software checks, AI evaluation, simulation, and hardware validation.
- [Coconut lightweight core tests](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40937571854) completed successfully: **36 selected tests passed** under Python 3.12 using pytest only. This is a focused core/world-state test scope, not Coconut's full test suite and not AI-performance validation.

**Next engineering step:** add a tiny report emitter and schema-validation tests to the shared core, then adopt the report format project by project. Do not publish guessed metrics or mark a planned simulator as executed.


## Report generator implementation — 30 October 2026

- Added [dependency-free report builder and contract validator](tools/pui89_report.py). It writes the shared JSON report structure, records explicit software/AI/simulation/hardware claims, and rejects invalid status/count/commit/failure fields without requiring a JSON Schema package.
- Added [six contract tests](tests/test_pui89_report.py), including valid report acceptance, missing fields, invalid status/commit, negative counts, incomplete failure details, and a CLI round-trip.
- Updated the combined quality workflow to run the report-contract tests and trigger on changes to the standard, schema, generator, and tests.
- **Verification status:** [combined workflow run 40944240576 passed](https://github.com/Pui89/Pui89.github.io/actions/runs/40944240576). All six report-contract tests passed; the three shared-core project checks also passed in that run, along with five Coconut evaluator tests and four dataset-preflight tests. The validator is a dependency-free contract check, not a complete implementation of every JSON Schema keyword.


## Automated per-project verification reports — 30 October 2026

The [combined quality workflow run 41062484106](https://github.com/Pui89/Pui89.github.io/actions/runs/41062484106) completed successfully. It generated and validated one standardized JSON report for each project from the actual selected shared-core and safety/conformance test outcomes:

- `reports/coconut-harvest-verification.json`
- Sentinel's current scope is a four-legged inspection robot dog; no physical prototype, validated mobility, integrated sensors or field performance is claimed. Previous software-workflow results are not carried forward.

The reports were uploaded with the combined Markdown/JSON report and test logs in the [workflow artifact](https://github.com/Pui89/Pui89.github.io/actions/runs/41062484106/artifacts/12979947742). Artifact retention is 14 days (through 13 November 2026).

**Scope limitation:** these reports cover only the two selected dependency-free shared suites per project. They are not full-suite, AI-performance, simulator-fidelity or physical-hardware validation results. The report generator uses the actual discovered test totals and separates passed, failed, skipped and blocked counts.

**Next:** improve failure-summary parsing for all unittest summary formats, add explicit report-schema validation, and extend the same evidence contract to separately executed project-specific suites without installing heavy AI dependencies by default.


## Shared health-gate upgrade — 31 October 2026

A matching dependency-free `pui89_core/health_gate.py` module, regression tests, and a dedicated lightweight GitHub Actions workflow have been added to all three application repositories:

- [Coconut Harvest AI health-gate workflow](https://github.com/Pui89/Coconut-Harvest-AI/actions/workflows/pui89-health-gate.yml)
- Sentinel's current scope is a four-legged inspection robot dog; no physical prototype, validated mobility, integrated sensors or field performance is claimed. Previous software-workflow results are not carried forward.

The gate checks required telemetry types, emergency-stop state, sensor freshness, perception/localization/communications health, safety-monitor health, operator approval, and finite confidence. Outcomes are limited to `SIMULATION_READY`, `SAFE_HOLD`, `STOPPED`, or `REQUEST_HUMAN_REVIEW`. Every outcome explicitly sets `physical_actuation_permitted=false`.

Ten regression tests per repository cover healthy simulation-only proposals, missing/malformed telemetry, emergency stop, unhealthy safety monitor, sensor faults, missing operator approval, low/invalid confidence, invalid thresholds, and absent input.

**Verification status:** workflows were created and queued at the time of this update; passing results have not yet been confirmed. The change adds a software-level gate, not a certified safety controller or hardware interlock.


## Long-horizon robustness evaluation — 31 October 2026

The shared platform now contains a dependency-free [PUI89 Long-Horizon Evaluation Framework](https://github.com/Pui89/Pui89.github.io/blob/main/PUI89_LONG_HORIZON_EVALUATION.md), including a deterministic runner, synthetic scenarios, regression tests and a lightweight [GitHub Actions workflow](https://github.com/Pui89/Pui89.github.io/actions/workflows/pui89-long-horizon-evaluation.yml).

The first scenario pack exercises multi-step baseline behavior, missing/stale evidence, sensor recovery, conflicting/noisy/OOD evidence, uncertainty carry-forward and latched stop behavior. Reports contain per-step state traces and injected faults.

**Verification:** the corrected long-horizon workflow completed successfully in run [41115502053](https://github.com/Pui89/Pui89.github.io/actions/runs/41115502053). This confirms the synthetic policy test workflow, not real-world robustness or AI performance.

**Scope:** synthetic policy tests only. No AI accuracy, statistical calibration, real sensor performance, simulation fidelity or physical robot safety is established. Project-specific adapters for the three applications are still pending.


## Adaptive agent orchestration policy — 31 October 2026

The central repository now includes a deterministic [adaptive orchestrator](https://github.com/Pui89/Pui89.github.io/blob/main/tools/pui89_adaptive_orchestrator.py), [ten policy tests](https://github.com/Pui89/Pui89.github.io/blob/main/tests/test_pui89_adaptive_orchestrator.py), a read-only [GitHub Actions workflow](https://github.com/Pui89/Pui89.github.io/actions/workflows/pui89-adaptive-orchestrator.yml), and the [protocol and limitations](https://github.com/Pui89/Pui89.github.io/blob/main/PUI89_ADAPTIVE_AGENT_ORCHESTRATOR.md).

The policy validates referenced evidence records and fails closed on stop conditions, invalid provenance, safety holds, human-review requests, and missing/stale evidence. Conflicting agent claims trigger specialist verification without voting or averaging. All outcomes are simulation-only; physical actuation is explicitly disabled.

**Verification status:** source, test, workflow and protocol files were fetched from the repository after commit. The latest orchestrator CI run has not yet been independently confirmed. No live multi-agent execution or project adapter is claimed.


## First project adapter — Coconut Harvest AI (31 October 2026)

The Coconut repository now contains a project adapter that converts caller-supplied maturity labels into the shared PUI89 evidence/message contract and passes them through a vendored snapshot of the policy orchestrator. Six regression tests and a dedicated workflow were added. The adapter is not a detector and does not infer maturity from images or authorize harvesting.

**Verification status:** repository files were fetched after commit; the dedicated Actions run has not yet been confirmed. The central contract/orchestrator and Coconut vendored copies require synchronization when either changes.


## Open-source resource preflight — added 31 October 2026

- [Read-only resource preflight tool](https://github.com/Pui89/Pui89.github.io/blob/main/tools/pui89_resource_preflight.py)
- [Preflight unit tests](https://github.com/Pui89/Pui89.github.io/blob/main/tests/test_pui89_resource_preflight.py)
- [Resource preflight workflow](https://github.com/Pui89/Pui89.github.io/actions/workflows/pui89-resource-preflight.yml)
- [Free-first adoption standard](https://github.com/Pui89/Pui89.github.io/blob/main/PUI89_FREE_RESOURCE_STACK.md)

The tool reports a point-in-time software/platform and system RAM/disk snapshot and checks whether selected optional packages are present. It is read-only: no network access, package installation, model download, paid service, GPU/VRAM test or inference. Unit tests and workflow status must be checked in Actions before marking this addition as CI-verified. Run locally for the user's own computer; hosted runner measurements do not describe the laptop.


## Shared world-state prototype — added 31 October 2026

- [World-state standard](https://github.com/Pui89/Pui89.github.io/blob/main/PUI89_WORLD_STATE_STANDARD.md)
- [Python prototype](https://github.com/Pui89/Pui89.github.io/blob/main/tools/pui89_world_state.py)
- [Observation JSON Schema](https://github.com/Pui89/Pui89.github.io/blob/main/schemas/pui89-world-state-observation.schema.json)
- [Six focused unit tests](https://github.com/Pui89/Pui89.github.io/blob/main/tests/test_pui89_world_state.py)
- [World-state Actions workflow](https://github.com/Pui89/Pui89.github.io/actions/workflows/pui89-world-state.yml)

This is a deterministic record organiser, not a perception or sensor-fusion model. It preserves conflicts and stale inputs, and never authorises physical action. Project adapters and CI verification are not yet confirmed.


## Mission Replay & Audit — prototype added 31 October 2026

- [Audit and replay documentation](https://github.com/Pui89/Pui89.github.io/blob/main/PUI89_MISSION_REPLAY_AUDIT.md)
- [Replay engine](https://github.com/Pui89/Pui89.github.io/blob/main/tools/pui89_mission_replay.py)
- [Nine unit tests](https://github.com/Pui89/Pui89.github.io/blob/main/tests/test_pui89_mission_replay.py)
- [GitHub Actions workflow](https://github.com/Pui89/Pui89.github.io/actions/workflows/pui89-mission-replay.yml)

Status: code and workflow committed; CI result and integration into the three project runners are not yet confirmed. Logs are not cryptographically authenticated and replay is not ground truth.
