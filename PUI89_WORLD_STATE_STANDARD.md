# PUI89 World-State Observation Standard

**Status:** implemented as a dependency-free prototype and JSON schema; project-specific integration is a separate step.

## Purpose
Give Coconut Harvest AI, Extreme Flood Rescue AI and Multimodal Narcotics Screening AI a common way to represent timestamped observations without erasing source provenance, uncertainty, missing data or disagreement.

## Observation contract
Each record identifies an observation, entity, attribute, value, timezone-aware timestamp, source, modality, evidence kind and quality. Optional confidence is a bounded caller-supplied value, not a calibrated probability. Optional limitations explain known gaps.

See [the JSON Schema](schemas/pui89-world-state-observation.schema.json) and [the Python validator/summariser](tools/pui89_world_state.py).

## Deterministic state handling
- Conflicting distinct values remain visible and produce `REQUEST_HUMAN_REVIEW`.
- Stale or future-dated observations produce `SAFE_HOLD`.
- Invalid records are listed as rejected with reasons.
- No value is averaged, voted on or silently selected.
- No physical action is permitted.

The freshness limit and current timestamp are supplied by the caller. This tool does not infer sensor health, perform perception, estimate calibrated uncertainty or establish simulator/field validity.

## Example
```json
{
  "observation_id": "obs-001",
  "entity_id": "palm-row-3",
  "attribute": "maturity_stage",
  "value": "mature_green",
  "observed_at": "2026-10-31T10:00:00Z",
  "source_id": "image-session-12",
  "modality": "rgb",
  "evidence_kind": "observed",
  "quality": "valid",
  "limitations": ["Visual label requires annotation review"]
}
```

## Local test
```bash
PYTHONPATH=tools python -m unittest discover -s tests -p "test_pui89_world_state.py" -v
```

## Integration sequence
1. Keep the common record format stable.
2. Add thin project adapters that map existing observations to this schema.
3. Test source IDs, timestamps, stale inputs, missing modalities and conflicts.
4. Connect outputs to the shared policy orchestrator only after adapter tests pass.
5. Keep outputs advisory/simulation-only until separate project safety validation is completed.
