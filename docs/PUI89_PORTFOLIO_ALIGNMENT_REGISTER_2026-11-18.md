# PUI89 Portfolio Alignment Register

**Review date:** 21 November 2026  
**Portfolio identity confirmation:** Founder-confirmed Sentinel quadruped identity, 21 November 2026.  
**Purpose:** Keep public portfolio pages, product repositories and shared engineering documentation aligned.  
**Status:** Documentation governance record; not a product implementation or validation report.

## Authoritative portfolio scope

PUI89 has exactly six active product projects:

| No. | Product | Repository | Public project page | Current evidence label |
|---:|---|---|---|---|
| 1 | Coconut Harvest AI | [Coconut-Harvest-AI](https://github.com/Pui89/Coconut-Harvest-AI) | [EN](https://pui89.github.io/coconut.html) · [TH](https://pui89.github.io/coconut-th.html) | Implemented — software/evaluation-preparation work; real-image detector accuracy and physical harvesting are not validated |
| 2 | PUI89 Sentinel — All-Terrain Exploration & Inspection Robot | [PUI89-All-Terrain-Inspection-Robot](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot) | [EN](https://pui89.github.io/sentinel.html) · [TH](https://pui89.github.io/sentinel-th.html) | Specified — four-legged quadruped requirements; no physical prototype or field validation |
| 3 | PUI89 AI HOME | [AI-Home-Safety-Robot](https://github.com/Pui89/AI-Home-Safety-Robot) | [EN](https://pui89.github.io/home.html) · [TH](https://pui89.github.io/home-th.html) | Implemented — early software foundations; no physical robot or validated home-safety performance |
| 4 | PUI89 AI NOMAD | [AI-Mobile-Assistant-Robot](https://github.com/Pui89/AI-Mobile-Assistant-Robot) | [EN](https://pui89.github.io/nomad.html) · [TH](https://pui89.github.io/nomad-th.html) | Implemented — early software foundations; ground-use four-wheel assistant, not airline luggage; physical mobility is unvalidated |
| 5 | PUI89 AI Global SUV | [PUI89-AI-Global-SUV](https://github.com/Pui89/PUI89-AI-Global-SUV) | [EN](https://pui89.github.io/ai-global-suv.html) · [TH](https://pui89.github.io/ai-global-suv-th.html) | Implemented — early software-only safety/contract foundation; no vehicle integration, road testing or certification |
| 6 | PUI89 AI Step-Through Scooter | [AI-Step-Through-Scooter](https://github.com/Pui89/AI-Step-Through-Scooter) | [EN](https://pui89.github.io/ai-robot-motorcycle.html) · [TH](https://pui89.github.io/ai-robot-motorcycle-th.html) | Specified — rider-first two-wheel step-through requirements; no functioning scooter, rider trials or road certification |

**Shared AI Core** is common engineering infrastructure for these six products. It is not a seventh product.

Flood and road-water awareness may remain advisory requirements within the AI Global SUV and AI Step-Through Scooter, subject to product-specific evidence and safety gates. This capability does not constitute a separate product or validated flood-driving capability.

## Sentinel identity and multimodal scope

PUI89 Sentinel is a **four-legged quadruped exploration and inspection robot**. Its General Multimodal Intelligence is a general inspection capability that may combine authorised vision, audio, text, map, spatial and sensor/time-series evidence with provenance, quality checks and uncertainty.

Sentinel is **not** a narcotics-screening product. Narcotics detection, X-ray screening payloads and chemical-identification functions are outside its current product scope. Historical screening-related repository artifacts must be labelled as legacy and must not be represented as current Sentinel capabilities.

Sentinel and NOMAD are distinct:
- Sentinel: four articulated legs; supervised inspection and evidence capture.
- NOMAD: four ground-contact caster wheels; suitcase-style mobile assistant for ground use.

## Evidence and maturity rules

- Use evidence labels such as Proposed, Specified, Implemented, Simulated, Software-tested, Bench-tested, Field-tested, Validated, Certified or Unknown only when the corresponding evidence exists.
- An **Implemented** label describes the documented software work in scope; it does not imply a built physical product.
- Do not publish commercial-readiness percentages unless a dated, approved evidence register explicitly authorises them. Prefer the maturity label, evidence date, limitations, next gate and blockers.
- Keep synthetic, simulation, software, bench, physical and field evidence separate.
- Do not infer model accuracy, safety, reliability, certification, manufacturing readiness or commercial availability from documentation or a passing software test.
- Show stage colours consistently: Electric Cyan for active progress/highlight, neutral grey for not assessed/not started, amber for pending evidence or blockers, green only for an evidence-verified passed gate, and red for a verified critical issue. Colour never substitutes for the text status and evidence.

## Cross-portfolio engineering topics

Public READMEs and web pages should describe these as shared engineering directions, not as proof that every feature is implemented:

- **Industrial AI Platform:** software-first integration and efficiency across real product constraints; PUI89 is not claiming semiconductor manufacturing.
- **Perception & Task Intelligence:** observe, perceive, assess, decide and respond with provenance, uncertainty, abstention and human review.
- **General multimodal intelligence:** authorised vision, audio, text, spatial/map and sensor/time-series observations, with timestamp alignment, quality and disagreement handling.
- **Heterogeneous compute:** CPU/GPU/NPU/MCU task placement, memory and power awareness, model sizing, quantisation, scheduling, edge inference and fallback.
- **Simulation & digital twins:** staged process, routing and robotics simulation before controlled prototypes; simulated outcomes must remain labelled as simulation.
- **Safety and human authority:** AI outputs are bounded observations/proposals; independent safety controls and authorised human decisions remain authoritative.
- **Security, privacy and recovery:** least privilege, safe input handling, evidence integrity, failure reporting, recovery/version history and privacy-by-design. Do not publish sensitive security configurations.
- **Hardware and materials sourcing:** exact manufacturer/model, country-of-origin evidence, compatibility, supplier, dated price, lead time and lifecycle/landed-cost review before purchase.
- **Open-source-first governance:** review provenance, licensing, security, privacy, compute requirements and maintainability before adopting external tools, models or datasets.

Product-specific configurations must remain distinct. Do not copy a capability from one product to another merely because both use Shared AI Core.

## Website alignment checklist

The public website should use the same six-product scope in English and Thai across:
- Portfolio home pages: `index.html`, `th.html`.
- Product pages: Coconut, Sentinel, HOME, NOMAD, Global SUV and Step-Through Scooter, in both languages.
- Group pages: `ai-vehicles.html` and `ai-vehicles-th.html`.
- Shared engineering pages: `ai-core.html` and `ai-core-th.html`.
- Evidence and maturity pages: `evidence.html`, `evidence-th.html`, and the Development Observatory data source.
- Growth, company, support and materials pages, including their Thai counterparts.

Do not let stale cached search snippets, historical project pages or archived project material override the live repository README and current portfolio register.

## 21 November 2026 founder confirmation and audit update

The founder explicitly confirmed that the official PUI89 Sentinel product is the **four-legged quadruped All-Terrain Exploration & Inspection Robot**. This resolves the prior identity ambiguity. The official six-product portfolio remains unchanged. Narcotics screening, X-ray screening payloads and chemical-identification functions remain excluded from Sentinel. Historical screening-related repository assets and archived documentation are retained as legacy records and must not be described as current product features.

The bilingual public Sentinel pages (`sentinel.html` and `sentinel-th.html`) were rechecked. Their product names, descriptions and multimodal scope identify the quadruped inspection robot; both pages explicitly distinguish general inspection intelligence from narcotics screening and state that narcotics detection, X-ray screening and chemical identification are outside the current scope. No Sentinel page correction is required for this identity decision. This is a content-alignment audit only; it does not validate a physical robot, sensors or field performance.

The canonical portfolio source is now [PUI89 Portfolio Source of Truth v1.1](../PUI89_PORTFOLIO_SOURCE_OF_TRUTH_V1.1.md). The v1.0 file is retained as historical version evidence.

## Review outcome and remaining work

This register records the current authoritative names, scope and evidence labels, including the founder-confirmed Sentinel identity recorded on 21 November 2026. It does not claim that every legacy sentence, historical artifact, cached search result or external reference has already been migrated. Continue with small, reviewable pull requests; preserve history; do not write directly to default branches or merge without approval.
