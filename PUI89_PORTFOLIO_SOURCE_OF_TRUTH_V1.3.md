# PUI89 — Portfolio Source of Truth v1.3

**Version:** 1.3  
**Review baseline:** 28 November 2026  
**Active portfolio:** exactly six products. **PUI89 Shared AI Core is shared infrastructure, not a seventh product.**

This document is the current identity and scope reference for PUI89's public portfolio. It is not evidence that products are built, validated, certified, commercially available or ready for deployment.

## 1. Six active products

| # | Canonical product name | Canonical repository | Website (EN / TH) |
|---:|---|---|---|
| 1 | Coconut Harvest AI | [Pui89/Coconut-Harvest-AI](https://github.com/Pui89/Coconut-Harvest-AI) | [EN](https://pui89.github.io/coconut.html) · [TH](https://pui89.github.io/coconut-th.html) |
| 2 | PUI89 Sentinel — All-Terrain Inspection Robot Dog | [Pui89/PUI89-All-Terrain-Inspection-Robot](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot) | [EN](https://pui89.github.io/sentinel.html) · [TH](https://pui89.github.io/sentinel-th.html) |
| 3 | PUI89 AI HOME — Indoor Assistance Robot | [Pui89/AI-Home-Safety-Robot](https://github.com/Pui89/AI-Home-Safety-Robot) | [EN](https://pui89.github.io/home.html) · [TH](https://pui89.github.io/home-th.html) |
| 4 | PUI89 AI NOMAD — Compact Four-Wheel Mobile Assistant | [Pui89/AI-Mobile-Assistant-Robot](https://github.com/Pui89/AI-Mobile-Assistant-Robot) | [EN](https://pui89.github.io/nomad.html) · [TH](https://pui89.github.io/nomad-th.html) |
| 5 | PUI89 AI Global SUV | [Pui89/PUI89-AI-Global-SUV](https://github.com/Pui89/PUI89-AI-Global-SUV) | [EN](https://pui89.github.io/ai-global-suv.html) · [TH](https://pui89.github.io/ai-global-suv-th.html) |
| 6 | PUI89 AI Step-Through Scooter | [Pui89/AI-Step-Through-Scooter](https://github.com/Pui89/AI-Step-Through-Scooter) | [EN](https://pui89.github.io/ai-robot-motorcycle.html) · [TH](https://pui89.github.io/ai-robot-motorcycle-th.html) |

## 2. Product identity and current design/research boundaries

- **Coconut Harvest AI:** four coconut maturity classes (young green, mature green, yellow and brown). Rights-cleared images, human-reviewed labels, leakage-safe splits and held-out CPU evaluation are required before reporting model performance. The 0–30 m range is a design challenge/target, not a validated operating range.
- **Sentinel:** quadruped All-Terrain Inspection Robot Dog for supervised inspection, environmental awareness and evidence capture. RGB, depth, thermal and 360° LiDAR are research modalities, not proof of installed sensors. Narcotics detection/screening, X-ray screening and related forensic spectra/datasets are excluded from current scope.
- **AI HOME:** compact four-wheel indoor assistant. Proposed complete-system mass target 4–6 kg, maximum 10 kg, including battery and installed hardware. These are design targets, not measured prototype mass.
- **AI NOMAD:** discreet premium upright suitcase-style four-wheel mobile assistant with four integrated wheels and a retractable telescopic handle. It is designed to blend naturally into public spaces and move smoothly, quietly and unobtrusively. Proposed target mass approximately 7 kg, maximum 10 kg. It is not a quadruped or security-patrol robot; physical mobility remains unvalidated.
- **AI Global SUV:** medium-size five-door SUV concept; AI remains advisory and does not autonomously steer, accelerate or brake. Current research preferences are RWD-first with AWD capability, Full HEV (not PHEV), and a 700 mm wading-depth target. These are research preferences, not validated vehicle specifications, supplier selections or certified capabilities.
- **AI Step-Through Scooter:** rider-first two-wheel step-through concept with flat-floor/easy-mounting design intent. AI is advisory; no autonomous steering, throttle or braking is claimed.

## 3. Shared infrastructure and excluded portfolio items

- **PUI89 Shared AI Core** is shared architecture and engineering infrastructure, not an additional product.
- **PUI89-Research** is the central research/governance repository, not a product.
- **Extreme Flood Rescue AI** is excluded from the active six-product portfolio. Historical records should be preserved; flood/road-water awareness may be studied as a bounded advisory capability in relevant mobility products.
- Historical Sentinel narcotics/X-ray screening work is outside current Sentinel scope. Do not reintroduce its datasets, forensic spectra or screening requirements into current pages.

## 4. Evidence vocabulary

Use evidence-linked states: **Proposed, Specified, Implemented, Simulated, Software-tested, Bench-tested, Field-tested, Validated, Certified, Unknown.**

A later state does not follow automatically from an earlier one. Simulation is not field testing; software tests do not establish physical safety; certification requires the applicable certificate and scope. Do not publish unsupported commercial-readiness percentages or imply that sensors are installed based only on a design document.

## 5. BOM and prototype-cost rules

The bilingual BOM framework is maintained in [PUI89-Research — English](https://github.com/Pui89/PUI89-Research/blob/main/docs/PROTOTYPE_BOM_AND_COST_FRAMEWORK.md) and [ภาษาไทย](https://github.com/Pui89/PUI89-Research/blob/main/docs/PROTOTYPE_BOM_AND_COST_FRAMEWORK.th.md).

- Unknown prices remain **TBD** until a dated source or quotation is recorded.
- Record exact manufacturer/part number, origin evidence, supplier/source, currency, quantity, shipping, taxes, lead time and compatibility.
- Do not infer country of manufacture from brand nationality.
- Do not double-count chips already included on purchased boards/modules.
- Prototype cost estimates are planning figures, not procurement approval or supplier commitments.

## 6. Change control

- Update English and Thai pages together.
- Preserve historical records and label legacy names rather than destructively rewriting history.
- Use feature branches and reviewable pull requests; no direct default-branch writes, auto-merge or deployment.
- This register does not establish company registration, manufacturing, customer deployment, certification or physical validation.

**Previous baseline:** [Portfolio Source of Truth v1.2](PUI89_PORTFOLIO_SOURCE_OF_TRUTH_V1.2.md).
