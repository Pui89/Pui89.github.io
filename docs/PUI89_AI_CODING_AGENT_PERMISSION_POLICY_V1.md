# PUI89 AI Coding Agent Permission Policy

**Version:** 1.0  
**Effective date:** 8 November 2026  
**Status:** Proposed — review required before adoption  
**Scope:** All current and future PUI89 repositories and AI coding agents

## 1. Purpose

This policy defines the minimum permissions and approval workflow for AI agents that inspect, edit, test, or otherwise interact with PUI89 source repositories. It is tool- and model-provider-independent. A tool-specific configuration is an implementation aid, not proof that the policy is enforced.

## 2. Mandatory principles

1. **Read-only by default.** An agent may inspect ordinary project files but must not modify them without explicit, scoped approval.
2. **Least privilege.** Grant only the minimum access needed for one task, repository, and session.
3. **Human authority.** An agent cannot approve its own plan, permissions, changes, tests, pull request, merge, release, deployment, or physical action.
4. **Zero-cost operation.** No paid API, subscription, cloud GPU, paid runner, metered inference, purchase, or recurring service without explicit founder approval. The default is no spending.
5. **Non-Chinese AI supply chain.** Do not use Chinese-origin models, model providers, model-hosting services, or unclear-provenance AI services. Verify publisher, ownership/control, hosting path, licence, and model provenance. If uncertain, mark NOT APPROVED.
6. **Data minimisation.** Do not expose credentials, secrets, private datasets, personal data, or unrelated repositories to an agent or model service.
7. **Evidence before acceptance.** Every accepted change must have a reviewable diff, relevant test results, limitations, and a traceable commit.
8. **No autonomous physical authority.** AI agents must not actuate robots, vehicles, sensors, valves, breakers, alarms, or other physical equipment.

## 3. Permission matrix

| Operation | Default | Conditions |
|---|---|---|
| Read ordinary files in the approved repository | Allow | Exclude secrets and sensitive data |
| Search and inspect repository source | Allow | Do not expose secret values in output |
| Read secrets, tokens, credentials, private keys or production configuration | Deny | Never request them for coding tasks |
| Propose a plan or code patch | Allow | Proposal only; no implied permission to execute |
| Edit, create, rename or delete files | Ask | Explicit approval for the named files and task |
| Run shell commands or tests | Ask | Exact command and working directory shown before execution |
| Install or update packages, tools or models | Deny | Requires separate explicit approval after cost, source, licence and resource review |
| Access files outside the approved repository | Deny | Separate, narrow approval required; default remains blocked |
| Network access, web fetch, remote API or MCP tools | Deny | Separate review of destination, data sent and cost required |
| Git status, diff and log inspection | Allow where safely configured | Read-only commands only |
| Git commit | Ask | Show staged diff and exact commit message |
| Git push, force push, merge or PR merge | Deny | Founder performs separately |
| Change repository settings, secrets, rulesets or permissions | Deny | Founder-only action |
| Release, publish or deploy | Deny | Founder-only action |
| Hardware, robot or vehicle actuation | Deny | Not delegated to coding agents |

A permission prompt is not a sandbox. Shell commands execute with the host process's available filesystem, process, and network authority unless a separate OS/container sandbox restricts them.

## 4. Required operating workflow

1. Identify the repository, current branch, commit SHA and working-tree state.
2. Inspect existing issues, pull requests and relevant files to avoid duplicate work.
3. Produce a plan listing intended files, commands, dependencies, network destinations and expected evidence.
4. Identify any secrets, personal data, model/data licensing, cost or supply-chain implications.
5. Obtain explicit approval for the exact scope before edits or commands.
6. Make the smallest change on a dedicated branch; never edit the default branch directly.
7. Show the complete diff and explain every changed file.
8. Run only approved tests; do not install missing dependencies automatically.
9. Report passed, failed, skipped and not-run checks separately, with commit SHA and logs/evidence links.
10. Stop for human review. Do not merge, release, deploy, or perform hardware actions.

Approval is task-scoped and one-time by default. Do not select persistent “always allow” permissions for shell commands, edits, network access, or external directories.

## 5. Isolation and secret protection

- Use a clean, dedicated working copy containing no credentials or production secrets.
- Prefer a low-privilege OS account and a disposable, resource-limited sandbox for shell execution.
- Disable network egress in the sandbox unless a separately approved task requires a specific destination.
- Mount only the target repository; do not mount home directories, SSH folders, cloud credentials, browser profiles, password stores, or unrelated projects.
- Do not rely on editor rewind or Git alone to recover shell-command side effects.
- Preserve a clean Git checkpoint before any approved mutation.
- If adequate isolation is unavailable, keep the agent in read-only mode and do not permit shell execution.

## 6. Model and data-provider requirements

Before using any model, verify and record:

- Model name, publisher, ownership/control and provenance.
- Provider and actual hosting/processing location where ascertainable.
- Model-weight and software licences and permitted use.
- Whether prompts, source code, files, logs or telemetry leave the local machine.
- Whether data is retained or used for training, and applicable privacy controls.
- Local/offline operation and network-egress behaviour.
- RAM, VRAM, disk, latency and power requirements.
- Any API, usage, subscription, bandwidth or storage charges.

A local coding-agent application does not imply local inference. If model traffic leaves the machine, classify the workflow as remote processing and do not use it until the provider and data handling are approved. If origin, licence, hosting or cost is unclear, mark NOT APPROVED.

## 7. Acceptance gates

A change is eligible for human acceptance only when applicable evidence is available:

- [ ] Correct repository, branch and base commit identified.
- [ ] Existing work and open PR overlap checked.
- [ ] Plan and permission scope approved.
- [ ] No secrets or unapproved data were exposed.
- [ ] No unapproved cost, dependency, download or network access occurred.
- [ ] Diff reviewed and limited to intended files.
- [ ] Relevant tests run; outcomes and skipped tests disclosed.
- [ ] Security, privacy, licence and supply-chain impacts reviewed.
- [ ] Rollback/recovery path documented.
- [ ] Human reviewer explicitly accepts the change.

A passing unit test does not prove model accuracy, physical safety, cybersecurity assurance, certification, or field readiness.

## 8. Enforcement and rollout

- Keep this policy as the canonical portfolio-level standard.
- Tool-specific files must be version-specific and reviewed against the official documentation for the exact installed release.
- Do not copy configuration blindly across tools or versions.
- Begin with read-only inspection in a non-production test repository.
- Validate deny/ask behaviour using harmless test files and harmless commands before any real project work.
- Extend to other repositories only after the configuration has been independently checked.
- Review after tool upgrades, provider changes, security incidents, or permission regressions.

## 9. Implementation status

This document is a proposed standard. Adding it to a repository does not enforce permissions in an installed coding agent. The accompanying OpenCode V2 example is an illustrative configuration template, not a verified sandbox or a universal agent policy. It must be checked against the installed OpenCode version and tested before use.

**PUI89 rule: AI may inspect and propose; humans authorise consequential changes; evidence determines acceptance.**
