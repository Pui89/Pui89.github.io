# PUI89 AI Robotics — Product Evidence Dashboard

**Snapshot captured:** 2026-10-25 03:20 UTC (10:20 ICT)  
**Snapshot type:** Static, manually refreshed evidence snapshot from GitHub repository and Actions metadata. This page does **not** poll GitHub live. Refresh the SHAs and workflow links before reusing the status after repository changes.  
**Purpose:** Show the exact commit tested, what its completed checks establish, remaining evidence gaps, and the next engineering action. This is not an independent audit or product certification.

## Latest default-branch SHAs and CI evidence

Only completed checks tied to the exact SHA are described as current evidence. A workflow that passed on an earlier commit is identified separately.

| Project / repository | Default branch SHA | Completed checks for that exact SHA | State and evidence boundary |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | [`a609c3ecadbb4022b22dd2ceb73ba5d580a5a735`](https://github.com/Pui89/Coconut-Harvest-AI/commit/a609c3ecadbb4022b22dd2ceb73ba5d580a5a735) | [Coconut CI: success](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40146543415) — source compilation and dependency-light benchmark regression tests; [Pages build/deployment: success](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40146543338). | **Partial software verification on this SHA.** The dedicated Python test workflow last passed on earlier SHA [`ea1f3164de541ff8fe11dd26353cd100d40a10aa`](https://github.com/Pui89/Coconut-Harvest-AI/commit/ea1f3164de541ff8fe11dd26353cd100d40a10aa) ([run](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40145584089)); that run is not evidence for the current SHA. No detector accuracy, orchard generalisation, dataset rights, or physical safety is established. |
| [Flood Rescue AI — repository currently named Extreme-Flood-Rescue-AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | [`1bd02985b8ed458272aa286eb5842563d0976c35`](https://github.com/Pui89/Extreme-Flood-Rescue-AI/commit/1bd02985b8ed458272aa286eb5842563d0976c35) | [Python tests: success](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40145590956) — Python 3.10, 3.11, and 3.12. | **Partial software verification on this SHA.** A matching completed run for the broader regression, security, and Ruff checks was not found. Earlier checks on another SHA must not be treated as current verification. No field-rescue readiness, real flood navigation, amphibious capability, or physical safety is established. |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | [`0e506c24d923c938e9715370dfe103bcd99f468f`](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/0e506c24d923c938e9715370dfe103bcd99f468f) | [Python tests: success](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40144923301) — Python 3.10, 3.11, and 3.12; [local-first app regression: success](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40144923308) — Python 3.10, 3.11, and 3.12. | **These checks passed on this SHA.** They do not establish chemical identity, validated substance detection, real-world screening performance, or operational/enforcement suitability. Appearance alone cannot establish chemical identity or wrongdoing. |
| [PUI89 static website/dashboard](https://github.com/Pui89/Pui89.github.io) | [`ecca041880ac20825033ba6a2ffbc223c6eeb774`](https://github.com/Pui89/Pui89.github.io/commit/ecca041880ac20825033ba6a2ffbc223c6eeb774) | [Portfolio build/deploy: success](https://github.com/Pui89/Pui89.github.io/actions/runs/40133740040); [Pages build/deployment: success](https://github.com/Pui89/Pui89.github.io/actions/runs/40133740008). | **Website build and deployment passed on this SHA.** The dashboard content remains a manually refreshed static snapshot; successful deployment does not mean the project statuses update live. |

## Portfolio summary and next actions

| Project | Implemented evidence observed | Main evidence gap | Next action |
|---|---|---|---|
| **Coconut Harvest AI** | Dataset manifest hashing, candidate-ID path validation, annotation audit tooling, and benchmark regression checks exist in the repository. | Permissioned and representative held-out data; verified source licences; annotation correctness; tree/source/session leakage prevention; comparable detector results. The documented initial HSV baseline scored precision 0 and recall 0 at IoU ≥ 0.50 on only two images, which is not a reliable performance estimate. | Finish provenance/licence and annotation QA; keep unresolved candidates blocked; define tree/source/session-separated splits before reporting metrics. |
| **Flood Rescue AI** | Python tests pass on the current SHA; evidence-first upgrade gates are documented. | Current-SHA coverage for broader regression/security/lint checks; repeatable simulator results for sensor loss, communication loss, obstacles, degraded conditions, and recovery. | Run the missing checks against the current SHA; retain deterministic simulation scenarios and report mission success, collisions, mapping error, recovery, and human interventions. Do not claim field rescue readiness. |
| **Multimodal Screening AI** | Python tests and local-first app regression checks pass on the current SHA. | Authorized expert-reviewed ground truth; individual-modality versus fusion comparison; calibration, abstention, and missing/conflicting/corrupted-input evaluation; privacy and human-review evidence. | Test missing/conflicting modalities and uncertainty handling; require authorized human review for consequential decisions. Model output must not independently prove substance identity or wrongdoing. |
| **PUI89 dashboard** | Static site build and deployment pass on the current website SHA; project links and limitations are documented. | Dashboard is not live and this snapshot will become stale as repositories change. The current Pages workflow validates the site on pushes to `main` and scheduled runs, not on pull requests. | Refresh exact SHAs and CI evidence after material changes; consider a separate, build-only pull-request validation workflow in a later change. |

## Relevant open pull requests observed at snapshot time

These are open proposals, not completed or validated changes. Check each PR's current state before relying on it.

- **Coconut Harvest AI:** [PR #84 — protection policy (draft)](https://github.com/Pui89/Coconut-Harvest-AI/pull/84); [PR #67 — RGB-D localization input validation](https://github.com/Pui89/Coconut-Harvest-AI/pull/67); [PR #65 — 0–30 m concept requirements](https://github.com/Pui89/Coconut-Harvest-AI/pull/65); [PR #64 — engineering evidence matrix](https://github.com/Pui89/Coconut-Harvest-AI/pull/64); [PR #34 — malformed annotation-container tests](https://github.com/Pui89/Coconut-Harvest-AI/pull/34); [PR #30 — benchmark-validator tests](https://github.com/Pui89/Coconut-Harvest-AI/pull/30).
- **Flood Rescue AI:** [PR #50 — replace legacy artwork](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/50); [PR #17 — application CI and reproducible benchmark framework](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/17); [PR #13 — simulation-first mapping baseline (draft)](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/13). The repository's canonical name is now `Extreme-Flood-Rescue-AI`; the product display name remains Flood Rescue AI.
- **Multimodal Screening AI:** [PR #39 — protection policy (draft)](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/39); [PR #11 — application CI and benchmark framework](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/11); [PR #9 — robotics integration scaffold](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/9); [PR #7 — evidence-aware screening workflow](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/7).
- **Website/dashboard:** [PR #7 — this SHA-tied evidence snapshot](https://github.com/Pui89/Pui89.github.io/pull/7) is being refreshed by this branch; [PR #10 — one-command local automation](https://github.com/Pui89/Pui89.github.io/pull/10) remains a separate draft; [PR #1 — engineering standard](https://github.com/Pui89/Pui89.github.io/pull/1) remains open.

## Status labels

- **Implemented:** code or documentation exists in the repository.
- **Automated checks passed:** the named workflow passed for the exact linked SHA; this is not blanket certification.
- **Partial verification:** some checks passed on the current SHA, but a broader suite was not found on that SHA.
- **Prototype:** initial software exists, but product performance may not be established.
- **Simulation-tested:** use only when the simulator, scenario configuration, and repeatable results are retained.
- **Field-validated:** use only after an approved protocol and representative real-world results exist.
- **Deployment-ready:** use only after applicable safety, privacy, security, licensing, reliability, support, and operational requirements have been reviewed.

Automated tests help detect software regressions. They do not prove detector accuracy, robot safety, competitive advantage, or customer demand. Inspect the workflow and linked commit before quoting a result.

## Zero-spend-first development

Target **฿0 additional spending**. Use existing hardware and local/free tools. Do not make chargeable API/cloud calls, purchase data/equipment, download large model weights, or commit to paid services without explicit approval. If reliable evaluation needs unavailable resources, document the gap instead of fabricating results.

**Company principle:** publish what the evidence supports, identify what remains unknown, and make the next experiment clear.
