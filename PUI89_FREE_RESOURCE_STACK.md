# PUI89 Free-First Resource and Technology Adoption Standard

**Status:** operational policy and read-only preflight tool  
**Scope:** Coconut Harvest AI, Extreme Flood Rescue AI, Multimodal Narcotics Screening AI and the shared PUI89 AI Core.

## Purpose

Adopt useful engineering tools without creating surprise bills, unnecessary downloads, unsafe automation or unsupported capability claims. "Free" means no paid service is required by the current workflow; it does not mean every third-party tool, model, dataset or runner is cost-free in every context.

## Adoption ladder

| Stage | Candidate capability | Entry condition | Evidence required before advancing |
|---|---|---|---|
| 1 | Python standard-library tests, JSON contracts, deterministic scenarios | Available now | Passing tests and reproducible reports |
| 2 | Local image tooling such as OpenCV or Pillow | A task needs it | Package licence, install size, Python compatibility and tests |
| 3 | ONNX Runtime / OpenVINO inference | A real model and benchmark task exist | Model licence, runtime licence, hardware fit, model hash and measured baseline |
| 4 | VLM experiments | A defined image-understanding gap exists | Model-card review, weight size, RAM/VRAM estimate, offline check and task-specific evaluation |
| 5 | ROS 2 / Gazebo / Nav2 simulation | A project has a minimal simulator scenario | Supported OS/version, installation footprint, reproducible launch and recorded scenario |
| 6 | VLA or hardware-connected action proposals | Earlier stages are stable | Mock-action tests, simulation evidence, hazard analysis, human authorisation and independent review |

No stage is automatically approved by the existence of a package or model.

## Resource preflight

Run from the root of the `Pui89.github.io` repository (where the tool currently lives):

```bash
python tools/pui89_resource_preflight.py
python tools/pui89_resource_preflight.py --output resource-report.json
```

The tool uses only Python's standard library. It reports Python/platform, CPU count, available system memory, free disk, and presence of selected optional packages. It does not access the network, install packages, download model weights, invoke paid services, inspect private credentials, test GPU/VRAM, or run inference.

The resource labels are conservative planning hints, not compatibility guarantees. Available memory and disk change over time. GPU/VRAM, driver compatibility, model licence and model suitability require separate checks.

## Non-negotiable cost and safety controls

- Do not add paid APIs, cloud GPU, subscriptions or metered services to the default workflow.
- Do not automatically install optional AI/robotics packages or download model weights in CI.
- Pin and review dependencies before adding them; prefer optional extras over mandatory base dependencies.
- Check the exact model and dataset licences and provenance; a permissive code licence does not grant rights to model weights or training data.
- Record model source, version, SHA-256, licence, file size and intended offline use before any model evaluation.
- Do not upload sensitive project or government data to external services without explicit authorisation.
- Keep VLA outputs as proposals; physical actuation remains disabled unless a separate, documented safety and authorisation process permits it.
- If a tool's cost, licence, provenance or resource requirement is unclear, defer adoption.

## Project-specific use

- **Coconut Harvest AI:** first prioritise dataset provenance, annotation quality, leakage-safe splits and a held-out detector baseline. Do not download a large VLM to compensate for an unreviewed dataset.
- **Extreme Flood Rescue AI:** first establish one repeatable simulation baseline and test stale/conflicting sensors, communication loss and conservative stopping. Treat the 15 m figure as a scenario target only.
- **Multimodal Narcotics Screening AI:** first validate sensor provenance, calibration and modality-specific evidence handling. Keep human review; image appearance alone cannot establish chemical identity.

## Verification

The accompanying GitHub Actions workflow runs only standard-library unit tests and creates a runner resource report. A GitHub-hosted runner report describes that temporary runner, not the user's laptop. Run the script locally for a local snapshot. A passing preflight test validates the reporting code, not model performance or robot readiness.
