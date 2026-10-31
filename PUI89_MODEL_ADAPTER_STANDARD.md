# PUI89 Model Adapter Standard

**Status:** mock-only adapter implemented; local model inference is not enabled.

## Purpose

A controlled envelope for future model integrations to submit observations to the shared PUI89 evidence and policy pipeline. The first implementation is a deterministic, standard-library-only mock. It proves the software boundary, not model capability.

## Current implementation

- The mock adapter validates project identity, request metadata, timezone-aware timestamps, evidence provenance and synthetic-fixture labels.
- It passes a mock agent message through the existing evidence validator and adaptive policy simulator.
- It rejects malformed requests, missing provenance, non-synthetic evidence in mock mode and hardware-command fields.
- It returns observations only; proposed_actions is always empty.
- It marks the response MOCK_OBSERVATION_ONLY, records that inference was not performed and keeps physical actuation disabled.
- Eight regression tests cover valid requests, missing provenance, non-synthetic evidence, stale/future evidence, unknown projects, hardware-command rejection and invalid timestamps.

## Project boundaries

| Project | Future model-output boundary |
|---|---|
| Coconut Harvest AI | Describe candidate visible maturity cues for comparison with labelled evidence. Do not claim harvest readiness or command cutting/capture. |
| Extreme Flood Rescue AI | Describe candidate hazards for operator review and simulation. Any VLA output remains a simulated proposal. |
| Multimodal Narcotics Screening AI | Organise visible context for human review only. Do not infer chemical identity, guilt or enforcement action from VLM output. |

## Request envelope

A mock request contains a registered project_id, unique request_id, timezone-aware ISO-8601 timestamp, task description, non-empty provenance list explicitly marked synthetic, and non-empty mock_observations fixture list. The adapter does not fetch images or files.

## Response guarantees

- Adapter mode is MOCK; inference_performed is false.
- No model ID or revision is asserted.
- No action is emitted in proposed_actions.
- Policy results retain simulation_only true and physical_actuation_permitted false.
- Invalid or unsafe input is rejected with a SAFE_HOLD policy result.
- Policy CONTINUE means only that a synthetic software-contract snapshot passed checks. It is not permission to operate a robot.

## Run locally

    PYTHONPATH=tools python -m unittest discover -s tests -p "test_pui89_model_adapter.py" -v

No third-party package, model weight, network access, GPU or paid service is required.

## Future local inference gate

1. Review exact upstream model card, licence text, revision and gated-access terms.
2. Inspect dependencies and supply-chain risks.
3. Verify model size, disk, RAM and VRAM requirements against the actual target machine.
4. Obtain explicit approval before any optional download or package installation.
5. Isolate offline inference behind this envelope and emit provenance, uncertainty and abstention metadata.
6. Evaluate synthetic tests, then rights-reviewed held-out project data.
7. Retain each project's domain-specific human-review and no-actuation boundary.

**Not established:** real model inference, model accuracy, calibrated confidence, sensor truth, domain performance, simulator fidelity, physical safety or field readiness.
