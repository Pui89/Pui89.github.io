"""PUI89 mock-only model adapter boundary; standard library only."""
from __future__ import annotations
from datetime import datetime
from typing import Any
from pui89_adaptive_orchestrator import evaluate
from pui89_agent_contract import validate_evidence, validate_message

PROJECTS = {"coconut_harvest", "extreme_flood_rescue", "multimodal_narcotics_screening"}
FORBIDDEN_COMMAND_FIELDS = {"actuate", "actuator_command", "hardware_command", "physical_action", "execute_action", "robot_command"}

def _valid_timestamp(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.tzinfo is not None and parsed.utcoffset() is not None
    except (TypeError, ValueError, AttributeError):
        return False

def _error(status: str, errors: list[str], request_id: str | None = None) -> dict[str, Any]:
    return {
        "schema_version": "1.0", "request_id": request_id, "status": status,
        "observations": [], "proposed_actions": [],
        "policy_result": {"action": "SAFE_HOLD", "reason": "model adapter request failed validation",
                          "simulation_only": True, "physical_actuation_permitted": False},
        "errors": errors,
        "limitations": ["No model inference was performed.",
                        "No physical action or hardware command is available through this adapter."]
    }

def run_mock_adapter(request: Any, *, now: str, max_evidence_age_seconds: float = 3600) -> dict[str, Any]:
    """Validate a request and route synthetic observations through PUI89 policy."""
    if not isinstance(request, dict):
        return _error("REJECTED", ["request must be an object"])
    request_id = request.get("request_id")
    if FORBIDDEN_COMMAND_FIELDS.intersection(request):
        return _error("REJECTED", ["physical command fields are forbidden"], request_id)
    required = {"project_id", "request_id", "timestamp", "task", "evidence", "mock_observations"}
    errors = [f"missing required field: {key}" for key in sorted(required - request.keys())]
    if request.get("project_id") not in PROJECTS:
        errors.append("project_id is not a registered PUI89 project")
    if not isinstance(request_id, str) or not request_id.strip():
        errors.append("request_id must be a non-empty string")
    if not _valid_timestamp(request.get("timestamp")):
        errors.append("timestamp must be ISO 8601 with timezone")
    if not _valid_timestamp(now):
        errors.append("now must be ISO 8601 with timezone")
    if not isinstance(request.get("task"), str) or not request["task"].strip():
        errors.append("task must be a non-empty string")
    if isinstance(max_evidence_age_seconds, bool) or not isinstance(max_evidence_age_seconds, (int, float)) or max_evidence_age_seconds < 0:
        errors.append("max_evidence_age_seconds must be a non-negative number")
    evidence = request.get("evidence")
    evidence_by_id = {}
    if not isinstance(evidence, list) or not evidence:
        errors.append("evidence must be a non-empty array")
    else:
        for index, item in enumerate(evidence):
            errors.extend(f"evidence[{index}]: {e}" for e in validate_evidence(item))
            if isinstance(item, dict) and isinstance(item.get("source_id"), str):
                sid = item["source_id"]
                if sid in evidence_by_id:
                    errors.append(f"duplicate evidence source_id: {sid}")
                evidence_by_id[sid] = item
                if item.get("evidence_kind") != "synthetic":
                    errors.append(f"evidence[{index}] must be labelled synthetic for mock execution")
    observations = request.get("mock_observations")
    if not isinstance(observations, list) or not observations:
        errors.append("mock_observations must be a non-empty array")
    elif not all(isinstance(item, dict) for item in observations):
        errors.append("mock_observations entries must be objects")
    if errors:
        return _error("REJECTED", errors, request_id)
    message = {
        "agent_id": "pui89.mock_adapter", "task_id": request_id, "timestamp": now,
        "source_ids": sorted(evidence_by_id), "observations": observations, "claims": [],
        "confidence": None, "confidence_interpretation": "not_applicable",
        "uncertainty": ["Synthetic fixture only; no model inference or calibrated confidence."],
        "limitations": ["Observation-only mock; not a domain prediction."],
        "status": "PROPOSED", "requested_action": "VERIFY"
    }
    message_errors = validate_message(message, evidence_by_id)
    if message_errors:
        return _error("REJECTED", [f"adapter message: {e}" for e in message_errors], request_id)
    policy = evaluate([message], evidence_by_id, now=now,
                      max_evidence_age_seconds=max_evidence_age_seconds)
    return {
        "schema_version": "1.0", "request_id": request_id, "project_id": request["project_id"],
        "adapter": {"id": "pui89.mock_adapter", "mode": "MOCK",
                    "model_id": None, "model_revision": None, "inference_performed": False},
        "status": "MOCK_OBSERVATION_ONLY", "observations": observations, "proposed_actions": [],
        "agent_message": message, "policy_result": policy, "errors": [],
        "limitations": [
            "Synthetic fixture observations are not model predictions or real sensor evidence.",
            "No model weights, model libraries, network services or external APIs were used.",
            "Policy CONTINUE is not a recommendation to act and never authorizes hardware.",
            "A future local model adapter requires separate licence, resource, provenance and safety review."
        ],
        "physical_actuation_permitted": False
    }
