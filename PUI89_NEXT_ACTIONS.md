# PUI89 Engineering Roadmap

Updated: 2026-10-30

## Shared engineering foundation

- [x] Lightweight CI and project-specific test workflows exist across all three repositories.
- [x] Shared-interface smoke checks and machine-readable simulation artifacts exist.
- [x] Fault-injection and human-approval scenario coverage has been expanded.
- [x] Pre-commit configuration exists in all three project repositories.
- [ ] Run the new local cross-project runner on a workspace containing all three cloned repositories.
- [ ] Review generated JSON/CSV reports and resolve any failures or missing checks.
- [ ] Consider extracting truly common interfaces into a versioned shared package only after duplication and compatibility have been measured.

## Project work

### Coconut Harvest AI
- [ ] Obtain the original candidate image file and verify its SHA-256 from the actual bytes.
- [ ] Review all draft bounding boxes and record human QA decisions.
- [ ] Verify source licence, attribution, provenance and dataset split integrity.
- [ ] Only then run a held-out detector benchmark and report measured metrics.

### Extreme Flood Rescue AI
- [ ] Extend simulation scenarios for sensor dropouts, stale telemetry and communication loss/recovery.
- [ ] Verify safe-hold and controlled-resume rules in software tests.
- [ ] Add simulator telemetry only when a real configured simulator emits it.

### All-Terrain Inspection Robot Dog — PUI89 Sentinel
- [ ] Define the first narrow industrial inspection mission and measurable operating envelope.
- [ ] Complete quadruped system requirements and a product-specific hazard analysis.
- [ ] Compare leg, actuator, joint, foot, power and compute candidates with verified origin and compatibility evidence.
- [ ] Define RGB, depth, LiDAR, IMU and joint/foot-state interfaces and calibration requirements.
- [ ] Establish repeatable gait, terrain, obstacle, slip, fall and communications-fault simulation scenarios.
- [ ] Keep all physical mobility and inspection claims unvalidated until controlled tests produce evidence.

## Later, gated upgrades

- [ ] Evaluate optional local VLM/VLA models only after checking licence, disk, RAM, VRAM and download size.
- [ ] Add ROS 2/Gazebo only when a concrete simulation requirement justifies the extra setup.
- [ ] Add physical sensor or actuator monitoring only with suitable equipment and a safe test plan.

## Guardrails

- No invented metrics, test results, data provenance, or physical capability claims.
- No paid APIs, subscriptions, or cloud GPU dependencies in the default workflow.
- A skipped check is not a passing check.
- All material changes go through reviewable pull requests and existing CI.
