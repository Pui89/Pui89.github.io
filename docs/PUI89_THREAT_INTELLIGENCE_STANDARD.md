# PUI89 Threat Intelligence & Security Evidence Standard

**Status:** Proposed shared standard  
**Schema:** [pui89-threat-intelligence.schema.json](../schemas/pui89-threat-intelligence.schema.json)  
**Scope:** All current and future PUI89 project repositories; Shared AI Core is the common infrastructure layer.  
**Policy:** Zero-cost first, evidence-led, least privilege, human approval, no unnecessary rulesets.

## Purpose

Use one consistent, machine-readable record for credible cyber threats and defensive findings that may affect PUI89 repositories, websites, workflows, dependencies, AI models, datasets, credentials, applications or future robotic systems.

A threat report is not proof that PUI89 has been targeted or compromised. Separate external threat intelligence from observations made in PUI89 repositories.

## Required record fields

Each record must include:
- Unique ID, record date, category, title and current status.
- Source URLs, source type and publication/access dates where known.
- Affected PUI89 projects and concrete assets where established.
- Evidence descriptions, URLs, observation dates and commit SHAs where applicable.
- Confidence and severity as separate assessments.
- Attribution caveats and verification gaps.
- Defensive mitigations, responsible role, approval/implementation state and measurable validation criteria.

## Evidence and attribution rules

1. Prefer primary government, CERT, standards-body, vendor incident-response and GitHub advisory sources.
2. Record the original publication date and the date the information was reviewed.
3. Attribute actor claims to the source. Do not present vendor attribution as independently proven fact.
4. Mark inaccessible settings, incomplete scans and unsupported claims as **unverified**.
5. A threat's existence does not establish PUI89 exposure. Map relevance to specific assets and evidence.
6. Never publish secret values, exploit payloads, private user data or operational details that would enable abuse.

## Defensive categories

Track APT campaigns, AI-assisted phishing, malware, credential theft, software and dependency supply-chain compromise, GitHub Actions/workflow attacks, model/checkpoint provenance, dataset integrity, prompt injection and unsafe agent/tool use, secrets exposure, website compromise, ransomware and cryptographic transition risks.

Post-quantum cryptography is a migration-readiness topic, not a reason to copy attacker tooling or replace algorithms without a documented interoperability and security review. Distinguish standard encryption from post-quantum algorithms.

## Status and risk semantics

- **new / monitoring:** intelligence is being assessed.
- **mitigation_proposed:** a defensive action is recommended but not approved.
- **mitigation_in_progress:** an approved action is underway.
- **mitigated:** a control has been implemented but validation may remain.
- **resolved:** acceptance criteria have been tested and evidence is linked.
- **accepted_risk:** explicitly accepted by the project owner with rationale and review date.
- **not_applicable:** evidence supports that the threat does not apply to the assessed asset.
- **unverified:** access or evidence is insufficient to decide.

Confidence describes the strength of supporting evidence; severity describes potential impact. Do not use confidence as a substitute for severity.

## Project integration

Every project should:
1. Link to this shared standard and schema rather than maintain a divergent copy.
2. Keep project-specific threat records in a documented location, using the common schema.
3. Record affected repository, workflow, dependency, model, dataset or application component precisely.
4. Link remediation to a test, workflow run, reviewed commit or other acceptance evidence.
5. Preserve a history of new, recurring, mitigated and resolved findings.

The PUI89 website repository hosts the canonical schema. Projects should reference its version and avoid copying it unless a deliberate versioned snapshot is required.

## Operating boundaries

- Read-only review by default.
- No paid APIs, subscriptions, cloud GPUs, paid runners, metered scans or surprise billing.
- No package installation, model downloads, untrusted code execution, malware execution or live-target testing during routine review.
- No repository edits, merges, deployments, permission changes or physical robot actions without explicit founder approval.
- Do not add GitHub rulesets as a routine response. Review existing controls and propose a change only when a concrete, verified defect justifies it.
- Use least privilege, constrained tools, explicit allowlists, input/output validation, safe failure and human approval for high-impact actions.

## Minimum validation before calling a record resolved

- The source and affected asset are identified.
- The proposed mitigation is implemented in an approved change.
- The relevant test or check passes on the exact commit being reported.
- Evidence is linked and reproducible.
- Remaining limitations are documented.

A passing workflow does not prove a repository is secure, malware-free, penetration-tested or certified.
