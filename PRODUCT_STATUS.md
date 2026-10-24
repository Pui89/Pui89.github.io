# PUI89 AI Robotics — Product Evidence Dashboard

**Evidence snapshot captured:** 2026-10-24 03:36 UTC  
**Snapshot type:** Static, manually refreshed snapshot from GitHub's repository, pull-request, and Actions APIs. This page does **not** poll GitHub live. Refresh the SHAs and run links before reusing this status after repository changes.  
**Purpose:** Show which exact repository commits have completed checks, what those checks establish, and the remaining evidence gaps. This is not an independent audit or product certification.

## Latest default-branch SHAs and CI evidence

Each row identifies the default-branch SHA read during this snapshot. Only checks completed for that exact SHA are labelled as passing.

| Repository | Default branch SHA | Latest completed checks for that exact SHA | State and caveat |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | [`351b613ae4b1a105f93020ad27235cf6c8519af9`](https://github.com/Pui89/Coconut-Harvest-AI/commit/351b613ae4b1a105f93020ad27235cf6c8519af9) | [Python tests: success](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40039803975); [regression tests: success](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40039803851); [CI: success](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40039803890); [security: success](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40039803839); [Ruff: success](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40039803792); [Pages build/deployment: success](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40039804244) | **Automated checks passed on this SHA.** These checks do not establish detector accuracy, dataset licensing, orchard generalisation, or physical safety. |
| [Flood Rescue AI](https://github.com/Pui89/Flood-Rescue-AI) | [`30b6020f5e00de2cae9bee8f05b9506d38d2c8f6`](https://github.com/Pui89/Flood-Rescue-AI/commit/30b6020f5e00de2cae9bee8f05b9506d38d2c8f6) | [Python tests: success](https://github.com/Pui89/Flood-Rescue-AI/actions/runs/40057664809) | **Partial verification on this SHA.** A matching run for the broader regression, security, and Ruff workflows was not found. Those checks passed on the previous SHA [`b087dfb1d1da87412d1edeeb568bbe84b14a0348`](https://github.com/Pui89/Flood-Rescue-AI/commit/b087dfb1d1da87412d1edeeb568bbe84b14a0348) ([regression](https://github.com/Pui89/Flood-Rescue-AI/actions/runs/40057057363), [Ruff](https://github.com/Pui89/Flood-Rescue-AI/actions/runs/40057057278), [security](https://github.com/Pui89/Flood-Rescue-AI/actions/runs/40057057273)); do not treat those as verification of the current SHA. |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | [`aa874329d654d1f1e36e5b5c5ec1c02d1bfa1357`](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/aa874329d654d1f1e36e5b5c5ec1c02d1bfa1357) | [Python tests: success](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40052725805); [local-first app regression: success](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40052725811) | **These two checks passed on this SHA.** An earlier Python test run failed on the previous SHA `2ab470b6aeb18f13a08b0a82edd7697a7ffeb161` ([failed run](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40052463751)); the later run on the current SHA succeeded. |
| [PUI89 static website/dashboard](https://github.com/Pui89/Pui89.github.io) | [`c7a6446f0f319f791dff33f233ba76aa25f9922a`](https://github.com/Pui89/Pui89.github.io/commit/c7a6446f0f319f791dff33f233ba76aa25f9922a) | [Portfolio deployment: success](https://github.com/Pui89/Pui89.github.io/actions/runs/40045239252); [Pages build/deployment: success](https://github.com/Pui89/Pui89.github.io/actions/runs/40045238805) | **Website build/deployment checks passed on this SHA.** This does not mean the project status shown here is dynamically refreshed. |

## Portfolio summary

| Project | Current evidence | Not yet established | Next priority |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | Dataset manifest hash verification and candidate-ID path checks are merged into the observed default-branch history; automated checks listed above passed on the snapshot SHA. | Permissioned, representative held-out evaluation; reliable detector performance; orchard generalisation; autonomous harvesting; physical safety. The documented initial HSV baseline scored precision 0 and recall 0 at IoU ≥ 0.50 on only two images. | Finish provenance/licence review and annotation QA; create tree/source/session-separated held-out data; compare detectors on the same fixed split. |
| [Flood Rescue AI](https://github.com/Pui89/Flood-Rescue-AI) | Sensor-failure safe-stop tests are merged; Python tests passed on the snapshot SHA. | Real flood navigation, amphibious mobility, human evacuation performance, field rescue capability, physical safety, and full CI confirmation on the current SHA. | Run and retain full checks on the current SHA; add repeatable simulation metrics for mission success, collisions, mapping error, recovery, and human interventions. |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | Python tests and local-first application regression checks passed on the snapshot SHA. | Validated substance detector, chemical identity, real-world screening performance, or operational/enforcement suitability. | Define a narrow lawful task and authorized expert-reviewed ground truth; evaluate individual modalities against fusion, missing/conflicting inputs, calibration, and abstention. Appearance alone cannot establish chemical identity. |

## Open work and blockers observed

These are open pull requests at snapshot time, not completed work:

- **Coconut Harvest AI:** [PR #67 — RGB-D localization input validation](https://github.com/Pui89/Coconut-Harvest-AI/pull/67), [PR #65 — 0–30 m concept requirements](https://github.com/Pui89/Coconut-Harvest-AI/pull/65), [PR #64 — engineering evidence matrix](https://github.com/Pui89/Coconut-Harvest-AI/pull/64), [PR #34 — malformed annotation-container tests](https://github.com/Pui89/Coconut-Harvest-AI/pull/34), and [PR #30 — benchmark-validator tests](https://github.com/Pui89/Coconut-Harvest-AI/pull/30).
- **Flood Rescue AI:** [PR #17 — application CI and reproducible benchmark framework](https://github.com/Pui89/Flood-Rescue-AI/pull/17), [PR #13 — simulation-first mapping baseline](https://github.com/Pui89/Flood-Rescue-AI/pull/13), and [PR #33 — project overview wording](https://github.com/Pui89/Flood-Rescue-AI/pull/33). The immediate verification gap is that broader checks were not observed on the current default-branch SHA.
- **Multimodal Narcotics Screening AI:** [PR #11 — application CI and benchmark framework](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/11), [PR #9 — robotics integration scaffold](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/9), and [PR #7 — evidence-aware screening workflow](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/7).
- **Website/dashboard:** [PR #1 — engineering standard](https://github.com/Pui89/Pui89.github.io/pull/1) remains open. This status snapshot is a separate change and does not replace or merge that PR.

## Status labels and interpretation

- **Implemented:** code or documentation exists in the repository.
- **Automated checks passed:** the named workflow passed for the exact linked commit; this is not blanket certification.
- **Partial verification:** some checks passed for the current SHA, but a broader suite was not found on that SHA.
- **Prototype:** initial working software exists, but product performance may not be established.
- **Not yet measured:** there is no adequate, comparable evidence for the claim.
- **Simulation-tested:** only use when a specified simulator, scenario configuration, and repeatable results are retained.
- **Field-validated:** only use after an approved protocol and representative real-world results exist.
- **Deployment-ready:** only use after applicable safety, privacy, security, licensing, reliability, support, and operational requirements are reviewed.

Automated tests help detect software regressions. They do not prove detector accuracy, robot safety, competitive advantage, or customer demand. Inspect the workflow and linked commit before quoting a result.

## Next actions

1. **Coconut Harvest AI:** complete provenance and annotation checks; maintain leakage-safe splits; report detector metrics only from a documented, held-out evaluation.
2. **Flood Rescue AI:** confirm full regression, security, and lint checks on the exact current default-branch SHA; continue simulation fault injection for sensor loss, communications loss, obstacles, and degraded conditions.
3. **Multimodal Screening AI:** add or complete tests for missing/conflicting/corrupted inputs, calibration, abstention, privacy, and authorized human review.
4. **Website/dashboard:** refresh this static snapshot after meaningful repository changes. A SHA or workflow status is only current as of the stated snapshot time.

## Zero-spend-first development

Target **฿0 additional spending**. Use existing hardware and local/free tools. Do not make chargeable API/cloud calls, purchase data/equipment, or commit to paid services without explicit approval. If a reliable evaluation needs unavailable resources, document the gap instead of fabricating results.

**Company principle:** publish what the evidence supports, identify what remains unknown, and make the next experiment clear.
