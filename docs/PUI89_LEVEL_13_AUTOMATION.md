# PUI89 Level 13 — Cross-Project Automation

**Status:** automation implemented in this branch; execution evidence is pending a GitHub Actions run.  
**Purpose:** run a small, dependency-free verification set against the current seven-project portfolio.

## What the workflow does

The workflow `.github/workflows/pui89-level13-portfolio-verification.yml` checks out the portfolio repositories and runs selected existing Python `unittest` suites through `tools/pui89_level13_portfolio_smoke.py`.

It records, per project:
- repository and exact checked-out commit SHA;
- each selected test suite and its result;
- a plain-language note when a repository or test suite is unavailable;
- a machine-readable JSON report, Markdown summary and individual test logs.

## Current selected suites

| Project | Selected suites |
|---|---|
| Coconut Harvest AI | `test_pui89_core.py`, `test_pui89_ai_core_conformance.py` |
| Extreme Flood Rescue AI | `test_pui89_core.py`, `test_pui89_ai_core_conformance.py` |
| Multimodal Narcotics Screening AI | `test_pui89_core.py`, `test_pui89_ai_core_conformance.py` |
| PUI89 AI HOME | Existing tests if its repository checkout is available |
| PUI89 AI NOMAD | `test_core.py`, `test_pui89_shared_workflow_contract.py`, `test_pui89_shield_policy.py` |
| PUI89 AI Robot Car | `test_contracts.py`, `test_safety.py` |
| PUI89 AI Robot Motorcycle | `test_motorcycle_risk_scenarios.py` |

The AI HOME repository checkout was not accessible to the setup review (GitHub returned 404). Its step is therefore non-blocking and the report must show it as BLOCKED if it remains unavailable. This is not a pass.

## Trigger and cost controls

- Manual trigger: GitHub Actions → **PUI89 Level 13 Cross-Project Verification** → Run workflow.
- Pull-request trigger: only when the verifier, this document or its workflow changes.
- No cron schedule; no recurring runner usage is added.
- Python standard library only; no `pip install`, model downloads, dataset downloads, hosted inference, paid API, cloud GPU or hardware connection.
- Read-only repository permissions; no token for cross-repository writes; no automatic merge or release.
- The GitHub-hosted runner may still count against account Actions quotas. Check current account allowances before repeated use; no unlimited-free usage is claimed.

## Status meanings

- `PASS`: every selected suite for that project discovered at least one test and exited successfully.
- `FAIL`: one or more selected suites failed or discovered no tests.
- `BLOCKED`: the repository checkout or tests directory was unavailable; no pass is claimed.
- Portfolio `REVIEW_REQUIRED`: at least one project is BLOCKED but none of the selected suites failed.
- Portfolio `FAIL`: at least one selected suite failed.
- Portfolio `PASS`: all seven project checkouts and selected suites passed.

## Evidence boundary

This is a selected software smoke test, not a full test-suite run. Passing results do not establish AI accuracy, model quality, calibration, sensor truth, simulation realism, hardware readiness, road safety, certification or field performance. Each project result is kept separate; no cross-project score is calculated.
