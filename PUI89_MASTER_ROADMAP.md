# PUI89 Master Roadmap — Status, Work in Progress, Fixes, Next Steps and Future Upgrades

**Updated:** 29 October 2026  
**Purpose:** one transparent source of truth for what is complete, what is being checked, what remains unfinished, and the next development level across PUI89.

> **Status note:** "In progress" below means the next engineering task is identified and its evidence gate is open. It does not mean a background process is continuously running. Only completed GitHub Actions runs and committed files count as evidence.

## Executive status

- **Shared test foundation:** selected CI scopes passed 52 tests in the last verified run on 29 October 2026 (39 shared-core, 5 Coconut evaluator, 4 Coconut preflight). A later queued run must be checked before claiming it also passed.
- **Full-suite reliability:** **not finished**. Earlier broad runs exposed missing optional dependencies and import/package setup errors. The current 52-test pass does not resolve those failures.
- **AI performance:** no new genuine held-out detector results have been established by the latest combined run.
- **Simulation:** repeatable scenario plans exist for Flood Rescue and Narcotics Screening; plans are not executed simulator evidence.
- **Physical robots:** none of the three concepts is declared physically validated.
- **Cost/model gate:** no large VLM/VLA model or paid service is required for the current phase.

## Status definitions

| Label | Meaning |
|---|---|
| **Done — verified** | A named artifact or test result exists and was checked. |
| **Implemented — verification pending** | Code/document exists, but its latest run or integration is not yet confirmed. |
| **Checking** | Evidence, inputs, tests or assumptions are being inspected as the next task; do not imply a continuous background process. |
| **Fixing** | A known defect or test-environment issue has a defined repair task; do not call it fixed until a regression test passes. |
| **Blocked** | A prerequisite is missing, such as a rights-reviewed dataset, real model predictions, configured simulator or physical sensor. |
| **Planned** | Future capability; not yet evidence of implementation. |
| **Not measured / not validated** | No valid measurement or appropriate validation evidence is available. |

## 1. Coconut Harvest AI

**Overall stage:** software prototype and dataset/evaluation preparation.  
**Latest verified selected tests:** 22 passing tests in the combined run (13 shared-core + 5 evaluator + 4 dataset-preflight).

### Done — verified
- Shared PUI89 core contract tests passed in the recorded combined run.
- Detection-evaluator unit tests passed. They validate metric code, not a trained detector.
- Dataset-preflight validator was added; four tests passed against temporary synthetic CSV fixtures.
- README and safety/validation gates distinguish design intent from demonstrated capability.

### Checking / processing next
- Check the actual dataset manifest for source, licence, hashes, duplicates, annotation quality and class consistency.
- Check train/validation/test split leakage using source/tree/session identifiers.
- Inspect current dataset approval status before any training or benchmark.
- Confirm a real detector, checkpoint and reproducible prediction-export path are available before starting an accuracy benchmark.

### Fixing / unfinished
- Full project test suite still needs environment/import repair; the selected shared-core pass is not a full-suite pass.
- The new preflight tool still needs to be run against the real reviewed manifest and image files; synthetic unit tests do not verify the actual project dataset.
- No real held-out ground-truth/prediction pair has been established in the published combined run.
- No validated four-stage detector, 3D reachability, cutting/capture system or physical harvesting result is claimed.

### Next process (in order)
1. Inventory candidate images and provenance; reject or quarantine unclear rights.
2. Review labels and boxes; detect duplicates and invalid annotations.
3. Freeze a source/tree/session-aware held-out split and hash the manifest.
4. Run the validator against that real manifest and image root; fix every blocker.
5. Run the actual detector on held-out images; save raw predictions, checkpoint hash, thresholds, environment and logs.
6. Report per-class precision/recall/F1 and error examples; add mAP only with a correctly implemented and defined protocol.
7. Test uncertainty, occlusion, invalid targets, people/animal exclusion and safe hold.
8. Only then configure simulation and consider hardware feasibility/safety gates.

