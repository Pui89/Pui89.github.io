# PUI89 Public Website — Security Core Adoption Record

**Shared standard:** PUI89 Security Core Standard v0.1, proposed in [PUI89-Shared-AI-Core PR #13](https://github.com/Pui89/PUI89-Shared-AI-Core/pull/13). The shared standard is currently a draft and has not been merged.
**Scope:** Public website source, static assets, publishing workflow, domain/DNS configuration where observable, visitor-facing forms or external links, and repository access.
**Review date:** 2026-11-10
**Overall status:** IN PROGRESS — technical enforcement has not yet been independently verified.

## Control status

| Control area | Current evidence status | Required next verification |
|---|---|---|
| Repository ownership and access | Unknown | Inspect collaborators, outside collaborators, GitHub Apps, deploy keys, webhooks and token scopes |
| Default-branch protection | Unknown | Inspect actual rulesets/branch protection, required reviews/checks, bypass actors, force-push and deletion controls |
| Publishing workflow | Unknown | Inspect Pages build/deploy workflow, workflow permissions, action SHA pins and secret exposure |
| Secrets and configuration | Unknown | Check tracked files/history safely; verify no private credentials or sensitive configuration are published |
| Dependencies and assets | Unknown | Review third-party scripts, packages, embedded widgets, asset provenance and licences |
| Privacy and external links | Unknown | Inspect analytics, forms, third-party requests, cookies and any visitor data collection |
| Domain and DNS | Unknown | Verify registrar/DNS account security, MFA, recovery and ownership controls outside this repository |
| Backup and recovery | Unknown | Identify independent website/source backup and successful restore evidence |

## Required audit outputs

For every control, record one status: **Specified**, **Configured**, **Tested**, **Failed**, **Unknown**, or **Not applicable** (with reason). Attach evidence links and dates. Record findings, severity, remediation owner, and verification result.

## Zero-cost constraints

No paid API, subscription, metered service, new package, or external integration is authorised by this record. If cost or data-transfer behaviour is uncertain, stop and request owner approval.

## Recovery evidence

- Independent backup location / credential boundary: Unknown
- Backup integrity evidence: Unknown
- Last successful restore drill: Unknown
- Website deployment rollback test: Unknown

Do not describe the website as hardened until relevant repository, publishing, account and domain controls have been configured and verified.
