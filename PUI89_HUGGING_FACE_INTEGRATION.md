# PUI89 Hugging Face Integration

**Status:** integration foundation added; model execution is not enabled.  
**Policy:** local-first, optional, review-gated, no automatic downloads.

## Why Hugging Face belongs in PUI89

The Hugging Face Hub provides model repositories, datasets, model cards, version history and interactive Spaces. PUI89 can use it as a discovery and provenance source while keeping inference local and optional. A Hub listing is not proof that a model is suitable, safe, free of restrictions or compatible with the user's machine.

## First candidates

The initial registry is `config/pui89-huggingface-registry.json`.

| Candidate | Potential PUI89 role | Initial status |
|---|---|---|
| `HuggingFaceTB/SmolVLM-256M-Instruct` | Compact image description and evidence summarisation; possible evaluation across the three applications | Candidate only; licence and hardware review required |
| `lerobot/smolvla_base` | Vision-language-action research in offline simulation, initially Coconut and Flood | Candidate only; licence and hardware review required |
| `huggingface/lerobot` | Robotics data formats, training/evaluation tooling and research reference | Candidate only; licence and dependency review required |

These entries are discovery targets, not endorsements or approvals. The licence fields are deliberately blank until the exact repository card and licence text are checked at the time of adoption. Model sizes and RAM/VRAM needs are also deliberately unfilled until verified and measured.

## Integration design

1. **Registry:** record exact Hub ID, source URL, intended projects, use boundary, licence evidence and resource review.
2. **Preflight:** inspect local Python/runtime, free disk and available memory. Add GPU/VRAM checks only through a documented optional path.
3. **Adapter interface:** model adapters accept a validated PUI89 input envelope and return observations or proposed actions with source/model/version metadata.
4. **Safety and provenance:** pass outputs through the existing evidence contract, uncertainty handling, world-state checks and project policy gate.
5. **Evaluation:** use synthetic fixtures first; then lawful, provenance-documented project datasets with held-out splits. Record model revision, file hashes, runtime, memory, latency, failures and task metrics.
6. **Approval:** only enable local inference after licence review, resource testing, dependency review and passing offline tests.

## Project boundaries

- **Coconut Harvest AI:** VLM outputs may describe visible maturity cues for comparison with labelled observations. They do not replace a validated detector or establish harvest readiness by themselves.
- **Extreme Flood Rescue AI:** VLM outputs may describe visible hazards for simulation and operator review. SmolVLA action sequences remain simulated proposals and cannot command a robot.
- **Multimodal Narcotics Screening AI:** visual-language outputs may organise visible context for a human reviewer only. RGB/VLM output cannot establish chemical identity, guilt or grounds for enforcement. Missing, stale, conflicting or uncertain evidence must abstain or request human review.

## Non-negotiable cost and safety controls

- No paid inference endpoint or subscription.
- No cloud GPU dependency.
- No model or dataset downloads in CI or by default.
- No package installation from the registry validator.
- No external upload of private project data.
- No direct hardware actuation; simulated proposals only.
- No model is approved until its exact licence, model card, dependencies, size and local resource fit are reviewed.
- Recheck upstream model cards and licences before every adoption decision; Hub metadata and model files can change.

## Validation

Run from the repository root:

```bash
python tools/pui89_hf_registry.py
PYTHONPATH=tools python -m unittest discover -s tests -p "test_pui89_hf_registry.py" -v
```

The validator uses only the Python standard library. It reads the local JSON registry and does not contact Hugging Face.

## Official references

- [Hugging Face Hub documentation](https://huggingface.co/docs/hub)
- [Model cards and licence metadata](https://huggingface.co/docs/hub/model-cards)
- [Gated model access](https://huggingface.co/docs/hub/models-gated)
- [Model download documentation](https://huggingface.co/docs/hub/models-downloading)
- [SmolVLM candidate](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct)
- [SmolVLA candidate](https://huggingface.co/lerobot/smolvla_base)
- [LeRobot framework](https://github.com/huggingface/lerobot)

**Evidence boundary:** a valid registry means the candidate metadata passes local structural checks. It does not mean the models were downloaded, executed, benchmarked, licensed for PUI89's intended use or validated on any project.
