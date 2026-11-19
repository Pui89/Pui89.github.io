# PUI89 Product Operating Coverage Standard v1.0

**Status:** Proposed product-allocation and measurement standard. This document does not certify or verify physical performance.

**Applies to:** The six active PUI89 products. Shared AI Core is common infrastructure, not a seventh product.

## PUI89 Product Philosophy

> **Build what you wish existed as a user.**  
> **สร้างสิ่งที่คุณอยากให้มีในฐานะผู้ใช้งาน**

Start with the user, then use engineering to create products that provide practical value in real life. Apply this philosophy to all six active PUI89 products. Product requirements must come from real user needs, operating contexts, safety considerations and evidence—not from adding AI features simply because they are technically possible.

**ภาษาไทย:** เริ่มต้นจากผู้ใช้งาน สู่การใช้วิศวกรรมสร้างผลิตภัณฑ์ที่มีประโยชน์ในชีวิตจริง นำหลักการนี้ไปใช้กับผลิตภัณฑ์ทั้ง 6 รายการ โดยกำหนดความต้องการจากปัญหาและบริบทการใช้งานจริง คำนึงถึงความปลอดภัยและหลักฐาน ไม่เพิ่มฟีเจอร์ AI เพียงเพราะเทคโนโลยีทำได้

## 1. Governing rules

1. Define one unit by the product's actual user task and operating environment.
2. Do not force every product into square metres. Use hectares, mapped floor area, inspection routes, assigned tasks, or vehicle operating routes as appropriate.
3. Do not publish a numerical coverage, throughput, range, endurance, accuracy, or productivity claim until a defined test has produced traceable evidence.
4. Distinguish **Proposed**, **Design Target**, **Implemented**, **Tested**, **Verified**, and **Certified**. A specification or software test is not physical validation or regulatory certification.
5. Record the test configuration, sensor/model versions, environment, operating time, workload, failures, safety interventions, and limitations.
6. Do not silently change an approved product definition or specification. Changes require a reason, evidence, version history, and review.
7. Essential controls, status, alerts, and recovery must be available on the product or its appropriate local operator station; a smartphone app must not be mandatory.

## 2. Per-product unit and coverage definition

| Active product | One-unit allocation rule | Correct coverage measure | Numerical coverage status |
|---|---|---|---|
| **PUI89 AI HOME** | **One robot and one charging dock per floor.** A multi-floor home uses one coordinated household system with a robot assigned to each floor. | Mapped, accessible operating area per floor; rooms reached; task completion and operating time. Stairs are not assumed traversable. | No verified m²-per-unit figure. Set a floor-specific design envelope and validate it in representative homes. |
| **Coconut Harvest AI** | One unit is assigned to a defined plantation block and harvesting workflow. | Hectares and trees/bunches inspected or serviced per working day; include terrain, tree spacing, maturity mix, setup and human intervention. | No verified hectares/day figure. Earlier 1–5 ha/day figures are withdrawn as unsupported planning estimates. |
| **PUI89 Sentinel — All-Terrain Exploration & Inspection Robot** | One quadruped robot is assigned to a defined inspection mission/site zone. | Mapped inspection area or route length per mission, operating time, terrain class, inspection tasks completed and safe recovery rate. | No verified m², km, or hours-per-charge figure. Do not describe Sentinel as a screening lane/station product. |
| **PUI89 AI NOMAD — Carry-on Suitcase-Style Mobile AI Assistant** | One unit is assigned to one traveller and their luggage-use task. | Journey/task coverage: travel duration, handling events, location continuity where supported, tamper/event monitoring and battery endurance. | No verified m² coverage. The earlier 500–2,000 m² facility-zone estimate is withdrawn as the wrong measure for the suitcase product. |
| **PUI89 AI Global SUV** | One AI system per vehicle. | Approved vehicle operating domain and routes; separately specify front, rear and side sensing zones, conditions, speeds and driver-warning behaviour. | No verified route, sensor-range, autonomy or road-coverage claim. Driver remains in control unless a separately validated and authorised system is developed. |
| **PUI89 AI Step-Through Scooter** | One AI system per scooter. | Approved vehicle operating domain and routes; separately specify front/rear sensing zones, conditions, speeds and rider-warning behaviour. | No verified route, sensor-range or autonomy claim. No autonomous throttle, steering or braking in the initial scope. |

