# Model, Data and Software Supply-Chain Policy

## User-directed procurement constraint

This project excludes Chinese-origin AI models, Chinese model providers and Chinese model-hosting services from its approved model stack. No such model or service is used by the initial foundation.

This is a project-specific security and procurement constraint. National origin alone is not a technical security assessment; every component still requires evidence-based review.

## Approved starting posture

- Python standard library for the initial core.
- pytest for tests; Ruff may be added after version and licence review.
- No model downloads, telemetry, remote inference, API keys or cloud GPU.
- No hidden optional dependency that contacts an external model endpoint.
- Prefer offline, reproducible execution.

## Future model approval checklist

Before any model is added, record:
1. Model and publisher identity, ownership and country of origin.
2. Exact weights, release, checksum and download source.
3. Licence and commercial/redistribution restrictions.
4. Training-data and evaluation-data provenance where disclosed.
5. Runtime dependencies, transitive dependencies and known vulnerabilities.
6. Network calls, telemetry, data retention and processing location.
7. Required hardware, resource footprint and cost.
8. Benchmark results against a transparent non-ML baseline.
9. Failure modes, uncertainty calibration and rollback plan.
10. Human reviewer and approval date.

## Open-source does not automatically mean safe

Review licence compatibility, maintainer health, release integrity, dependency provenance, security advisories, update policy and network behavior. Do not execute untrusted model code or install packages directly from arbitrary repositories.

## Data policy

Use synthetic data for the first demonstrator. Real building data requires documented permission, privacy review, retention limits, access controls and a lawful basis. Do not upload private audio, indoor imagery or occupancy data to external model services by default.
