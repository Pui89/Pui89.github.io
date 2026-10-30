# PUI89 AI Robotics

**An independent AI initiative exploring practical intelligence across agriculture, disaster response, and public-safety screening.**

PUI89 develops AI applications and robotics concepts around a shared engineering question:

> How can intelligent systems perceive real-world environments, represent uncertainty, support decisions, and move safely from software experiments toward validated robotic applications?

PUI89 brings together domain knowledge, independent software development, applied research questions, and an evidence-led engineering process. The initiative is in development; project concepts, software tests, simulations, and visual designs are described separately from validated model performance or physical robot capability.

- **Public portfolio:** https://pui89.github.io/
- **Official initiative profile:** https://pui89.github.io/company.html
- **Thai profile:** https://pui89.github.io/company-th.html
- **Growth roadmap:** https://pui89.github.io/growth.html
- **Thai growth roadmap:** https://pui89.github.io/growth-th.html
- **Partnership and trust:** https://pui89.github.io/support.html
- **GitHub:** https://github.com/Pui89
- **Collaboration:** puinuanmanee@gmail.com

---

## Latest portfolio engineering update — 30 October 2026

The three flagship repositories now share the PUI89 AI Core safety contract and automated conformance checks. Their merged rule-based simulation evaluations each completed **7/7 scenarios and 9/9 steps, with 0 reported failures**:

- [Coconut Harvest AI simulation evidence](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881372992)
- [Extreme Flood Rescue AI simulation evidence](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40919457152)
- [Multimodal Screening AI simulation evidence](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40919469891)

Coconut's merged dataset audit also passed 15 checks across dataset structure, image hashes and split leakage: [audit run and evidence artifact](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40944312469).

