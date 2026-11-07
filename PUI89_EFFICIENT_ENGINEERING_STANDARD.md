# PUI89 Efficient Engineering Standard

**Status:** Proposed shared engineering standard  
**Applies to:** All seven PUI89 projects and the shared AI Core  
**Cost policy:** Zero-cost-first. No paid API, subscription, cloud GPU, metered service, hardware purchase, or paid dataset is authorised by this standard.  
**Evidence rule:** Record measured results; never claim an efficiency improvement without a reproducible before/after comparison.

## 1. Purpose

Build AI products that deliver useful, safe and dependable performance with the minimum resources reasonably required. Efficiency must not weaken accuracy, safety, privacy, security, accessibility, evidence integrity or human oversight.

**Engineering principle:** Low Resources. High Intelligence. Measurable Reliability.

## 2. Ten efficiency dimensions

1. **Memory:** measure idle, typical and peak RAM; avoid unnecessary copies and eager loading; release resources; detect leaks and out-of-memory behaviour.
2. **Compute:** measure CPU/GPU use and workload; avoid duplicate inference and unnecessary polling; select model size and execution frequency to fit the device.
3. **Energy:** for physical devices, measure watts and watt-hours for defined tasks, idle/standby draw and battery runtime under a documented workload. Do not estimate physical power from CPU percentages.
4. **Thermal:** record ambient and component temperatures under sustained workloads when sensors are available; assess throttling, enclosure ventilation and safe shutdown behaviour.
5. **Storage:** track application, model, cache, dataset and log footprint; use retention limits and avoid duplicate artifacts.
6. **Network:** measure bytes transferred per task, request frequency, offline behaviour and reconnection handling; avoid mandatory cloud dependencies where local operation is feasible.
7. **Latency:** record startup, processing and inference latency (including p50/p95 where sample counts support it); distinguish cold-start from warmed-up results.
8. **Software complexity:** minimise dependencies, duplicated logic, background services and maintenance burden; review licences, security and platform compatibility before adoption.
9. **Offline / edge resilience:** support local processing when appropriate; define safe behaviour for network loss, stale inputs, resource exhaustion and partial functionality.
10. **Lifecycle / repairability:** favour modularity, serviceability, replaceable components, durability and reduced electronic waste; treat material and environmental claims as testable requirements.

## 3. Measurement protocol

Every benchmark record should include:

- project, component, commit/version and benchmark date;
- device model, OS, runtime, power mode and relevant hardware limits;
- dataset/scenario identity, size, licence/provenance status and configuration;
- workload, duration, warm-up, repetitions and sample count;
- idle, typical and peak RAM; CPU/GPU utilisation where available;
- startup and task latency; throughput and task success;
- model and application storage footprint;
- network bytes and request count where applicable;
- watts, watt-hours, battery runtime and temperatures **only when measured with suitable physical instrumentation**;
- accuracy, error cases, uncertainty and safety-gate outcomes;
- raw results, method, limitations and reproducible command.

Compare like with like: same device, workload, data, configuration and measurement method. Report median and spread where meaningful. Do not compare a single screenshot or one run as a benchmark. A faster or smaller system is not an improvement if task quality, safety or reliability degrades.

## 4. Resource-aware runtime behaviour

Where appropriate and validated, applications should:

- use demand-driven processing rather than continuous full-rate inference;
- use lightweight screening before expensive analysis, with escalation when justified;
- batch or cache only when freshness and safety requirements permit;
- set bounded queues, timeouts, retry limits and memory budgets;
- expose degraded, offline, low-battery and sensor-fault states;
- reduce nonessential work when resources are constrained;
- preserve essential safety monitoring and emergency functions;
- fail conservatively when required evidence is missing, stale or conflicting.

Resource scheduling must never silently disable required sensors, safety checks, human review, evidence logging or emergency-stop pathways.

## 5. Architecture and technology policy

