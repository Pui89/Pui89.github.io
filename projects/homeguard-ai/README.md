# HOMEGUARD AI
### Multi-Modal Predictive Building Intelligence System

**Detect Early. Locate Precisely. Protect Better.**

HOMEGUARD AI is a proposed evidence-driven platform for building condition monitoring. It is designed to combine environmental, acoustic, electrical and structural observations; identify deviations from documented baselines; communicate uncertainty; and recommend human verification.

> **Current status: FOUNDATION / SIMULATION-READY DESIGN.** This repository area is an initial software foundation, not a deployed building-monitoring product. No real sensors, buildings, alarms, or safety outcomes are claimed.

## Product principles

1. **Evidence before conclusions** — every finding traces to observations, timestamps, units, quality and baseline context.
2. **Uncertainty is visible** — missing, stale, uncalibrated or conflicting inputs reduce confidence; they are never silently treated as normal.
3. **Human authority** — the system informs and prioritizes inspection. It does not control electrical circuits, disable alarms, certify structural safety, evacuate occupants, or replace qualified professionals.
4. **Privacy by design** — process acoustic features rather than conversations where possible; avoid unnecessary indoor video, face recognition and personal profiling.
5. **Open, portable and auditable** — documented interfaces, reproducible simulation, pinned dependencies and machine-readable reports.
6. **No model nationality shortcuts** — no Chinese-origin AI models, model providers or model-hosting services are included in this foundation. Every future model must pass a documented provenance, ownership, licence, data-flow and security review. This is a procurement and risk policy, not a claim that nationality alone establishes technical risk.
7. **No hidden cost** — no paid API, cloud GPU, subscription or metered inference dependency.

## Initial capabilities

- Typed sensor observations and baseline records
- Input-quality and calibration-status checks
- Transparent baseline-deviation detection
- Evidence-linked findings with uncertainty and limitations
- Deterministic synthetic three-floor building scenario
- JSON report output
- Automated tests and continuous integration

The 29-capability catalogue is a product roadmap, not 29 implemented AI models. Initial algorithms are deterministic and explainable. Machine learning is introduced only when suitable, lawfully usable, representative data and measurable validation criteria exist.

## Quick start

Requires Python 3.11 or newer. The core foundation uses the Python standard library.

```bash
python -m pip install -e ".[dev]"
pytest
homeguard-simulate --seed 89 --output report.json
```

## Repository map

- `src/homeguard_ai/` — core contracts, evaluation and deterministic simulator
- `schemas/` — machine-readable report contract
- `tests/` — automated safety and regression checks
- `.github/workflows/` — CI checks
- `docs/` — architecture, safety, model-provenance and roadmap

## Evidence labels

| Label | Meaning |
|---|---|
| PROPOSED | Planned, not implemented |
| IMPLEMENTED | Code exists |
| TESTED | Automated or documented test passed |
| SIMULATION-ONLY | Demonstrated only with synthetic inputs |
| MEASURED | Quantitative result captured with method and conditions |
| VERIFIED | Independently or reproducibly checked against stated criteria |
| NOT_VALIDATED | Real-world performance has not been established |

## Safety boundary

HOMEGUARD is a monitoring and decision-support concept. Certified smoke, fire, CO and electrical protection devices remain primary. Credible emergency indicators should trigger established emergency procedures and qualified assistance; the software must never delay them. No recommendation in this project is a professional structural, electrical, fire or medical assessment.

## Funding and partnership readiness

The first demonstrator is intended to establish technical feasibility with reproducible synthetic data. A real pilot requires a building partner, qualified engineering oversight, suitable calibrated sensors, privacy review, safety case and independent validation.

See [Architecture](docs/ARCHITECTURE.md), [Safety case](docs/SAFETY_CASE.md), [Model and supply-chain policy](docs/MODEL_AND_SUPPLY_CHAIN_POLICY.md), and [Roadmap](docs/ROADMAP.md).