## 3. AI HOME household deployment rule

For AI HOME, the recommended product package is:

- One floor = one AI HOME robot.
- One floor = one dedicated charging dock.
- Robots coordinate through the AI HOME Household Network when connectivity is available.
- Each robot must retain essential local operation and safe behaviour if the household network is unavailable.
- Each floor has its own mapped operating area and access limitations.
- Do not claim stair climbing or automatic inter-floor transport unless a dedicated mechanism has been designed, risk-assessed, and validated.

Examples: a three-storey home is planned as three AI HOME robots and three charging docks; a two-storey home is planned as two robots and two docks. This is a product-allocation recommendation, not a claim of demonstrated performance.

## 4. Product-specific AI and sensor evidence

Sensor lists and AI functions must remain product-specific. Shared AI Core may provide reusable sensor registration, timestamp/provenance handling, quality checks, fusion interfaces, uncertainty, failure reporting, alert contracts and resource-aware edge inference. It does not make every sensor or AI capability installed in every product.

For each proposed sensor or AI capability, record:

- Exact sensor class and intended function; selected manufacturer/model only when verified.
- Quantity, mounting location, orientation, field of view or measurement envelope.
- Interface, calibration method, sampling rate and health/fault behaviour.
- AI task, model provenance/licence, compute and memory needs.
- Operating conditions, known blind spots and privacy implications.
- Acceptance criteria, test method, test results and evidence location.

No specific camera count, LiDAR count, radar count, model accuracy, detection distance, throughput, battery runtime or area capacity is approved by this standard.

## 5. Required validation record

Before a numerical operating-coverage claim is published, retain a product-specific report with:

1. Unit configuration and hardware/software versions.
2. Site, route, floor plan or plantation-block definition.
3. Environmental and operating conditions.
4. Workload, start/end times, operating duration and number of trials.
5. Successful task counts, incomplete tasks, failures and human interventions.
6. Safety events, stop/recovery behaviour and excluded conditions.
7. Power use and battery endurance where relevant.
8. Measurement method, uncertainty and limitations.
9. Reviewer, date, evidence links and approved wording for public claims.

A result applies only to the tested configuration and conditions. Do not generalise it to all homes, farms, sites, roads, climates or users without additional evidence.

## 6. Public-claim guardrail

Use wording such as:

- **Proposed:** "Designed to target..." or "The project is evaluating..."
- **Implemented:** "The repository contains..." followed by the exact software component.
- **Tested:** state the test, configuration and conditions.
- **Verified:** state the evidence and validated operating envelope.
- **Certified:** name the applicable certification and authorised issuer only after it is actually granted.

Never present concept imagery, a planned sensor, a design target, synthetic data, a software unit test, or an unexecuted test plan as proof of physical product capability.

---

# ภาษาไทย

**สถานะ:** มาตรฐานข้อเสนอสำหรับการจัดสรรผลิตภัณฑ์และการวัดพื้นที่/ขอบเขตการทำงาน ยังไม่ใช่การรับรองหรือยืนยันประสิทธิภาพทางกายภาพ

**ขอบเขต:** ผลิตภัณฑ์ PUI89 ที่กำลังพัฒนา 6 รุ่น โดย Shared AI Core เป็นโครงสร้างพื้นฐานร่วม ไม่ใช่ผลิตภัณฑ์รุ่นที่ 7

## 1. กฎหลัก

