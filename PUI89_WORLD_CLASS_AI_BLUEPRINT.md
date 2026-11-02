# PUI89 World-Class AI Blueprint — Zero-Cost, Evidence-First

**Version:** 1.0  
**Review date:** 2 November 2026  
**Scope:** Four PUI89 products and the shared PUI89 AI Core  
**Operating constraint:** no purchases, paid APIs, subscriptions, cloud GPUs, metered inference, or unapproved recurring services.

## 1. The ambition

Build PUI89 as one coherent, safety-aware AI engineering programme—not four unrelated demonstrations. The target is world-class engineering discipline: traceable evidence, reproducible experiments, strong tests, explicit uncertainty, robust failure handling, privacy, secure supply chains and independent validation.

“World-class” is a target for the quality of the engineering process. It is not a claim that the four products already have world-class model accuracy, certified safety, deployed sensors or working robots.

## 2. Portfolio architecture

Use a **shared core with four domain adapters**. Reuse contracts and verification tools; do not force unlike domains into identical models, sensors, thresholds or safety cases.

| Product | Specialist AI direction | Highest-value evidence gate |
|---|---|---|
| **Coconut Harvest AI** | Fruit detection, four-stage maturity assessment, orchard scene understanding, target localisation, uncertainty-aware harvest planning | Resolve data rights/provenance and annotation QA; then run a frozen, tree/source-separated held-out vision benchmark |
| **Extreme Flood Rescue AI** | Human/animal candidate perception, terrain/water state estimation, hazard mapping, communications-aware navigation research and mission prioritisation | Reproducible scenario and fault testing; later validate water physics, platform stability and navigation separately |
| **Multimodal Narcotics Screening AI** | Modality-quality assessment, calibrated evidence fusion, anomaly screening and human-reviewed inspection workflow | Lawful sensor/data provenance and expert-reviewed modality-specific evaluation; report false positives and false negatives |
| **HOMEGUARD AI** | Structural health monitoring, electrical/environmental condition signals, water/fire/air monitoring, acoustic/light/thermal evidence and building-level change detection | Extend sensor-quality and spatial evidence contracts; later validate calibrated sensors and building-specific baselines |

## 3. Shared PUI89 AI Core

The shared core should provide these reusable capabilities:

1. **Evidence ledger:** immutable references, source identifiers, hashes, timestamps, units, calibration metadata, quality flags and reviewer history.
2. **World-state model:** what is known, unknown, stale, changing, conflicting and inferred; preserve time and spatial context.
3. **Sensor and modality quality:** missing, stale, duplicated, frozen, clipped, drifting, uncalibrated, malformed and implausible readings.
4. **Uncertainty and abstention:** distinguish confidence from evidence quality; allow UNKNOWN, ABSTAIN, SAFE_HOLD and REQUEST_HUMAN_REVIEW.
5. **Decision and policy gate:** bounded recommendations, explicit preconditions, domain-specific allowlists and traceable rejection reasons.
6. **Scenario and fault engine:** deterministic seeds, expected outcomes, injected faults and reproducible failure reports.
7. **Evaluation and assurance:** dataset/model/configuration hashes, frozen splits, per-class metrics, calibration, latency and limitations.
8. **Continuous improvement:** detect regressions, propose changes, run tests and create reviewable pull requests; never self-approve consequential changes.

### Canonical observation contract

Every adapter should preserve, where applicable:

- `observation_id`, `project_id`, `scenario_id`, `source_id`, `modality`, `sensor_id`
- `observed_at`, `received_at`, clock/sequence information and freshness
- `value`, `unit`, `location` and domain-specific context
- `quality_status`, `calibration_status`, `provenance_ref`, `content_hash`
- `uncertainty`, `confidence_method`, `missing_reason` and review status

Do not invent absent values. Keep raw observations distinct from derived features, model predictions, hypotheses and human conclusions.

### Common decision states

- `UNKNOWN`: required evidence is absent or not interpretable.
- `ABSTAIN`: the system cannot support a reliable prediction.
- `REQUEST_HUMAN_REVIEW`: an authorised person must assess the case.
- `SAFE_HOLD`: the simulated/controlled workflow must not progress.
- `PROPOSED`: a recommendation exists but is not approved.
- `APPROVED`: an authorised human approval is recorded for the defined scope only.

A software state is not a certified physical emergency stop and does not authorise a hardware action.

## 4. High-value technology stack

Adopt technology by measured need, not fashion. The first stack should remain small, transparent and dependency-light.

