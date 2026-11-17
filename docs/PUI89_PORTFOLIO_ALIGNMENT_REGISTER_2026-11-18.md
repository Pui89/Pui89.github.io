# PUI89 Portfolio Alignment Register

**Review date:** 18 November 2026  
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

**Extreme Flood Rescue AI** is an inactive historical standalone project. Preserve its repository and engineering history, but do not list it as an active product, include it in current product counts, show it in portfolio navigation or assign it a current product maturity status. Flood and road-water awareness may remain product-specific advisory requirements for the SUV and Scooter, subject to their own evidence gates.

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

## Website alignment checklist

The public website should use the same six-product scope in English and Thai across:
- Portfolio home pages: `index.html`, `th.html`.
- Product pages: Coconut, Sentinel, HOME, NOMAD, Global SUV and Step-Through Scooter, in both languages.
- Group pages: `ai-vehicles.html` and `ai-vehicles-th.html`.
- Shared engineering pages: `ai-core.html` and `ai-core-th.html`.
- Evidence and maturity pages: `evidence.html`, `evidence-th.html`, and the Development Observatory data source.
- Growth, company, support and materials pages, including their Thai counterparts.

Do not let stale cached search snippets, historical project pages or archived project material override the live repository README and current portfolio register.

## Review outcome and remaining work

This register records the current authoritative names, scope and evidence labels identified during the 18 November 2026 documentation review. It does not claim that every legacy sentence, historical artifact, cached search result or external reference has already been migrated. Continue with small, reviewable pull requests; preserve history; do not write directly to default branches or merge without approval.
