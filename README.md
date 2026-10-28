# PUI89 AI Robotics

Public-facing website for PUI89's independent AI and robotics initiative, presenting technology projects, engineering principles, and a responsible path toward future products.

## Cross-project command centre

- **Latest project status:** [PUI89 Cross-Project Command Centre](https://github.com/Pui89/Pui89.github.io/blob/main/reports/pui89-command-centre.md)
- Read-only summary of the latest public repository commits and recent GitHub Actions runs; unknown or missing results are never treated as passing tests.
- Updated by a free weekly GitHub Actions workflow; no paid AI API, model download or third-party Python package is required.

## Support, sponsorship and open-source collaboration

- **Partner landing page:** [PUI89 AI Robotics — Partner with us](https://pui89.github.io/support.html)
- **One-page partner brief:** [PARTNER_BRIEF.md](PARTNER_BRIEF.md)

PUI89 welcomes technical mentors, research collaborators, agricultural and robotics partners, open-source contributors, in-kind resources, and relevant sponsorship or grant introductions.

- **Support brief:** [Support PUI89 AI Robotics](SUPPORT_AND_SPONSORSHIP.md)
- **Public website:** https://pui89.github.io/
- **Main contact:** puinuanmanee@gmail.com
- **Projects:** [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI), [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI), and [Multimodal-Narcotics-Screening-AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI).

Potential supporters should identify the expertise, resources, data access, or milestone they can help with. PUI89 is an initiative in development; this invitation does not imply existing sponsors, customers, incorporated-company status, or validated field performance.

## Website

Public portfolio: https://pui89.github.io/

The [Research Portfolio](RESEARCH_PORTFOLIO.md) summarises the projects' research questions, evidence plans, and limitations. The [Growth Roadmap](GROWTH_ROADMAP.md) describes the cost-conscious development approach. The [Market and Product Strategy](MARKET_AND_PRODUCT_STRATEGY.md) sets out the first customer hypothesis, discovery questions, pilot evidence, and a 90-day plan. The [Innovation Strategy](INNOVATION_STRATEGY.md) describes proposed technical differentiators, research questions, and a staged path beyond individual prototypes.

The [Support and Sponsorship Brief](SUPPORT_AND_SPONSORSHIP.md) explains ways to collaborate, and the [Support Milestones](SPONSOR_MILESTONES.md) document defines proposed work packages and measurable acceptance evidence. The [Free-First Upgrade Status](FREE_FIRST_UPGRADE_STATUS.md) records the latest verified CI results, shared agentic-workflow foundation, and the current dataset/evaluation blockers. The [Free-First Tools and Models Guide](FREE_FIRST_TOOLS_AND_MODELS.md) collects local AI models, testing/security tools, SEO resources, and cost/licence guardrails; the website includes a matching Free tools section. The [Long-Term Free-First Operating Plan](FREE_FIRST_LONG_TERM_PLAN.md) defines local-first fallbacks, portable backups, maintenance cadence, and no-surprise-spending rules.

The [Early Pilot Brief](COCONUT_ORCHARD_PILOT_BRIEF.md) outlines the first customer-discovery offer, potential measures, data handling, and limitations for a proposed coconut orchard workflow.

## Purpose

Present three projects with clear links, engineering principles, and honest descriptions of what is implemented versus proposed:

- [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) — agricultural AI and robot workflow research.
- [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) — simulation-first disaster reconnaissance and rescue-support research.
- [Multimodal-Narcotics-Screening-AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) — local-first, human-reviewed screening workflow prototype.

## Recent project updates — 26 October 2026

The project repositories have received recent documentation and engineering updates:

- [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI): merged RGB-D localization input validation ([PR #67](https://github.com/Pui89/Coconut-Harvest-AI/pull/67)), orchard robot concept requirements ([PR #65](https://github.com/Pui89/Coconut-Harvest-AI/pull/65)), and an automated protection policy ([PR #84](https://github.com/Pui89/Coconut-Harvest-AI/pull/84)). These changes strengthen software validation and document future safety requirements; they do not validate physical reach, harvesting, or sensor accuracy.
- [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI): refreshed the README to clarify simulation-only flood-depth scenarios and the current status of optional local inference ([PR #67](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/67)).
- [Multimodal-Narcotics-Screening-AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI): refreshed the README to clarify inference limits, evidence requirements, and human review ([PR #42](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/42)).

**Current priority:** verify the original coconut image files, hashes, reuse rights, and annotations before approving any dataset for training. The latest repository snapshot I checked records 34 candidate records and 0 approved for training. Project-specific repositories remain the source of truth for their latest status.

These updates are repository and software/documentation evidence only. They do not establish validated field performance, physical robot capability, certified safety, or a validated narcotics detector.

## Engineering standard

See [ENGINEERING_STANDARD.md](ENGINEERING_STANDARD.md) for the project-wide rules on evidence maturity, release gates, safety, security, licensing, cost control, and company-building milestones.

## Evidence and status policy

PUI89 AI Robotics is currently used as a project and initiative identity. This website does not claim that a legal entity has been incorporated, or that products are commercially validated, robots are certified, customers are deployed, or funding has been secured. Each repository is the source of truth for implementation and test status. Concept artwork is not operational evidence; synthetic test data is not a real-world benchmark.

## Cost policy

Prefer open-source tools and local workflows. Review paid services, hardware purchases, licences, privacy obligations, and deployment costs before adopting them. GitHub Pages availability and usage remain subject to GitHub's terms and quotas.

## Website

Static HTML/CSS. No analytics, third-party fonts, tracking scripts, external JavaScript libraries, or paid API calls are required.

Website source: [index.html](index.html)

## Local preview

Open `index.html` in a browser, or run a local static server from the repository root:

```bash
python -m http.server 8000
```

Then visit `http://127.0.0.1:8000`.

## Publishing

The repository can be published with GitHub Pages using the included Actions workflow. In the repository settings, confirm **Settings → Pages → Build and deployment → Source: GitHub Actions** if it is not already configured. The website should only be described as live after a successful deployment is verified.

## Company-development status

The website is designed to present the work professionally while the future business is being developed. Before offering products or services, confirm the appropriate legal and tax requirements, intellectual-property rights, privacy obligations, safety requirements, and customer needs. The website itself is static and does not require paid hosting or a custom domain. GitHub Pages availability and quotas remain subject to GitHub's terms.

## Free-first AI tooling policy

PUI89 prioritises useful, reproducible engineering over adopting every available AI platform. The current preferred stack is:

- **Automation:** Python and GitHub Actions for repository checks and repeatable reports, subject to platform quotas.
- **Computer vision:** OpenCV and PyTorch for local experiments when each project has suitable data, hardware, and model licences.
- **Testing and observability:** pytest, Ruff where configured, structured logs, versioned data manifests, and reproducible benchmark reports.
- **AI agents:** existing Python decision-support workflows first; a framework such as LangGraph is optional and should be added only for a specific multi-step requirement.
- **Retrieval:** local documentation search first; optional local vector indexing only when it solves a demonstrated problem.

**Cost policy:** no paid API, cloud GPU, new subscription, hosted inference, or unexpected billing change without explicit approval. Free tiers may have quotas and terms. Open-source code does not automatically make model weights or datasets unrestricted; review their licences and usage rights separately.

**Evidence policy:** automated tests verify software behaviour, not model accuracy, commercial readiness, or physical-robot safety. Each project's repository remains the source of truth for its actual implementation and test status.