| Layer | Preferred candidates | Adoption rule |
|---|---|---|
| Core contracts and reports | Python standard library, JSON, JSON Schema | Active baseline; version contracts and test compatibility |
| Testing and code quality | pytest, Ruff, static checks | Use in CI where already supported; avoid redundant test frameworks |
| Vision | OpenCV; PyTorch only for a justified experiment | No model training until data rights, labels and held-out split are approved |
| Portable inference | ONNX Runtime | Optional; use only with a verified model licence and measured CPU/RAM fit |
| Signal processing | NumPy and SciPy | Optional for actual sensor/signal analysis; compare results with known synthetic signals |
| Robotics | ROS 2, Nav2, MoveIt 2 and Gazebo | Research candidates only; choose one officially compatible OS/distribution/simulator pairing before installation |
| Simulation and world state | Existing deterministic scenario tools; simulator telemetry only when a real simulator is configured | Do not call a toy grid a physical digital twin |
| Observability | Machine-readable JSON/CSV, hashes, concise CI summaries | Keep evidence small, privacy-preserving and reproducible |
| Supply-chain security | Dependabot, OpenSSF Scorecard, least-privilege workflow permissions, pinned actions, SBOM/provenance when feasible | Enable incrementally; review findings and maintenance overhead |

Do not install all of these at once. The current standard-library and existing CI foundations are the correct default. Optional packages and models require a documented preflight: official source, maintainer, licence, provenance, security history, download size, RAM/VRAM/disk, offline operation, data restrictions and total cost.

## 5. AI model strategy

Use a **model ladder**, not one giant model for everything:

- **Level 0 — deterministic intelligence:** explicit rules, contracts, world-state tracking, quality gates and reproducible reports. This is the current foundation.
- **Level 1 — small specialist models:** only for a defined task with lawful, reviewed data and a frozen evaluation set.
- **Level 2 — multimodal models:** optional research assistants for candidate descriptions or feature proposals; never treat generated text as ground truth.
- **Level 3 — planning/VLA research:** structured plans first, strict tool/action allowlists, simulation-only execution and human approval.
- **Level 4 — edge deployment:** only after resource, latency, security, reliability and field-validation gates pass.

No model is selected or downloaded merely because it is popular or described as open source. Verify the actual weight licence, code licence, training-data disclosures, commercial-use terms, publisher/control, model provenance, security and hardware fit. A permissive code licence does not automatically mean model weights or training data are unrestricted.

**PUI89 supply-chain restriction:** do not adopt Chinese-origin AI models, AI providers or model-hosting services. Check the actual publisher, ownership/control and hosting path rather than inferring origin from a model name. If origin, licence or hosting is unclear, mark NOT APPROVED. No remote inference or automatic model download.

## 6. Automation: what can run automatically

### Safe to automate by default

1. Validate repository structure, schemas and documentation links.
2. Run syntax, unit, regression and negative tests.
3. Check evidence manifests, file hashes and data-split leakage.
4. Run deterministic synthetic scenarios with fixed seeds.
5. Inject missing, stale, conflicting, malformed and out-of-range inputs.
6. Generate machine-readable reports with commit, configuration and input hashes.
7. Compare current results with previous verified baselines and flag regressions.
8. Open a GitHub issue or pull request with proposed changes and test evidence.
9. Produce a concise cross-project status snapshot from verified workflow results.

### Must remain human-approved

- Merging code, releasing versions or changing safety thresholds.
- Approving datasets, licences, model weights or new external dependencies.
- Sending data to external services or enabling network access.
- Enabling scheduled jobs that materially increase resource use.
- Installing large simulators/models or changing the operating system.
- Any real-world screening, emergency, structural or electrical conclusion.
- Any physical robot, actuator, valve, breaker, alarm or building-control action.

No unrestricted self-modifying agent, automatic PR merge, autonomous enforcement decision or physical actuation.

## 7. Project-specific engineering priorities

### 01 — Coconut Harvest AI

- Keep the training gate closed until source rights, hashes, labels and independent annotation review are complete.
- Split by tree/orchard/source/session to reduce leakage.
- Evaluate each maturity class separately; report precision, recall, F1 and localisation metrics with counts and uncertainty.
- Treat height estimation, reachability, fruit cutting and capture as separate tasks.
- SAFE_HOLD when maturity, target location, reachability, stability, tool state or approval is unknown.
- 0–30 m remains a design target, not validated capability.

### 02 — Extreme Flood Rescue AI

- Maintain explicit water depth, current, obstacle, localisation, communications and platform state.
- Test sensor loss, stale data, communication failure, map uncertainty and emergency-stop requests.
- Report route completion, collision, false-safe and safe-hold outcomes per scenario and platform.
- Keep land, amphibious/boat and aerial concepts separately validated.
- 15 m remains a simulation/design target; do not infer buoyancy, pressure resistance or rescue capability from software tests.

### 03 — Multimodal Narcotics Screening AI

- Identify the physical quantity measured by each sensor; do not fuse modality labels without calibration and provenance.
- Use only lawful, authorised and appropriately licensed evaluation data.
- Measure false-positive and false-negative rates by class and modality, plus abstention and calibration.
- Treat an alert as a hypothesis, never proof of chemical identity or guilt.
- Require authorised human review; no automated search, detention, seizure or enforcement.

