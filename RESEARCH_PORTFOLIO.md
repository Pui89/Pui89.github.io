# PUI89 AI Robotics — Research Portfolio

This page summarises the research direction behind the public projects. It distinguishes implemented software from planned work and does not claim results that have not been measured.

## Research approach

The common theme is **practice-oriented AI for consequential real-world workflows**: define a useful task, build a testable software component, evaluate it on appropriate data, document uncertainty and failure modes, and keep human oversight and safety requirements explicit.

The repositories are the authoritative source for implementation details, dependencies, tests, and current limitations.

## 1. Coconut Harvest AI

**Application area:** agricultural perception and robot-workflow research.

**Research questions**
- How reliably can a vision system detect target coconuts across changes in lighting, scale, viewpoint, clutter, and partial occlusion?
- Which evaluation protocol makes errors and limitations visible, rather than relying on selected demo images?
- What additional sensing, calibration, reachability checks, and independent safeguards would be required before any physical harvesting workflow could be considered?

**Evidence plan**
- Document dataset provenance, licences, annotation definitions, and split strategy.
- Validate dataset structure and label syntax before training or evaluation.
- Establish a fixed held-out evaluation set and compare a documented baseline.
- Report sample counts, precision/recall or other task-appropriate metrics, latency, and representative failure cases only when actually measured.
- Keep perception experiments separate from physical cutting or actuation.

**Current boundary:** a software/prototype research effort. Dataset validation is not proof of annotation correctness, model accuracy, orchard robustness, or physical-robot safety.

Repository: [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI)

## 2. Flood Rescue AI

**Application area:** simulation-first reconnaissance and hazard-mapping support.

**Research questions**
- How should a robotic reconnaissance workflow represent uncertain observations and communicate them to a human operator?
- How can simulation tests exercise navigation failures, sensor limitations, and degraded communication before field trials?
- Which safeguards should prevent an uncertain perception result from being treated as a confirmed hazard or rescue decision?

**Evidence plan**
- Start with reproducible simulation scenarios and explicit assumptions.
- Measure task completion, coverage, latency, and failure behavior only where the implementation supports those measurements.
- Keep simulated results clearly labelled and separate from field validation.

**Current boundary:** research/prototype direction; real-world rescue performance is not established by simulation or concept material.

Repository: [Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI)

## 3. Multimodal Narcotics Screening AI

**Application area:** human-reviewed multimodal inspection and screening support.

**Research questions**
- How should evidence from different modalities be presented when signals disagree or are incomplete?
- How can uncertainty, missing inputs, and out-of-distribution cases trigger abstention or escalation to qualified review?
- How can evaluation avoid implying that a screening model establishes chemical identity or justifies enforcement action?

**Evidence plan**
- Define the intended use and limitations of each input modality.
- Test failure handling, missing-input behavior, and human-review pathways.
- Report task-specific metrics only against an appropriately sourced and licensed evaluation set.

**Current boundary:** a screening-workflow prototype, not a validated chemical-identification system or autonomous enforcement tool.

Repository: [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI)

## Cross-project standards

- **Reproducibility:** record code version, environment, configuration, dataset version, and exact evaluation protocol.
- **Honest evidence:** distinguish code implementation, automated tests, simulation, measured benchmarks, and real-world validation.
- **Responsible data use:** document provenance, permissions, licences, privacy, and any access restrictions.
- **Safety and oversight:** communicate uncertainty; keep consequential actions under appropriate human oversight and independent safeguards.
- **Free-first development:** default to local and free/open-source options. Do not introduce paid services or commitments without explicit approval.

## Status language

Use these labels precisely:
- **Implemented:** code or a workflow exists in the repository.
- **Tested:** a named test has run and its result is recorded.
- **Benchmarked:** performance was measured using a documented protocol and stated data.
- **Simulated:** tested in a specified simulation environment.
- **Field-validated:** evaluated under described real-world conditions.
- **Planned:** not yet implemented or verified.

A project card, illustration, passing unit test, or dataset-format check alone does not establish model accuracy or real-world readiness.
