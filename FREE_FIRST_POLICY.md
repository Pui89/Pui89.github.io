# PUI89 AI Robotics — Free-First Engineering Policy

**Status:** Active project policy  
**Applies to:** PUI89 AI Robotics repositories, prototypes, demos, and development workflows  
**Default budget for new recurring or metered spend:** USD 0

## 1. Default decision rule

Prefer tools and workflows that can be used at no additional cost with the hardware and accounts already available. A tool is not considered suitable merely because it has a free trial: check renewal terms, usage limits, billing triggers, licence conditions, and export options first.

## 2. No-spend guardrails

Do not start or enable any of the following without explicit approval from the project owner:

- Paid APIs, model endpoints, subscriptions, or usage-based services.
- Cloud compute, hosted GPU instances, storage, bandwidth, or other metered infrastructure.
- Paid datasets, image licences, commercial model licences, or third-party data services.
- Hardware, sensors, robot components, or paid software purchases.
- Automatic workflows that may trigger any of the above.

Never store payment credentials, API keys, passwords, or other secrets in source code, issues, logs, screenshots, or public documentation.

## 3. Preferred workflow

1. Inspect existing code, local hardware, and available test results before adding dependencies.
2. Prefer local execution, lightweight CPU tests, and simulation-first development.
3. Use free/open-source packages where their licences and maintenance status are appropriate.
4. Pin or document dependencies when useful, and explain installation requirements.
5. Keep optional heavy dependencies separate from core checks wherever practical.
6. Make tests deterministic and small enough to run locally without paid infrastructure.
7. Record what was actually run, the environment, results, limitations, and any failures.

## 4. Open source is not the same as unrestricted

Before using an image, dataset, pretrained model, dependency, or external asset, review its licence and usage conditions. Check attribution, redistribution, commercial-use, privacy, and model-specific restrictions where relevant. Do not assume that publicly accessible data can automatically be reused for training.

## 5. Evidence and honesty

- A passing software test proves only the tested behavior; it does not prove real-world AI accuracy or robot safety.
- Synthetic examples must be labelled as synthetic.
- A benchmark must identify its inputs, hardware/software environment, metric definitions, and limitations.
- Failed experiments should remain documented when they materially affect project conclusions.
- Do not claim field deployment, customer adoption, safety certification, or performance that has not been independently demonstrated.

## 6. Approval checklist for any proposed cost

Before asking for approval, document:
- Why the paid option is necessary and what free alternatives were checked.
- Maximum one-off and recurring cost, billing unit, and cancellation method.
- Usage caps or spending limits available.
- What measurable project outcome the spend is expected to enable.
- Whether the project can proceed without it.

**No explicit approval means no purchase and no new paid service.**

## 7. Practical priorities

For Coconut Harvest AI, prioritise dataset rights and quality review, annotation checks, leakage-safe splits, reproducible local evaluation, and simulation before cloud training or hardware purchases.

For Flood Rescue AI, prefer local simulation and offline testing before physical robot hardware.

For Multimodal Screening AI, prefer local-first, human-reviewed workflows and avoid paid hosted inference unless separately approved.

---

This policy is a practical project rule, not a guarantee that every third-party service or dependency will remain free. Re-check terms before adopting or upgrading tools.
