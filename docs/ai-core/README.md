# PUI89 AI Core

**Shared engineering foundation for PUI89's agriculture, disaster-response and public-safety AI programmes.**

Status: **Foundation specification — implementation and conformance are tracked separately.**

## Purpose

PUI89 AI Core defines a common way for the three project repositories to describe system state, evidence, uncertainty, failures, test results and readiness. It is intended to make engineering progress reproducible and partner review easier.

It is not a trained AI model, a robot operating system, a safety certification, or proof that any concept is field-ready.

## Shared project portfolio

| Programme | Mission | Evidence boundary |
|---|---|---|
| Coconut Harvest AI | Agricultural perception and harvesting workflow | Software checks and rule-based scenarios do not establish detector accuracy, orchard performance or a working harvesting robot |
| Extreme Flood Rescue AI | Flood reconnaissance and rescue-support concepts | Scenario checks do not validate water physics, buoyancy, navigation, rescue performance or operation at target depths |
| Multimodal Narcotics Screening AI | Multimodal screening workflow with human review | Software checks do not establish detection accuracy, operational suitability or lawful deployment |

## Core contract

Every project status report should capture:

1. **Identity** — project, report version, timestamp, code revision and reporting scope.
2. **Capabilities** — implemented, tested, simulated, proposed, blocked or not assessed.
3. **Evidence** — source, run identifier, test scope, result and limitations.
4. **Data provenance** — source, licence review, consent/authority where relevant, annotation and split status.
5. **Uncertainty** — missing, stale, noisy or conflicting inputs and how they affect decisions.
6. **Failures** — detected failures, severity, mitigation, owner and retest evidence.
7. **Readiness** — separate software, data, model, simulation, hardware, safety and deployment states.
8. **Costs and dependencies** — licence, compute, hardware, external service and maintenance requirements.

## Status vocabulary

Use only these controlled values where applicable:

- implemented
- tested
- simulated
- proposed
- blocked
- not_assessed
- not_applicable

A status must not be promoted because a document or diagram exists. A proposed robot mechanism remains proposed until the relevant physical evidence exists.

## Evidence levels

| Level | Meaning | Does not imply |
|---|---|---|
| E0 — Concept | Idea, requirement or design | Implementation |
| E1 — Software | Code, unit tests, static checks | Model accuracy or real-world performance |
| E2 — Controlled simulation | Repeatable simulated scenarios | Validated physics or field performance |
| E3 — Bench / lab | Instrumented tests on real components | Operational deployment |
| E4 — Field pilot | Controlled field evaluation with documented protocol | General safety certification or broad reliability |
| E5 — Independent validation | External evaluation against defined criteria | Universal suitability |

Evidence level is assigned per capability, not per project. A project can have E1 software and E0 hardware simultaneously.

## Minimum report rules

- Use ISO 8601 timestamps in UTC.
- Pin each result to a commit SHA and configuration where available.
- Keep raw evidence links and a short plain-language interpretation.
- Record both passed and failed tests; never report only successful runs.
- Separate test counts from performance metrics.
- Missing evidence must be not_assessed, not assumed successful.
- Mark historical evidence as historical and re-run before using it for a current funding claim.
- Do not claim live monitoring unless a functioning data source and scheduled collection are configured.

## Initial evidence baseline

The public portfolio README records three rule-based scenario evaluations dated 30 October 2026, each reporting 7/7 scenarios and 9/9 steps with zero reported failures. It also records a Coconut dataset audit with 15 checks passed. These are historical repository-reported software/scenario checks, not independent verification.

- [Coconut scenario run](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881372992)
- [Flood scenario run](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40919457152)
- [Screening scenario run](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40919469891)
- [Coconut dataset audit](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40944312469)

Before external use, verify that these workflow runs remain accessible and correspond to the current repository history.

## First implementation sequence

1. Adopt the shared status schema and report template in all three repositories.
2. Add a validator that rejects invalid status values, missing provenance and unsupported readiness promotion.
3. Generate reports from repository evidence rather than manually asserting project-wide readiness.
4. Add a portfolio roll-up only after all three projects publish compatible reports.
5. Add simulator telemetry only for configured simulators; hardware telemetry only when real equipment exists.
6. Consider local VLM/VLA components only after licence, RAM, compute, privacy and reproducibility checks.

## Funding and partnership use

The AI Core is an enabling research and engineering work package, not a grant claim by itself. Funding proposals should identify a specific use case, named partner, measurable deliverable, budget, co-funding requirement, timeline and evaluation protocol. PUI89's legal and applicant eligibility must be checked for each programme before applying.

## Related files

- [Machine-readable report schema](status-report.schema.json)
- [Initial portfolio baseline](portfolio-status.json)
- [Partner and funding brief](partner-brief.md)