### 04 — HOMEGUARD AI

- Extend the tested foundation with building/floor/room/component/sensor context.
- Add sensor health, calibration, timestamp, drift, frozen-value, saturation and physical-plausibility checks.
- Correlate structural, electrical, water, fire, air/gas, acoustic, light and thermal evidence with explicit alternative explanations.
- Use synthetic three-floor demonstrations until calibrated real sensors and a qualified building pilot exist.
- Never replace certified fire, smoke, CO or electrical protection; never claim structural certification.

## 8. Quality gates and release evidence

Every meaningful change should pass these gates in order:

1. **G0 — cost/supply-chain:** no unapproved purchase, API, model, data source or dependency.
2. **G1 — correctness:** schema, syntax, unit, regression and negative tests.
3. **G2 — safety:** missing/stale/conflicting input, abstention, safe-hold and human-review tests.
4. **G3 — reproducibility:** fixed configuration/seed, code revision, input hashes and repeatable report.
5. **G4 — evaluation:** approved dataset, frozen split, appropriate metrics, sample counts and error analysis.
6. **G5 — simulation:** domain-specific scenarios and failure injection; label simulation-only.
7. **G6 — hardware readiness:** independent engineering review, risk analysis, hardware-in-the-loop and physical safeguards.
8. **G7 — field validation:** qualified partner, authorised setting, documented protocol and independent measurements.

A green CI badge proves only that the configured checks passed. It does not prove AI accuracy, safety certification or field readiness.

## 9. Zero-cost operating rules

- No paid APIs, hosted inference, cloud GPUs, subscriptions, paid datasets, paid runners or purchases.
- No model, dataset or simulator downloads by default.
- Prefer public-repository standard GitHub Actions where the current account and service terms permit; monitor minutes, storage, artifacts and billing settings.
- Keep CI jobs short; upload only small, non-sensitive reports with limited retention.
- Avoid large binary datasets and model weights in Git.
- Use local/offline tools only when available; do not require the user's laptop or manual terminal work for routine GitHub-side checks.
- If a proposed capability cannot be delivered without cost, mark it **BLOCKED — COST APPROVAL REQUIRED** and provide a free alternative or defer it.

“Zero cost” is an operating target, not a guarantee that every third-party service or future GitHub policy will remain free.

## 10. Execution roadmap

| Phase | Deliverable | Exit condition |
|---|---|---|
| **P0 — unify** | Shared contract, evidence labels, cost policy and four-project status matrix | All four projects report status without overstating evidence |
| **P1 — assure** | Cross-project fault cases, schema checks, provenance and regression reporting | Missing/invalid/conflicting evidence is handled conservatively |
| **P2 — measure** | First valid domain-specific benchmark, starting with Coconut data readiness | Approved data and reproducible metrics—or explicit NOT RUN |
| **P3 — simulate** | Domain-specific simulator evidence and failure analysis | Simulator/version/configuration and limits are recorded |
| **P4 — model** | Optional specialist model comparison | Licence, provenance, resource fit and held-out performance are verified |
| **P5 — partner** | Expert review, data partnerships and controlled pilots | Written permissions, risk controls and independent validation plan |
| **P6 — physical system** | Hardware integration and field validation | Separate engineering safety and field-evidence gates passed |

### First execution order

1. Reconcile the existing shared contracts; do not rewrite working project code.
2. Add HOMEGUARD to the cross-project evidence snapshot.
3. Create a single status vocabulary and common report index.
4. Audit each existing CI workflow for duplicated work, excessive artifacts and unnecessary schedules.
5. Add only missing, lightweight tests; preserve existing passing workflows.
6. Start the first genuine task-specific benchmark only when its data and ground truth are approved.

## 11. Reference standards and technical sources

These are engineering references, not claims of certification:

- [GitHub Actions and plan limits](https://github.com/pricing) — check current account limits and billing before adding workflows.
- [GitHub Pages limits and permitted use](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) — keep the portfolio informational; do not turn Pages into a commercial SaaS or transaction service.
- [OpenSSF Scorecard](https://openssf.org/projects/scorecard/) — automated open-source project security posture checks.
- [SLSA build provenance](https://slsa.dev/how-to/get-started) — stronger build integrity and provenance.
- [Sigstore](https://docs.sigstore.dev/) — artifact signing and verification.
- [Hugging Face model cards](https://huggingface.co/docs/hub/model-cards) — model task, licence and metadata review; a model card is not independent validation.
- [OpenSSF secure development guidance](https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software) — dependency selection, tests and vulnerability management.

---

**PUI89 engineering principle:** Observe carefully. Preserve evidence. Represent uncertainty. Test failure. Improve measurably. Keep people in control.
