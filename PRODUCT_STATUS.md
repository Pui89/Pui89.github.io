# PUI89 AI Robotics — Product Evidence Dashboard

**Last evidence review:** 28 October 2026  
**Purpose:** Give readers a clear view of what is implemented, what automated checks establish, and what still needs validation. This dashboard is a timestamped snapshot, not a live monitor or independent audit.

## Current repository snapshot

These are the latest default-branch commits returned by GitHub's commit search at the time of this review. They identify the code snapshot; they do **not** by themselves establish test success.

| Repository | Default branch | Reviewed commit |
|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | `main` | [`24a58ab`](https://github.com/Pui89/Coconut-Harvest-AI/commit/24a58abcc700d293f4c54a304c87fe4269930f62) |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | `main` | [`3a4c55e`](https://github.com/Pui89/Extreme-Flood-Rescue-AI/commit/3a4c55e43888e197bf426bdc4006fa92b653bf8f) |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | `main` | [`a8f7500`](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/a8f750055428a6f9aeaf89d62e5278b690218546) |
| [PUI89 website](https://github.com/Pui89/Pui89.github.io) | `main` | [`5fac7ad`](https://github.com/Pui89/Pui89.github.io/commit/5fac7ad3a860f1f346506cb3db16a5cb49e7ad46) |

**Verification limitation:** GitHub's combined commit-status endpoint returned no status records for these four SHAs during this review. This does not prove that no GitHub Actions workflows ran; it means this dashboard does not claim a current passing result for those exact commits. Use the Actions links below to inspect workflow runs and their commit SHAs before citing a pass.

## Portfolio summary

| Project | Current evidence | Not yet established | Next priority |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | Repository includes software and documented dataset/annotation audit and detector-comparison tooling. Historical test claims require checking the exact workflow and commit before reuse. | Strong detector performance, orchard generalization, customer value, autonomous harvesting, physical safety. The previously documented initial HSV baseline scored precision 0 and recall 0 at IoU ≥ 0.50 on only two images. | Build a permissioned, representative held-out dataset; review labels; run a reproducible detector comparison on the same images. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | Repository includes software safety-gate input-validation tests and a proposed rescue-robot concept. Current passing CI is not asserted here without a matching run. | Real flood navigation, amphibious mobility, human evacuation performance, field rescue capability, physical safety. | Create repeatable simulation scenarios and report mission success, collisions, mapping error, recovery, and human interventions. |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | Repository includes a local-first screening concept and software checks; current passing CI is not asserted here without a matching run. | Validated narcotics detector, chemical identity, real-world screening performance, operational or enforcement suitability. | Define a narrow lawful task and obtain authorized expert-reviewed ground truth before reporting performance. Appearance alone cannot establish chemical identity. |

## Status labels

- **Implemented:** code or documentation exists in the repository.
- **Automated checks passed:** the named automated workflow passed for the cited commit; this is not a blanket certification.
- **Prototype:** initial working software exists, but product performance may not be established.
- **Not yet measured:** there is no adequate, comparable evidence for the claim.
- **Pilot-evaluated:** only use after an actual consenting partner pilot with a documented protocol and results.
- **Deployment-ready:** only use after the applicable safety, privacy, security, licensing, reliability, support, and operational requirements have been reviewed.

## How to read CI results

Automated tests help detect regressions in code. They do not prove that a detector is accurate, that a robot is safe, that a product beats competitors, or that customers will pay. Always inspect the specific workflow and commit before quoting a test result.

- [Coconut Harvest AI Actions](https://github.com/Pui89/Coconut-Harvest-AI/actions)
- [Extreme Flood Rescue AI Actions](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions)
- [Multimodal Screening AI Actions](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions)
- [PUI89 website deployment and link checks](https://github.com/Pui89/Pui89.github.io/actions)

## Shared product standard

All three products link to their own benchmark protocol and the company-wide [Product Quality and Benchmark Standard](PRODUCT_QUALITY_AND_BENCHMARK_STANDARD.md) and [Trust, Quality and Customer Value Standard](TRUST_QUALITY_CUSTOMER_VALUE.md).

## Zero-spend-first development

Target **฿0 additional spending**. Use existing hardware and local/free tools. Do not make chargeable API/cloud calls, purchase data/equipment, or commit to paid services without explicit approval. If a reliable evaluation needs unavailable resources, document the gap instead of fabricating results.

**Company principle:** publish what the evidence supports, identify what remains unknown, and make the next experiment clear.
