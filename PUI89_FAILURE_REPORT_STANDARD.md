# PUI89 Verification and Failure Report Standard

## Purpose

Use one machine-readable report format across Coconut Harvest AI, Extreme Flood Rescue AI, Multimodal Narcotics Screening AI, and the shared PUI89 core. Reports should make failures, skipped checks, blocked prerequisites, and evidence limits visible.

Schema: `schemas/pui89-failure-report.schema.json`.

## Rules

1. Use `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, or `PARTIAL`.
2. Record the repository commit, run kind, timestamp, environment, and workflow URL when available.
3. Report passed, failed, skipped, and blocked counts separately. Never invent unknown counts.
4. Give each failure a stable ID, severity, category, message, and reproducibility status. Add a root cause only after it is confirmed.
5. Include metrics only when measured under a documented protocol. Unknown AI metrics must remain absent or null.
6. State whether a run measured AI performance, executed a simulator, or validated hardware.
7. A unit-test pass applies only to the software behavior tested. It does not prove AI accuracy, chemical identification, rescue effectiveness, worker safety, or physical robot readiness.
8. Never include secrets, credentials, or unnecessary personal or private sensor data.

## Status definitions

- `PASS`: all checks in the declared scope passed.
- `FAIL`: one or more checks in the declared scope failed.
- `BLOCKED`: a required prerequisite was unavailable.
- `NOT_RUN`: the check was not attempted.
- `PARTIAL`: some checks ran while others were skipped or blocked.

A partial test scope must never be described as a full-suite pass.
