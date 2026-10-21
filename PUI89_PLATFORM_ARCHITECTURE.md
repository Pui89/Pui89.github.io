# PUI89 AI Robotics — Shared Platform Architecture

**Purpose:** Define a practical, reusable architecture for PUI89's agriculture, field-robotics, rescue, and inspection projects. This is an engineering plan, not a claim that all modules are implemented or integrated.

## Product strategy

Build one reliable flagship workflow first—Coconut Orchard Intelligence—then extract proven reusable components. Avoid maintaining several disconnected demos that each reinvent data review, evaluation, logging, and safety checks.

## Reference architecture

```text
Real-world sensors / uploaded media
        |
        v
Input adapters and data provenance
(camera, RGB-D, LiDAR, thermal when available)
        |
        v
Perception interface
(detection, segmentation, tracking, uncertainty)
        |
        v
World / scene representation
(objects, coordinates, timestamps, confidence)
        |
        v
Task and route planning
(goal, constraints, reachable targets, fallback)
        |
        v
Safety supervisor and human approval
(independent limits, stop conditions, audit log)
        |
        v
Robot adapter or offline report
(simulation first; hardware only after validation)

Cross-cutting services:
dataset rights + annotation QA | reproducible evaluation | experiment records
configuration/versioning | failure reporting | privacy/licence controls
```

## Shared modules and acceptance criteria

| Module | Responsibility | Minimum evidence before reuse |
|---|---|---|
| Data and provenance | Record source, permission, file hash, capture group and review status | Missing or unapproved records fail closed |
| Perception adapter | Standardize image input and detections/segments/tracks | Unit tests, input validation, model/version metadata |
| Evaluation harness | Compare predictions to reviewed ground truth | Fixed thresholds, reproducible input files, failure cases |
| Scene representation | Store object identity, position frame, confidence and timestamp | Explicit coordinate frame and missing-depth behavior |
| Planner interface | Convert reviewed targets into candidate tasks | Constraint tests, no direct actuator command from untrusted model output |
| Safety supervisor | Reject unsafe or uncertain actions; support stop/fallback | Hazard analysis and tests; physical safety needs separate validation |
| Robot adapter | Connect planning to ROS 2 simulation or hardware interface | Simulation tests first; hardware interlocks and supervised trials before deployment |
| Operator interface | Show evidence, uncertainty, warnings and exportable reports | Human-readable failure states; no fabricated model outputs |
| Release evidence | Record code commit, data version, config, dependencies and results | Reproducible run instructions and honest status label |

## Product mapping

### 1. Coconut Orchard Intelligence — flagship first

**Current foundation:** local demo, offline annotation utility, dataset/annotation audit scripts, detector evaluation tools and an initial failed HSV-contour baseline documented in the Coconut Harvest AI repository.

**Next milestones:**
1. Finish rights and independent annotation review for a useful sample.
2. Run the fail-closed dataset promotion gate and resolve every blocked candidate intentionally.
3. Create a group-separated dataset only when there are enough distinct source groups.
4. Run a real detector locally only after model licence, storage, memory and dependency requirements are checked.
5. Report held-out detection metrics and error examples.
6. Add 3D target localization only when valid camera calibration and depth data are available.
7. Connect target candidates to ROS 2/Gazebo arm-reachability and harvest-sequence simulation.
8. Consider physical hardware only after simulation, safety analysis, budget approval and a supervised test plan.

### 2. PUI89 Field Robotics Platform

Reuse the perception, scene, evaluation, logging and safety interfaces. Use ROS 2 and Nav2 for robot middleware/navigation and Gazebo for simulation where appropriate. Keep the first platform simulation-first and hardware-independent.

**Acceptance evidence:** repeatable navigation scenarios, success/failure counts, collisions, recovery behavior, localization errors and intervention counts. Simulation evidence must be labelled as simulation.

### 3. Crop Health and Phenotyping AI

Reuse data provenance, image review, detection/segmentation, experiment tracking and evaluation. Keep crop-specific labels and evaluation protocols separate; do not assume a coconut model generalizes to plant disease or mungbean phenotypes.

**Acceptance evidence:** expert-reviewed labels, separate crop/task test sets, class-wise metrics and documented domain limitations.

### 4. Flood Rescue AI

Reuse mapping, scene representation, route planning and safety-supervisor concepts. Evaluate only in controlled simulation until suitable field permissions and safety procedures exist.

**Acceptance evidence:** scenario-level mission completion, hazard-map quality, collisions, localization failures and human interventions. Never imply the current prototype can evacuate people.

### 5. Multimodal Inspection AI

Reuse input adapters, uncertainty display, audit logging and evaluation. Each modality and target requires a lawful task definition and appropriately verified ground truth. A visual appearance must not be presented as chemical identification.

**Acceptance evidence:** modality ablation, false-positive/false-negative analysis, calibration/uncertainty review and an explicit human-escalation path.

## Delivery sequence

### Phase A — trust and data quality (now)
- Keep public claims aligned with code and recorded evidence.
- Enforce rights/annotation approval before dataset promotion.
- Make local workflows and tests easy to run on Windows.
- Maintain a list of known failures and blocked capabilities.

### Phase B — credible perception result
- Build a rights-cleared, reviewed, group-separated coconut dataset.
- Run an actual detector and compare against a documented baseline.
- Record inference latency and hardware/software environment.
- Do not optimize on the final test set.

### Phase C — simulation integration
- Define a sensor-independent detection message and coordinate-frame contract.
- Integrate with ROS 2/Gazebo simulation and test target-to-task flow.
- Add collision constraints, timeouts, uncertainty thresholds and operator approval.

### Phase D — customer discovery and supervised pilot
- Interview orchard operators and agricultural researchers before selecting a commercial feature set.
- Test whether inspection, counting, mapping or harvesting assistance solves a measurable problem.
- Do not claim customer demand or pilot success until actual evidence exists.

### Phase E — productization
- Add installer/release process, versioned configurations, audit exports, privacy review, security updates, support and documented hardware requirements.
- Keep physical actuation disabled by default and require independent safety controls.

## Free-first constraints

Default additional spend is **฿0**. Use the current laptop, local data and free/open-source software first. Do not trigger paid cloud compute, APIs, dataset subscriptions, hardware purchases or other chargeable services without explicit approval. If the current machine cannot run a model, document the limitation and choose a smaller model or simulation workflow rather than silently moving to paid compute.

## Honest status vocabulary

- **Implemented:** code is present.
- **Automated-tested:** named tests passed for a specified commit.
- **Simulated:** tested in a simulation; not physical validation.
- **Measured:** a documented experiment generated the stated result.
- **Field-validated:** a controlled real-world protocol was completed and documented.
- **Planned:** not implemented yet.

A passing data gate does not prove a model is accurate. A passing simulation does not prove physical safety. A working prototype does not establish commercial demand.
