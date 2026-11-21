# PUI89 Level 13 — Six-Product Verification Automation

**Updated:** 17 November 2026  
**Active portfolio:** exactly six products. Shared AI Core is shared infrastructure, not a seventh product.  
**Status:** workflow definition aligned to the six canonical product repositories; the first run against this updated scope is pending CI execution.

## Purpose

The workflow `.github/workflows/pui89-level13-portfolio-verification.yml` checks out the six active product repositories and runs selected existing Python `unittest` suites through `tools/pui89_level13_portfolio_smoke.py`.

It records, per product:
- canonical repository and exact checked-out commit SHA;
- each selected test suite and its result;
- a plain-language note when a repository or test suite is unavailable;
- a machine-readable JSON report, Markdown summary and individual test logs.

## Current active product scope and selected suites

| Active product | Canonical repository | Selected suites |
|---|---|---|
| Coconut Harvest AI | [Repository](https://github.com/Pui89/Coconut-Harvest-AI) | `test_pui89_core.py`, `test_pui89_ai_core_conformance.py` |
| PUI89 Sentinel — All-Terrain Exploration & Inspection Robot | [Repository](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot) | `test_pui89_core.py`, `test_pui89_ai_core_conformance.py` |
| PUI89 AI HOME | [Repository](https://github.com/Pui89/AI-Home-Safety-Robot) | `test_safety_gate.py`, `test_shared_core_v01.py` |
| PUI89 AI NOMAD | [Repository](https://github.com/Pui89/AI-Mobile-Assistant-Robot) | `test_pui89_shared_workflow_contract.py`, `test_pui89_shield_policy.py`; pytest-dependent `test_core.py` remains excluded |
| PUI89 AI Global SUV | [Repository](https://github.com/Pui89/PUI89-AI-Global-SUV) | `test_contracts.py`, `test_safety.py` |
| PUI89 AI Step-Through Scooter | [Repository](https://github.com/Pui89/AI-Step-Through-Scooter) | `test_motorcycle_risk_scenarios.py`, `test_shared_core_v01.py` |

The former Multimodal Narcotics Screening AI, AI Robot Car and AI Robot Motorcycle repository identities are not current active products. Their historical repositories and records are not deleted by this change and are not checked out as active products in this workflow.

## Trigger and cost controls

- Manual trigger: GitHub Actions → **PUI89 Level 13 Cross-Project Verification** → Run workflow.
- Pull-request trigger: only when the verifier, this document or its workflow changes.
- No cron schedule; no recurring runner usage is added.
- Python standard library only; no `pip install`, model downloads, dataset downloads, hosted inference, paid API, cloud GPU or hardware connection.
- Read-only repository permissions; no cross-repository writes, automatic merge or release.
- GitHub-hosted runner usage may count against account Actions quotas; no unlimited-free usage is claimed.

## Status meanings

- `PASS`: every selected suite for that product discovered at least one test and exited successfully.
- `FAIL`: one or more selected suites failed or discovered no tests.
- `BLOCKED`: repository checkout or tests directory was unavailable; no pass is claimed.
- Portfolio `REVIEW_REQUIRED`: at least one product is BLOCKED but none of the selected suites failed.
- Portfolio `FAIL`: at least one selected suite failed.
- Portfolio `PASS`: all six product checkouts and selected suites passed.

## Evidence boundary

This is a selected software smoke test, not a full test-suite run. Passing results do not establish AI accuracy, model quality, calibration, sensor truth, simulation realism, hardware readiness, road safety, certification or field performance. Each product result is kept separate; no cross-product score is calculated.

## Historical run

The first execution on 6 November 2026, [run 42249714511](https://github.com/Pui89/Pui89.github.io/actions/runs/42249714511), used the then-existing repository inventory and is retained as a historical audit record only. It is not a current six-product portfolio result. The updated six-product workflow must produce a new run before its outcome can be reported as current.
