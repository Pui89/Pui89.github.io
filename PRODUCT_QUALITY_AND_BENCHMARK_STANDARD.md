# PUI89 AI Robotics — Product Quality and Benchmark Standard

**Purpose:** Build products that can be compared fairly with relevant alternatives and improve against measurable acceptance criteria. This is a standard for evaluation, not a claim that PUI89 currently outperforms any competitor.

## 1. What “compare with all products” means

No honest test can compare one system with literally every product worldwide. PUI89 will compare each product against the most relevant alternatives in its actual task category, using public documentation, licence-compatible baselines, and repeatable tests. We will publish the comparison scope and date, and distinguish verified facts from vendor claims.

For each comparison, include:
- The user's task and operating conditions.
- Product/model name, version, date checked, source URL, licence, and hardware/runtime where known.
- Which capabilities were actually tested, which were taken from public documentation, and which were unavailable.
- Identical inputs, test split, ground truth, thresholds, and scoring rules wherever technically possible.
- Sample count, uncertainty/variation, failures, resource use, and total cost assumptions.
- A “not comparable” or “not tested” label where evidence is missing. Never invent a competitor score.

## 2. Shared quality dimensions

| Dimension | What to measure | Minimum evidence |
|---|---|---|
| Task performance | Task-specific quality (e.g. precision, recall, F1, IoU, localization error, route/task success) | Defined ground truth, fixed test split, baseline |
| Reliability | Failures, crashes, invalid outputs, repeatability | Automated regression tests and repeated runs |
| Uncertainty handling | Error rate on low-confidence cases, abstention quality, human-review rate | Predefined uncertainty protocol; calibration only if measured |
| Robustness | Lighting, occlusion, weather, viewpoint, sensor/input degradation, out-of-scope inputs | Stratified challenge set; limitations |
| Latency and resources | End-to-end p50/p95 latency, memory, CPU/GPU, power if measured | Named hardware, warm-up, repeated runs; no extrapolation |
| Human effort | Review time, correction rate, missed cases, workflow completion time | Observed protocol with sample size |
| Safety and control | Hazard analysis, interlocks, fail-safe behavior, human override | Tests and engineering review appropriate to system risk |
| Privacy and security | Data flow, retention, access control, dependency/security checks | Documented review; no unsupported “secure” claims |
| Cost and deployability | Cost per task, setup/support burden, offline capability, licence constraints | Transparent cost model, actual environment and licences |
| Usability and maintenance | Setup time, clear errors, docs, upgrade/reproducibility | Fresh-machine setup and usability feedback |

Metrics are task-dependent. Do not compress all dimensions into one overall score unless weights are explicitly justified and published. A leaderboard must not hide safety, cost, or missing evidence.

## 3. Benchmark protocol

1. **Define the job:** user, input, output, operating conditions, and decision that the product supports.
2. **Choose relevant alternatives:** include a simple baseline, current human workflow where measurable, and credible open-source/commercial alternatives relevant to the same job.
3. **Freeze evaluation data:** keep train/validation/test separate; use permissioned data and document inclusion/exclusion rules.
4. **Pre-register scoring:** choose metrics, thresholds, matching rules, hardware, timing method, and success criteria before inspecting test results.
5. **Run apples-to-apples tests:** same held-out examples and task definition; document unavoidable differences.
6. **Repeat and inspect failures:** report sample size, variation, subgroup performance where appropriate, and examples of failure.
7. **Report full costs:** include compute, setup, annotation, human review, maintenance, licence and any required hardware; distinguish cash cost from unpaid founder time.
8. **Publish an honest report:** results, limitations, reproducibility instructions, software/data versions, and the next improvement target.

Never tune on the final test set. Never describe a two-image experiment or synthetic-only run as real-world validation. If there is not enough evidence, state “not yet measured”.

## 4. Product-specific evaluation tracks

### Coconut Harvest AI — flagship candidate
- Detection: precision, recall, F1 and mAP at declared IoU thresholds; per-class results; false positives and misses.
- Robustness: lighting, occlusion, camera distance/viewpoint, background and orchard variation.
- Workflow: human correction time, inspection/report time, and reviewed agreement.
- System: end-to-end latency and resource use on named existing hardware.
- Robotics: simulation metrics first; no physical harvesting claim without separate mechanical, control, and safety validation.

### Flood Rescue AI — research track
- Perception/mapping: detection/localization error and map completeness against ground truth.
- Navigation: success rate, time, path length, recovery rate, collisions and hazard exposure in documented simulations.
- Robustness: sensor dropout, localization uncertainty, water/current/environment assumptions, communications loss.
- Safety: emergency-stop behavior, fail-safe transitions, and human override in simulation/test rigs.
- Simulation results must never be presented as real flood-rescue performance.

### Multimodal Narcotics Screening AI — restricted research track
- Do not claim chemical identification from appearance alone.
- Define the permitted screening task narrowly and use authorized, expert-reviewed, representative held-out data.
- Measure sensitivity/recall, specificity, false-positive rate, false-negative rate, calibration if measured, and abstention/human-review burden.
- Report subgroup/domain limitations and chain-of-custody/data provenance where applicable.
- No autonomous enforcement or consequential action based only on model output. If valid ground truth is unavailable, performance is “not yet measured”.

## 5. Release gates

- **Gate A — Reproducible software:** tests pass; installation and usage are documented; known issues listed.
- **Gate B — Baseline evidence:** task, dataset, ground truth, metrics, and simple baseline are defined.
- **Gate C — Comparative evidence:** relevant alternatives are evaluated fairly, or unavailable comparisons are clearly disclosed.
- **Gate D — Workflow value:** a real user task is evaluated with consent and documented measures.
- **Gate E — Deployment readiness:** security, privacy, licences, safety, support, total cost, and applicable requirements are reviewed.
- **Gate F — Commercial claims:** every public claim is traceable to evidence; no customer, ROI, accuracy, certification, or deployment claim without proof.

A product cannot skip a gate because a demo looks impressive. Safety-critical applications need independent domain and safety expertise beyond this checklist.

## 6. Free-first policy

Target **฿0 additional spend**. Use existing hardware, local execution, free/open-source tools and public documentation. Do not use chargeable APIs/cloud, purchase datasets/hardware, subscribe, or make financial commitments without the owner's explicit approval. Verify licences and free-tier quotas. “Open source” does not automatically mean every model or dataset is free for every use.

## 7. Standard benchmark report template

- Product/repository and commit:
- Evaluation date:
- Intended task and user:
- Candidate alternatives and source links:
- Data provenance, permission, sample count and split:
- Ground truth and annotator/review method:
- Hardware, software versions and runtime:
- Metrics, thresholds and scoring rules:
- Results per system (with uncertainty/variation):
- Failure cases and limitations:
- Human effort and end-to-end latency:
- Cash cost and non-cash effort:
- Reproduction steps:
- Release gate passed / not passed:
- Next experiment:
- Claims supported by this report:
- Claims not supported by this report:

**Principle:** Do not claim “best” until the relevant task, alternatives, test protocol, and evidence justify that conclusion. Build trust by showing exactly what is known and what remains unproven.
