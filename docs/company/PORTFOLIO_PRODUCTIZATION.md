# PUI89 Portfolio Productization Plan

## Shared foundation: PUI89 AI Core

Build reusable components once and integrate them through documented interfaces:

- Typed records: Observation, WorldState, ActionProposal and FailureReport.
- Evidence provenance, timestamps, source quality and uncertainty.
- Validation and safety gates before recommendations are surfaced.
- Human approval and abstention paths.
- Evaluation harness, benchmark records and regression tests.
- Audit trail: what is known, unknown, changed, failing and recommended.
- Model registry with exact publisher, licence, revision, hardware requirements and approval state.

The Core must remain modular. Projects should not copy the same safety, evidence or evaluation logic into separate implementations. Do not make every project depend on a large agent framework.

## First product wedge: evidence and evaluation toolkit

The most commercially plausible first software offer is a narrow toolkit that helps a research or engineering team:
1. Ingest structured observations.
2. Preserve source and timestamp provenance.
3. Represent uncertainty and missing/conflicting evidence.
4. Generate bounded, human-reviewable proposals.
5. Run repeatable scenario evaluations.
6. Export an auditable report.

Start as a local, dependency-light reference implementation. No hosted service, paid API, or automatic model download is required. Validate usefulness with one partner workflow before packaging it as a product.

## Project-specific first wedges

### Coconut Harvest AI
First wedge: crop image/data curation, maturity annotation workflow and harvest-planning decision support. Start with lawful, rights-cleared images and human-verified labels. Evaluate maturity classification against a documented baseline before any robot integration.

### AI HOME and AI NOMAD
First wedge: local-first household condition log and change report using manually entered or simulated sensor observations. Add sensors only after data quality, privacy, power and false-alarm behavior are understood. Do not market as a certified alarm or security system.

### Extreme Flood Rescue AI
First wedge: scenario authoring, route/mission simulation and operator decision-support reports. Validate scenario assumptions with domain experts. Do not claim rescue effectiveness or deploy an unvalidated craft.

### Sentinel Screening AI
First wedge: evidence-management and model-evaluation workflow for authorized research settings. Require lawful datasets, chain of custody, calibration and human review. Do not claim narcotics identification accuracy without representative validated data and independent evaluation; never automate enforcement.

### AI Robot Car
First wedge: simulation-only perception, world-state and safety-case research. No public-road testing or driving claims.

### AI Robot Motorcycle
First wedge: ergonomic requirements, stability and hazard simulation, and design verification planning. No rideable prototype or road-use claims until qualified engineering and regulatory review.

## Model adoption policy

Hugging Face and other model hubs are discovery sources, not automatic dependencies. Before adoption, record:
- Model ID, publisher and immutable revision.
- Model and code licences; commercial-use permission.
- Dataset provenance and restrictions.
- Runtime dependencies and security posture.
- RAM, storage, CPU/GPU and inference-time estimate.
- Known limitations and evaluation results.
- Whether local execution is possible within the approved cost envelope.

Default: rules and deterministic software first; optional models behind interfaces; no remote code execution; no unreviewed downloads; no model weights committed to Git.

## Definition of a sellable product

A product is not sellable merely because a repository, website, design image or demo exists. It needs:
- A defined buyer and use case.
- A working and reproducible deliverable.
- Evidence of performance and known limitations.
- Clear ownership and compatible licences.
- Security, privacy and safety controls.
- Deployment, documentation and support plan.
- A price based on delivery cost and customer value.
- Contract, warranty, liability and regulatory review appropriate to the product.

## Portfolio resource rule

Concentrate effort on the Shared AI Core and one first customer workflow. Keep other projects at research or concept maturity until the first workflow has measurable user value. Reuse the Core only where it genuinely reduces duplication; do not force identical features into projects with different hazards and users.
