# PUI89 AI Robotics — System Improvement Roadmap

**Approach:** free-first, evidence-led, safety-conscious and commercial-use-aware. Concepts, software tests, benchmark results, simulations and physical validation must be labelled separately.

## Portfolio priorities

| Priority | Project | Near-term deliverable | Evidence required before stronger product claims |
|---|---|---|---|
| 1 | Coconut Harvest AI | Licensed/clean dataset gate, repeatable detector baseline, harvest-planning review workflow | Held-out precision/recall, latency, field conditions, sensor calibration and supervised trials |
| 2 | Flood Rescue AI | Deterministic 0–15 m extreme-flood scenarios, hazard/communications fault tests, human-supervised mapping | Person/animal detection metrics, route/safe-stop evidence, hydrodynamic model limits and controlled field validation |
| 3 | Multimodal Screening AI | Licence register, modality-specific baseline, uncertainty and human-review workflow | Valid ground truth, false-positive analysis, sensor calibration, legal/privacy review and independent validation |
| Shared | PUI89 website | Consistent status cards, demos, evidence links, limitations and contact path | Every public claim linked to a reproducible test, documented dataset or clearly labelled concept |

## Shared engineering requirements
- Reproducible CI and tests on supported Python versions; review failing or stale workflows instead of assuming green status.
- Pin and audit dependencies; use least-privilege tokens, secret scanning, dependency review and supported GitHub Actions.
- Deterministic test fixtures; explicit timeouts; no hidden network calls or automatic model/data downloads in ordinary tests.
- Structured logs with timestamps, scenario/model/config versions, input provenance and clear error reasons.
- Safe failure: invalid, stale, contradictory or missing inputs should trigger an explicit reject/abstain/hold path.
- Performance measured on named hardware with dataset version, commit SHA, model hash and methodology. Never publish fabricated scores.
- Accessibility, clear installation instructions, small sample demos, documented resource requirements and no surprise cloud/API charges.

## Automation policy
Automate linting, unit tests, schema validation, license-register checks, documentation link checks and benchmark-report format validation. Keep model downloads, dataset acquisition, physical actuation, safety overrides and commercial release decisions behind explicit human approval.

## 90-day evidence-led sequence
1. **Weeks 1–2:** audit open pull requests and CI; resolve stale status statements; create dataset/license registers.
2. **Weeks 3–4:** freeze small legal evaluation samples and write leakage-safe split manifests.
3. **Weeks 5–8:** run deterministic baselines and fault-injection tests; publish real metrics and failure cases.
4. **Weeks 9–10:** improve usability, setup instructions, demo evidence and human-review flows.
5. **Weeks 11–13:** customer discovery and supervised pilot design; document support, maintenance, privacy, licensing and risk boundaries.

## Product-readiness gates
- **G0 — traceability:** source, licence, requirements and limitations documented.
- **G1 — software reliability:** tests and CI pass; errors fail safely.
- **G2 — measurable performance:** independent held-out evaluation with reproducible results.
- **G3 — workflow validation:** users can understand outputs, uncertainty and escalation.
- **G4 — deployment validation:** privacy, security, maintenance, support and applicable regulatory obligations reviewed.
- **G5 — commercial claim:** only claims supported by evidence from the intended operating environment are published.

## Commercial principle
Commercial potential is not the same as current sellability. Begin with a narrow software or decision-support offering that can be evaluated by a real user. Do not sell a life-safety or narcotics-detection guarantee before the relevant hardware, data, validation and approvals exist.