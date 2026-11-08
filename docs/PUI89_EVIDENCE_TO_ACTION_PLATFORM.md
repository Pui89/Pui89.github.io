# PUI89 Evidence-to-Action Intelligence Platform

**Version:** 1.0.0  
**Status:** Architecture and implementation contract — proposed for review  
**Date:** 8 November 2026  
**Applies to:** PUI89 projects and future PUI89 repositories

## Mission

PUI89 builds evidence-driven intelligent systems that can explain what they know, expose what they do not know, justify recommendations, preserve decision provenance, and demonstrate improvement through reproducible evaluation.

The platform is not a claim that PUI89 already has a deployed autonomous system. It is a shared engineering architecture to be implemented and validated incrementally.

## Seven reusable capabilities

1. **Evidence Intelligence Engine** — provenance, timestamps, quality, confidence, uncertainty, conflicts, missing inputs and traceable claims.
2. **World-State and Digital-Twin Layer** — versioned environment state linked to source observations; simulation is explicitly labelled and never treated as field proof.
3. **Predictive Safety Intelligence** — hazard identification, operating-envelope checks, fail-closed behavior and escalation when evidence is inadequate.
4. **Multimodal Intelligence** — controlled fusion of compatible modalities with per-modality quality, availability and provenance.
5. **Self-Evaluation Engine** — reproducible tests, calibration, robustness, abstention, regression tracking and evidence-backed release gates.
6. **Autonomous Engineering Assistant** — read-only inspection and proposed patches by default; tests and changes require explicit permission appropriate to their impact.
7. **PUI89 Mission Control** — a future dashboard aggregating verified project status, test results, risks, open decisions and next actions. It must not display invented progress.

## Shared decision cycle

`OBSERVE → NORMALIZE → UPDATE WORLD STATE → EVALUATE → PROPOSE → SAFETY GATE → HUMAN AUTHORIZATION → VERIFY → LEARN`

A proposal is not an execution command. The shared core must not directly actuate motors, cutters, propulsion, alarms, locks, screening enforcement or external systems.

## Contract boundaries

Use the versioned contracts already established by the AI Core foundation:

- `schemas/pui89-observation.schema.json`
- `schemas/pui89-world-state.schema.json`
- `schemas/pui89-action-proposal.schema.json`
- `schemas/pui89-failure-report.schema.json`

Every project adapter must preserve unknown values as unknown, attach evidence identifiers to material claims, reject unsupported schema versions, and report validation failures explicitly. Do not fabricate confidence values or calibration status.

## Evidence record minimum

Each observation or derived claim should record, where applicable:

- stable evidence ID and schema version;
- source type and source identifier;
- capture/creation timestamp and clock/time-zone context;
- modality and measurement units;
- quality/validity status;
- provenance and licence/permission context for datasets;
- uncertainty or an explicit `not_estimated` state;
- links to supporting, contradicting or superseding evidence;
- whether the evidence is real, synthetic, simulated, manually entered or inferred.

## Safety gate outcomes

- `ALLOW_FOR_HUMAN_REVIEW`: checks passed for review only; not permission to actuate.
- `HOLD`: evidence is incomplete, stale, uncertain, conflicting or awaiting review.
- `BLOCK`: a prohibited action, critical hazard, invalid input or operating-envelope violation is detected.

Missing safety-critical inputs, untrusted provenance, stale evidence, unresolved critical conflicts, failed checks and unknown operating conditions must never silently pass.

## Evaluation and progress measurement

Report progress using evidence-backed gates, not subjective completion percentages. Each gate has one of four states:

- `NOT_STARTED`
- `IN_PROGRESS`
- `PASS` — reproducible evidence is attached and acceptance criteria are met.
- `BLOCKED` — a named dependency or failure prevents completion.

For every metric record the numerator, denominator, dataset/scenario version, test command, environment, date, result artifact and reviewer. If a denominator or evidence artifact is missing, report `NOT_MEASURED`; do not estimate.

Minimum evaluation dimensions:

| Dimension | Required evidence |
|---|---|
| Contract validity | Positive and negative schema tests |
| Evidence integrity | Missing, stale, malformed and provenance-invalid cases |
| Uncertainty | Unknown handling, calibration where measurable, abstention behavior |
| Robustness | Noise, missing modalities, conflicting inputs and distribution shifts |
| Safety | Hazard cases, boundary cases, fail-closed behavior and human-review routing |
| Reliability | Repeatability, regression suite and failure reporting |
| Simulation boundary | Synthetic/simulated results clearly separated from real-world evidence |
| Security and supply chain | Workflow permissions, dependency/licence review and secret-handling checks |

## Project-specific adapters

- Coconut Harvest AI: maturity observations, tree/workspace state, worker/animal exclusion, reach and cutter interlocks.
- Extreme Flood Rescue AI: water level/current/obstacles, communications loss, victim reports, rescue-zone constraints and human mission authorization.
- PUI89 Sentinel Screening: modality quality, sensor availability, provenance, abstention, false-positive/false-negative evaluation and authorised human review; no autonomous enforcement.
- PUI89 AI HOME / NOMAD: environmental observations, sensor-health state, hazard severity, change/deterioration evidence and independent certified safety-device boundaries.

## Mission Control requirements

Mission Control is a planned presentation layer, not yet a delivered dashboard. When implemented it must show:

- per-project gate status and last verified evidence date;
- tests passed/failed/not run, with links to logs or artifacts;
- known risks, severity, owner/decision required and mitigation;
- current software/simulation/hardware validation boundary;
- changes since the previous review;
- next recommended action and why it is next.

Do not convert README commercial-readiness estimates into engineering completion percentages. Do not claim real-time monitoring unless a live data path and its freshness are tested.

## Cost, licensing and privacy guardrails

- Prefer existing standard-library capabilities and already available tools.
- No paid API, subscription, hosted GPU, cloud runtime, model download or new recurring service without explicit approval.
- Assess source code, model weights, datasets and hardware separately for licence, provenance, security, privacy and deployment permissions.
- Avoid sending private, personal, sensitive or operational data to external services without an approved data-handling basis.
- Do not add a dependency merely for convenience when a standard-library implementation is sufficient.

## Automation and approval policy

Automation may inspect repositories, produce reports, run already configured safe tests and prepare proposed changes. It must not merge pull requests, change branch protections, alter repository secrets, enable workflows, deploy software, purchase services, or command physical devices without explicit user authorization.

## Definition of done for a shared-core integration

A project is integrated only when:

1. Its adapter validates against the shared contracts.
2. Unknown, stale, conflicting and malformed evidence is tested.
3. Its safety gate fails closed for critical unknowns.
4. Proposals are separated from execution.
5. Required human-review paths are tested.
6. Evaluation results are reproducible and linked.
7. Project documentation clearly states what remains unvalidated.

A documentation-only adoption guide is planning evidence, not proof that runtime integration is complete.
