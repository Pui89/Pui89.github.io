# PUI89 AI Robotics — Research Portfolio

This page summarises the research direction behind the public projects. It distinguishes implemented software from planned work and does not claim results that have not been measured.



> **Current portfolio boundary (17 November 2026):** PUI89 has exactly six active products. Shared AI Core is infrastructure, not a seventh product. Sentinel's current identity is All-Terrain Exploration & Inspection Robot. See [the authoritative six-product source of truth](PUI89_PORTFOLIO_SOURCE_OF_TRUTH_V1.0.md).

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

## 2. PUI89 Sentinel — All-Terrain Exploration & Inspection Robot

**Project name:** PUI89 Sentinel.  
**Application area:** four-legged quadruped robotics for supervised inspection of industrial facilities, infrastructure, warehouses, logistics yards, ports and selected outdoor environments.

**Research questions**
- Which quadruped leg, joint, actuator and foot architectures provide a practical balance of stability, payload, serviceability and cost?
- How should gait, foothold selection, localisation and body-state estimation respond to uneven terrain, obstacles, slip and sensor uncertainty?
- How can RGB, depth, LiDAR, IMU and joint/foot-contact observations be aligned with timestamps, calibration state, provenance and uncertainty?
- How should the robot propose inspection tasks while keeping motion bounded by independent safety controls and human approval?
- Which simulation scenarios and controlled tests are necessary before publishing terrain, mobility, endurance or inspection-performance claims?

**Evidence plan**
- Define the first inspection mission, operating envelope, no-go conditions and measurable acceptance criteria.
- Complete a hazard analysis covering emergency stop, people, terrain, stability, power, battery, thermal and communications failure.
- Compare candidate components using exact model numbers, manufacturer, manufacturing origin evidence, compatibility, supplier and dated quotations.
- Establish simulation and fault-injection scenarios before hardware procurement.
- Validate perception, mobility and safety separately; do not infer physical performance from software tests or simulation.

**Current boundary:** concept and engineering requirements only. No physical prototype, validated locomotion, integrated sensor suite or field performance is claimed.

Repository: [PUI89 Sentinel — All-Terrain Exploration & Inspection Robot — PUI89 Sentinel](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot)

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
