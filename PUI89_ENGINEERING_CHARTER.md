# PUI89 Engineering Charter — Evidence, Safety, and Reproducibility

**Purpose:** help external developers, researchers, and potential collaborators understand what PUI89 has built, what has been tested, and what remains a proposal.

## Working principles

1. **Evidence before claims.** Every technical claim must point to code, a test, a benchmark artifact, or a documented limitation.
2. **Failures stay visible.** Never relabel failed, skipped, blocked, or unrun tests as passed.
3. **Reproducibility.** Record the commit, environment, command, data version/hash, split policy, configuration and output artifact for each experiment.
4. **Safe by default.** Action proposals remain simulation-only until a separate hardware safety programme is designed and independently reviewed.
5. **Cost awareness.** Prefer standard-library tests and small, optional dependencies. Do not enable paid APIs, cloud GPUs, or large downloads automatically. Check repository visibility and runner allowances before expanding CI.
6. **Data rights and privacy.** Record data source, licence, permitted use, consent/privacy constraints where applicable, and hashes. Do not publish sensitive or unlawfully collected data.
7. **No unsupported universal claims.** Do not claim operation in every environment, high accuracy, chemical identification, or physical robot readiness without appropriate evidence.
8. **Human oversight.** Uncertain or consequential screening decisions must be escalated to a qualified human, not treated as an autonomous determination.

## Evidence labels

- **Implemented:** code or configuration exists.
- **Unit-tested:** named tests passed in a recorded run.
- **Measured:** an experiment has actual results and sufficient metadata to reproduce it.
- **Simulation-validated:** predefined simulation scenarios passed with recorded limits.
- **Real-world validated:** tests support performance under stated physical conditions.
- **Not run / blocked / failed:** explicit statuses; never silently omit them.

## Minimum experiment record

Every published benchmark should include:
- repository and commit SHA;
- exact command and software/runtime versions;
- dataset source, licence, manifest hash and sample counts;
- train/validation/test split policy, with source/tree/session separation where relevant;
- model/checkpoint identifier and hash, or state that no model was run;
- metric definitions, thresholds, uncertainty/limitations and failed cases;
- machine-readable results plus a human-readable summary.

## Safety gates by project

### Coconut Harvest AI
Do not infer cutting success from image classification. Measure detector/classifier performance on held-out data; separately assess localization, reachability, grasp/cut planning, worker/animal exclusion and emergency stop in simulation before any hardware testing.

### Extreme Flood Rescue AI
Do not infer rescue readiness from a concept image or a single simulated water level. Define scenario boundaries, currents/obstacles/sensor faults, safe-stop behavior and clear limits. Simulation is not real flood certification.

### Multimodal Narcotics Screening AI
Do not treat ordinary RGB images as proof of chemical identity. State what each sensor can measure, validate each modality, document false-positive/false-negative rates and use human review. Use lawful, licensed data.

## Review checklist before merging a change

- [ ] Tests are reproducible and results are recorded.
- [ ] No fabricated metrics, test outcomes or hardware claims.
- [ ] Dependencies and licences are documented.
- [ ] Data provenance and split leakage are considered.
- [ ] Failure paths and uncertainty are tested.
- [ ] Costs and automated downloads are checked.
- [ ] README distinguishes current implementation from future work.

## Immediate priority
Stabilize the shared core and dependency/import setup for full project suites; then establish the Coconut held-out detector baseline. Do not add optional VLM/VLA stacks or robotics simulation until these gates are satisfied.