**Evidence boundary:** these are rule-based scenario and software-verification results. They are not model accuracy metrics, proof of dataset licensing or annotation correctness, validated simulator physics, physical robot performance, safety certification, or commercial deployment. The PUI89 Command Centre dataset-monitoring addition is proposed in [PR #33](https://github.com/Pui89/Pui89.github.io/pull/33) and is not yet merged.

## 1. Mission and vision

### Mission

Build practical, modular, and responsibly evaluated AI applications that help people understand complex environments and make better-informed decisions.

### Vision

Develop a reusable AI engineering foundation that connects perception, world-state understanding, uncertainty-aware reasoning, task planning, simulation, and—only after appropriate validation—robotic action.

### Guiding principles

- **Evidence before claims:** distinguish implemented software, tested components, proposed designs, simulation results, and field-validated performance.
- **Human oversight:** keep consequential decisions under appropriate human authority.
- **Safety by design:** uncertain, missing, stale, or conflicting inputs should lead to conservative handling rather than unsupported action.
- **Reproducibility:** record code versions, data provenance, configurations, test results, metrics, and failure cases.
- **Cost-conscious development:** prefer local-first and open-source tools where suitable; review licences, resource requirements, privacy, and total cost before adoption.
- **Responsible collaboration:** seek domain experts, research partners, data stewards, and engineering mentors.

---

## 2. Three flagship AI applications

The projects address different domains but share common engineering foundations.

### 2.1 Coconut Harvest AI

**Agricultural AI application and robotic harvesting concept**

Repository: [Pui89/Coconut-Harvest-AI](https://github.com/Pui89/Coconut-Harvest-AI)

Research direction:
- Coconut fruit detection and maturity assessment.
- Computer vision and, where supported, depth-aware perception.
- Orchard scene understanding and localization inputs.
- Uncertainty-aware harvest task planning.
- Proposed robotic arm, cutting mechanism, collection basket, and harvest verification workflow.

Current boundary: the maturity categories and 0–30 m palm-height range are design/research targets, not validated detector coverage or demonstrated physical reach. The project does not claim a trained, accurate all-stage detector or a working physical harvesting robot. Dataset provenance, reuse rights, image hashes, annotation quality, and leakage-safe evaluation must be established before training claims are made.

### 2.2 Extreme Flood Rescue AI

**AI application for disaster reconnaissance and rescue-support robotics concepts**

Repository: [Pui89/Extreme-Flood-Rescue-AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI)

Research direction:
- Human and animal detection research.
- Flood-scene perception and hazard awareness.
- World-state tracking, navigation, and communication-failure handling.
- Ground, boat, and aerial platform concepts.
- Repeatable scenario design and simulation-first evaluation.

Current boundary: scenarios up to 15 m flood depth are design/simulation targets only. They do not establish validated water physics, navigation, buoyancy, rescue capability, or operation at that depth. Ground, boat, and aerial platforms require separate evaluation; results must not be transferred between platforms without evidence.

### 2.3 Multimodal Narcotics Screening AI

**AI-assisted screening workflow and mobile robotic inspection concept**

Repository: [Pui89/Multimodal-Narcotics-Screening-AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI)

Research direction:
- A provenance-aware workflow for multiple permitted data modalities.
- Modality quality, calibration, timestamp, and sensor-disagreement checks.
- Uncertainty handling and escalation to authorised human review.
- A proposed quadruped inspection assistant for controlled, authorised environments.
- Evaluation of false positives, false negatives, and modality-specific limitations.

Current boundary: this is not a validated narcotics detector. Candidate substance categories do not imply validated class-specific performance. RGB images alone cannot establish chemical identity. X-ray or chemical screening requires suitable, separately validated sensors and lawful procedures. AI outputs must not independently accuse, detain, search, or make enforcement decisions.

---

## 3. Shared PUI89 AI Core

The proposed shared foundation is the **PUI89 AI Core**: reusable software contracts and verification tools that can support all three applications without pretending that every domain has identical sensors, risks, or performance requirements.

### Shared engineering capabilities

| Capability | Purpose |
|---|---|
| Common interfaces | Consistent data and component contracts across projects |
| Perception inputs | Validate image and sensor observations |
| World-state tracking | Maintain timestamped observations, hazards, stale data, and conflicts |
| Uncertainty handling | Preserve unknown or low-confidence states instead of forcing a guess |
| Task planning | Represent objectives as reviewable steps and action proposals |
| Agent interfaces | Support model-optional, multi-step decision workflows |
| VLM/VLA interfaces | Prepare controlled integration points for future vision-language and action research |
| Automated testing | Verify software contracts and expected failure behaviour |
| Failure reporting | Record errors, missing evidence, and blocked gates |
| Experiment reporting | Preserve configuration, code version, data hashes, metrics, and latency |
| Simulation evidence | Record scenario inputs and simulated outcomes where a simulator is actually configured |

### Intended system loop

1. **Perceive** — receive and validate images or sensor observations.
2. **Understand** — update world state and identify hazards or inconsistencies.
3. **Assess** — estimate confidence and identify unknown information.
4. **Plan** — produce a bounded task proposal with constraints.
5. **Gate** — apply safety rules and human-review requirements.
6. **Simulate or act** — begin with offline/simulated actions; hardware action requires separate authorisation and validation.
7. **Verify** — record outcomes, failures, and reproducible evidence.

The shared core is an engineering direction, not a claim that all modules are complete or that the three projects have achieved autonomous operation.

---

## 4. Agentic AI, VLM and VLA research direction

PUI89 intends to progress in stages rather than adopting large models before the underlying software and evidence are ready.

- **Agentic workflows:** structured input validation, decision steps, policy gates, review routing, and evidence reports.
- **Vision-language models (VLMs):** optional future experiments for image-and-language understanding, subject to model licence, provenance, hardware fit, and measurable evaluation.
- **Vision-language-action (VLA):** begin with mock interfaces and constrained action proposals; do not connect an unvalidated model directly to physical actuators.
- **Simulation:** test proposed actions in suitable, repeatable environments before considering hardware.
- **Human oversight:** preserve explicit review and safe-hold behaviour for uncertain, conflicting, or out-of-scope conditions.

A model being downloadable or runnable does not establish that it is suitable, accurate, safe, or licensed for a particular application.

---

## 5. Verification and evidence status

Repository snapshots dated **29 October 2026** reported the following combined software-test outcomes:

| Project | Reported test evidence | What it means |
|---|---:|---|
| Shared PUI89 AI Core | 13 tests passed | Shared software checks passed in the reported run |
| Coconut detection evaluator | 5 tests passed | Evaluator logic tested; detector accuracy not measured |
| Coconut dataset preflight | 4 tests passed | Preflight tool tested on synthetic fixtures; real dataset approval is separate |

These are dated repository-reported results, not a live guarantee of current CI status. Check each repository's Actions page and current reports for later runs.

### What these results do not prove

- They do not establish model accuracy or generalisation.
- They do not validate a real-world dataset or its reuse rights.
- They do not prove simulator fidelity or real-world rescue performance.
- They do not validate chemical identification or narcotics screening.
- They do not establish physical robot operation, safety certification, or commercial readiness.

Use **NOT RUN**, **NOT MEASURED**, **UNKNOWN**, or **NOT VALIDATED** where evidence is absent. Never replace missing results with estimates.

### Current evidence links

- [PUI89 Cross-Project Verification Snapshot](PUI89_CROSS_PROJECT_VERIFICATION.md)
- [Cross-Project Command Centre](reports/pui89-command-centre.md)
- [Coconut Harvest AI Actions](https://github.com/Pui89/Coconut-Harvest-AI/actions)
- [Extreme Flood Rescue AI Actions](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions)
- [Multimodal Narcotics Screening AI Actions](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions)

---

## 6. Development roadmap

### Phase 1 — Reliable software foundations
- Keep automated checks passing and reproducible across all three repositories.
- Maintain common interfaces, machine-readable reports, and consistent status definitions.
- Test world-state updates, stale observations, uncertainty, conflicting inputs, and failure paths.
- Preserve project-specific safety and data requirements.

### Phase 2 — Evidence and evaluation
- Complete dataset provenance, licensing, annotation, and quality reviews.
- Establish leakage-safe train/validation/test splits where model training is appropriate.
- Define domain-specific metrics and baselines before reporting model performance.
- Publish failure cases, sample counts, thresholds, configurations, and limitations.

### Phase 3 — Simulation and agentic workflows
- Configure a simulator only where it materially supports a project.
- Record simulator versions, scenario parameters, seeds, telemetry, and outcomes.
- Expand model-optional agentic workflows and mock VLA interfaces.
- Verify safe-hold and human-review behaviour under faults.

### Phase 4 — Optional local model evaluation
- Check licence and usage terms, download size, RAM, VRAM, disk, and offline operation first.
- Prefer small, resource-appropriate experiments.
- Do not download large model weights or install substantial toolchains automatically.
- Compare against deterministic baselines and report measured results.

### Phase 5 — Supervised hardware feasibility
- Define hardware, sensor, mechanical, environmental, and safety requirements.
- Conduct controlled, supervised tests only after simulation and risk reviews.
- Validate each platform and operating envelope independently.
- Do not infer field capability from concept art, unit tests, or simulation-only results.

---

## 7. Research and engineering themes

PUI89's cross-project research interests include:

- Applied computer vision and multimodal perception.
- Agricultural intelligence and precision agriculture.
- Disaster reconnaissance and human/animal detection.
- Uncertainty-aware AI and safe decision support.
- World-state representation and task planning.
- Agentic workflows and VLM/VLA integration.
- Simulation-first robotics and reproducible evaluation.
- Human-in-the-loop systems, provenance, and responsible deployment.

These are areas of investigation and development, not a list of claimed expertise or completed research results.

---

## 8. Founder and initiative background

PUI89 is led by an independent creator whose background combines agricultural science, public-sector agricultural research, and work involving agricultural information and ICT systems.

The initiative follows a domain-led approach: identify a practical problem, translate it into an AI application and robotics concept, build software foundations, test assumptions, document limitations, and seek appropriate technical collaboration.

PUI89 does not present a traditional computer science or robotics degree as a prerequisite for its founder's work. Instead, the portfolio should be assessed through transparent project artefacts, reproducible tests, technical decisions, research questions, and demonstrated learning. Specialist engineering review remains important for advanced robotics, sensing, safety, and deployment.

---

## 9. Collaboration, support and future development

PUI89 welcomes:
- Research collaborators and academic mentors.
- AI, computer vision, robotics, and software engineering contributors.
- Agricultural researchers, growers, and potential pilot partners.
- Disaster-response and humanitarian domain experts.
- Responsible sensing and screening specialists.
- Open-source contributors, in-kind technical support, and relevant sponsorship or grant introductions.

Useful collaboration should be tied to a clear milestone: for example, dataset review, an independent annotation audit, a reproducible benchmark, a simulator scenario, a hardware feasibility study, or a supervised pilot.

### Partner resources

- [Partner landing page](https://pui89.github.io/support.html)
- [One-page partner brief](PARTNER_BRIEF.md)
- [Support and Sponsorship Brief](SUPPORT_AND_SPONSORSHIP.md)
- [Proposed Support Milestones](SPONSOR_MILESTONES.md)
- [Research Portfolio](RESEARCH_PORTFOLIO.md)
- [Innovation Strategy](INNOVATION_STRATEGY.md)
- [Growth Roadmap](GROWTH_ROADMAP.md)
- [Market and Product Strategy](MARKET_AND_PRODUCT_STRATEGY.md)

PUI89 is currently an initiative and project identity in development. This README does not imply that a legal company has been incorporated, that funding or sponsorship has been secured, that customers are deployed, or that products are commercially validated.

---

## 10. Free-first and responsible technology policy

PUI89 prioritises useful, reproducible engineering and avoids unnecessary recurring costs.

Preferred approach:
- Python and standard-library tools for lightweight checks where practical.
- GitHub Actions for repository automation, subject to platform quotas and current terms.
- OpenCV and suitable local ML frameworks for experiments when justified.
- pytest and static-analysis tools where configured.
- Structured JSON/CSV reports, hashes, versioned manifests, and clear experiment records.
- Local-first workflows and optional model runtimes only after resource and licence checks.

No paid API, cloud GPU, subscription, hosted inference service, automatic model download, or recurring-cost commitment should be introduced without explicit approval. Free tiers can have limits and changing terms. Open-source software does not automatically make model weights or datasets unrestricted; check each licence and data-use condition.

---

## 11. Project links

| Resource | Link |
|---|---|
| PUI89 public portfolio | https://pui89.github.io/ |
| Coconut Harvest AI | https://github.com/Pui89/Coconut-Harvest-AI |
| Extreme Flood Rescue AI | https://github.com/Pui89/Extreme-Flood-Rescue-AI |
| Multimodal Narcotics Screening AI | https://github.com/Pui89/Multimodal-Narcotics-Screening-AI |
| PUI89 website source | https://github.com/Pui89/Pui89.github.io |

---

## 12. Status and claims policy

PUI89 distinguishes clearly between:

- **Implemented:** code or documentation exists in the repository.
- **Unit-tested:** specified software behaviour passed a recorded test.
- **Evaluated:** a defined experiment was run and its evidence is available.
- **Simulation-tested:** a configured simulator produced recorded results for specified scenarios.
- **Hardware-tested:** a physical component or system was tested under documented conditions.
- **Field-validated:** independent or appropriately controlled real-world evidence supports the stated operating conditions.
- **Proposed / target:** a design intention or future milestone, not a demonstrated capability.

Concept images are illustrations, not operational evidence. Synthetic fixtures are software-test inputs, not real-world benchmarks. A passing software test is not proof of model accuracy, physical safety, or deployment readiness.

**PUI89's commitment is to build carefully, test transparently, report limitations honestly, and advance from software foundations toward real-world applications only when evidence justifies the next step.**
