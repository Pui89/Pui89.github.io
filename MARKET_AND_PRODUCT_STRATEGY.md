# PUI89 AI Robotics — Market and Product Strategy

**Purpose:** Turn the current technical portfolio into a credible path toward a useful, valuable business. This is a working strategy and set of hypotheses—not evidence of existing customers, revenue, market share, incorporation, or validated product performance.

## Executive decision

**Build one narrow, measurable offer before trying to sell three robotics concepts.**

The first commercial hypothesis to test is a **coconut orchard assessment and harvest-planning workflow**, initially delivered as software-assisted analysis rather than an autonomous cutting robot.

A practical first version could help a farm operator or service provider review orchard images, record visible coconut bunches, flag uncertain cases for human review, and produce a structured inspection report. Only include functions that are actually implemented and validated. If image detection is not yet reliable, start with a human-reviewed data-collection and reporting workflow and treat automated detection as experimental.

Why this is the first hypothesis:
- It is closest to the founder's agriculture background and the existing Coconut Harvest AI project.
- An offline or human-reviewed workflow can be tested before purchasing robot hardware.
- It creates a measurable question: can the workflow save enough inspection time, improve record consistency, or support a better harvest plan to justify its cost?
- It avoids making physical cutting, robot safety, and full autonomous operation prerequisites for the first customer conversation.

This is a hypothesis to validate, not a claim that demand or willingness to pay has already been established.

## 1. Choose a specific first customer

Interview people in these groups before choosing a final buyer:

1. Coconut farm owners or managers who regularly inspect trees and plan harvests.
2. Agricultural service providers or cooperatives that coordinate work across multiple farms.
3. Agricultural equipment dealers or integrators who may eventually need a perception component.

Ask who owns the problem, who performs the current work, who approves purchases, and who pays. Do not assume the person using a tool is the person buying it.

### Customer discovery questions

Ask about the last real occasion, not a hypothetical future:
- How do you currently inspect trees and estimate which bunches are ready?
- How much time does the process take per tree, block, or visit?
- How are records stored, and what gets missed or repeated?
- What happens when an estimate is wrong?
- Which decisions depend on the information, and what does a mistake cost?
- What tools or services have you already tried? Why did they work or fail?
- Who would approve a small trial, and what evidence would they need?
- What measurable result would make a trial worth continuing?

Record answers, date, customer role, current workaround, quantified pain if they can provide it, objections, and next step. Keep private information out of public notes unless permission is explicit.

## 2. Offer a low-risk first service

### Candidate offer: Orchard Inspection Report

**Potential input:** Images collected by the farm or a field operator, with agreed permissions and basic context such as orchard block and capture date.

**Potential output:** A reviewable report containing image references, candidate bunch observations where supported, uncertain cases, manual corrections, and a concise summary. Any automated count or maturity classification must be clearly labelled experimental until separately validated.

**Human role:** A person reviews uncertain observations and approves the final record. The system must not issue physical cutting commands.

**First delivery mode:** A small, controlled, offline workflow or assisted analysis service. Use sample data only when the licence and consent allow it. Do not upload a customer's images to a third-party service without explicit permission and an appropriate data-handling review.

**Do not promise yet:** yield prediction, maturity accuracy, labour savings, ROI, orchard-wide robustness, autonomous harvesting, or safe physical operation. These require evidence under defined conditions.

## 3. Prove value with a small pilot

Agree the protocol with a prospective pilot partner before collecting results. Start with a manageable, representative sample and record the conditions.

Measure:
- Time required for the current inspection method versus the assisted workflow.
- Human-reviewed count agreement on a defined sample, if counting is in scope.
- Missed observations and false detections, with examples.
- Fraction of cases requiring human correction or escalation.
- Time to prepare the final report.
- Failure cases under occlusion, lighting variation, distance, and image quality.
- Data collection, review, setup, and support time required to deliver the service.

Report sample size, collection conditions, annotation procedure, model/configuration version, and limitations. Use a held-out evaluation set and avoid splitting near-duplicate frames from the same capture session across training and evaluation. Do not publish a percentage or savings claim until it has actually been measured.

### Pilot success gate

Continue only if the results answer a real customer problem and the partner agrees the outcome is useful. A pilot is not automatically a success because the software runs. Record negative results and revise or stop the hypothesis when the evidence is weak.

## 4. Commercial model to test—not assume

Test these options through customer conversations:
- **Paid assessment service:** a defined inspection/reporting task with transparent scope.
- **Per-site or per-season workflow:** only if repeat usage and the buyer's budget support it.
- **Integration/licensing:** later, if an equipment or software partner needs a validated component.
- **Robotics integration:** later still, after perception, control interfaces, and independent safety requirements have been validated.

Do not set a price from guesswork alone. First estimate the full delivery cost: data preparation, human review, travel, support, compute, maintenance, insurance or compliance where applicable, and founder time. Ask prospective buyers how they budget for the current process and what comparable alternatives cost. A high-value product solves a costly, frequent, important problem—not merely a technically impressive one.

