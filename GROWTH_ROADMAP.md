# PUI89 AI Robotics — Growth Roadmap

**Purpose:** Build a technically credible, commercially useful AI and robotics business through evidence, disciplined spending, and customer validation.

This roadmap is a plan, not a claim that PUI89 is already an incorporated company, that the projects are certified products, or that customers, revenue, funding, or field validation already exist.

## Operating principles

1. **Evidence before claims.** Distinguish implemented code, automated test results, benchmark results, simulations, and real-world validation.
2. **Customer value before feature count.** Prioritise problems that a defined customer group genuinely needs solved.
3. **Free-first execution.** Prefer local development and free/open-source tools. Do not add paid APIs, cloud compute, datasets, subscriptions, or hardware costs without explicit approval.
4. **Safety and human oversight.** Keep safety-critical actions behind appropriate independent safeguards and human approval. Never treat a software test as proof of physical safety.
5. **Maintainable, reusable technology.** Reuse tested components where appropriate, document dependencies, track licences, and keep projects reproducible.
6. **Protect trust.** Publish limitations, failures, data provenance, and the exact conditions under which results were measured.

## Stage 1 — Establish a reliable foundation

### Engineering milestones
- Keep automated tests passing on all three project repositories.
- Make installation and test instructions reproducible on a clean environment.
- Track known limitations, dependencies, licences, and security issues.
- Maintain a clear status label for each capability: implemented, tested, simulated, field-tested, or planned.
- Keep the public portfolio and project READMEs consistent with actual repository evidence.

### Exit evidence
- Reproducible test commands and recorded results.
- No unsupported claims of physical capability, certification, or customer deployment.
- A documented issue list with priorities and owners.

## Stage 2 — Prove one flagship workflow

**Initial focus: Coconut Harvest AI.**

- Audit image rights and record dataset sources and licences.
- Review annotation definitions and sample quality.
- Split data by tree, orchard, or capture session where possible to reduce leakage.
- Establish a fixed evaluation set and baseline.
- Report sample counts, precision, recall, false positives, missed detections, and failure examples where the selected task and labels support those metrics.
- Record code version, configuration, commands, and limitations.
- Keep the prototype disconnected from physical cutting commands.

### Exit evidence
A third party can reproduce the benchmark and understand exactly what it does—and does not—show. Do not set a performance target until the dataset and task definition justify it; never invent results to make the project look stronger.

## Stage 3 — Validate a real customer problem

Before building expensive hardware or a large feature set:

- Identify a specific user and purchasing decision-maker.
- Conduct problem interviews without presenting assumptions as established demand.
- Document the current workflow, costs, pain points, safety requirements, and alternatives.
- Test whether the proposed product would improve a measurable outcome.
- Record objections and evidence that would disprove the product hypothesis.

### Exit evidence
A documented problem statement, defined user group, competing alternatives, and a small set of measurable pilot success criteria.

## Stage 4 — Run a controlled pilot

Only after the software evidence and problem validation justify it:

- Define the pilot scope, operating environment, data handling, human responsibilities, and stop conditions.
- Agree success metrics with the pilot partner before testing.
- Start in simulation or offline decision-support mode where appropriate.
- Use independent safety review and suitable safeguards before any physical robot operation.
- Record failures, downtime, intervention rate, and the cost of operating the workflow.
- Do not claim a successful outcome unless it was directly measured.

### Exit evidence
A written pilot report with methodology, measured outcomes, limitations, and customer feedback.

## Stage 5 — Build a repeatable business

After a pilot demonstrates useful value:

- Choose a sustainable delivery model: software, support, integration, licensing, or a suitable combination.
- Estimate the full cost to deliver and maintain each deployment.
- Review intellectual property, third-party licences, privacy, liability, and applicable regulatory requirements with qualified advisers when needed.
- Establish support, versioning, security updates, documentation, and customer onboarding.
- Seek partnerships or funding only when the evidence and business need justify them.

### Exit evidence
A credible cost model, a clear offer, a repeatable deployment process, and evidence of customer willingness to pay—not valuation claims based only on a concept or repository.

## Portfolio roles

- **Coconut Harvest AI:** initial flagship candidate; focus on reproducible perception evaluation and staged robotics feasibility.
- **Flood Rescue AI:** simulation-first reconnaissance and hazard mapping; prioritise failure handling, safe stopping, and realistic scenario tests.
- **Multimodal Narcotics Screening AI:** human-reviewed decision support; prioritise uncertainty handling, sensor-health checks, and abstention when evidence is insufficient.

These roles are provisional priorities, not a conclusion that any project is already commercially validated. Reassess them when technical and customer evidence changes.

## Monthly review

Review these questions at least monthly:

- What changed in the code, and what tests passed?
- What new benchmark or validation evidence was produced?
- Which failures remain unresolved?
- What did potential users actually say or do?
- What costs, licence obligations, or safety risks were identified?
- What is the single highest-value next task?

## Definition of progress

Progress is not the number of features, lines of code, images, or ambitious claims. Progress means lower technical uncertainty, stronger reproducibility, clearer customer value, safer operation, and credible evidence that the product can be delivered sustainably.