### Next level / future upgrades
- **Level A — data integrity:** audited, rights-reviewed dataset and leakage-safe split.
- **Level B — measurable perception:** reproducible held-out detector benchmark.
- **Level C — robust decisions:** uncertainty-aware target selection and safe-stop regression tests.
- **Level D — simulation:** recorded reachability/occlusion/collision scenarios, if a suitable simulator is configured.
- **Level E — physical prototype:** only after mechanical design review, risk assessment, guarded testing and qualified supervision.
- **Longer term:** RGB/depth/LiDAR fusion, tree/palm geometry, maturity estimation, arm/cutter/basket control and harvest verification. All remain future work until implemented and measured.

## 2. Extreme Flood Rescue AI

**Overall stage:** software prototype, input-safety gates and simulation planning.  
**Latest verified selected tests:** 13 shared-core tests passed in the recorded combined run.

### Done — verified
- Shared PUI89 core contract tests passed in the recorded combined run.
- Safety and validation documentation was added.
- A repeatable scenario matrix documents environment changes and fault injection.
- Existing README distinguishes software/synthetic demonstrations from real rescue capability.

### Checking / processing next
- Identify which current demos use synthetic/scripted inputs versus actual trained models.
- Confirm the intended simulator, version, supported vehicle model and available telemetry before claiming a simulation is running.
- Define measurable acceptance criteria and a baseline scenario before adding complexity.

### Fixing / unfinished
- Earlier broad test runs reported optional-dependency and import/setup errors; they remain separate from the shared-core pass.
- The scenario matrix is a plan, not evidence that all scenarios ran.
- No new simulator performance results are established by the latest combined test run.
- The 15 m depth figure is a design/simulation target, not a verified operating envelope.
- No physical boat, ground robot, drone, field navigation or rescue performance is validated by the combined tests.

### Next process (in order)
1. Stabilize tests and identify synthetic-only components.
2. Select one supported simulator and a minimal baseline environment; check licence, hardware demand and install size first.
3. Run one baseline scenario with a fixed seed and save configuration, logs and outputs.
4. Add scenario variations: visibility, obstacles, flow assumptions, localization loss, communication loss, conflicting sensors and low energy.
5. Measure safe-stop success, collisions, route completion, detection errors and uncertainty per scenario.
6. Add regression tests for every failure and repeat with fixed seeds.
7. Evaluate ground, boat and aerial platforms independently; do not combine unlike results.
8. Consider ROS 2/Nav2 integration only after a minimal reproducible simulation works.

### Next level / future upgrades
- **Level A — software reliability:** input validation, fault injection and clear failure reports.
- **Level B — repeatable simulation:** fixed seeds, documented environment and automated scenario reports.
- **Level C — perception/navigation evaluation:** measured errors, route metrics and uncertainty under degraded conditions.
- **Level D — multi-platform experiments:** separately configured ground/boat/aerial simulations.
- **Level E — field research:** only with qualified rescue partners, safety review, controlled trials and appropriate approvals.
- **Longer term:** SLAM/GPS-denied navigation, multimodal human/animal detection, water/current sensing, communication resilience and coordinated rescue workflow. The 15 m design target must not be represented as proven capability.

## 3. Multimodal Narcotics Screening AI

**Overall stage:** screening workflow software prototype and robotic concept.  
**Latest verified selected tests:** 13 shared-core tests passed in the recorded combined run.

### Done — verified
- Shared PUI89 core contract tests passed in the recorded combined run.
- Safety/human-review gates and a repeatable scenario matrix were documented.
- README wording distinguishes candidate categories and concept art from validated detection capability.

### Checking / processing next
- Define each intended sensor and the physical quantity it measures.
- Separate visual object/context observations from actual sensor-based chemical evidence.
- Identify lawful, licensed, provenance-documented datasets or reference samples suitable for each sensing method.
- Define the calibration procedure, human-review workflow and audit trail before any performance claim.

### Fixing / unfinished
- Earlier broad test runs reported optional-dependency and import/setup errors; they remain separate from the shared-core pass.
- The scenario matrix has not been established as executed simulation or sensor testing.
- No class-specific held-out performance has been measured by the latest combined run.
- No validated chemical sensor, X-ray capability, physical quadruped or real-world screening performance is established.
- RGB images alone cannot confirm that a substance is present.

