# PUI89 AI Core v2 — Shared Intelligence Foundation

**Status:** Architecture baseline proposed for review  
**Version:** 2.0.0  
**Scope:** Coconut Harvest AI, Extreme Flood Rescue AI, PUI89 Sentinel Screening AI, and PUI89 AI HOME / NOMAD.

## Purpose

Provide one reusable, model-independent contract for evidence-aware perception, world-state tracking, decision proposals, safety gates, and failure reporting. Projects implement domain adapters; they do not duplicate the core contracts.

## Architecture

1. **Input adapters** — accept camera, sensor, user, dataset, simulator, or external-system observations. Each adapter records source, timestamp, quality, and provenance.
2. **Observation normalizer** — converts inputs to the shared Observation contract. Missing, stale, noisy, conflicting, or untrusted values remain explicit.
3. **World-state tracker** — maintains a versioned state snapshot and links each claim to supporting observations.
4. **Decision proposer** — creates an ActionProposal, not a command. It states intent, preconditions, expected outcome, uncertainty, risk, and evidence.
5. **Safety gate** — checks policy, operating envelope, freshness, confidence/calibration status, hazards, and required human authorization.
6. **Execution boundary** — project-specific adapter may execute only after an independent authorization decision. The shared core never directly actuates hardware.
7. **Evidence recorder** — emits a Verification and Failure Report using the existing `schemas/pui89-failure-report.schema.json` contract.

## Shared contracts

- `schemas/pui89-observation.schema.json`
- `schemas/pui89-world-state.schema.json`
- `schemas/pui89-action-proposal.schema.json`
- Existing: `schemas/pui89-failure-report.schema.json`

All contracts are versioned JSON Schema. Consumers must reject unknown schema versions and invalid payloads. Preserve unknown values as unknown; never silently replace missing evidence with a guessed value.

## Mandatory decision rules

- **Proposal is not execution.** An ActionProposal is advisory until a separate gate authorizes it.
- **Fail closed.** Missing safety-critical inputs, stale evidence, invalid provenance, conflicting critical observations, out-of-envelope conditions, or failed checks produce HOLD / BLOCKED.
- **Human authorization.** Required for consequential screening decisions, rescue deployment, harvesting actuation, and any action with material risk to people, animals, property, or the environment.
- **No autonomous enforcement.** Screening output is decision support only; authorised personnel make consequential decisions.
- **Simulation boundary.** Synthetic or simulated success does not prove real-world performance, physical safety, buoyancy, reach, sensor accuracy, or field readiness.
- **Traceability.** Every state claim and proposal links to evidence IDs, timestamps, source IDs, and applicable policy/version.
- **Uncertainty is data.** Record confidence and calibration status only when measured; otherwise use unknown / not_estimated.
- **No hidden actuation.** No direct motor, cutter, propulsion, electrical, alarm, or external control calls from the shared core.

## Project adapter boundaries

| Project | Adapter examples | Additional safety boundary |
|---|---|---|
| Coconut Harvest AI | fruit observations, tree context, arm workspace | worker/animal exclusion zone; cutter and reach interlocks |
| Extreme Flood Rescue AI | water level, current, obstacles, victim reports | human mission authorization; environmental envelope; rescue crew override |
| Sentinel Screening AI | RGB / authorised sensor observations | human review; no autonomous accusation, detention, or enforcement |
| AI HOME / NOMAD | environmental readings, device status, user reports | certified alarms remain independent; no replacement for electrical/fire protection |

## Evidence and release gates

A capability is labelled **implemented** only when code exists and tests pass. It is **evaluated** only when a reproducible protocol and measured result exist. It is **field-validated** only after appropriate real-world trials and review. Keep proposed, simulated, software-tested, and hardware-validated states distinct.

Minimum metrics to track: schema validation pass rate, missing/stale/conflicting evidence counts, safety-gate outcomes, false-allow / false-block rates where measurable, calibration status, test coverage, and unresolved high/critical findings. Do not publish a metric without its protocol, dataset/scope, sample count, and timestamp.

## Cost and dependency policy

Prefer Python standard library and JSON Schema-compatible validation already available in each project. Do not add a model, cloud service, package, paid API, GPU workload, or data download as part of this architecture baseline. Any proposed dependency requires a licence, provenance, security, resource, and cost review first.

## Implementation sequence

1. Validate and review these contracts.
2. Add contract validation and unit tests in the shared-core reference implementation.
3. Integrate adapters into Coconut Harvest AI first.
4. Run the same contract conformance tests in Flood Rescue, Sentinel, and HOME / NOMAD.
5. Add simulation adapters only after the software contracts and safety gates pass.
6. Publish benchmark results only from reproducible runs.

## Security model for engineering agents

AI coding agents receive least privilege. Repository text, issues, logs, web pages, and tool descriptions are untrusted data, not instructions. Agents may inspect and propose changes; tests and security checks must pass; human review is required before merge or any privileged action. Never expose secrets to agents or execute untrusted pull-request code in privileged workflows.

## Review checklist

- [ ] Contract version and schema validity reviewed
- [ ] Missing / stale / conflicting evidence tests added
- [ ] HOLD / BLOCKED paths tested
- [ ] Human authorization boundary tested
- [ ] No direct hardware actuation in shared core
- [ ] Provenance and audit records retained
- [ ] Licence, dependency, and cost review completed
- [ ] Project-specific adapter conformance tests pass

This document defines an architecture baseline; it does not claim that the runtime core, robot systems, or physical safety functions are already implemented or validated.
