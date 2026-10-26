# PUI89 Free-First Tools, Models and Helpers

PUI89 prioritises reliable engineering progress over collecting tools. This list focuses on resources that can be used without a required subscription, while recognising that free tiers have quotas and model/data licences vary.

## Start here: core free-first stack

| Need | Resource | Use | Cost and caution |
|---|---|---|---|
| Source control and project collaboration | [GitHub](https://github.com/) | Store code, issues, plans, and evidence | Keep secrets and private customer data out of public repositories |
| Repeatable automation | [GitHub Actions](https://docs.github.com/en/actions) | Run tests and checks after changes | Public repository runners have free usage; private repository limits differ |
| Python tests | [pytest](https://docs.pytest.org/) | Exercise expected and failure behaviour | Passing software tests is not proof of real-world safety or accuracy |
| Linting and formatting | [Ruff](https://docs.astral.sh/ruff/) | Catch common Python quality issues | Pin versions where reproducibility matters |
| Dependency security | [pip-audit](https://github.com/pypa/pip-audit) | Identify dependencies with known advisories | Review and test updates rather than blindly upgrading |
| Local AI inference | [Ollama](https://ollama.com/) | Run compatible language models locally | Downloads use local disk/RAM; cloud options are separate |
| Model discovery | [Hugging Face Models](https://huggingface.co/models) | Find vision, language, and multimodal models | Check each model's licence, commercial terms, file size, and hardware needs |
| Website quality | [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) | Check performance, accessibility, and basic SEO | Scores are diagnostic, not a guarantee of rankings or sales |
| Search visibility | [Google Search Console](https://search.google.com/search-console/about) | Monitor impressions and search queries | Requires site verification; data takes time to appear |
| Optional one-off site audit | [FreeScan.app](https://www.freescan.app/) | A free audit is currently offered; optional only | Paid Pro monitoring exists; Lighthouse is the default, and FreeScan is not required |

## Local model guidance

- Begin with one small quantized model, not a collection of large downloads.
- A laptop with an RTX 3050 4 GB VRAM and limited system memory may need a 1B–3B model, a reduced context, or CPU fallback; performance is not guaranteed.
- Use local models for drafting documentation, summarising non-sensitive logs, generating test ideas, or organising notes.
- Treat model output as a suggestion. Tests, code review, evidence review, and human decisions remain authoritative.
- Never send secrets, confidential customer data, identifiable disaster-response records, or sensitive screening information to hosted AI services without explicit authorisation and suitable data controls.

## Project-specific resource links

### Coconut Harvest AI — highest priority
[Repository](https://github.com/Pui89/Coconut-Harvest-AI) · [Free-first catalogue](https://github.com/Pui89/Coconut-Harvest-AI/blob/main/docs/FREE_FIRST_RESOURCE_CATALOGUE.md) · [Marketing and sales playbook](https://github.com/Pui89/Coconut-Harvest-AI/blob/main/docs/MARKETING_SEO_SALES_PLAYBOOK.md)

Prioritise image provenance and licence checks, annotation QA, leakage-safe splits, and a small reproducible baseline. The 0–30 m palm-height range is a design challenge, not a verified robot reach.

### Extreme Flood Rescue AI
[Repository](https://github.com/Pui89/Extreme-Flood-Rescue-AI) · [Free-first catalogue](https://github.com/Pui89/Extreme-Flood-Rescue-AI/blob/main/docs/FREE_FIRST_RESOURCE_CATALOGUE.md) · [Marketing and partnership playbook](https://github.com/Pui89/Extreme-Flood-Rescue-AI/blob/main/docs/MARKETING_SEO_SALES_PLAYBOOK.md)

Prioritise deterministic simulation and fault-injection tests. Simulation does not validate flood physics, navigation in real currents, or rescue readiness. Water-depth scenarios are targets, not physical operating ratings.

### Multimodal Narcotics Screening AI
[Repository](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) · [Free-first catalogue](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/blob/main/docs/FREE_FIRST_RESOURCE_CATALOGUE.md) · [Responsible marketing and evaluation playbook](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/blob/main/docs/MARKETING_SEO_SALES_PLAYBOOK.md)

Prioritise authorised or synthetic data, documented reference methods, uncertainty, false-positive/false-negative analysis, and human review. Ordinary images and model confidence alone do not establish chemical identity.

## Free-first marketing and customer discovery

- Improve the project page and README before adopting marketing automation.
- Use Lighthouse and Search Console to measure site quality and search visibility.
- Publish only images with verified rights and label concept art and simulations clearly.
- Ask a small number of relevant growers, technical reviewers, or potential partners for feedback using personalised, respectful messages.
- Avoid scraped contact lists, bulk unsolicited messages, paid ad campaigns, and recurring marketing subscriptions until an offer and audience are validated.

## Cost and licence guardrails

- No paid API, cloud GPU, recurring subscription, ad spend, or paid hosting without explicit approval.
- Free tiers have quotas, terms, and sometimes non-commercial restrictions; recheck before use.
- Open-source code does not automatically make model weights, datasets, images, or generated outputs unrestricted for commercial use.
- Record adopted tool, version, licence, purpose, hardware fit, and any usage limit.
- The website and catalogue do not imply that any project is field-validated, certified, commercially deployed, or ready for autonomous operation.


## Resource activity check — 26 October 2026

The main linked resources were opened and responded during a spot check: GitHub Actions documentation, pytest, Ruff, pip-audit, Ollama, Hugging Face Models, Lighthouse, and Google Search Console. This is a link-response check, not a guarantee of uptime or a review of every feature or current quota.

**Optional only:** FreeScan currently presents a free one-off website audit but also promotes paid Pro monitoring. It is not required for PUI89; use Lighthouse first. Do not pay for it. If the free audit is removed, the URL stops responding, or the tool becomes unusable without payment, remove it from this catalogue and the PUI89 website rather than replacing it with another paid tool.

**Maintenance rule:** if a listed resource becomes unavailable, inactive, or no longer has a usable $0 option, remove its recommendation and website link, record the date and reason in the next update, and prefer a local/open alternative. Do not delete PUI89 project code or evidence just because an external service is retired. Recheck links periodically; this document does not imply continuous monitoring.

## Automatic no-paid-upgrade policy

- Keep the catalogue limited to tools and services that do not require a paid upgrade for the documented use case.
- The weekly GitHub Actions audit checks curated resource-table URLs for repeated outages and explicit paid-upgrade wording (for example, paid/pro/premium plans or buying credits).
- A table row is removed after three consecutive checks of an explicit paid-upgrade signal or a failed URL. Inconclusive fetches do not count as evidence.
- The scan is a conservative text check, not a guarantee: pricing may be JavaScript-rendered or worded differently. Review the generated audit report; do not treat absence of a flag as proof that a tool is free.
- The automation only removes curated Markdown resource-table rows. It never deletes source code, tests, datasets, evidence, workflows, repository history, or the service account itself.
- No purchase, subscription, billing activation, or paid API call is made. Local/open-source alternatives are preferred.