1. กำหนดความหมายของหนึ่งเครื่องตามภารกิจและสภาพแวดล้อมการใช้งานจริงของผลิตภัณฑ์นั้น
2. ไม่บังคับใช้หน่วยตารางเมตรกับทุกผลิตภัณฑ์ ให้เลือกใช้เฮกตาร์ พื้นที่ชั้นที่ทำแผนที่ เส้นทางตรวจสอบ ภารกิจที่ได้รับมอบหมาย หรือเส้นทางยานพาหนะตามความเหมาะสม
3. ห้ามประกาศตัวเลขพื้นที่ครอบคลุม ปริมาณงาน ระยะตรวจจับ ระยะเวลาทำงาน ความแม่นยำ หรือผลิตภาพ จนกว่าจะมีผลทดสอบที่กำหนดวิธีและมีหลักฐานตรวจสอบย้อนกลับได้
4. แยกสถานะ **Proposed**, **Design Target**, **Implemented**, **Tested**, **Verified** และ **Certified** อย่างชัดเจน เอกสารข้อกำหนดหรือการทดสอบซอฟต์แวร์ไม่ใช่หลักฐานยืนยันสมรรถนะทางกายภาพหรือการรับรองตามกฎหมาย
5. บันทึกการกำหนดค่าที่ทดสอบ เวอร์ชันเซนเซอร์/โมเดล สภาพแวดล้อม ระยะเวลาทำงาน ภาระงาน ความล้มเหลว การแทรกแซงเพื่อความปลอดภัย และข้อจำกัด
6. ห้ามเปลี่ยนข้อกำหนดหรืออัตลักษณ์ผลิตภัณฑ์ที่อนุมัติแล้วโดยไม่มีการบันทึก ต้องมีเหตุผล หลักฐาน เวอร์ชัน และการทบทวน
7. การควบคุม สถานะ การแจ้งเตือน และการกู้คืนที่จำเป็นต้องใช้งานได้บนตัวผลิตภัณฑ์หรือสถานีควบคุมภายในที่เหมาะสม ไม่บังคับใช้แอปสมาร์ตโฟน

## 2. มาตรฐานการจัดสรรและการวัดขอบเขตต่อหนึ่งเครื่อง

