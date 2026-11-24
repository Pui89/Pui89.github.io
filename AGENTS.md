# PUI89 Agent Operating Rules

When asked to audit GitHub Actions or optimize workflow cost, follow
[the PUI89 Workflow Agent Guide](docs/PUI89_WORKFLOW_AGENT_GUIDE.md).

Default to read-only inspection. Do not modify workflows, run or rerun Actions,
change billing or repository settings, alter permissions, or merge PRs unless
the user gives separate, explicit approval for that specific action.

Use the dependency-free static inventory:
`python3 tools/pui89_workflow_audit.py`

Never claim cost savings from YAML alone. Correlate findings with measured
GitHub Actions job durations and billing usage. Preserve security and required
checks. Do not use paid APIs, metered services, cloud GPUs, or models/providers
with unclear or Chinese origin.
