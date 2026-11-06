# PUI89 AI Robotics

**An independent AI initiative exploring practical intelligence across agriculture, disaster response, public-safety screening, home assistance and mobile robotics.**

PUI89 develops AI applications and robotics concepts around a shared engineering question:

> How can intelligent systems perceive real-world environments, represent uncertainty, support decisions, and move safely from software experiments toward validated robotic applications?

The initiative combines domain knowledge, independent software development, applied research questions and an evidence-led engineering process. Project concepts, software tests, simulations and visual designs are distinguished from validated model performance or physical robot capability.

**Public portfolio:** https://pui89.github.io/  
**Official initiative profile:** https://pui89.github.io/company.html  
**Thai profile:** https://pui89.github.io/company-th.html  
**GitHub:** https://github.com/Pui89  
**Collaboration:** puinuanmanee@gmail.com

## PUI89 engineering principles

- **Evidence before claims:** separate proposed designs, implemented code, automated tests, simulations and field-validated performance.
- **Human oversight:** consequential decisions remain under appropriate human authority.
- **Safety by design:** missing, stale, noisy or conflicting evidence leads to conservative handling.
- **Reproducibility:** record code versions, data provenance, configurations, test results, metrics and failure cases.
- **Zero-cost foundation:** do not introduce paid APIs, subscriptions, cloud GPUs, hosted inference, model downloads or recurring-cost commitments without explicit approval.
- **Supply-chain care:** check origin, licence, security, resource requirements and total cost before adopting tools or dependencies. PUI89 excludes Chinese-origin AI models, providers and model-hosting services from its approved stack.
- **Responsible collaboration:** work with domain experts, research partners, data stewards and engineering mentors.

## Portfolio directory — seven separate projects

Each project has its own repository, product boundary, engineering requirements and evidence status. English and Thai project pages are separate.

