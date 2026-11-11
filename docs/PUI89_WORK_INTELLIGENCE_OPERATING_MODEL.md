# PUI89 Work Intelligence — Operating Model

**Status:** Proposed operating architecture; not deployed autonomous agents.  
**Policy:** Zero-cost first, evidence-led, human-supervised, protected pull requests.  
**Scope:** Website, Shared AI Core and all current/future PUI89 project repositories.

## Purpose
Increase research and engineering throughput by standardising intake, triage, execution, verification and approval. Prefer event-driven automation to additional scheduled polling.

## Work pipeline
1. **Intake:** record problem, repository/project, source, expected outcome, constraints and owner.
2. **Triage:** assess value, urgency, dependencies, cost, security/safety risk and evidence required.
3. **Execute:** use a feature branch; keep changes small and reviewable.
4. **Verify:** run deterministic tests and checks; capture exact commit SHA, commands, environment and results.
5. **Approve:** human review before merge, release, external communication, destructive changes, credential/permission changes, spending or hardware actuation.

## Specialist responsibility areas
- Research Intelligence: primary literature, official docs, standards, grants and opportunities with provenance.
- Engineering Intelligence: requirements, architecture, interfaces, constraints and acceptance criteria.
- Verification Intelligence: tests, schemas, regressions, benchmarks and failure reports.
- Security Intelligence: secrets, permissions, dependencies, licences, branch protection and recovery.
- Documentation Intelligence: README, technical records, changelogs and claim/evidence alignment.
- Project Coordination: shared dependencies, duplicate work, blockers and Shared AI Core reuse.
- Partnership Intelligence: universities, researchers, grant programmes and sponsors; verify eligibility and dates.
- Website Intelligence: bilingual parity, links, sitemap, accessibility, metadata and evidence consistency.

These are responsibility areas, not deployed autonomous agents.

## Event-driven automation candidates
- Pull request opened/synchronized: run existing tests, schema checks, link checks and documentation validation.
- Issue opened/labelled: classify work and attach project/priority/risk/evidence labels.
- Commit pushed: run deterministic regression checks and record status for that SHA.
- Release candidate: assemble evidence summary and require human approval.
- Dependency update: inspect changelog, licence, vulnerability and compatibility before merge.
- Scheduled work: use only where event-driven triggers cannot satisfy the requirement; account for existing scheduled-task capacity.

Before adding or changing GitHub Actions, inspect existing workflows, permissions, third-party actions, minutes and artifact retention. Avoid workflows that create unbounded loops or unnecessary repeated runs.

## Evidence contract
Every verification record should include:
- repository and project;
- branch and full commit SHA;
- date/time and environment;
- command/workflow and version;
- result: passed, failed, skipped or unknown;
- relevant logs/artifacts and limitations;
- reviewer/approval status where applicable.

Never interpret missing checks as success. A green CI run proves only that named checks passed for that commit; it does not prove model accuracy, physical safety, certification or field performance. Keep measured, synthetic, estimated, proposed and unknown evidence distinct.

## Zero-cost and security boundaries
- No paid API, subscription, cloud GPU, metered service or model download without explicit approval.
- Review GitHub Actions usage and billing exposure before enabling additional workflows, artifacts or external services.
- No secrets in source, public issues, logs, fixtures or static website assets.
- Least privilege; minimal permissions; avoid untrusted third-party actions; review pinned versions and licences.
- Do not weaken branch protection, bypass required checks or merge without approval.
- Destructive changes, credential changes, external communications, financial commitments and physical actuation require human approval.
- Preserve version history and test restoration; do not claim recovery until a restore test passes.

## Implementation sequence
1. Improve the existing read-only Command Centre; do not duplicate its portfolio dashboard.
2. Add bilingual Work Intelligence documentation and connect it to the homepage and Command Centre.
3. Audit existing GitHub Actions and repository protections before proposing event-driven workflow changes.
4. Introduce structured issue templates and shared verification reports only after repository-specific review.
5. Pilot one low-risk workflow on the website repository; validate cost, permissions, outputs and rollback.
6. Expand across project repositories only after successful pilot evidence.

## Current implementation boundary
The Work Intelligence page and this operating model are documentation/presentation only. They do not create a task backend, deploy agents, schedule monitoring, change repository settings or execute GitHub Actions.
