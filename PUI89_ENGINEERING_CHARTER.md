# PUI89 Engineering Charter — Evidence, Safety, and Reproducibility

**Purpose:** help external developers, researchers, and potential collaborators understand what PUI89 has built, what has been tested, and what remains a proposal.

## Working principles

1. **Evidence before claims.** Every technical claim must point to code, a test, a benchmark or a clearly marked design proposal.
2. **Reproducibility.** Record repository, commit, command, environment, input/data provenance, configuration, thresholds, outputs and limitations.
3. **Safety before autonomy.** Uncertain, stale, missing or conflicting inputs must lead to a documented degraded mode, hold, stop or human review—not an invented confident result.
4. **Cost and licence gate.** No paid API, cloud GPU, recurring service, large model download or new dependency by default. Review licence, storage, RAM/VRAM, cost and rollback before adopting any optional component.
5. **No evidence inflation.** Unit tests do not prove model accuracy; a simulator plan does not prove a scenario ran; a simulation does not prove field safety; a concept image does not prove a physical robot exists.
6. **Human accountability.** Safety-critical rescue and screening decisions remain with authorised people until a system has been independently assessed and approved for a specific use.

## Evidence levels

- **Planned:** design or test specification exists; work may not be implemented.
- **Implemented:** code or document exists; behaviour may not have been verified.
- **Unit-tested:** named automated tests passed in a recorded run.
- **Measured:** an actual model/system was run on identified data with reproducible metrics.
- **Simulation-validated:** a configured simulator ran recorded scenarios with defined acceptance criteria and repeatable logs.
- **Real-world validated:** appropriate physical trials and independent safety review support the specific claim.
- **Blocked / not run:** evidence is missing or a prerequisite has failed. Never replace this label with a success claim.

## Minimum experiment record

Record repository and commit, experiment ID, exact command, environment and dependency versions, input source/licence and hash, train/validation/test split policy, model/checkpoint hash where applicable, thresholds, random seed, counts, metrics, logs/artifacts and known limitations. Keep synthetic, real and simulated data explicitly separate.

## Shared quality workflow

The combined PUI89 workflow runs selected dependency-free tests and publishes reports. The last verified run on 29 October 2026 passed 52 tests across the selected scopes: 39 shared-core tests, 5 Coconut evaluator tests and 4 Coconut dataset-preflight tests. This is **not** a full-suite pass. Earlier broad project test runs reported optional-dependency and import/setup errors; they remain a separate repair task. Check the workflow before quoting any result as current.

## Project gates

### Coconut Harvest AI
1. Check dataset provenance, licence, image hashes, annotation quality and duplicates.
2. Prevent leakage across source/tree/session groups.
3. Run a real detector on a held-out set and report precision, recall and F1 with counts, thresholds and error examples. Do not call a single-threshold evaluation mAP.
4. Test uncertainty, geometry assumptions, people/animal exclusion, invalid targets and safe hold.
5. Run simulation only after a real simulator and scenarios are configured; hardware work requires independent risk assessment and physical safety controls.

### Extreme Flood Rescue AI
1. Separate scripted/synthetic software demonstrations from trained perception and simulator results.
2. Configure a simulator and log scenario IDs, seeds, environment, sensor failures, collisions, route outcomes and safe-stop results.
3. Test loss of localization, communication, sensor conflicts, low energy, poor visibility and out-of-envelope conditions.
4. Evaluate ground, boat and aerial platforms separately. A 15 m design target is not evidence of operation at that depth.
5. Do not claim field rescue readiness without qualified partners and staged safety approval.

### Multimodal Narcotics Screening AI
1. State what each sensor physically measures; RGB appearance alone cannot confirm chemical identity.
2. Validate sensor calibration, cross-sensitivity, provenance and lawful sample governance.
3. Test missing/conflicting modalities, drift, benign lookalikes, low signal quality and out-of-distribution inputs.
4. Report class-specific errors and uncertainty only from a genuine held-out evaluation.
5. Preserve auditability, trained human review, privacy and legal safeguards. Do not present an alert as proof that a person or item contains a substance.

## Definition of done for a project upgrade

- Acceptance criteria are written before implementation.
- Tests include normal cases, edge cases and injected failures.
- Tests are run and logs reviewed; failures are reported and fixed rather than hidden.
- A regression test covers each fixed defect.
- The README, status tracker and evidence report agree.
- Costs, licences, security and hardware risks have been checked.
- The claim uses the correct evidence level.

## Immediate shared priorities

1. Keep the combined workflow reliable and repair the broader test-environment/import failures.
2. Run and review the newly added Coconut dataset-preflight checks against real, rights-reviewed data when such a manifest is ready.
3. Measure the Coconut detector only after real held-out labels and predictions are available.
4. Implement and run the Flood Rescue and Screening scenario matrices; do not mark them complete merely because the plans exist.
5. Revisit VLM/VLA models and ROS 2 only after the above gates, with explicit licence, cost and resource checks.
