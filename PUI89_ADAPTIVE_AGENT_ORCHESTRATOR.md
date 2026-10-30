# PUI89 Adaptive Agent Orchestrator

## Purpose
A deterministic, standard-library policy simulator that routes validated PUI89 agent messages. It does not execute AI models, specialist agents, external tools, or robot actions.

## Decision order
1. `STOP` — a critical stop is latched.
2. `SAFE_HOLD` — message or evidence provenance is invalid, or a safety hold is requested.
3. `REQUEST_HUMAN_REVIEW` — an agent explicitly requires human judgement.
4. `REQUEST_EVIDENCE` — required evidence is absent, stale, future-dated, or no messages were supplied.
5. `REQUEST_SPECIALIST_VERIFICATION` — agents disagree on a claim key. No voting, averaging, or automatic resolution occurs.
6. `CONTINUE` — policy checks pass for the supplied simulation snapshot.

## Safety boundary
Every result has `simulation_only: true` and `physical_actuation_permitted: false`. `CONTINUE` is not permission to operate hardware.

## Limitations
Evidence presence and age do not prove truth, sensor quality, or calibration. Confidence is not interpreted as a calibrated probability. The evaluator does not measure model accuracy, real-world robustness, or physical safety.

## Run tests
```bash
PYTHONPATH=tools python -m unittest discover -s tests -p "test_pui89_adaptive_orchestrator.py" -v
```