| Project | Repository | English website | Thai website |
|---|---|---|---|
| Coconut Harvest AI | [GitHub](https://github.com/Pui89/Coconut-Harvest-AI) | [English](https://pui89.github.io/coconut.html) | [ไทย](https://pui89.github.io/coconut-th.html) |
| Extreme Flood Rescue AI | [GitHub](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | [English](https://pui89.github.io/flood-rescue.html) | [ไทย](https://pui89.github.io/flood-rescue-th.html) |
| Multimodal Narcotics Screening AI | [GitHub](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | [English](https://pui89.github.io/screening.html) | [ไทย](https://pui89.github.io/screening-th.html) |
| AI HOME — indoor assistant | [GitHub](https://github.com/Pui89/HOMEGUARD-AI) | [English](https://pui89.github.io/home.html) | [ไทย](https://pui89.github.io/home-th.html) |
| AI NOMAD — outdoor mobile assistant | [GitHub](https://github.com/Pui89/AI-NOMAD) | [English](https://pui89.github.io/nomad.html) | [ไทย](https://pui89.github.io/nomad-th.html) |
| PUI89 AI Robot Car | [GitHub](https://github.com/Pui89/ai-robot-car) | [English](https://pui89.github.io/ai-robot-car.html) | [ไทย](https://pui89.github.io/ai-robot-car-th.html) |
| PUI89 AI Robot Motorcycle — EasyRide | [GitHub](https://github.com/Pui89/ai-robot-motorcycle) | [English](https://pui89.github.io/ai-robot-motorcycle.html) | [ไทย](https://pui89.github.io/ai-robot-motorcycle-th.html) |

**Portfolio count: 7 projects · 7 repositories · 7 English project pages · 7 Thai project pages.**

AI HOME and AI NOMAD are separate products: HOME is an indoor four-wheel concept; NOMAD is an outdoor quadruped mobile-assistant concept. They may share PUI89 AI Core software contracts, but physical design, navigation, payload, sensors, environmental limits and safety validation remain separate.

The car and motorcycle are early-stage research concepts, not built, road-tested, road-certified or validated vehicles.

## Shared PUI89 AI Core

PUI89 prioritises a reusable software foundation instead of duplicating project-specific intelligence. Shared interfaces are intended to include:

| Contract or capability | Purpose |
|---|---|
| WorldState | Timestamped state, hazards, stale observations and conflicts |
| Observation | Validated sensor or data input with provenance |
| ActionProposal | Bounded, reviewable proposed action—not direct actuator authority |
| FailureReport | Structured faults, missing evidence and blocked safety gates |
| Uncertainty handling | Preserve unknown and low-confidence states |
| Evidence alignment | Link claims and decisions to source observations |
| Safety gates | Enforce constraints, safe-hold and human-review requirements |
| Evaluation records | Preserve configurations, test cases, metrics and failure examples |

The intended workflow is: perceive → validate → update world state → assess uncertainty → propose → apply safety gates → simulate or request authorised action → verify → report.

Shared contracts do not make the projects identical. Each domain retains its own sensor, mechanical, environmental, data and safety requirements.

## Agentic AI, VLM and VLA research direction

PUI89 intends to progress in controlled stages:
- **Agentic workflows:** structured input validation, multi-step reasoning records, policy gates, review routing and evidence reports.
- **Vision-language models (VLMs):** optional experiments only after licence, provenance, hardware and evaluation checks.
- **Vision-language-action (VLA):** begin with mock interfaces and constrained action proposals; never connect an unvalidated model directly to physical actuators.
- **Simulation-first robotics:** test proposed actions in repeatable environments before considering hardware.
- **Human oversight:** preserve safe-hold and explicit review for uncertain, conflicting or out-of-scope conditions.

A model being available does not establish that it is accurate, safe, suitable or licensed for a particular use.

## Project-specific research areas

- **Coconut Harvest AI:** fruit detection, maturity assessment, orchard perception and proposed harvesting workflows. Dataset rights, annotation quality and model performance require separate evidence.
- **Extreme Flood Rescue AI:** flood-scene awareness, human/animal detection research, navigation and simulation-first rescue-support concepts. Scenario depths and platform capabilities remain design targets unless validated.
- **Multimodal Narcotics Screening AI:** provenance-aware multimodal screening research with uncertainty and authorised human review. RGB alone cannot establish chemical identity; no autonomous enforcement decisions.
- **AI HOME:** indoor assistance and home-safety observations. The concept is separate from NOMAD and is not a certified alarm or building-safety system.
- **AI NOMAD:** outdoor mobile assistance, carrying-support research, supervised following and environmental awareness. Payload, locomotion and weather limits remain unvalidated.
- **AI Robot Car:** early-stage intelligent vehicle research concept; no roadworthiness or autonomous-driving claim.
- **AI Robot Motorcycle — EasyRide:** early-stage mobility and rider-assistance research concept; no roadworthiness or autonomous-driving claim.

## Verification and status policy

Use explicit labels:
- **PROPOSED** — design intention or future milestone.
- **IMPLEMENTED** — code or documentation exists.
- **UNIT-TESTED** — specified software behaviour passed a recorded test.
- **SIMULATION-TESTED** — a configured simulator produced recorded results for specified scenarios.
- **MEASURED** — a quantitative result is supported by a documented method and conditions.
- **HARDWARE-TESTED** — a physical component or system was tested under documented conditions.
- **FIELD-VALIDATED** — appropriate real-world evidence supports the stated operating envelope.
- **NOT RUN / NOT MEASURED / UNKNOWN / NOT VALIDATED** — evidence is absent.

A passing unit test is not proof of model accuracy, simulator fidelity, physical safety, field performance or deployment readiness. Concept images are illustrations, not operational evidence. Check each repository's Actions page and current reports for the latest run status.

## Development roadmap

1. **Shared software foundations:** maintain common contracts, machine-readable reports, safety gates and cross-project conformance tests.
2. **Evidence and evaluation:** verify data provenance, licensing, annotation quality, leakage-safe splits and domain-specific metrics.
3. **Agentic and simulation workflows:** test stale inputs, conflicting observations, uncertainty, fault handling and safe-stop behaviour.
4. **Optional local model evaluation:** check licence, origin, download size, RAM, VRAM, disk and offline operation first. No automatic model downloads.
5. **Supervised hardware feasibility:** define platform-specific mechanical, sensor, environmental and safety requirements before any controlled physical test.

## Collaboration and initiative status

PUI89 welcomes research collaborators, academic mentors, AI and robotics engineers, domain experts, data stewards, open-source contributors and responsible sponsors. Useful collaboration should be linked to a clear milestone such as dataset review, independent annotation audit, reproducible benchmark, simulator scenario, hardware feasibility study or supervised pilot.

PUI89 is an independent initiative and project identity in development. This README does not imply that a legal company has been incorporated, that funding or sponsorship has been secured, that customers are deployed, or that any product is commercially validated.

**PUI89's commitment is to build carefully, test transparently, report limitations honestly and advance toward real-world applications only when evidence justifies the next step.**