| ผลิตภัณฑ์ | หลักการจัดสรรต่อหนึ่งเครื่อง | วิธีวัดขอบเขตที่ถูกต้อง | สถานะตัวเลข |
|---|---|---|---|
| **PUI89 AI HOME** | **หุ่นยนต์ 1 ตัวและแท่นชาร์จ 1 จุดต่อ 1 ชั้น** บ้านหลายชั้นใช้หุ่นยนต์ประจำแต่ละชั้นและประสานงานเป็นระบบเดียว | พื้นที่ใช้งานที่เข้าถึงได้และทำแผนที่ในแต่ละชั้น จำนวนห้องที่เข้าถึงได้ งานที่ทำสำเร็จ และระยะเวลาทำงาน ไม่ถือว่าขึ้นบันไดได้ | ยังไม่มีตัวเลข ตร.ม. ที่ผ่านการยืนยัน ให้กำหนดขอบเขตออกแบบรายชั้นและทดสอบในบ้านตัวอย่าง |
| **Coconut Harvest AI** | หนึ่งเครื่องรับผิดชอบแปลงสวนและกระบวนการเก็บเกี่ยวที่กำหนด | เฮกตาร์และจำนวนต้น/ทะลายที่สำรวจหรือดำเนินงานต่อวัน โดยคำนึงถึงภูมิประเทศ ระยะปลูก ระดับความแก่ เวลาเตรียมระบบ และการแทรกแซงของมนุษย์ | ยังไม่มีตัวเลขเฮกตาร์/วันที่ผ่านการยืนยัน ตัวเลขเดิม 1–5 เฮกตาร์/วันให้ยกเลิกการใช้เป็นข้ออ้าง เนื่องจากไม่มีหลักฐานรองรับ |
| **PUI89 Sentinel — หุ่นยนต์สี่ขาสำรวจและตรวจสอบพื้นที่** | หุ่นยนต์หนึ่งตัวรับผิดชอบภารกิจตรวจสอบหรือเขตพื้นที่ที่กำหนด | พื้นที่หรือระยะเส้นทางตรวจสอบต่อภารกิจ ระยะเวลาทำงาน ประเภทภูมิประเทศ งานตรวจสอบที่สำเร็จ และอัตราการกู้คืนอย่างปลอดภัย | ยังไม่มีตัวเลข ตร.ม. กิโลเมตร หรือชั่วโมงต่อการชาร์จที่ผ่านการยืนยัน ห้ามอธิบาย Sentinel ว่าเป็นผลิตภัณฑ์สถานีตรวจสัมภาระ |
| **PUI89 AI NOMAD — ผู้ช่วย AI รูปแบบกระเป๋าเดินทางถือขึ้นเครื่อง** | หนึ่งเครื่องต่อผู้เดินทางหนึ่งคนและภารกิจเกี่ยวกับสัมภาระของบุคคลนั้น | ขอบเขตภารกิจการเดินทาง เช่น ระยะเวลาการเดินทาง เหตุการณ์การจัดการสัมภาระ ความต่อเนื่องของตำแหน่งเมื่อระบบรองรับ การติดตามเหตุผิดปกติ และระยะเวลาแบตเตอรี่ | ไม่มีพื้นที่ ตร.ม. ที่เหมาะสม ตัวเลขเดิม 500–2,000 ตร.ม. ให้ยกเลิก เพราะใช้หน่วยวัดผิดกับผลิตภัณฑ์กระเป๋าเดินทาง |
| **PUI89 AI Global SUV** | ระบบ AI หนึ่งระบบต่อรถยนต์หนึ่งคัน | ขอบเขตการใช้งานและเส้นทางที่อนุญาต พร้อมระบุเขตตรวจจับด้านหน้า ด้านหลัง และด้านข้างตามสภาพแวดล้อมและความเร็ว | ยังไม่มีข้ออ้างเรื่องระยะทาง เส้นทาง ระยะตรวจจับ หรือระบบขับขี่อัตโนมัติ ผู้ขับขี่ยังคงควบคุมรถ |
| **PUI89 AI Step-Through Scooter** | ระบบ AI หนึ่งระบบต่อรถจักรยานยนต์หนึ่งคัน | ขอบเขตการใช้งานและเส้นทางที่อนุญาต พร้อมระบุเขตตรวจจับด้านหน้า/หลังตามสภาพแวดล้อมและความเร็ว | ยังไม่มีข้ออ้างเรื่องระยะทาง ระยะตรวจจับ หรือระบบขับขี่อัตโนมัติ ในขอบเขตเริ่มต้นไม่มีการควบคันเร่ง พวงมาลัย หรือเบรกโดยอัตโนมัติ |

## 3. มาตรฐานการจัดสรร AI HOME ภายในบ้าน

- หนึ่งชั้น = หุ่นยนต์ AI HOME หนึ่งตัว
- หนึ่งชั้น = แท่นชาร์จประจำชั้นหนึ่งจุด
- หุ่นยนต์ทุกตัวประสานงานผ่าน AI HOME Household Network เมื่อระบบเครือข่ายพร้อมใช้งาน
- หุ่นยนต์แต่ละตัวต้องยังคงทำงานพื้นฐานและรักษาพฤติกรรมปลอดภัยได้เมื่อเครือข่ายส่วนกลางขัดข้อง
- แต่ละชั้นมีพื้นที่ทำงานและข้อจำกัดการเข้าถึงที่ทำแผนที่แยกกัน
- ห้ามอ้างว่าปีนบันไดหรือเคลื่อนย้ายระหว่างชั้นโดยอัตโนมัติ จนกว่าจะออกแบบ ประเมินความเสี่ยง และทดสอบกลไกเฉพาะแล้ว

ตัวอย่าง: บ้าน 3 ชั้นวางแผนเป็น AI HOME 3 ตัวและแท่นชาร์จ 3 จุด บ้าน 2 ชั้นวางแผนเป็น 2 ตัวและ 2 จุด นี่เป็นข้อเสนอการจัดสรรผลิตภัณฑ์ ไม่ใช่การยืนยันว่ามีสมรรถนะดังกล่าวผ่านการทดสอบแล้ว

## 4. หลักฐานด้านเซนเซอร์และ AI ของแต่ละผลิตภัณฑ์

