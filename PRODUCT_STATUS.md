# PUI89 — Product Evidence Dashboard

**Portfolio review baseline:** 28 November 2026  
**Active products:** exactly six. **Shared AI Core is infrastructure, not a seventh product.**

The authoritative identities, bilingual pages, product boundaries and design/research preferences are maintained in [PUI89 Portfolio Source of Truth v1.3](PUI89_PORTFOLIO_SOURCE_OF_TRUTH_V1.3.md).

| # | Active product | Current evidence boundary | Next evidence gate |
|---:|---|---|---|
| 1 | Coconut Harvest AI | Software/evaluation preparation; no real-image accuracy claim without rights-cleared held-out test results. Four maturity classes; 0–30 m is a design target only. | Dataset rights, human labels, leakage-safe test split, CPU metrics and failure cases. |
| 2 | PUI89 Sentinel — All-Terrain Inspection Robot Dog | Quadruped concept and requirements; RGB/depth/thermal/360° LiDAR are research modalities, not confirmed installed hardware. No physical mobility or field capability claim. Narcotics/X-ray screening is excluded. | Define first supervised inspection mission, operating envelope, hazards and measurable acceptance criteria before hardware selection. |
| 3 | PUI89 AI HOME | Four-wheel indoor assistant design/software preparation; 4–6 kg target mass, 10 kg maximum including battery and installed hardware. Not measured. | Verify design mass budget, sensor/compute configuration and repeatable indoor software evaluation. |
| 4 | PUI89 AI NOMAD | Dog-inspired four-wheel mobile assistant with manual handling handle; approximately 7 kg target mass, 10 kg maximum. Physical mobility and outdoor performance are not validated. | Define assistance tasks, terrain envelope, wheel/handle engineering, stability, runtime and safe stop. |
| 5 | PUI89 AI Global SUV | Medium-size SUV concept; AI is advisory only. RWD-first/AWD-capable, Full HEV and 700 mm wading depth are research preferences, not validated specifications. | Validate road/context perception offline; assess vehicle platform, safety interfaces, water-ingress engineering and regulatory scope. |
| 6 | PUI89 AI Step-Through Scooter | Two-wheel step-through concept; rider remains in control. Powertrain and hardware configuration remain open. | Define powertrain, rider ergonomics, road/water warning scenarios and measurable software acceptance criteria. |

## Evidence maturity labels

Use only: **Proposed, Specified, Implemented, Simulated, Software-tested, Bench-tested, Field-tested, Validated, Certified, Unknown.**

Do not publish unsupported commercial-readiness percentages. Each maturity claim must link to the relevant specification, commit, test, simulation report, bench record, field report or certificate. A passing workflow is not product validation.

## Latest research repository milestones — 28 November 2026

The PUI89-Research repository records merged work for the six-product register, environmental/material/safety qualification reference, preliminary Coconut Harvest AI literature review, FreeCut communication workflow, and 360-degree perception framework/validation protocol ([PR #6](https://github.com/Pui89/PUI89-Research/pull/6), [#7](https://github.com/Pui89/PUI89-Research/pull/7), [#9](https://github.com/Pui89/PUI89-Research/pull/9), [#10](https://github.com/Pui89/PUI89-Research/pull/10), [#11](https://github.com/Pui89/PUI89-Research/pull/11), [#12](https://github.com/Pui89/PUI89-Research/pull/12)). The Hybrid End-to-End Multimodal AI architecture remains open for review in [PR #8](https://github.com/Pui89/PUI89-Research/pull/8). These are repository/documentation milestones, not completed experimental or physical validation.

## Prototype BOM and cost

See the [bilingual six-product BOM and prototype-cost framework](https://github.com/Pui89/PUI89-Research/tree/main/docs/PROTOTYPE_BOM_AND_COST_FRAMEWORK.md). Until configurations and dated supplier evidence are available, product prototype costs remain **TBD — not yet responsibly estimable**. No purchase or supplier commitment is implied.

## Coconut Harvest AI — required evidence sequence

1. Dataset manifest and source provenance.
2. Licence record with reuse and commercial-use terms.
3. Human annotation guide and reviewed labels.
4. Leakage-safe train/validation/test split.
5. Held-out CPU evaluation with reproducible environment and command.
6. Per-class precision, recall and F1, confusion matrix, sample counts and false-positive/false-negative examples.
7. Failure analysis and limitations.

No image download, dataset reuse approval, model training, purchase or physical test is implied by this plan.
