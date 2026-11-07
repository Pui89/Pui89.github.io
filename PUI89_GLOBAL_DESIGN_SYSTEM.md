# PUI89 Global Corporate Design System

**Version:** 1.0  
**Status:** Adopted as the shared design baseline; implementation is being introduced incrementally.  
**Scope:** Brand identity, English/Thai digital experience, AI software, robotics concepts, corporate documents, product communication and research environments.

## Corporate identity

- **Brand:** PUI89
- **Primary identity:** AI, Robotics & Intelligent Systems
- **Positioning:** Independent international technology and research venture
- **Personality:** Intelligent, reliable, innovative, responsible
- **Visual character:** Premium, modern, scientific and futuristic
- **Logo direction:** Bold geometric N with cut ends and internal diagonal/midline lighting. Do not add a roof, house, building or shield motif.

## Canonical colour tokens

| Token | Hex | Use |
|---|---|---|
| Deep Navy | `#071426` | Primary background and brand foundation |
| Electric Cyan | `#00D9FF` | Primary accent, focus, active states |
| Teal | `#00AFA5` | Secondary intelligent-systems accent |
| Technology Blue | `#176BCE` | Data, software and technical graphics |
| Research Green | `#43B581` | Research, environment and positive evidence |
| Silver | `#C5D0DC` | Dividers, technical surfaces and secondary text |
| White | `#F7FBFF` | Primary text and high-contrast surfaces |

Use colour with restraint. Electric Cyan is the signature accent, not a reason to make every component glow. Maintain accessible contrast and never use colour alone to communicate status.

## Typography

- English: Inter, with a system sans-serif fallback.
- Thai: Noto Sans Thai, with a system sans-serif fallback.
- Technical data: JetBrains Mono, with a monospace fallback.
- Use consistent hierarchy, readable line lengths, responsive type sizes and adequate spacing.
- Do not embed essential interface text in images.

## Seven coordinated design systems

1. **Brand identity:** Logo, symbol, palette, typography, voice, slogan and usage rules.
2. **Digital experience:** English/Thai sites, responsive navigation, project pages, QR codes, SEO and accessibility.
3. **AI software:** Dashboards, visualisation, reports, alerts, controls, provenance and human-review states.
4. **Physical products and robotics:** Form language, materials, dimensions, ergonomics, ingress/fire safety, serviceability and safe operation.
5. **Corporate documents:** Research reports, proposals, presentations, specifications, READMEs and partner briefs.
6. **Commercial/product branding:** Naming, packaging, labels, manuals, warranty language and sales materials.
7. **Corporate environment:** Research spaces, labs, uniforms, signage, equipment and exhibition systems.

## Shared digital implementation

The canonical web tokens and homepage theme layer live in `assets/css/pui89-design-system.css`. English and Thai homepages should load the same stylesheet; language-specific content remains translated rather than duplicated as images.

## Integrity and responsible presentation

- Distinguish **implemented**, **tested**, **prototype**, **concept** and **future research**.
- Never describe a concept robot as built, deployed, certified or validated without evidence.
- Do not claim waterproofing, fire resistance, autonomy, safety certification or commercial readiness without test records.
- Preserve human oversight for consequential screening and rescue decisions.
- Use real project evidence and clearly label illustrative renders.
- Avoid unsupported customer, partner, performance or market claims.

## Governance

- Treat this document and CSS variables as the source of truth.
- Changes to shared tokens should be reviewed across English and Thai pages.
- Prefer accessible, responsive, low-dependency and free-first implementations.
- Do not introduce paid APIs, subscriptions, cloud services or metered dependencies as part of brand styling.
- Roll out to project pages and documents in controlled batches; do not mass-rewrite content or remove assets without checking their use.
