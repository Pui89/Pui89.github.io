# PUI89 Portfolio Engineering Audit

**Snapshot date:** 8 November 2026  
**Scope:** Seven active PUI89 project repositories and the public website repository  
**Method:** Read-only GitHub source, workflow-directory and ruleset inspection  
**Change policy:** This audit branch does not modify any default branch or merge any pull request.

## Executive result

The portfolio already contains substantial project documentation and automation. The most important portfolio-level gaps are **canonical shared-contract implementation, evidence traceability, and meaningful review gates**.

- **7/7 repositories** have at least one active GitHub ruleset.
- **24 active rulesets out of 25 total** were returned by the rulesets API; one is disabled.
- **97 workflow files** were listed across the seven repositories.
- A PUI89 security-audit workflow file is present in every repository.
- Flood Rescue and Screening also expose CodeQL and dependency-review workflow files.
- Observation, WorldState, ActionProposal and FailureReport are documented across the portfolio. This PR now proposes four machine-readable JSON Schema drafts (0.1.0-draft) and checks their structure. They are **not yet a released package or integrated across project adapters**.
- One representative active ruleset per repository was inspected. Each sampled ruleset requires pull requests and prevents non-fast-forward updates, but the sampled settings require **zero approving reviews** and do not require code-owner review or review-thread resolution.
- The classic branch-protection endpoint returned HTTP 403 for all seven repositories. Its settings and required status checks remain **unverified**.
- This audit did not execute project tests or recompute maturity scores.

Detailed machine-readable evidence: [Portfolio evidence register](pui89-portfolio-evidence-register.json).

## Status legend

- **GREEN — verified:** directly observed in inspected source or GitHub API response.
- **AMBER — improvement required:** a documented gap or risk needing engineering work.
- **GREY — not verified:** no conclusion should be inferred.

## Repository inventory

| Project | Default-branch snapshot | Active / total rulesets | Workflow files |
|---|---|---:|---:|
| Coconut Harvest AI | `dea9d2a` | 6 / 7 | 21 |
| Extreme Flood Rescue AI | `abeb16f` | 7 / 7 | 29 |
| Multimodal Narcotics Screening AI | `f8a3c48` | 7 / 7 | 31 |
| AI HOME | `a0b657a` | 1 / 1 | 3 |
| AI NOMAD | `f617fc7` | 1 / 1 | 7 |
| AI Robot Car | `abf6fa5` | 1 / 1 | 3 |
| AI Robot Motorcycle | `54ccef1` | 1 / 1 | 3 |
| **Total** |  | **24 / 25** | **97** |

Exact commit SHAs, ruleset IDs, sampled settings and workflow counts are stored in the JSON register. Counts are a snapshot, not a live dashboard.

## Seven improvement workstreams

### 1. Shared AI Core — canonical implementation

**Current evidence:** all seven READMEs and supporting standards refer to the four shared contracts. This PR adds four machine-readable JSON Schema drafts under `schemas/pui89/`. The Robot Car repository also has a local `contracts.py`, but its module docstring calls these contracts temporary and local.

**Implemented in this PR:** draft Observation, WorldState, ActionProposal and FailureReport JSON Schemas with explicit version 0.1.0-draft. A dependency-free check verifies the four schema files and enforces the ActionProposal safety constants. **Next:** review the draft, publish a versioned package, migrate adapters and add full schema-conformance tests. Keep ActionProposal advisory-only. Physical actuation remains outside the shared layer.

**Status: AMBER** — draft schemas and structural checks are proposed; package release and portfolio-wide adapter integration are not yet verified.

### 2. Evidence register and maturity integrity

A machine-readable register now records repository snapshots, ruleset inventory, workflow counts, observed gaps and next actions. A dependency-free validator checks the register and the four draft contract schema files.

For future maturity reporting:
- derive every percentage or score from named evidence gates;
- link each credited gate to a commit, test run, benchmark, reviewed dataset record or reproducible artefact;
- separate code presence from successful execution and measured performance;
- never award progress merely because a workflow file or plan exists;
- use NOT RUN, NOT MEASURED, UNKNOWN or NOT VALIDATED when evidence is absent.

