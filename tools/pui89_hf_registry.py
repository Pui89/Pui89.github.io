#!/usr/bin/env python3
"""Validate the PUI89 Hugging Face candidate registry without network or downloads."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_REGISTRY = Path(__file__).resolve().parents[1] / "config" / "pui89-huggingface-registry.json"
ALLOWED_LICENSE_STATES = {"RECHECK_REQUIRED", "REVIEWED"}
ALLOWED_RESOURCE_STATES = {"NOT_TESTED", "TESTED"}
ALLOWED_APPROVAL = {"NOT_APPROVED", "APPROVED_FOR_OFFLINE_EVALUATION"}


def validate_registry(data: Any) -> list[str]:
    """Return validation errors; an unreviewed candidate is valid but never approved."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["registry root must be a JSON object"]

    policy = data.get("policy")
    if not isinstance(policy, dict):
        errors.append("policy must be an object")
    else:
        for key in ("network_access", "automatic_downloads", "package_installation",
                    "paid_inference", "hardware_actuation"):
            if policy.get(key) is not False:
                errors.append(f"policy.{key} must be false")

    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        return errors + ["resources must be a non-empty array"]

    seen: set[str] = set()
    for index, item in enumerate(resources):
        prefix = f"resources[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        resource_id = item.get("id")
        if not isinstance(resource_id, str) or not resource_id.strip():
            errors.append(f"{prefix}.id must be a non-empty string")
        elif resource_id in seen:
            errors.append(f"{prefix}.id is duplicated: {resource_id}")
        else:
            seen.add(resource_id)

        url = item.get("source_url")
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"{prefix}.source_url must use HTTPS")

        projects = item.get("intended_projects")
        if not isinstance(projects, list) or not projects or not all(
            isinstance(value, str) and value.strip() for value in projects
        ):
            errors.append(f"{prefix}.intended_projects must be a non-empty string array")

        license_review = item.get("license_review")
        if not isinstance(license_review, dict):
            errors.append(f"{prefix}.license_review must be an object")
        else:
            if license_review.get("status") not in ALLOWED_LICENSE_STATES:
                errors.append(f"{prefix}.license_review.status is invalid")
            if license_review.get("status") == "REVIEWED":
                for field in ("license", "reviewed_on", "review_evidence_url"):
                    if not license_review.get(field):
                        errors.append(f"{prefix}.license_review.{field} required for REVIEWED")

        resource_review = item.get("resource_review")
        if not isinstance(resource_review, dict):
            errors.append(f"{prefix}.resource_review must be an object")
        elif resource_review.get("status") not in ALLOWED_RESOURCE_STATES:
            errors.append(f"{prefix}.resource_review.status is invalid")

        if item.get("approval") not in ALLOWED_APPROVAL:
            errors.append(f"{prefix}.approval is invalid")
        if item.get("download") != "DISABLED":
            errors.append(f"{prefix}.download must remain DISABLED")

        # An item cannot be approved for evaluation until both reviews are complete.
        if item.get("approval") == "APPROVED_FOR_OFFLINE_EVALUATION":
            if not isinstance(license_review, dict) or license_review.get("status") != "REVIEWED":
                errors.append(f"{prefix} cannot be approved before licence review")
            if not isinstance(resource_review, dict) or resource_review.get("status") != "TESTED":
                errors.append(f"{prefix} cannot be approved before resource testing")

    return errors


def load_registry(path: Path | str = DEFAULT_REGISTRY) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    args = parser.parse_args()
    try:
        data = load_registry(args.registry)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"REGISTRY_INVALID: {exc}")
        return 2
    errors = validate_registry(data)
    if errors:
        print("REGISTRY_INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"REGISTRY_VALID: {len(data['resources'])} candidates; all downloads remain disabled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
