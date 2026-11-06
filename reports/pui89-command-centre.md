# PUI89 AI Robotics — Cross-Project Status Dashboard

**Evidence snapshot:** 6 November 2026 (UTC)  
**Scope:** six active project areas and the public PUI89 website. This is a point-in-time read of GitHub default-branch commits, workflow runs and open pull requests. It is not a live monitor, independent audit, product certification or field-performance assessment.

## Portfolio at a glance

| Project | Main-branch snapshot | Automated evidence | Current stage / next priority |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | [75c92c1](https://github.com/Pui89/Coconut-Harvest-AI/commit/75c92c1c13d0729e44e41ed7f650b95787d664d1) · 6 Nov | Main-branch PUI89 Automated Verification, Shared Intelligence Contract, Free Local Checks, Pitfall Detector Checks and Pages deployment passed for this SHA. [Actions](https://github.com/Pui89/Coconut-Harvest-AI/actions) | Software and dataset-audit foundation. Next: permissioned, representative coconut imagery; reviewed labels; leakage-safe held-out evaluation; detector comparison. Harvesting robot, reach, payload and field safety remain unvalidated. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | [9a003ca](https://github.com/Pui89/Extreme-Flood-Rescue-AI/commit/9a003cae7379c39337b90dab6af6048d524917ef) · 6 Nov | Main-branch Automated Verification, Free Local Checks, Pitfall Detector Checks and Python tests passed for this SHA. [Actions](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions) | Simulation-first rescue planning and safety-gate foundation. Next: repeatable scenarios, navigation/recovery evidence, collision and intervention metrics. Amphibious mobility, carrying people and field rescue are not validated. |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | [c7836d9](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/c7836d980a0dd93012e4ff4620e439a169293575) · 6 Nov | Main-branch Automated Verification, Free Local Checks, Software and Observability Checks, Shared Intelligence Contract, local-first regression and Python tests passed for this SHA. [Actions](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions) | Screening-assistant software foundation. Next: lawful, authorised and expert-reviewed data; modality-specific evaluation; uncertainty, provenance and human review. No validated narcotics detector or enforcement capability is claimed. |
| [HOMEGUARD AI — HOME / NOMAD](https://github.com/Pui89/Guard-Ai-Home-Nomad) | [76322d0](https://github.com/Pui89/Guard-Ai-Home-Nomad/commit/76322d01a8b02f872fa0446ffe8377643e318896) · 6 Nov | HOMEGUARD CI, HOMEGUARD Security and PUI89 Shared Intelligence Contract passed for this SHA. [Actions](https://github.com/Pui89/Guard-Ai-Home-Nomad/actions) | Software-first home/outdoor safety foundation. NOMAD robot-dog redesign is in [PR #28](https://github.com/Pui89/Guard-Ai-Home-Nomad/pull/28), currently **blocked by merge conflicts**; main still shows the earlier four-wheel suitcase concept. Proposed weight target remains 8–10 kg, maximum 12 kg; not a measured built robot. |
| [PUI89 AI Robot Car](https://github.com/Pui89/ai-robot-car) | [58870aa](https://github.com/Pui89/ai-robot-car/commit/58870aa977b8c079769249ae4b01d3f46da269fb) · 6 Nov | Quality checks passed for this exact main-branch SHA. [Actions](https://github.com/Pui89/ai-robot-car/actions) | Early software and vehicle-intelligence concept. Open PRs: [#1 security baseline](https://github.com/Pui89/ai-robot-car/pull/1), [#2 commercial-readiness standard](https://github.com/Pui89/ai-robot-car/pull/2). No built vehicle, road testing or autonomous driving validation. |
| [PUI89 AI Robot Motorcycle](https://github.com/Pui89/ai-robot-motorcycle) | [77846bb](https://github.com/Pui89/ai-robot-motorcycle/commit/77846bb3076ee84ab25c2653a7992f2df6412c2a) · 6 Nov | Latest visible main-branch Quality checks passed on an earlier commit; the current main SHA has no matching check-run in this snapshot. The new design PR #4 has a successful basic-checks run. [Actions](https://github.com/Pui89/ai-robot-motorcycle/actions) | Rider-centred advisory concept. [PR #4](https://github.com/Pui89/ai-robot-motorcycle/pull/4) adds new concept art and design documentation; PR is open and mergeable. No physical build, sensor integration or road test. |

## Website and publishing status

- [PUI89 English and Thai homepages](https://github.com/Pui89/Pui89.github.io) are being updated to present all six project areas.
- [Website PR #118](https://github.com/Pui89/Pui89.github.io/pull/118) publishes the motorcycle concept artwork to both language pages. HTML validation, website checks and build passed; deployment is skipped for a pull request and will occur only after merge.
- [Website PR #115](https://github.com/Pui89/Pui89.github.io/pull/115) is an older broader bilingual update and remains open; it is not treated as published.
- [Website PR #119](https://github.com/Pui89/Pui89.github.io/pull/119) contains HOME indoor robot pages and remains open.
- The HOMEGUARD NOMAD dog redesign is not yet on main because project PR #28 has merge conflicts.

## Cross-project engineering standard

The shared direction is to reuse common contracts and safeguards rather than duplicate project-specific infrastructure:

- Versioned `Observation`, `WorldState`, `ActionProposal` and `FailureReport` interfaces.
- Source, timestamp, freshness, provenance, calibration and uncertainty tracking.
- Safety gates and human approval; proposal-only until a separate safety case permits any hardware pathway.
- Repeatable tests, structured failure reports and evidence-linked benchmark records.
- Explicit handling of missing, stale, noisy, conflicting or corrupted inputs.
- Clear reporting of what is known, unknown, changed, failing and what evidence would prove improvement.

The presence of a shared-contract workflow passing on a commit proves only that the named software checks passed. It does not prove all six projects are fully integrated or that their physical concepts are safe.

## Priority order

1. Stabilise and reuse the shared AI Core contracts and reporting.
2. Continue project-specific deterministic tests and simulation scenarios.
3. Improve dataset provenance and evaluation quality for Coconut and Screening.
4. Improve flood simulation coverage and fail-safe evidence.
5. Resolve HOMEGUARD NOMAD PR #28 conflicts and verify the robot-dog artwork before merging.
6. Merge AI Motorcycle PR #4, then website PR #118; update the site only after successful checks.
7. Keep AI Car and Motorcycle software-only/simulation-first until separate engineering and safety reviews justify hardware work.

## Cost, security and evidence boundaries

- Maintain the strict zero-cost policy: no paid APIs, subscriptions, metered services, cloud GPUs, model downloads or new packages without explicit approval.
- Review third-party action changes, licences, dependencies and supply-chain risk before merging.
- Do not claim real-time performance, field readiness, autonomy, waterproof/fire resistance, certification or commercial deployment without relevant test evidence.
- Workflow success is commit-specific. A cancelled run is not a pass; a missing run is unknown, not a failure or success.
- This report reads GitHub metadata; it does not execute tests or change project repositories.
