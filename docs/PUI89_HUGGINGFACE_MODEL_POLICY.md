# PUI89 Hugging Face Model Policy

**Status: candidate catalogue only — no model weights downloaded, installed, fine-tuned, or evaluated by this policy.**

PUI89 uses Hugging Face as a discovery and reference catalogue, not as automatic approval to execute or ship a model. The mandatory model-origin rule is **NON-CHINESE ORIGIN ONLY** across every current and future PUI89 project.

## 1. Mandatory origin and supply-chain rule

- Exclude models developed, owned, published, or maintained by Chinese companies, universities, research institutes, state entities, or development teams.
- Exclude Chinese-origin model providers, inference services, rebranded checkpoints, community conversions, and forks where the upstream provenance is not independently established.
- If developer identity, ownership, publisher, upstream source, checkpoint lineage, or provenance is unclear, mark **REJECTED / ORIGIN UNVERIFIED** and do not download or use it.
- Check the exact Hugging Face repository and immutable revision, not just the model-family name. Re-check ownership and provenance before every adoption or release.
- The non-Chinese developer rule does not automatically establish that every training-data source is non-Chinese or that training-data rights are clear. Dataset provenance, privacy, copyright and lawful-use review remain separate mandatory gates.

## 2. Initial non-Chinese candidate catalogue

These exact model repositories are candidate references selected from model cards identifying Microsoft, Meta, Google and OpenAI as the developers/publishers. This is **not a blanket approval** for production or commercial redistribution.

| Hugging Face checkpoint | Publisher shown by model card | Model-card licence | Intended research role | Adoption status |
|---|---|---|---|---|
| [microsoft/Florence-2-base](https://huggingface.co/microsoft/Florence-2-base) | Microsoft | MIT | Image description, candidate object localization, OCR and visual-language tasks | CANDIDATE — review custom code before execution |
| [facebook/dinov2-base](https://huggingface.co/facebook/dinov2-base) | Meta AI | Apache-2.0 | Visual feature extraction, image similarity and downstream vision research | CANDIDATE — checkpoint/resource review required |
| [google/siglip2-base-patch16-224](https://huggingface.co/google/siglip2-base-patch16-224) | Google | Apache-2.0 | Image-text similarity, zero-shot category exploration and visual representation | CANDIDATE — dataset/task evaluation required |
| [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) | OpenAI | Apache-2.0 | Optional multilingual speech-to-text / voice-interface research | CANDIDATE — privacy, language and resource review required |

**Important licence distinction:** the model-card licence applies to the stated repository/checkpoint. It does not grant rights to third-party training data, external datasets, trademarks, dependencies, or any separate asset. Check the exact revision's LICENSE, model card, notices, and relevant upstream terms before commercial use. A permissive model licence is not a guarantee of safe, accurate, or lawful use.

### Security note

Florence-2 documents use of trust_remote_code=True. Do not enable remote model code by default. Inspect and pin the exact source revision, review the code and dependencies, and obtain explicit approval before executing it. Prefer safe weight formats such as Safetensors where available; do not load untrusted pickle-based checkpoints.

## 3. Project-specific model mapping

- **Coconut Harvest AI:** Florence-2 for candidate fruit/scene localization and descriptions; DINOv2 for visual features; SigLIP 2 for image-text similarity. Requires its own rights-cleared, human-reviewed coconut dataset and maturity-specific evaluation.
- **Flood Rescue AI:** Florence-2, DINOv2 and SigLIP 2 for scene/object research; Whisper tiny as an optional operator speech interface. No autonomous rescue, navigation or propulsion authority.
- **Sentinel Multimodal Screening AI:** Florence-2, DINOv2 and SigLIP 2 for RGB research and evidence organization only. These are not narcotics classifiers. X-ray and chemical-sensor models need separate modality-specific provenance, licensing, data and validation reviews. No enforcement decisions.
- **AI HOME:** Florence-2, DINOv2 and SigLIP 2 for indoor visual observations; Whisper tiny as an optional voice interface. Not substitutes for certified alarms or validated fire, electrical, structural, water or environmental sensors.
- **AI NOMAD:** Florence-2, DINOv2 and SigLIP 2 for outdoor scene research; Whisper tiny for optional voice input. No locomotion, following, navigation or motor authority.
- **AI Car:** SigLIP 2, DINOv2 and Florence-2 for offline road-scene research; Whisper tiny for optional voice input. Advisory research only; no steering, throttle, braking or vehicle control.
- **AI Motorcycle / EasyRide:** SigLIP 2, DINOv2 and Florence-2 for offline road-scene research; Whisper tiny for optional voice input. Advisory research only; no steering, throttle, braking, motor or battery control.

## 4. Mandatory adoption gates

Before any model is downloaded, executed, fine-tuned, integrated, or redistributed:

1. **Origin:** verify original developer, current owner, publisher, upstream project, checkpoint lineage and non-Chinese origin.
2. **Licence:** inspect the exact revision's model card, licence file, notices, restrictions and commercial-use permissions.
3. **Data:** review training-data disclosures and separately verify all project datasets, consent, privacy, copyright, provenance and reuse rights.
4. **Security:** pin an immutable revision; inspect code and dependencies; check file formats and hashes; reject unexplained binaries, unsafe deserialization, remote-code execution and suspicious install scripts.
5. **Resources:** record parameter count, actual download size, RAM/VRAM, disk, CPU/GPU needs, runtime and offline feasibility. Do not assume a model is suitable for a low-resource laptop.
6. **Cost:** no paid APIs, subscriptions, hosted inference, cloud GPUs, metered services or unexpected billing. Do not enable a paid endpoint.
7. **Evaluation:** use a lawful, representative, leakage-safe dataset; record baseline, metrics, uncertainty, failure cases, latency and reproducible configuration.
8. **Safety:** models provide observations or bounded proposals only. Independent deterministic safety gates and human oversight remain mandatory. Never grant a general-purpose model direct authority over physical actuators or consequential decisions.
9. **Approval:** document reviewer, exact checkpoint revision, evidence and approval before changing status from CANDIDATE.

## 5. Status vocabulary

- **CANDIDATE:** listed for research; not downloaded or tested.
- **DOWNLOADED:** exact checkpoint obtained after approval; not yet evaluated.
- **EVALUATED:** reproducible task-specific evaluation completed and recorded.
- **APPROVED:** documented technical, legal, security, cost and safety review passed for a clearly defined use.
- **REJECTED / ORIGIN UNVERIFIED:** excluded; do not download or use.

A README link is not evidence of integration. Do not claim accuracy, real-time capability, safety, certification, or production readiness without project-specific evidence.

## 6. Zero-cost default

This catalogue update adds documentation links only. It does not install packages, download weights, run benchmarks, activate hosted inference, or change hardware controls. Any future installation or evaluation must be a separately approved, cost-checked task.

**PUI89 rule: Non-Chinese origin only. Exact-checkpoint review. Evidence before adoption. Zero-cost by default.**
