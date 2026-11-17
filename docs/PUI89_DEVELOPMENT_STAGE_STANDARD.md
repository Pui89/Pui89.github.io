# PUI89 Evidence-Based Development Maturity Standard

**Updated:** 17 November 2026  
**Scope:** exactly six active products plus Shared AI Core as shared infrastructure.  
**Policy:** commercial-readiness percentages and unsubstantiated completion scores are not used.

## Evidence labels

Use one label per product for its strongest currently evidenced development state. These labels are descriptive, not a numeric scale; **Unknown** is used whenever the evidence is insufficient to classify a state.

| Label | Minimum evidence to use the label |
|---|---|
| Proposed | A product or capability idea exists, but requirements are not yet baselined. |
| Specified | Intended use, requirements, constraints, interfaces or acceptance criteria are documented. |
| Implemented | A relevant software or engineering component exists in a traceable repository version. This does not imply integration or physical capability. |
| Simulated | A reproducible simulation exists with inputs, configuration, outputs and limitations recorded. |
| Software-tested | Relevant software tests were executed on a named commit and results are recorded. |
| Bench-tested | Identified physical components or a prototype were tested on a controlled bench against stated criteria. |
| Field-tested | A supervised test was conducted in a representative real environment, with permission, safety controls and a dated report. |
| Validated | The system met predefined acceptance criteria across the required operating conditions; validation scope and limitations are explicit. |
| Certified | An applicable third-party or regulatory certificate exists and its scope is linked. |
| Unknown | Evidence is missing, stale, conflicting or insufficient to assign another label. |

A product can have different labels for software, simulation and physical subsystems. Do not infer a physical label from software evidence. Simulation is not field testing; a software test does not prove physical safety; certification requires a valid certificate and scope.

## Current active-product evidence labels

| Active product | Current label | Evidence boundary and next gate |
|---|---|---|
| Coconut Harvest AI | Implemented | Software and evaluation-preparation components exist. Rights-cleared real-image dataset, human-reviewed labels, leakage-safe held-out split, CPU metrics and failure analysis remain pending. |
| PUI89 Sentinel — All-Terrain Exploration & Inspection Robot | Specified | Concept and engineering requirements are documented. Define the first supervised inspection mission, site, operating envelope and hazards before hardware selection. |
| PUI89 AI HOME | Implemented | Software foundation exists. Complete robot mass target is 8 kg and maximum 10 kg including battery and all installed hardware; no prototype mass measurement is claimed. |
| PUI89 AI NOMAD | Implemented | Software foundation exists for a ground-use four-wheel mobile assistant robot. It is not luggage or airline baggage; physical mobility remains unvalidated. |
| PUI89 AI Global SUV | Implemented | Software-only advisory and safety-contract foundation exists. No vehicle integration, road testing or autonomous control is claimed. |
| PUI89 AI Step-Through Scooter | Specified | Rider-first step-through concept and requirements are documented. Road-water/flood-risk warnings are advisory; no physical scooter or road validation is claimed. |

## Shared infrastructure

**PUI89 Shared AI Core** supports reusable contracts, orchestration, evidence provenance, safety and test tooling. It is infrastructure, not a seventh product, and is not assigned a product maturity label.

## Reporting requirements

Every maturity claim must include:
- exact repository and commit/version;
- review date and reviewer;
- linked test, simulation, bench, field or certificate evidence as applicable;
- test environment, method and acceptance criteria;
- limitations, failures, unknowns and next gate.

Do not display commercial-readiness percentages, a completion percentage or a numeric stage score. Do not treat a planned test as a test result or an unrun workflow as a pass.

## Historical records

Earlier five-stage, seven-stage and commercial-readiness percentage displays are superseded by this evidence-label standard. Dated historical reports remain preserved as historical records and must not be presented as current product status.

## ภาษาไทย — มาตรฐานสถานะการพัฒนาตามหลักฐาน

ใช้ป้ายสถานะที่สูงที่สุดซึ่งมีหลักฐานจริงรองรับ โดยไม่แปลงเป็นเปอร์เซ็นต์หรือคะแนนความพร้อมเชิงพาณิชย์:

- **Proposed — เสนอแนวคิด:** มีแนวคิด แต่ยังไม่กำหนดข้อกำหนดหลัก
- **Specified — กำหนดข้อกำหนดแล้ว:** มีเอกสารวัตถุประสงค์ ข้อกำหนด ข้อจำกัด หรือเกณฑ์ยอมรับ
- **Implemented — นำไปใช้แล้ว:** มีซอฟต์แวร์หรือองค์ประกอบทางวิศวกรรมใน repository ที่ตรวจสอบเวอร์ชันได้ ไม่ได้แปลว่ารวมระบบหรือมีความสามารถทางกายภาพแล้ว
- **Simulated — จำลองแล้ว:** มีผลจำลองที่ทำซ้ำได้ พร้อมข้อมูลนำเข้า การตั้งค่า ผลลัพธ์ และข้อจำกัด
- **Software-tested — ทดสอบซอฟต์แวร์แล้ว:** มีผลทดสอบซอฟต์แวร์บน commit ที่ระบุและมีบันทึกผล
- **Bench-tested — ทดสอบบนแท่นแล้ว:** มีการทดสอบชิ้นส่วนหรือต้นแบบจริงในสภาพแวดล้อมควบคุมตามเกณฑ์ที่กำหนด
- **Field-tested — ทดสอบภาคสนามแล้ว:** มีรายงานการทดสอบภายใต้การกำกับในสภาพแวดล้อมจริงที่เป็นตัวแทน พร้อมการอนุญาตและมาตรการความปลอดภัย
- **Validated — ตรวจสอบยืนยันแล้ว:** ผ่านเกณฑ์ยอมรับที่กำหนดไว้ในเงื่อนไขการใช้งานที่เกี่ยวข้อง พร้อมระบุขอบเขตและข้อจำกัด
- **Certified — ได้รับการรับรอง:** มีใบรับรองจากหน่วยงานที่เกี่ยวข้องและระบุขอบเขตชัดเจน
- **Unknown — ไม่ทราบ:** หลักฐานไม่ครบ ล้าสมัย ขัดแย้ง หรือไม่เพียงพอ

สถานะของซอฟต์แวร์ การจำลอง และฮาร์ดแวร์อาจแตกต่างกัน ห้ามใช้ผลทดสอบซอฟต์แวร์แทนหลักฐานความปลอดภัยทางกายภาพ และห้ามใช้ผลจำลองแทนการทดสอบภาคสนาม

พอร์ตโฟลิโอปัจจุบันมี 6 ผลิตภัณฑ์เท่านั้น ส่วน Shared AI Core เป็นโครงสร้างพื้นฐานร่วม ไม่ใช่ผลิตภัณฑ์ลำดับที่ 7 โดย HOME มีน้ำหนักเป้าหมาย 8 กก. และสูงสุด 10 กก. รวมแบตเตอรี่และอุปกรณ์ติดตั้งทั้งหมด; NOMAD เป็นหุ่นยนต์ผู้ช่วยเคลื่อนที่ภาคพื้นดินแบบ 4 ล้อ ไม่ใช่สัมภาระขึ้นเครื่องบิน; Sentinel ต้องกำหนดภารกิจตรวจสอบแรกก่อนเลือกฮาร์ดแวร์