- Keep Python for AI research, dataset tooling, evaluation and model experimentation where it remains the most suitable tool.
- Evaluate Rust selectively for resource-sensitive system services, data handling and future edge interfaces; do not rewrite functioning projects solely to adopt a language.
- Consider ONNX Runtime or other inference runtimes only after checking exact licence, model compatibility, platform support, security, footprint and reproducible performance.
- Treat GPUI as an optional future desktop UI candidate, not a current requirement. A desktop application is not required to deliver the current web products.
- Prefer standard-library tooling and existing project dependencies when they meet the need.
- No package, model, dataset, framework, hosted service or hardware is automatically approved. Check licence, provenance, security, hardware fit and total cost first.
- Shared AI Core contracts remain technology-neutral and machine-readable. Project-specific sensor and safety requirements remain distinct.

## 6. Safety and quality gates

Efficiency changes must pass applicable tests for:

- functional correctness and regression;
- accuracy and task quality on valid held-out evidence;
- missing, noisy, stale and conflicting inputs;
- uncertainty propagation and calibration where applicable;
- resource exhaustion and recovery;
- offline operation and interrupted connectivity;
- safe-state behaviour and human override;
- security, dependency and licence review.

No benchmark may authorise physical actuation. Hardware control remains separately authorised and safety-validated. Simulation and software tests do not prove physical energy use, battery endurance, thermal safety, waterproofing, fire resistance or field performance.

## 7. Project-specific emphasis

| Project | Priority efficiency evidence |
|---|---|
| Coconut Harvest AI | Image pipeline RAM/latency, edge inference footprint, energy per inspection/harvest-assessment task |
| Flood Rescue AI | Offline operation, battery endurance, sensor/network resilience, thermal and power budgets |
| PUI89 Sentinel | Modality-specific processing cost, provenance-preserving storage, review latency and false-positive/false-negative trade-offs |
| AI HOME | Standby power, event-triggered processing, local operation, privacy-preserving storage |
| AI NOMAD | Battery runtime, portable compute/thermal budget, offline navigation and sensor duty cycles |
| AI Robot Car | Perception latency, energy budget, fault handling and simulation-only resource benchmarks |
| AI Robot Motorcycle | Low-power monitoring, advisory latency, thermal/battery health and fail-safe degradation |

The shared AI Core provides common benchmark schemas and reporting; it must not impose identical thresholds across different products.

## 8. Rollout stages

1. **Baseline first:** add dependency-light software measurements (RAM, CPU, latency, storage) to existing verification workflows where feasible.
2. **Benchmark reproducibly:** record configuration, workload, repeated measurements and limitations.
3. **Optimise one bottleneck:** make one evidence-backed change at a time.
4. **Regression gate:** rerun functional, safety, security and performance checks.
5. **Physical measurement later:** add power, temperature and battery tests only when suitable equipment is available and explicitly approved.
6. **Product readiness:** publish project-specific efficiency evidence and remaining limitations; do not generalise one project's results to another.

## 9. Reporting language

Use **measured**, **tested**, **simulated**, **estimated**, **proposed** and **not measured** precisely. Do not state that PUI89 is low-power, energy-efficient, long-battery-life, low-heat, or lower-RAM than a competitor until comparable measurements support the specific claim.

## 10. Acceptance checklist

- [ ] Baseline and workload are documented.
- [ ] Device and software environment are documented.
- [ ] Measurements are repeatable and comparable.
- [ ] RAM, CPU, latency and storage are measured where relevant.
- [ ] Power, battery and temperature are measured only with appropriate instrumentation.
- [ ] Accuracy, safety and reliability did not regress.
- [ ] Offline and resource-exhaustion behaviour are checked where relevant.
- [ ] Dependencies, licences, provenance and cost are reviewed.
- [ ] Raw evidence, limitations and next actions are recorded.
- [ ] No unsupported performance or product-readiness claim is made.

---
PUI89 independent R&D initiative. This standard defines development requirements; it does not certify any product or establish that every measurement is already implemented.