รายการเซนเซอร์และความสามารถ AI ต้องแยกตามผลิตภัณฑ์ Shared AI Core สามารถจัดเตรียมระบบทะเบียนเซนเซอร์ การจัดการเวลาและแหล่งที่มาของข้อมูล การตรวจคุณภาพข้อมูล ส่วนเชื่อมต่อการรวมข้อมูล ความไม่แน่นอน รายงานความล้มเหลว สัญญาการแจ้งเตือน และการประมวลผล Edge AI ที่คำนึงถึงทรัพยากรได้ แต่ไม่ได้หมายความว่าทุกผลิตภัณฑ์ติดตั้งเซนเซอร์หรือความสามารถ AI เหมือนกันแล้ว

สำหรับเซนเซอร์หรือความสามารถ AI ที่เสนอแต่ละรายการ ต้องบันทึกชนิดและหน้าที่ จำนวน ตำแหน่งติดตั้ง ทิศทาง มุมมองหรือขอบเขตการวัด อินเทอร์เฟซ วิธีสอบเทียบ อัตราการเก็บข้อมูล การตรวจสุขภาพอุปกรณ์ งาน AI แหล่งที่มาและใบอนุญาตของโมเดล ความต้องการทรัพยากร สภาพการใช้งาน จุดบอด ผลกระทบด้านความเป็นส่วนตัว เกณฑ์การยอมรับ วิธีทดสอบ ผลทดสอบ และตำแหน่งจัดเก็บหลักฐาน

มาตรฐานนี้ยังไม่อนุมัติจำนวนกล้อง LiDAR เรดาร์ ความแม่นยำของโมเดล ระยะตรวจจับ ปริมาณงาน ระยะเวลาแบตเตอรี่ หรือความสามารถพื้นที่ใด ๆ

## 5. รายงานทดสอบที่ต้องมีก่อนประกาศตัวเลข

ก่อนเผยแพร่ตัวเลขขอบเขตการทำงาน ต้องมีรายงานเฉพาะผลิตภัณฑ์ที่ระบุการกำหนดค่าของเครื่องและเวอร์ชันฮาร์ดแวร์/ซอฟต์แวร์ พื้นที่หรือเส้นทางที่ทดสอบ สภาพแวดล้อม ภาระงาน ระยะเวลาและจำนวนครั้งที่ทดสอบ งานที่สำเร็จและไม่สำเร็จ ความล้มเหลว การแทรกแซงของมนุษย์ เหตุการณ์ด้านความปลอดภัย การหยุดและการกู้คืน การใช้พลังงาน วิธีวัด ความไม่แน่นอน ข้อจำกัด ผู้ทบทวน วันที่ และลิงก์หลักฐาน

ผลทดสอบใช้ได้เฉพาะกับการกำหนดค่าและสภาพที่ทดสอบเท่านั้น ห้ามขยายผลเป็นข้ออ้างสำหรับบ้าน สวน สถานที่ ถนน ภูมิอากาศ หรือผู้ใช้ทุกประเภทโดยไม่มีหลักฐานเพิ่มเติม

## 6. ข้อกำหนดการสื่อสารต่อสาธารณะ

- **Proposed:** ใช้คำว่า “ออกแบบโดยมีเป้าหมาย...” หรือ “อยู่ระหว่างศึกษาความเป็นไปได้...”
- **Implemented:** ระบุส่วนซอฟต์แวร์ที่มีอยู่ใน repository อย่างเจาะจง
- **Tested:** ระบุการทดสอบ การกำหนดค่า และเงื่อนไข
- **Verified:** ระบุหลักฐานและขอบเขตการใช้งานที่ผ่านการยืนยัน
- **Certified:** ระบุชื่อการรับรองและหน่วยงานผู้ออกได้ต่อเมื่อได้รับจริงแล้วเท่านั้น

ห้ามใช้ภาพแนวคิด เซนเซอร์ที่วางแผนไว้ เป้าหมายการออกแบบ ข้อมูลสังเคราะห์ การทดสอบซอฟต์แวร์ หรือแผนทดสอบที่ยังไม่ได้ดำเนินการ เป็นหลักฐานยืนยันความสามารถของผลิตภัณฑ์จริง
