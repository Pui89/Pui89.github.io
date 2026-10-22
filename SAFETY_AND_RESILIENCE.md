# PUI89 AI Robotics — Safety, Security & Resilience

## Purpose and status

This document defines cross-project requirements for the Coconut Harvest AI, Flood Rescue AI, and Multimodal Narcotics Screening AI projects. It is a development standard, not a certification or a claim that every control is already implemented. Each repository must identify what is implemented, tested, in progress, and planned.

## Shared safety requirements

- **Safe states:** Define the safe state for each operating mode. On a critical fault, inhibit hazardous actions and stop or hold motion when that is the safer response.
- **Fault detection:** Check sensor freshness/validity, software health, power, temperature, actuator feedback, communication status, and watchdogs where the hardware supports them.
- **Human control:** Provide clear fault/status reporting, an emergency stop for physical systems, manual recovery instructions, and deliberate restart checks.
- **No unsafe continuation:** A system must not continue a hazardous task merely because a sensor, model, network, or controller has failed.
- **Recovery:** Preserve useful diagnostic logs, isolate the fault, restore from trusted software/configuration backups, and verify the system before returning to operation.

## Cybersecurity and malicious interference

Threats to consider include unauthorized access, stolen credentials, malicious or compromised dependencies, malware/ransomware, poisoned or altered input data, denial of service, network loss, tampering with configuration, and unauthorized firmware/software changes.

Required development practices:
1. Apply least privilege and separate operator, developer, and service permissions.
2. Do not hard-code passwords, tokens, or private keys; keep secrets out of source control and logs.
3. Validate inputs and treat downloaded models, images, documents, datasets, and other external files as untrusted until checked.
4. Pin and review dependencies where practical; use available free security checks and update vulnerable components deliberately.
5. Keep backups of code, configuration, labels, and important evidence; test restoration rather than assuming backups work.
6. Record significant faults and security-relevant events without exposing credentials or unnecessary personal data.
7. Define a response for suspected compromise: stop risky functions, disconnect affected components when safe, preserve logs, notify the responsible operator, restore from trusted sources, and retest.
8. Do not claim complete protection against hackers, malware, theft, or physical attacks. Test against stated threat scenarios and document remaining risk.

## Physical, electrical, and environmental hazards

Consider loss or fluctuation of power, battery overheating, electrical shorts, damaged cables, actuator jams, mechanical wear, falling objects, water ingress, fire, collision, unstable terrain, blocked sensors, impact, theft, and deliberate tampering.

Before any hardware trial:
- Identify hazards and define who may be exposed.
- Use appropriate electrical protection, fusing, battery handling, enclosure, strain relief, and environmental protection for the actual design.
- Ensure hazardous tools/actuators default to disabled during startup, fault, reboot, and communication loss.
- Provide an accessible emergency stop and a safe way to isolate power.
- Test emergency stop, watchdog, sensor-loss, communication-loss, and restart behavior without exposing people to the hazard.
- Require a human inspection and explicit reset before resuming after a critical fault.
- Do not test physical attack scenarios involving weapons or real threats; use safe simulations, dummy signals, and controlled bench tests.

## Project-specific requirements

### Coconut Harvest AI
- A perception/model failure, uncertain target, stale sensor data, communication loss, unexpected motion, or actuator fault must inhibit cutting and harvesting actions.
- Keep people clear of the arm, cutter, falling fruit, and moving platform.
- Do not rely on AI alone for stability, reach, collision avoidance, or confirmation that a harvest is safe.
- Treat tree height, payload, reach, cutting reliability, and capture success as unverified until measured under the intended conditions.

### Flood Rescue AI
- Loss of localization, depth sensing, communications, power margin, or obstacle detection must trigger the defined safe behavior for the platform and environment.
- Do not send a robot, boat, or drone into a hazardous area based only on an uncertain model prediction.
- Keep a human responsible for rescue decisions; avoid actions that could endanger survivors or responders.
- Test water, terrain, GPS-denied, sensor-loss, and link-loss scenarios in simulation before any controlled physical trial.

### Multimodal Narcotics Screening AI
- Treat model outputs as uncertain screening hypotheses, not proof of chemical identity or guilt.
- Require authorized human review and independent confirmatory procedures where appropriate.
- Protect chain of custody, source metadata, file hashes, access logs, privacy, and evidence integrity.
- Reject or quarantine corrupted, malformed, or suspicious files; do not execute content embedded in submitted evidence.
- Never automate enforcement or consequential decisions from the model score alone.

## Verification gates

For each safeguard, record: requirement ID, hazard/threat, implementation status, test procedure, expected result, observed result, evidence link, date, and reviewer. At minimum, verify:
- model/process crash;
- camera or sensor unavailable, stale, obstructed, or inconsistent;
- network or remote-control loss;
- low battery, power interruption, and reboot;
- actuator/controller fault;
- corrupted or unexpected input;
- unauthorized access attempt and configuration change;
- backup restoration and post-incident recovery;
- emergency stop and restart interlock on physical hardware.

Use simulation and safe bench tests first. Field tests require a separate risk assessment, permission, supervision, and suitable protective measures. A passing software test does not establish real-world safety.

## Reporting and maintenance

Report reproducible issues through the relevant repository's GitHub Issues page. Do not publish credentials, exploit instructions, private personal information, or sensitive operational details in a public issue. For a suspected active compromise, stop affected operations and contact the project maintainer through a trusted channel.

Review these requirements when hardware, models, dependencies, deployment environments, or intended uses change. Free/open-source tooling is preferred; do not add paid services, subscriptions, cloud compute, or purchases without explicit approval.