**Status: GREEN** for the dated register and structural validator; **AMBER** for automated evidence collection and cross-project scoring.

### 3. Bilingual website consistency

The English and Thai Shared AI Core pages now link to the same dated evidence register. Both language versions retain equivalent claims, limitations and status definitions. This website update remains subject to PR review and is not live until merged.

**Status: GREEN** in this proposed change; publication pending review.

### 4. Project README quality

Keep the central register authoritative for portfolio-wide facts. Each project README should retain its own purpose and operating boundary, implemented software and test evidence, project-specific data/licence/safety risks, benchmark results and known failure cases, and next milestone. Avoid copying a second, competing portfolio-wide status table into every README.

**Status: AMBER** — existing READMEs contain substantial project information; cross-linking and evidence freshness need continued review.

### 5. Repository protection and supply-chain security

**Observed:** active rulesets exist across all seven repositories. The sampled rulesets enforce pull-request changes and non-fast-forward protection but do not require an approving review.

Next checks:
1. Inspect all 25 rulesets for overlapping or contradictory conditions before editing any.
2. Confirm classic branch protection and required status checks in the repository owner's GitHub settings; this integration could not read that endpoint.
3. Select required CI checks that actually exist and are stable.
4. Decide whether an independent reviewer can approve changes. Do not configure an approval requirement that makes legitimate maintenance impossible for a solo maintainer.
5. Confirm secret scanning, dependency review, CodeQL coverage and licence review per repository; workflow names alone do not prove their checks pass.
6. Preserve least-privilege workflow permissions, pin third-party actions where practical, and avoid exposing secrets in logs.

**No rulesets or branch-protection settings were changed by this audit.**

**Status: AMBER** — active protection exists, but review depth and overlapping rulesets need attention.

### 6. Repeatable engineering validation

Before adding larger models, sensors or hardware:
- establish a shared contract conformance test suite;
- test missing, malformed, stale, noisy and conflicting inputs;
- test uncertainty propagation and abstention;
- test safe-stop/no-action outcomes and recovery reporting;
- use deterministic scenarios and fixed seeds;
- record commit, environment, command, scenario, seed, counts, failures and limitations.

A passing software test does not validate a dataset, model accuracy, simulator physics, waterproofing, fire resistance, vehicle safety or field performance.

**Status: AMBER** — project workflows and test documentation exist; a canonical cross-project conformance suite is the next engineering milestone.

### 7. Research and product credibility

Use these evidence labels consistently in websites, READMEs, proposals and reports:

| Label | Meaning |
|---|---|
| IMPLEMENTED | Code or configuration exists in the cited revision. |
| TESTED | A named test ran and its result is recorded. |
| MEASURED | A reproducible metric was computed on a documented evaluation set. |
| SIMULATION-ONLY | Evidence comes only from simulation or synthetic scenarios. |
| PROPOSED | Planned or conceptual work; not yet implemented. |
| NOT VALIDATED | The real-world capability remains unproven. |

Do not imply incorporation, customers, partnerships, certification, waterproofing/fire performance, autonomous operation or field validation without specific evidence.

**Status: GREEN** — these claim boundaries are part of the documented PUI89 engineering approach; keep enforcing them.

## Cost and safety controls retained

This change adds no paid service, API, subscription, cloud GPU, paid runner, runtime dependency or model download. It adds no scheduled workflow, does not command physical hardware, does not change branch rulesets or default branches, and does not merge any pull request.

The new validation workflow runs only on relevant pull requests, relevant pushes and manual dispatch. It checks register totals, repository identifiers, full commit SHAs, draft schema metadata and ActionProposal safety constants; it is not a full JSON Schema meta-validator.

## Recommended implementation order

1. Canonical shared AI Core schema and compatibility tests.
2. Evidence register updates tied to exact commits and workflow artefacts.
3. Cross-project deterministic conformance tests.
4. Ruleset and branch-protection review by the repository owner.
5. Project-specific benchmark and dataset validation.
6. Bilingual website and README status updates based only on verified evidence.

**Audit limitation:** this is a read-only configuration and source audit. It is not a penetration test, complete dependency/licence audit, full branch-protection review, model evaluation, physical safety assessment or certification.
