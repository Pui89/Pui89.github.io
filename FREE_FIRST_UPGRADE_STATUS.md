# PUI89 Free-First Upgrade Status

**Checked:** 26 October 2026 (UTC)  
**Approach:** free-first, local-first, evidence-led. This report records repository and CI evidence only; it is not a claim of field validation.

## Latest repository checks

| Project | Current commit checked | Latest relevant checks | Result at time of update |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | `9f57b57ccc` | [Agent unit tests](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40261589536), [project CI](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40261589534), [security](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40261589555) | Agent tests passed; project CI/security were still running |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | `43d81e4496` | [Python tests](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40261447385); earlier [PUI89 Free Local Checks](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40260765627) | Python tests still running; earlier free checks passed |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | `1ecbf6dcfb` | [Python tests](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40261452232), [app regression checks](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40261452252) | Passed |

The [PUI89 website deployment](https://github.com/Pui89/Pui89.github.io/actions/runs/40261494147) completed successfully after the homepage status link was added.

## Existing agentic engineering foundation

All three project repositories already contain a Python-based agentic workflow, command-line runner, tests, free-first checks and project-specific frontier-upgrade plan. The next step is to improve and verify existing tools rather than add a duplicate agent framework.

- [Coconut frontier upgrade plan](https://github.com/Pui89/Coconut-Harvest-AI/blob/main/docs/FRONTIER_AI_UPGRADE_PLAN.md)
- [Flood frontier upgrade plan](https://github.com/Pui89/Extreme-Flood-Rescue-AI/blob/main/docs/FRONTIER_AI_UPGRADE_PLAN.md)
- [Screening frontier upgrade plan](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/blob/main/docs/FRONTIER_AI_UPGRADE_PLAN.md)



## Automatic candidate-download guardrail

The scheduled [coconut candidate refresh run](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40261485656) failed because three of five source requests returned HTTP 429 rate limits. It downloaded two review candidates, recorded **0 training-approved images**, and uploaded an approximately 11.6 MB artifact with 14-day retention. This is not a dataset promotion and does not authorize training.

To reduce recurring network/artifact activity, the candidate-download workflow is now **manual-only** in commit `9f57b57ccc`. A person must deliberately dispatch it; ordinary pushes and the weekly schedule no longer trigger external candidate downloads. Existing artifacts follow their stated retention period.

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
