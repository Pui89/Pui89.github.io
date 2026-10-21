# PUI89 AI Robotics — Product Evidence Dashboard

**Last evidence review:** 22 October 2026  
**Purpose:** Give readers a clear view of what is implemented, what automated checks establish, and what still needs validation. This dashboard is based on repository documentation and recent GitHub Actions results; it is not an independent audit.

## Portfolio summary

| Project | Current evidence | Not yet established | Next priority |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | Python test suite passed on the latest checked commit; dataset/annotation audit tools and fair detector-comparison tooling are documented. | Strong detector performance, orchard generalization, customer value, autonomous harvesting, physical safety. The documented initial HSV baseline scored precision 0 and recall 0 at IoU ≥ 0.50 on only two images. | Build a permissioned, representative held-out dataset; review labels; run a reproducible detector comparison on the same images. |
| [Flood Rescue AI](https://github.com/Pui89/Flood-Rescue-AI) | Python tests passed on the latest checked commit; software safety-gate input-validation tests exist. | Real flood navigation, amphibious mobility, human evacuation performance, field rescue capability, physical safety. | Create repeatable simulation scenarios and report mission success, collisions, mapping error, recovery, and human interventions. |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | Python tests and local-first app regression checks passed on the latest checked commit. | Validated narcotics detector, chemical identity, real-world screening performance, operational or enforcement suitability. | Define a narrow lawful task and obtain authorized expert-reviewed ground truth before reporting performance. Appearance alone cannot establish chemical identity. |

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
- [Flood Rescue AI Actions](https://github.com/Pui89/Flood-Rescue-AI/actions)
- [Multimodal Screening AI Actions](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions)
- [PUI89 website deployment and link checks](https://github.com/Pui89/Pui89.github.io/actions)

## Shared product standard

All three products link to their own benchmark protocol and the company-wide [Product Quality and Benchmark Standard](PRODUCT_QUALITY_AND_BENCHMARK_STANDARD.md) and [Trust, Quality and Customer Value Standard](TRUST_QUALITY_CUSTOMER_VALUE.md).

## Zero-spend-first development

Target **฿0 additional spending**. Use existing hardware and local/free tools. Do not make chargeable API/cloud calls, purchase data/equipment, or commit to paid services without explicit approval. If a reliable evaluation needs unavailable resources, document the gap instead of fabricating results.

**Company principle:** publish what the evidence supports, identify what remains unknown, and make the next experiment clear.
