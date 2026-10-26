# PUI89 Free-First Upgrade Status

**Checked:** 26 October 2026 (UTC)  
**Approach:** free-first, local-first, evidence-led. This report records repository and CI evidence only; it is not a claim of field validation.

## Latest repository checks

| Project | Commit checked | Latest relevant checks | Result |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | `155d18ce1ee0` | [Python tests](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40260685004), [PUI89 Free Local Checks](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40260684889), [project CI](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40260684890) | Passed |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | `b6ec5664ba58` | [Python tests](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40260765625), [PUI89 Free Local Checks](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40260765627) | Passed |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | `fcd2516c5c94` | [Python tests](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40260691329), [PUI89 Free Local Checks](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40260691273), [app regression checks](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40260691216) | Passed |

The [PUI89 website deployment](https://github.com/Pui89/Pui89.github.io/actions/runs/40227356481) also completed successfully for the website commit checked before this status report was added. A new deployment should be checked separately after this change.

## Existing agentic engineering foundation

All three project repositories already contain a Python-based agentic workflow, command-line runner, tests, free-first checks and project-specific frontier-upgrade plan. The next step is to improve and verify existing tools rather than add a duplicate agent framework.

- [Coconut frontier upgrade plan](https://github.com/Pui89/Coconut-Harvest-AI/blob/main/docs/FRONTIER_AI_UPGRADE_PLAN.md)
- [Flood frontier upgrade plan](https://github.com/Pui89/Extreme-Flood-Rescue-AI/blob/main/docs/FRONTIER_AI_UPGRADE_PLAN.md)
- [Screening frontier upgrade plan](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/blob/main/docs/FRONTIER_AI_UPGRADE_PLAN.md)

## Highest-priority blocker: Coconut dataset

The recorded audit contains **34 candidate rows and 0 approved for training**. Many rows have missing provenance/licence details, and annotation review is still pending or not complete. Do not train or publish model-performance claims from this batch until the rights and annotation gates are satisfied.

Recommended order:

1. Review each image's source page, exact licence terms, creator credit and attribution requirements; do not infer reuse permission from public availability.
2. Review the actual image file and annotation together, resolving the flagged geometry and image-specific issues before marking any annotation passed.
3. Verify file hashes and remove exact/near duplicates where possible.
4. Split by source/tree/session to reduce leakage, then freeze a held-out test set.
5. Run a baseline only on an approved, reviewed split and publish metrics with the command, versions, hardware, sample count and limitations.

## Project-specific next steps

- **Coconut:** dataset rights, annotation QA, leakage checks, then a reproducible vision baseline.
- **Flood:** deterministic fault/scenario tests; treat water depths as simulation parameters, not proof of rescue capability.
- **Screening:** data governance, held-out evaluation, false-positive/false-negative analysis and human review for uncertain or consequential outcomes.

## Cost and evidence guardrails

- No paid API, subscription, hosted inference or cloud GPU was added as part of this work.
- Keep local checks standard-library/lightweight where possible; do not download large models just to satisfy a roadmap.
- GitHub Actions and GitHub Pages still operate under their platform terms and quotas; check account usage separately if cost certainty is required.
- A passing software test is not evidence of physical robot safety, field performance, validated narcotics detection, or commercial readiness.
- Any capability not supported by a reproducible test remains **planned**, **in progress** or **unverified**.

## Operating command

From a local clone of each project, inspect the existing tool and its help before running it. Prefer the repository's documented test command and the existing `tools/run_agentic_workflow.py` runner. The workflow proposes/reports; it does not control hardware or autonomously promote data.