## 5. A 90-day evidence plan

### Days 1–15: Understand the workflow
- Prepare a one-page explanation and a short interview script.
- Speak with several relevant users across more than one role or operation where feasible.
- Document the current workflow, pain points, buyer, alternatives, and reasons not to buy.
- Do not treat polite interest or social-media likes as demand validation.

### Days 16–30: Narrow the use case
- Select one workflow based on the strongest repeated evidence.
- Specify inputs, outputs, human review, data permissions, and failure handling.
- Audit dataset sources, licences, labels, and train/validation/test separation.
- Publish a clear known-limitations list.

### Days 31–60: Build the smallest credible demonstration
- Implement only the minimum needed for the chosen workflow.
- Add reproducible tests and a fixed evaluation protocol.
- Compare with a transparent baseline or current manual workflow.
- Save a small set of representative successes and failures with permission.
- Keep costs at $0 unless the owner explicitly approves a documented expense.

### Days 61–90: Seek a controlled pilot
- Share the demonstration and proposed measurement plan with a suitable partner.
- Agree scope, permissions, responsibilities, success measures, and stop conditions in writing.
- Run a pilot only when a partner, suitable data, and the required safeguards are available.
- Publish a short evidence report; if no pilot is available, document what was learned and continue discovery rather than inventing results.

This is a prioritisation plan, not a promise that customer access or a pilot will be secured within 90 days.

## 6. How the three projects fit together

- **Coconut Harvest AI — flagship candidate:** focus first on a measurable agriculture workflow and reproducible perception evidence.
- **Flood Rescue AI — research and partnership track:** continue simulation-first hazard mapping and failure testing. Real emergency deployments require specialist partners, realistic validation, and safety review.
- **Multimodal Screening AI — limited research track:** keep human review, uncertainty, data governance, and abstention central. Do not market it as chemical identification or autonomous enforcement.

Do not split scarce time across three commercial launches. Reuse software and documentation where useful, but make one project the primary route to customer evidence.

## 7. Trust is part of the product

Before any customer deployment:
- Clarify dataset, model, and dependency licences and permitted commercial use.
- Agree data ownership, retention, access, deletion, and confidentiality.
- Document security, failure modes, and human responsibilities.
- Keep software output separate from physical actuation until a suitable engineering and safety process exists.
- Review applicable Thai law, privacy obligations, product liability, and any sector-specific requirements with qualified advisers before making consequential claims or deployments.
- Keep the company identity truthful: PUI89 AI Robotics is currently an independent project identity unless and until legal incorporation is completed.

## 8. Weekly founder dashboard

Track facts rather than vanity metrics:

| Area | Weekly evidence |
|---|---|
| Customer discovery | Conversations completed; recurring problems; buyer identified; objections |
| Product | Workflow completed; bugs fixed; test results; known limitations |
| Evaluation | Dataset/version; sample count; baseline; measured errors; failure cases |
| Delivery | Time to prepare data, review results, and produce an output |
| Commercial | Pilot invitations, explicit next steps, and any documented willingness to pay |
| Risk and cost | Spend (target $0 by default); data/licence issues; safety blockers |

**Weekly decision:** What is the single action most likely to reduce the biggest uncertainty—customer need, technical performance, safe delivery, or willingness to pay?

## The principle for building a high-value company

Do not try to look like a large robotics company before proving one valuable job. Build a narrow workflow, measure it honestly, make it dependable, learn who pays for the result, and expand only when evidence justifies the next step.


## Zero-spend operating rule

**Budget for planned digital development: ฿0 in additional spending.** Use existing equipment, free tiers only when they require no payment method or create no billable exposure, free/open-source software, public documentation, and local tests wherever practical.

- Do not buy hardware, datasets, domains, certificates, subscriptions, credits, or paid support without the project owner's explicit approval.
- Do not enable paid APIs, cloud compute, hosted inference, storage upgrades, or services that can generate usage charges.
- Before using any free service, check quotas, renewal terms, payment-method requirements, and whether overages can be charged. If unclear, choose a local or no-cost alternative.
- Prefer local CPU/GPU execution on existing equipment and GitHub-hosted features within the existing no-additional-spend limits. Never assume a quota or free tier is unlimited or permanent.
- Record any unavoidable cost before a proposed action and stop for approval; never incur it on the owner's behalf.
- Keep customer discovery remote and no-cost where possible; do not promise a free customer pilot that would require travel, equipment, support, or other unbudgeted work.
- Legal registration, tax/accounting advice, insurance, certification, travel, and physical robot fabrication may carry unavoidable costs. They are not authorized by this strategy and must be researched and approved separately before proceeding.

**Hard rule: if an action may create a charge or financial commitment, do not proceed until the owner explicitly approves it.**
