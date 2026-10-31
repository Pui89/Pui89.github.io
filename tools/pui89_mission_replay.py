"""PUI89 deterministic mission event log validation and replay.

Standard-library only. This is an audit/replay utility, not a robot controller.
It never issues commands or authorises physical actuation.
"""
from __future__ import annotations
from datetime import datetime, timezone
from typing import Any, Iterable

EVENT_TYPES = {
    "MISSION_CREATED", "OBJECTIVE_SET", "OBSERVATION_RECEIVED", "STATE_UPDATED",
    "PLAN_PROPOSED", "PLAN_REVISED", "TASK_STARTED", "TASK_COMPLETED",
    "TASK_FAILED", "FAULT_DETECTED", "SAFE_HOLD", "HUMAN_REVIEW_REQUESTED",
    "HUMAN_REVIEW_RECORDED", "MISSION_PAUSED", "MISSION_RESUMED",
    "MISSION_STOPPED", "MISSION_COMPLETED", "NOTE"
}
SEVERITY = {"info", "warning", "error", "critical"}


def _timestamp(value: Any):
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed.astimezone(timezone.utc)


def validate_event(event: Any) -> list[str]:
    if not isinstance(event, dict):
        return ["event must be an object"]
    errors = []
    required = ("event_id", "mission_id", "sequence", "timestamp", "event_type", "source", "summary")
    for key in required:
        if key not in event:
            errors.append(f"missing required field: {key}")
    for key in ("event_id", "mission_id", "source", "summary"):
        if key in event and (not isinstance(event[key], str) or not event[key].strip()):
            errors.append(f"{key} must be a non-empty string")
    if "sequence" in event and (isinstance(event["sequence"], bool) or not isinstance(event["sequence"], int) or event["sequence"] < 0):
        errors.append("sequence must be a non-negative integer")
    if "timestamp" in event and _timestamp(event["timestamp"]) is None:
        errors.append("timestamp must be ISO-8601 with timezone")
    if "event_type" in event and event["event_type"] not in EVENT_TYPES:
        errors.append("unsupported event_type")
    if "severity" in event and event["severity"] not in SEVERITY:
        errors.append("unsupported severity")
    if "evidence_refs" in event and not (isinstance(event["evidence_refs"], list) and all(isinstance(x, str) and x.strip() for x in event["evidence_refs"])):
        errors.append("evidence_refs must be a list of non-empty strings")
    if "details" in event and not isinstance(event["details"], dict):
        errors.append("details must be an object")
    return errors


def replay_mission(events: Iterable[dict[str, Any]], *, mission_id: str | None = None) -> dict[str, Any]:
    """Validate and replay a mission log in sequence order without changing it."""
    accepted, rejected = [], []
    seen_ids = set()
    for event in events:
        errors = validate_event(event)
        if not errors and mission_id is not None and event["mission_id"] != mission_id:
            errors = ["event belongs to a different mission"]
        if not errors and event["event_id"] in seen_ids:
            errors = ["duplicate event_id"]
        if errors:
            rejected.append({"event": event, "errors": errors})
            continue
        seen_ids.add(event["event_id"])
        accepted.append(event)

    accepted.sort(key=lambda e: (e["sequence"], e["timestamp"], e["event_id"]))
    sequence_numbers = [e["sequence"] for e in accepted]
    gaps = []
    if sequence_numbers:
        for expected in range(sequence_numbers[0], sequence_numbers[-1] + 1):
            if expected not in sequence_numbers:
                gaps.append(expected)

    timeline = []
    fault_count = 0
    human_review_count = 0
    terminal_state = "IN_PROGRESS" if accepted else "NO_VALID_EVENTS"
    for event in accepted:
        kind = event["event_type"]
        if kind in {"FAULT_DETECTED", "TASK_FAILED"}:
            fault_count += 1
        if kind == "HUMAN_REVIEW_REQUESTED":
            human_review_count += 1
        if kind == "MISSION_STOPPED":
            terminal_state = "STOPPED"
        elif kind == "MISSION_COMPLETED":
            terminal_state = "COMPLETED"
        elif kind == "SAFE_HOLD":
            terminal_state = "SAFE_HOLD"
        timeline.append({
            "sequence": event["sequence"], "timestamp": event["timestamp"],
            "event_id": event["event_id"], "event_type": kind,
            "severity": event.get("severity", "info"),
            "summary": event["summary"],
            "evidence_refs": list(event.get("evidence_refs", []))
        })

    return {
        "schema_version": "1.0",
        "mission_id": mission_id or (accepted[0]["mission_id"] if accepted else None),
        "timeline": timeline,
        "accepted_event_count": len(accepted),
        "rejected_event_count": len(rejected),
        "sequence_gaps": gaps,
        "fault_count": fault_count,
        "human_review_request_count": human_review_count,
        "terminal_state": terminal_state,
        "rejected_events": rejected,
        "audit_limits": [
            "Replay is a deterministic reconstruction of supplied log records, not ground truth.",
            "Events are not cryptographically signed; source identity and evidence references are not independently verified.",
            "Sequence gaps and rejected events may make the history incomplete.",
            "No robot commands are generated and physical actuation is never authorised."
        ],
        "simulation_only": True,
        "physical_actuation_permitted": False
    }