### Next process (in order)
1. Write a sensor-to-claim table: sensor, measured quantity, limitations, calibration and permitted conclusion.
2. Define lawful sample provenance, expert-confirmed labels and independent evaluation splits.
3. Build tests for missing modalities, stale data, sensor disagreement, calibration drift, benign lookalikes and low signal quality.
4. Implement abstention/human review and preserve the reason for each alert.
5. Run a genuine held-out evaluation for each sensor/model separately; report class-specific false positives/negatives, uncertainty and sample counts.
6. Add multimodal fusion only when individual modalities have documented evidence and calibrated outputs.
7. Test the workflow in a simulation or bench setup only if the actual environment and sensors are available and identified.
8. Keep privacy, auditability and lawful human decision-making as deployment gates.

### Next level / future upgrades
- **Level A — sensor specification:** clearly defined sensing modality and validated measurement procedure.
- **Level B — data and calibration:** lawful dataset/reference sample, provenance and calibration evidence.
- **Level C — reliable decision support:** modality health, uncertainty, abstention and human-review audit.
- **Level D — multimodal evaluation:** measured fusion benefit and failure analysis, not just a combined score.
- **Level E — controlled deployment research:** independent validation, privacy/security review and legal/operational approval.
- **Longer term:** adaptive robot navigation and inspection, sensor payload integration and operator workflow. Chemical/X-ray detection and quadruped operation remain unvalidated until separately demonstrated.

## 4. PUI89 shared platform and website

### Done — verified
- Combined GitHub Actions workflow and quality dashboard exist.
- Common engineering charter and experiment-record schema exist.
- Portfolio website has English and Thai pages linking to status evidence.
- Latest verified combined run passed 52 tests across the selected scopes.

### Checking / processing next
- The newest combined run checked on 29 October 2026 completed successfully (52 selected tests); continue checking the latest run before quoting results.
- Inspect actual job logs and artifact reports rather than inferring success from the workflow file.
- Ensure the three README status sections and central dashboard stay consistent.

### Fixing / unfinished
- Repair the broader project test environment/import errors without hiding tests or turning failures into skips.
- Extend CI carefully so optional-dependency tests are explicitly classified as passed, failed, skipped or blocked.
- Verify the newly added Coconut dataset-preflight tests and workflow log are still present in the newest run.
- The current 52-test scope does not test every project module or model.

### Next process (in order)
1. Confirm the newest combined run and archive its artifact.
2. Diagnose each broad-suite failure; decide whether the cause is missing declared dependencies, packaging/import paths or genuine code defects.
3. Add the smallest justified test dependencies or isolate optional test groups; do not install heavy AI packages by default.
4. Add regression tests for repaired failures and rerun affected scopes.
5. Make reports explicitly show PASS / FAIL / BLOCKED / NOT RUN and list skipped tests.
6. Add experiment-record output for real model/simulation runs once those experiments exist.
7. Add optional VLM/VLA/ROS 2 only after licence, RAM/VRAM, storage, runtime and cost checks.
8. Review access permissions, secret handling, dependency licences and GitHub Actions usage before expanding automation.

### Next level / future upgrades
- **Level A — transparent CI:** all test scopes and failures visible.
- **Level B — shared machine-readable reports:** consistent project status, environment, failures and artifact links.
- **Level C — reproducible benchmarks:** data/model hashes, fixed configuration, metrics and error analysis.
- **Level D — simulation telemetry:** only where a simulator is configured and runs.
- **Level E — hardware telemetry:** only with suitable connected equipment and safe test conditions.
- **Longer term:** a shared PUI89 AI Core with common observation/action interfaces, world-state tracking, uncertainty representation, fault reports and mock VLA interfaces. Keep it modular and dependency-light.

## Definition of done for the next milestone

