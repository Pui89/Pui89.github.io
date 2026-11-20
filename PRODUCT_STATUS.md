# PUI89 — Product Evidence Dashboard

**Portfolio review baseline:** 21 November 2026  
**Active products:** exactly six. **Shared AI Core is infrastructure, not a seventh product.**

The authoritative names, canonical repositories, bilingual website links, product boundaries and evidence vocabulary are maintained in [PUI89 Portfolio Source of Truth v1.2](PUI89_PORTFOLIO_SOURCE_OF_TRUTH_V1.2.md).

| # | Active product | Canonical repository | Current evidence boundary | Next evidence gate |
|---:|---|---|---|---|
| 1 | Coconut Harvest AI | [Repository](https://github.com/Pui89/Coconut-Harvest-AI) | Software/evaluation preparation; no real-image accuracy claim unless a rights-cleared held-out test report is linked. | Dataset rights, human labels, leakage-safe test split, CPU metrics and failure cases. |
| 2 | PUI89 Sentinel — All-Terrain Exploration & Inspection Robot (quadruped) | [Repository](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot) | Quadruped concept and requirements; no physical mobility or field capability claim. Narcotics screening, X-ray screening and chemical identification are outside product scope. | Define first supervised inspection mission and operating envelope before hardware selection. |
| 3 | PUI89 AI HOME | [Repository](https://github.com/Pui89/AI-Home-Safety-Robot) | Design/software preparation; complete mass requirement is 8 kg target, 10 kg maximum. | Verify design mass budget and later measure complete prototype mass. |
| 4 | PUI89 AI NOMAD | [Repository](https://github.com/Pui89/AI-Mobile-Assistant-Robot) | Compact dog-inspired four-wheel outdoor/mobile assistant with retractable manual handling handle; no physical mobility or outdoor validation. Not a security-patrol robot. | Define practical assistance tasks, supervised mobility envelope, wheel/handle engineering, terrain limits and safe stop. |
| 5 | PUI89 AI Global SUV | [Repository](https://github.com/Pui89/PUI89-AI-Global-SUV) | Vehicle concept; AI support remains advisory. | Validate road/context perception offline and document driver-warning limits. |
| 6 | PUI89 AI Step-Through Scooter | [Repository](https://github.com/Pui89/AI-Step-Through-Scooter) | Two-wheel step-through scooter concept; AI support remains advisory. | Define road-water/flood-risk warning scenarios; unknown water means do not enter. |


## Evidence maturity labels

Use only: **Proposed, Specified, Implemented, Simulated, Software-tested, Bench-tested, Field-tested, Validated, Certified, Unknown.**

Do not publish unsupported commercial-readiness percentages. Each maturity claim must link to the relevant specification, commit, test, simulation report, bench record, field report or certificate. A passing workflow is not product validation.

## How to read automated checks

Automated tests establish only the software behavior they actually exercise for the cited commit. They do not establish model accuracy, dataset rights, physical safety, robot performance, roadworthiness, certification or customer demand. A missing workflow run is **Unknown**, not a pass or a failure.

## Coconut Harvest AI — required evidence sequence

1. Dataset manifest and source provenance.
2. Licence record with reuse and commercial-use terms.
3. Human annotation guide and reviewed labels.
4. Leakage-safe train/validation/test split.
5. Held-out CPU evaluation with reproducible environment and command.
6. Per-class precision, recall and F1, confusion matrix, sample counts and false-positive/false-negative examples.
7. Failure analysis and limitations.

No image download, dataset reuse approval, model training, purchase or physical test is implied by this plan.
