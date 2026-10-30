# PUI89 Agent Message and Evidence Provenance Standard

**Status:** contract design and validator implementation are separate gates; project adapters are not yet integrated.

This standard defines a common auditable record for proposals from specialist software agents across Coconut Harvest AI, Extreme Flood Rescue AI and Multimodal Narcotics Screening AI.

## Agent message fields

- `agent_id`, `task_id`: stable identifiers.
- `timestamp`: ISO 8601 with an explicit timezone.
- `source_ids`: identifiers of the evidence records used.
- `observations`: structured observations kept separate from interpretations.
- `claims`: records containing `claim_id`, `claim_key`, `value` and `evidence_ids`.
- `confidence`: a number from 0 to 1 or null. Numeric confidence is uncalibrated unless independently demonstrated otherwise.
- `uncertainty`, `limitations`: explicit arrays.
- `status`: PROPOSED, NEEDS_EVIDENCE, SAFE_HOLD, HUMAN_REVIEW or STOPPED.
- `requested_action`: CONTINUE, REQUEST_EVIDENCE, VERIFY, SAFE_HOLD, REQUEST_HUMAN_REVIEW or STOP.

## Evidence provenance fields

Every evidence record identifies `source_id`, `source_type`, `source_ref`, timezone-aware `timestamp`, `evidence_kind`, `modality` and `lineage`. An optional SHA-256 digest identifies exact source bytes. Evidence kinds distinguish observed, inferred, synthetic, derived and unknown. Lineage records upstream evidence or transformation identifiers.

## Disagreement policy

Claims with the same `claim_key` and different values are flagged for review. The system retains the contributing agent and evidence references and leaves the resolution empty. It does not vote, average confidence, infer consensus or decide which claim is true.

## Application boundaries

- Coconut: maturity and geometry claims must link to source images or sensor records; occlusion and unverified reachability remain limitations.
- Flood Rescue: water-level, flow, localization and victim-detection claims retain sensor/time provenance; stale or conflicting measurements must not be silently merged.
- Narcotics Screening: RGB appearance is not chemical identification. Substance-related claims require validated sensor evidence, calibration and human review.

## Verification limits

Contract tests establish record-shape enforcement only. They do not validate agent reasoning, source authenticity, sensor calibration, evidence truth, model calibration, AI performance, simulator fidelity or physical safety. All initial checks use the Python standard library and do not invoke models, external APIs, cloud GPUs or hardware.
