# HOMEGUARD AI Safety Case — Initial

**Status: PROPOSED. Not a certification or completed hazard analysis.**

## Intended use

Monitor and summarize building-condition observations to help a responsible person decide what needs verification.

## Out of scope

- Replacing certified fire, smoke, carbon-monoxide or electrical protection.
- Declaring a building structurally safe or unsafe.
- Diagnosing the exact cause of a smell, sound, crack or temperature anomaly from one sensor.
- Operating breakers, wiring, valves, lifts, doors, fire systems or evacuation controls.
- Making tenant, insurance, law-enforcement or access decisions about individuals.

## Hazard controls

| Hazard | Required control |
|---|---|
| Missed fire/CO/electrical emergency | Certified independent alarms and protective devices remain primary; software cannot delay emergency response |
| False alarm | Show evidence, uncertainty, thresholds and human verification steps |
| Missing or stale data | Explicit data-gap and sensor-health status; never imply normality |
| Bad calibration or mounting | Exclude or downgrade data and record calibration provenance |
| Incorrect causal inference | Use “possible” or “consistent with”; show alternative explanations |
| Privacy intrusion | Data minimization, local processing where feasible, access control and retention limits |
| Unsafe actuation | No actuator interface in the initial product; later actuation requires separate safety engineering and approval |
| Cyber compromise | Dependency pinning, secret scanning, least privilege, signed releases where practical and threat modelling |

## Escalation

A credible emergency indication should direct users to established local emergency procedures and qualified services. HOMEGUARD must never require a user to wait for additional AI analysis before acting on a certified alarm or obvious emergency.

## Release gates

1. Requirements and hazard review completed.
2. Input validation and failure-mode tests pass.
3. Report limitations are visible.
4. Security and privacy review completed.
5. Domain expert approves any pilot-specific thresholds.
6. No safety-critical action is automated.
