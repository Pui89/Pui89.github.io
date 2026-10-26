# PUI89 Long-Term Free-First Operating Plan

## Objective

Keep PUI89 useful and maintainable for as long as possible without depending on subscriptions, paid APIs, cloud GPUs, paid hosting, advertising spend, or a single vendor. “Free-first” means choosing tools that can be used at no required cost under their current terms; it does not promise that every service will remain free forever.

## Operating rules

1. **Local-first:** prefer Python, Git, local tests, local files, and small local models where practical.
2. **Open formats:** keep project data in documented formats such as CSV, JSON, YAML, Markdown, and ordinary image files; avoid proprietary lock-in.
3. **No surprise spending:** do not enable billing, paid APIs, cloud compute, subscriptions, paid domains, or ads without explicit approval.
4. **Free-tier limits:** assume hosted services can change quotas, suspend free plans, or add restrictions. Recheck terms before relying on them for critical work.
5. **Portable backups:** keep local copies of important source, documentation, data manifests, and releases. Use Git tags and exports for milestones.
6. **Evidence before scale:** add tools only when they solve a measured problem. Prefer a small reliable pipeline over many agents and frameworks.
7. **Human review:** AI agents may draft, classify, or suggest; a person reviews changes, safety-sensitive decisions, data rights, and public claims.
8. **Licences and privacy:** review code, model-weight, dataset, image, and dependency licences independently. Do not upload confidential or sensitive data to hosted tools without authorization.
9. **Security maintenance:** pin important dependencies, review advisories, keep secrets out of repositories, and test upgrades before adopting them.
10. **Document exit paths:** every critical hosted service should have a practical fallback or an export path.

## Stable baseline

| Function | Preferred no-required-subscription option | Fallback if availability or quotas change |
|---|---|---|
| Source control | Git locally; GitHub public repositories where appropriate | Local Git clone and portable repository mirror |
| Website | Static HTML/CSS on GitHub Pages | Keep static source exportable; publish on another free static host only after checking terms |
| Automated checks | Local pytest/Ruff/pip-audit; GitHub Actions for eligible free usage | Run the same checks locally |
| AI inference | Small local model with Ollama or compatible open-source runtime | Rule-based scripts, manual review, or a different licence-compatible local model |
| Vision development | OpenCV/PyTorch locally when hardware permits | Smaller datasets, CPU tests, deterministic fixtures, and lightweight baselines |
| Documentation | Markdown in Git | Local text files and exported release archives |
| Website diagnostics | Browser Lighthouse and available Search Console data | Manual browser checks and locally stored checklists |
| Task tracking | GitHub Issues/Projects if free terms fit | Markdown issue log, CSV task register, and Git commit history |
| Data/evaluation | Versioned manifests, checksums, split definitions, and local reports | Recreate reports from preserved manifests and scripts |

## Long-term model policy

- Start with a rule-based or small-model solution before adding a larger model.
- Choose model size based on measured memory and latency, not marketing claims.
- Store model name, exact version/revision, licence, source, checksum where available, hardware, configuration, and evaluation results.
- Keep a no-model fallback for basic workflows and critical safety checks.
- Do not make model downloads automatic in CI unless the files are small, licence-compatible, and permitted by the runner's storage/time limits.
- Never treat model output as proof of a fact, safety, chemical identity, rescue readiness, or physical capability.

## Project order

### 1. Coconut Harvest AI
First resolve image source and reuse rights, hashes, annotation geometry, reviewer status, and leakage-safe train/validation/test splits. Then establish a small reproducible baseline with documented precision/recall and runtime. Do not claim detection quality until results are measured on an appropriate held-out dataset. A 0–30 m palm-height range remains a design challenge, not verified reach.

### 2. Extreme Flood Rescue AI
Keep early development simulation-first. Use deterministic scenarios, fault injection, reproducible configuration files, and explicit simulation limits. Simulation does not prove safe navigation in real flood currents or operational rescue capability.

### 3. Multimodal Narcotics Screening AI
Use authorized data and appropriate reference methods. Record uncertainty and false-positive/false-negative risks, require authorized human review, and protect sensitive data. Ordinary RGB appearance or a model confidence score cannot establish chemical identity.

## Maintenance cadence

- **Every change:** run the smallest relevant local tests and inspect the diff.
- **Weekly when actively developing:** review open failures, licence questions, and the next highest-value blocker.
- **Monthly:** check dependency advisories, backup integrity, free-tier changes affecting critical services, and project status links.
- **At each milestone:** tag or export a reproducible snapshot with instructions, known limitations, and test evidence.
- **Before any public demo or customer pilot:** verify image/data rights, privacy, safety boundaries, accessibility, and all claims.

## Stop rules

Pause adding tools when a tool needs payment, billing activation, excessive downloads, unreviewed data access, unclear commercial rights, or creates more maintenance than value. Prefer a documented manual fallback over a fragile dependency. If an existing resource becomes unavailable, inactive, or no longer offers a usable $0 option, remove its recommendation and website link, record the date and reason, and use a local/open alternative where practical. Do not delete project code or evidence because an external tool retires.

## What this plan does not promise

No service, model, hardware, free tier, or open-source project is guaranteed to remain available or cost-free forever. PUI89 will re-evaluate dependencies and keep portable alternatives rather than promise permanent free access to third-party services.

## Automatic no-paid-upgrade policy

- Keep the catalogue limited to tools and services that do not require a paid upgrade for the documented use case.
- The weekly GitHub Actions audit checks curated resource-table URLs for repeated outages and explicit paid-upgrade wording (for example, paid/pro/premium plans or buying credits).
- A table row is removed after three consecutive checks of an explicit paid-upgrade signal or a failed URL. Inconclusive fetches do not count as evidence.
- The scan is a conservative text check, not a guarantee: pricing may be JavaScript-rendered or worded differently. Review the generated audit report; do not treat absence of a flag as proof that a tool is free.
- The automation only removes curated Markdown resource-table rows. It never deletes source code, tests, datasets, evidence, workflows, repository history, or the service account itself.
- No purchase, subscription, billing activation, or paid API call is made. Local/open-source alternatives are preferred.
