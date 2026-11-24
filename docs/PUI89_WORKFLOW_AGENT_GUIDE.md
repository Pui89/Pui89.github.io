# PUI89 Workflow Agent Guide

## Purpose
Use a free-tier or local agentic coding assistant to review GitHub Actions usage and workflow design. The first phase is strictly read-only.

## Recommended operating modes
- Use Google Antigravity's individual free tier as a standalone desktop agent, subject to its published weekly quotas. Do not route its account/session through third-party agents or automate account rotation.
- Alternatively use OpenCode with an approved local model provider. Do not select models or providers with unclear provenance or Chinese origin. Do not enable paid API providers, credit top-ups, auto-recharge, or metered inference.
- OpenHands is optional only when a suitable local model and sufficient local compute are already available; do not provision paid cloud resources.

## First task
1. Open this repository in the chosen agent.
2. Ask it to read this guide and `AGENTS.md`.
3. Run `python3 tools/pui89_workflow_audit.py`.
4. Review the generated inventory against GitHub Actions run history and Billing > Usage. Static YAML cannot establish actual runner minutes or billed amounts.
5. Produce a written report separating verified facts, hypotheses, and unknowns.

## Mandatory safety boundaries
- Read-only by default. Do not edit, delete, rename, disable, merge, dispatch, rerun, or change permissions for workflows.
- Do not change billing, budgets, repository settings, branch protection, secrets, tokens, or permissions.
- Do not add an Actions workflow to run this auditor; that would consume runner minutes.
- Do not install packages, download models, use cloud GPUs, call paid APIs, or create subscriptions without explicit approval.
- Do not expose secrets, tokens, private data, or environment variables in reports.
- Preserve Security Audit, dependency checks, required checks, and evidence/contract tests unless the user separately approves a reviewed replacement.
- Do not infer savings from workflow names or YAML alone. Use measured job durations and runner billing data.
- Any proposed code change must be a minimal, separate pull request, with a rollback plan and explicit human approval before merge.

## Required report format
For each finding include:
- Evidence: exact workflow path and relevant trigger/job/step.
- Classification: verified fact, likely overlap, or hypothesis.
- Cost relevance: measured minutes if available; otherwise mark unknown.
- Security impact: checks potentially affected.
- Recommendation: no change, path-filter candidate, trigger adjustment candidate, or manual investigation.
- Validation and rollback plan.

## Agent prompt
"Perform a read-only audit of PUI89 GitHub Actions. Start by running
`python3 tools/pui89_workflow_audit.py`. Then inspect workflow YAML and recent
run/job history. Identify duplicate execution only when the same work is
demonstrably repeated. Do not change files, dispatch workflows, rerun jobs,
create PRs, or access billing/settings. Keep security checks intact. Report
verified facts separately from hypotheses and quantify savings only from
measured runner minutes."