- [x] Latest combined workflow status and artifact inspected: run 40877473235 passed its selected scopes; report artifact available through 12 November 2026.
- [ ] Broad-suite failures listed with root cause and repair plan.
- [ ] Coconut real dataset preflight run or explicitly marked blocked because a reviewed manifest is unavailable.
- [ ] No detector metric published without real held-out predictions and labels.
- [ ] Flood simulator selected and a baseline scenario actually run, or simulator work explicitly marked blocked.
- [ ] Screening sensor requirements and validation data source documented, or sensing work explicitly marked blocked.
- [ ] README, dashboard and portfolio use matching status labels.
- [ ] Optional model/simulator adoption has a documented licence/resource/cost decision.

## Bottom line

The immediate upgrade is **evidence quality and reliable test infrastructure**, not adding a large model just to appear more advanced. The strongest next milestone is a clean, reproducible CI run plus one real, auditable Coconut AI benchmark. Flood simulation and screening-sensor validation follow as separate, measured workstreams.


### New verified evidence — Coconut simulation-only run (29 October 2026)

[Run 40881372992](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881372992) completed successfully: 7/7 configured scenarios and 9/9 steps passed, with zero reported scenario failures. Hardware actuation was disabled. The artifact [coconut-simulation-report-40881372992](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881372992/artifacts/12901050654) records the run configuration hash and metrics.

**Interpretation:** this is a deterministic simulation-workflow result only. It is not evidence of trained-detector accuracy, real-world harvesting, physical safety or validated reach.


## Latest checked per-project verification update — 29 October 2026

After inspecting the newest default-branch workflow jobs and their logs:

- **Coconut Harvest AI:** [run 40881602888](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881602888) passed the lightweight verification job. Report: Python 3.11.17, compile errors 0, observability smoke PASS, failure count 0. Full dependency-backed tests explicitly were not run by this preflight. [Artifact](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881602888/artifacts/12901395117).
- **Extreme Flood Rescue AI:** [run 40878523954](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40878523954) passed the lightweight verification job. Report: Python 3.11.17, compile errors 0, observability smoke PASS, failure count 0. Full dependency-backed tests explicitly were not run by this preflight. [Artifact](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40878523954/artifacts/12898129816).
- **Multimodal Narcotics Screening AI:** [run 40878549402](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40878549402) passed syntax compilation and the dependency-free observability smoke test. This does not establish sensor or model performance. [Artifact](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40878549402/artifacts/12899860349).
- **Shared combined scope:** [run 40877473235](https://github.com/Pui89/Pui89.github.io/actions/runs/40877473235) passed 52 selected tests: 39 shared-core, 5 Coconut evaluator, 4 Coconut dataset-preflight.
- **Coconut simulation:** [run 40881372992](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881372992) passed 7/7 configured scenarios and 9/9 steps, with hardware actuation disabled.

### What these new checks change

**Now verified:** the newest per-project lightweight verification jobs succeeded, with zero Python compile errors reported for Coconut and Flood, and successful syntax/observability checks for Narcotics. The selected combined test scope and Coconut simulation-only scenario run also passed.

**Still not finished:** broad dependency-backed test coverage is not established by these lightweight jobs; actual Coconut dataset provenance/annotation validation and held-out detector metrics remain blocked on real reviewed inputs; Flood simulator scenarios and Narcotics sensor/calibration evaluations have not been demonstrated by these runs. Do not interpret CI green status as AI accuracy or physical robot readiness.

### Immediate engineering queue

1. Review and classify broad-suite failures from the dedicated Python test workflows, preserving the original error and test names.
2. Make the smallest justified packaging/dependency/import fixes and add regression tests; never suppress a failing test merely to make CI green.
3. Run the Coconut dataset validator against a real rights-reviewed manifest and annotation file once those inputs are available.
4. Build the first measured Coconut detector baseline only after a real held-out split and actual detector prediction CSV exist.
5. Implement deterministic, dependency-light Flood fault-injection scenarios before installing a large simulator.
6. Specify Narcotics sensor modality, calibration, permitted claims and human-review behavior before sensor-performance testing.
7. Check GitHub Actions usage and keep optional model/simulator installation gated by licence, disk/RAM/VRAM and cost review.
