# PUI89 Mission Replay & Audit

**Status:** dependency-free prototype and automated test suite committed; integration with project mission runners remains pending.

## What it does
- Validates a common event record with mission ID, event ID, sequence, timezone-aware timestamp, event type, source and summary.
- Reconstructs a deterministic, sequence-ordered event timeline.
- Flags duplicate event IDs, invalid records, mixed mission IDs and missing sequence numbers.
- Counts task failures/faults and human-review requests.
- Reports a terminal state when a stop, safe-hold or completion event appears.

## Event types
Mission lifecycle, objectives, observations, state updates, proposed plans, task start/completion/failure, faults, safe hold, human review, pause/resume, stop, completion and notes are represented by explicit event types.

## Local test
```bash
PYTHONPATH=tools python -m unittest discover -s tests -p "test_pui89_mission_replay.py" -v
```

## Important limits
Replay reconstructs only the supplied log; it is not ground truth. The prototype does not cryptographically sign records or independently verify source identity/evidence references. Missing sequence numbers and rejected events may indicate incomplete history. It does not issue robot commands, control actuators, or authorise physical operation.

## Next integration steps
1. Add event emitters to each project's existing test/mission runner.
2. Link observation IDs to the shared world-state records and failure reports.
3. Preserve raw event logs as run artifacts, with explicit synthetic/real-data labels.
4. Test replay against known scenarios and intentionally corrupted logs.
5. Consider cryptographic integrity and access controls before using logs for operational assurance.
