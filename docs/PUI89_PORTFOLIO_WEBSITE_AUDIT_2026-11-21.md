# PUI89 Website Portfolio Audit — 21 November 2026

**Scope:** Official six-product portfolio and bilingual Sentinel identity alignment.  
**Decision authority:** Founder-confirmed decision on 21 November 2026.  
**Canonical source:** [PUI89 Portfolio Source of Truth v1.1](../PUI89_PORTFOLIO_SOURCE_OF_TRUTH_V1.1.md).

## Official portfolio

The active portfolio remains exactly six products. PUI89 Shared AI Core is shared infrastructure, not a product.

1. Coconut Harvest AI
2. PUI89 Sentinel — All-Terrain Exploration & Inspection Robot (**quadruped**)
3. PUI89 AI HOME
4. PUI89 AI NOMAD
5. PUI89 AI Global SUV
6. PUI89 AI Step-Through Scooter

## Sentinel identity decision

The founder explicitly confirmed Sentinel as the four-legged quadruped All-Terrain Exploration & Inspection Robot. This resolves the prior ambiguity between the quadruped inspection robot and a historical narcotics-screening concept.

Narcotics detection, X-ray screening payloads and chemical-identification functions are **not** Sentinel capabilities and are excluded from the official product scope. Historical screening-related assets and archived records are preserved as legacy material; they are not to be promoted as current Sentinel product content.

## Bilingual page audit

| Check | English | Thai | Result |
|---|---|---|---|
| Canonical product identity | `sentinel.html` | `sentinel-th.html` | Aligned to quadruped inspection robot |
| General multimodal scope | General inspection intelligence | General inspection intelligence | Not represented as narcotics screening |
| Explicit scope boundary | Excludes narcotics, X-ray screening and chemical identification | Excludes narcotics, X-ray screening and chemical identification | Aligned |
| Capability qualification | No validated physical mobility or sensor runtime claim | No validated physical mobility or sensor runtime claim | Evidence boundary retained |

**Audit result:** No correction to the two Sentinel page bodies was required for this decision; both already describe the quadruped inspection product and explicitly exclude screening functions. This is a content-alignment result only, not proof of a built robot, sensor integration, mobility, safety or field validation.

## Portfolio governance

- Keep the active portfolio count at six.
- Keep the two SUV gallery design versions as previously selected; this audit does not alter them.
- Keep the public portfolio limited to the six active products. Do not expose a retired project as a current page, portfolio card, maturity record, review count, or product image. Preserve only generic, product-specific flood/road-water safety requirements where they apply to active mobility products.
- Preserve the existing bilingual QR assets and page destinations.
- Continue using feature branches and pull requests; do not write directly to the default branch or auto-merge.

## Related website work and verification status

- [PR #609 — Fix AI HOME bilingual QR section parity](https://github.com/Pui89/Pui89.github.io/pull/609) was merged on 20 November 2026. Its QR parity changes are part of the repository's subsequent `main` deployment; they remain a separate change from the Sentinel identity update.
- [PR #610 — Confirm Sentinel quadruped identity in portfolio source of truth](https://github.com/Pui89/Pui89.github.io/pull/610) was merged on 20 November 2026. Its source-of-truth and audit updates are included in `main`.
- The Pages deployment for the later `main` commit `63d32e4dea0d1e1274f3609a14746e0fe0af6ae7` completed successfully on 20 November 2026. This confirms deployment workflow success, not independent visual verification of every public page.


## NOMAD identity correction — 21 November 2026

The founder confirmed that PUI89 AI NOMAD is a compact, dog-inspired four-wheel outdoor/mobile assistant with a retractable handle for manual handling. It has four wheels, not articulated legs. Its product mission is practical assistance and supervised mobility in suitable environments; security patrol and luggage transport are outside scope. The product remains a concept with no validated physical mobility or outdoor performance.

The English and Thai NOMAD product pages were updated in this review branch to align product copy, mission, operating modes, identity distinctions, and search metadata. The current NOMAD hero illustration is still an older upright/suitcase-like concept and does not match the approved dog-inspired identity; it is explicitly disclosed as an outdated illustration and requires a separate approved visual replacement. No physical capability or test claim is added.
