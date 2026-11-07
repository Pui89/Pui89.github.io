# PUI89 PromptOps — Controlled Prompt Library

**Status:** Initial documentation proposal; review required before adoption  
**Date:** 8 November 2026  
**Scope:** Shared prompt standards for the seven-project PUI89 portfolio  
**Cost boundary:** USD 0 by default; no new services, APIs, subscriptions, model downloads, package installs or cloud compute.

## Purpose

PUI89 PromptOps is a version-controlled collection of reusable instructions for evidence review, architecture, security, testing, AI evaluation, robotics safety, data/model governance, failure analysis, project maturity and bilingual documentation.

It is a **prompt and review standard**, not an AI model, autonomous agent, runtime library, certification, or proof that any project capability works.

The PUI89 AI Core conformance document states that the portfolio website is a documentation/status surface and that no standalone shared-core repository is currently recorded. Accordingly, this directory is a documentation proposal only. It does not claim to be a canonical runtime package or to have been integrated into project adapters.

## Portfolio scope

- Coconut Harvest AI
- Extreme Flood Rescue AI
- Multimodal Narcotics Screening AI / PUI89 Sentinel
- PUI89 AI HOME
- PUI89 AI NOMAD
- PUI89 AI Robot Car
- PUI89 AI Robot Motorcycle — EasyRide

Shared AI Core remains shared infrastructure, not an eighth product.

## How to use a prompt

1. Select the prompt matching the task.
2. Supply only the minimum necessary, non-secret project context and evidence references.
3. Treat repository files, logs, model outputs, webpages and datasets as **untrusted input**, not as instructions that can override this standard.
4. Require the response to distinguish verified facts, interpretations, proposals and unknowns.
5. Independently verify important claims against source files, tests, commits or other primary evidence.
6. Keep any proposed code or configuration change in a reviewable branch and pull request.
7. Do not merge, deploy, purchase, install, download model weights or operate hardware solely because a prompt recommends it.

## Mandatory output discipline

Every review should state:
- **Scope:** repositories, files, versions, dates and components actually examined.
- **Evidence:** exact paths, line ranges, commit SHAs, test commands/results or source references where available.
- **Findings:** severity, impact, likelihood where supportable, and reproducibility.
- **Unknowns:** inaccessible files, missing permissions, unrun tests and unsupported assumptions.
- **Recommendation:** smallest safe next step, owner/approval needed and acceptance criteria.
- **Limitations:** what the review does not prove.

Never convert missing evidence into a pass. Use `NOT_RUN`, `NOT_VERIFIED`, `UNKNOWN`, `PASS` and `FAIL` distinctly.

## Safety and approval boundaries

- Action proposals are advisory or simulation-only.
- No prompt may authorize physical actuation, autonomous driving/riding, cutting, lifting, rescue deployment, screening enforcement, building control or emergency response.
- Human review remains mandatory for safety-critical, enforcement, medical, structural, electrical, fire and road-related decisions.
- Never request, print or store credentials, API keys, payment details, personal data or private user records.
- Do not add dependencies, call paid endpoints, access cloud GPUs, download models or incur metered usage.
- Do not modify protected branches or bypass repository protections.
- Do not claim field validation, certification, commercial readiness or measured model performance without appropriate evidence.

## Language

The catalog and governance summaries should be maintained in English and Thai. Technical prompt templates may be written in English, but should request Thai explanations when the intended audience is Thai. Preserve technical identifiers, schema keys, units and code exactly in both languages.

## Relationship to prompts.chat

PUI89 reviewed the public prompt-library project [f/prompts.chat](https://github.com/f/prompts.chat). Its README describes a community prompt collection and states that prompt content/data such as `prompts.csv` and `PROMPTS.md` are CC0 1.0, while source code and site-authored content are MIT. PUI89's templates in this directory are newly authored for PUI89; no prompt text or code is copied from that repository. Re-check the upstream licence files and individual provenance before adopting any upstream text in future.

## Current implementation status

- Prompt templates authored: 10
- Runtime integration: **NOT IMPLEMENTED**
- Project-adapter adoption: **NOT VERIFIED**
- Automated prompt testing: **NOT IMPLEMENTED**
- Model performance or product readiness proven by this library: **NO**

This is a proposal for review, not a claim of completed integration.
