# PUI89 Build, Repair & Grow Design Principle v1.0

**Status:** Design standard — proposed for review  
**Applies to:** All six active PUI89 products and the shared engineering foundation  
**Principle:** **Easy to Build. Easy to Repair. Built to Grow.**

> Build the simplest useful system first. Make its parts understandable, replaceable and serviceable. Add capability through verified modules instead of redesigning the whole product.

## 1. The three design commitments

### 1.1 Easy to Build
- Start with the smallest working configuration that can test the intended user need.
- Prefer documented, available, open-interface components and ordinary tools where they meet requirements.
- Separate essential functions from optional enhancements.
- Avoid custom boards, bespoke mechanisms, exotic connectors and unnecessary dependencies in early prototypes.
- Do not purchase or adopt a component until its electrical, mechanical, software, licensing, provenance and cost requirements have been reviewed.

### 1.2 Easy to Repair
- Divide the system into identifiable modules with documented boundaries.
- Make serviceable components accessible without dismantling unrelated subsystems.
- Use documented connectors, pinouts, cable labels, mounting patterns and replacement procedures.
- Provide diagnostics that identify the affected module and distinguish missing, disconnected, stale, uncalibrated and failed inputs.
- Prefer replaceable cables, mounts, sensor units, compute units and power-conversion modules where safe and practical.
- Preserve configuration, calibration and evidence during approved replacement; never silently overwrite important records.
- Design safe isolation, shutdown and recovery procedures before service work.

### 1.3 Built to Grow
- Define stable, versioned interfaces between sensors, compute, power, interaction, software and product-specific functions.
- Allow optional modules to be added or removed without breaking unrelated essential functions.
- Use adapters around vendor-specific drivers and SDKs; keep the shared software contracts vendor-neutral.
- Document compatibility, resource limits, dependencies and degraded behaviour for every extension.
- Reuse proven modules across products only where the operating environment, safety case and validation support reuse.

## 2. Modular architecture

Use these logical module groups where applicable:
1. **Perception:** cameras, ranging, environmental and other sensors.
2. **Compute:** host computer, accelerator, microcontroller and memory.
3. **Power:** input, battery, protection, conversion, monitoring and isolation.
4. **Connectivity:** wired and wireless links, with local operation not dependent on cloud access for essential functions.
5. **Mechanical:** chassis, mounts, enclosure, access panels and service fixtures.
6. **Interaction:** physical controls, displays, audio, lights and local operator station.
7. **Safety:** interlocks, protective stops, fault response and human-authority boundaries.
8. **Software:** device adapters, shared contracts, product logic, diagnostics, update and recovery.

These are logical boundaries, not a requirement to create a separate physical board or enclosure for every group. Avoid over-modularisation when it adds cost, wiring, failure points or complexity without a clear repair or upgrade benefit.

## 3. Module definition and replacement contract

For every replaceable module, record:
- module ID, product, subsystem and purpose;
- required capability and criticality;
- interface and version, connector/pinout, protocol and data format;
- voltage/current, bandwidth, compute, thermal and memory needs where applicable;
- dimensions, mounting, mass and environmental limits where applicable;
- preferred component plus at least one feasible alternative when available;
- software adapter, dependencies, licence and provenance;
- installation, calibration, diagnostic and replacement steps;
- expected failure modes, safe response and degraded capabilities;
- verification evidence, current status and known limitations.

A substitute is not automatically equivalent. Record what changes in accuracy, range, speed, reliability, environmental tolerance or safety. Do not silently replace one sensing modality with another or present a degraded capability as normal.

## 4. Graceful degradation and recovery

- Optional module missing: essential unrelated functions should continue where safe.
- Non-critical module fault: isolate the fault, show the limitation and continue only within a defined degraded mode.
- Critical sensor or safety subsystem unavailable, stale or untrusted: inhibit affected hazardous functions and enter the product-specific safe state.
- Compute overload or thermal/power limit: reduce or stop affected workloads according to a documented priority policy.
- Lost connectivity: preserve essential local operation and local alerts where technically supported.
- Repair or replacement: require inspection, configuration check, calibration where applicable, self-test and recorded return-to-service approval.

Never treat “the system still powers on” as proof that it is safe or fully functional.

## 5. Product-specific application

| Product | Initial modular design emphasis |
|---|---|
| Coconut Harvest AI | Stationary image-capture rig first; separately serviceable camera, lens/mount, lighting, compute and local operator interface. Harvesting mechanisms remain outside the initial prototype until separately specified and validated. |
| PUI89 Sentinel | Separate perception, compute, power, communications and quadruped mobility subsystems. Mobility and protective-stop design require their own hazard analysis and tests. |
| PUI89 AI HOME | Accessible indoor chassis, perception, compute, power and user-interface modules; prioritise safe low-speed operation and service access. |
| PUI89 AI NOMAD | Serviceable outdoor-capable mobility, perception, power and enclosure modules; validate weather and terrain limits rather than assuming protection. |
| PUI89 AI Global SUV | Keep AI perception and advisory computing isolated from safety-critical vehicle control. Driver authority remains; no unapproved steering, throttle, braking or vehicle-network command path. |
| PUI89 AI Step-Through Scooter | Serviceable monitoring and rider-information modules while preserving the conventional rider-controlled steering, throttle and braking architecture. Avoid distracting displays and unsafe service access. |

Shared software contracts, diagnostics, event records and selected sensor adapters may be reused. Mechanical structures, power systems, environmental protection and safety controls must remain product-specific where requirements differ.

## 6. Development levels

- **Level 1 — Basic:** minimum safe configuration that proves one essential workflow.
- **Level 2 — Standard:** improved sensing, serviceability and operational robustness after Level 1 evidence.
- **Level 3 — Advanced:** additional sensors, compute or capabilities only when user value, compatibility, cost and validation justify them.

Do not make Level 3 hardware a prerequisite for proving Level 1 value.

## 7. Design review checklist

Before approving a design or hardware purchase, ask:
- Can the first useful version be built with simpler, more available parts?
- Can a failed module be diagnosed and replaced independently?
- Are interfaces, connectors, power and mounting documented?
- Is there a realistic alternative, or an honest no-hardware/simulation fallback?
- What capability is lost or degraded when a module is unavailable?
- Are critical faults fail-safe and visible to the user?
- Can the system operate locally for essential functions?
- Can future modules be added without destabilising verified functions?
- Is the design repairable with reasonable tools, skills, time and cost?
- Is there evidence for every claim of compatibility, reliability or validation?

## 8. Evidence and maturity

Use the portfolio's evidence vocabulary: **Proposed, Specified, Implemented, Tested, Simulated, Validated, Certified, Unknown / Not tested**. A design document is not proof of a built prototype. A software test is not proof of physical reliability, safety, environmental protection or field performance.

Every module should carry an explicit state such as: Candidate; Selected, not purchased; Installed, not verified; Installed and verified; Temporary development substitute; Simulation/recorded-data only; Unavailable; or Not applicable.

## 9. Approval boundaries

This standard authorises documentation and design planning only. It does not authorise purchases, paid services, downloads, installations, physical modifications, autonomous vehicle control, safety bypasses or merging pull requests. Those actions require the appropriate separate review and approval.

---

## ภาษาไทย — หลักการออกแบบของ PUI89

**สร้างง่าย ซ่อมง่าย และต่อยอดได้**

> เริ่มจากระบบที่เล็กที่สุดซึ่งพิสูจน์ประโยชน์ได้จริง ออกแบบให้เข้าใจง่าย เปลี่ยนชิ้นส่วนและซ่อมบำรุงได้ และเพิ่มความสามารถผ่านโมดูลที่ผ่านการตรวจสอบ แทนการรื้อออกแบบระบบทั้งหมด

### 1. สร้างง่าย
- เริ่มจากต้นแบบที่เล็กที่สุดซึ่งทดสอบความต้องการสำคัญได้
- เลือกอุปกรณ์ที่หาได้ มีเอกสาร และใช้มาตรฐานการเชื่อมต่อที่เหมาะสม
- แยกฟังก์ชันจำเป็นออกจากฟังก์ชันเสริม
- หลีกเลี่ยงการออกแบบแผงวงจร กลไก หรือขั้วต่อเฉพาะโดยไม่จำเป็นในระยะแรก
- ตรวจสอบไฟฟ้า กลไก ซอฟต์แวร์ ใบอนุญาต แหล่งที่มา และต้นทุนก่อนจัดซื้อหรือเลือกใช้อุปกรณ์

### 2. ซ่อมง่าย
- แบ่งระบบเป็นโมดูลที่มีหน้าที่และขอบเขตชัดเจน
- เข้าถึงชิ้นส่วนที่ต้องซ่อมได้โดยไม่ต้องถอดระบบอื่นที่ไม่เกี่ยวข้อง
- จัดทำมาตรฐานขั้วต่อ ผังขา สายไฟ ป้ายกำกับ จุดยึด และขั้นตอนเปลี่ยนอะไหล่
- มีระบบวิเคราะห์ปัญหาที่แยกได้ว่าอุปกรณ์ขาดการเชื่อมต่อ ข้อมูลล้าสมัย ไม่ผ่านการปรับเทียบ หรือเสียหาย
- ออกแบบการตัดแยกพลังงาน การปิดระบบ และการกู้คืนอย่างปลอดภัยก่อนการซ่อม
- รักษาการตั้งค่า การปรับเทียบ และหลักฐานสำคัญระหว่างการเปลี่ยนอุปกรณ์ตามขั้นตอนที่อนุมัติ

### 3. ต่อเติมและพัฒนาได้
- กำหนดส่วนเชื่อมต่อระหว่างเซนเซอร์ หน่วยประมวลผล พลังงาน ส่วนติดต่อผู้ใช้ และซอฟต์แวร์ให้ชัดเจนและมีเวอร์ชัน
- เพิ่มหรือนำโมดูลเสริมออกได้โดยไม่ทำให้ฟังก์ชันจำเป็นอื่นเสียหาย
- แยกไดรเวอร์หรือ SDK เฉพาะผู้ผลิตไว้ใน adapter และใช้สัญญาข้อมูลกลางที่ไม่ผูกกับผู้ผลิต
- ระบุความเข้ากันได้ ข้อจำกัด และพฤติกรรมเมื่ออุปกรณ์ไม่พร้อม
- นำโมดูลที่พิสูจน์แล้วกลับมาใช้กับผลิตภัณฑ์อื่นเฉพาะเมื่อสภาพแวดล้อมและข้อกำหนดความปลอดภัยรองรับ

### 4. สถาปัตยกรรมโมดูล
จัดกลุ่มตามหน้าที่ ได้แก่ การรับรู้ข้อมูล การประมวลผล พลังงาน การเชื่อมต่อ โครงสร้างกลไก การโต้ตอบ ความปลอดภัย และซอฟต์แวร์ ทั้งหมดเป็นขอบเขตเชิงตรรกะ ไม่จำเป็นต้องแยกเป็นแผงวงจรหรือกล่องจริงทุกส่วน หลีกเลี่ยงการแบ่งโมดูลมากเกินไปจนเพิ่มต้นทุน สายไฟ จุดเสีย หรือความซับซ้อนโดยไม่เกิดประโยชน์ในการซ่อมหรืออัปเกรด

### 5. การทำงานเมื่ออุปกรณ์ขัดข้อง
- โมดูลเสริมไม่พร้อม: ฟังก์ชันอื่นที่ไม่เกี่ยวข้องควรทำงานต่อได้เมื่อปลอดภัย
- โมดูลที่ไม่สำคัญขัดข้อง: แจ้งข้อจำกัดและทำงานต่อได้เฉพาะในโหมดลดความสามารถที่กำหนดไว้
- เซนเซอร์หรือระบบความปลอดภัยที่สำคัญขัดข้อง ข้อมูลล้าสมัย หรือไม่น่าเชื่อถือ: ระงับฟังก์ชันเสี่ยงที่เกี่ยวข้องและเข้าสู่สถานะปลอดภัยเฉพาะผลิตภัณฑ์
- การเชื่อมต่อขาดหาย: รักษาฟังก์ชันพื้นฐานในพื้นที่และการแจ้งเตือนภายในเมื่อเทคโนโลยีรองรับ
- หลังซ่อมหรือเปลี่ยน: ตรวจสอบการติดตั้ง การตั้งค่า การปรับเทียบ และทดสอบก่อนอนุญาตให้กลับมาใช้งาน

การที่ระบบเปิดติดไม่ได้หมายความว่าระบบปลอดภัยหรือทำงานครบถ้วน

### 6. การประยุกต์ใช้กับผลิตภัณฑ์ทั้งหก
- **Coconut Harvest AI:** เริ่มจากชุดถ่ายภาพแบบติดตั้งอยู่กับที่ แยกกล้อง เลนส์ จุดยึด แสง หน่วยประมวลผล และส่วนติดต่อผู้ใช้ให้ดูแลได้ง่าย
- **Sentinel:** แยกระบบรับรู้ข้อมูล ประมวลผล พลังงาน สื่อสาร และการเคลื่อนที่แบบสี่ขา พร้อมวิเคราะห์อันตรายและทดสอบระบบหยุดป้องกันแยกต่างหาก
- **AI HOME:** เน้นโครงสร้างภายในบ้านที่เข้าถึงเพื่อซ่อมได้ เซนเซอร์ หน่วยประมวลผล พลังงาน และส่วนติดต่อผู้ใช้
- **AI NOMAD:** เน้นโมดูลการเคลื่อนที่กลางแจ้ง การรับรู้ พลังงาน และกล่องป้องกัน โดยต้องทดสอบขอบเขตสภาพอากาศและพื้นผิวจริง
- **AI Global SUV:** แยกระบบ AI รับรู้และให้คำแนะนำออกจากระบบควบคุมรถที่มีความสำคัญต่อความปลอดภัย ผู้ขับขี่ยังคงมีอำนาจควบคุม
- **AI Step-Through Scooter:** ออกแบบโมดูลตรวจสอบและแสดงข้อมูลให้ซ่อมได้ โดยไม่รบกวนระบบบังคับเลี้ยว คันเร่ง และเบรกที่ผู้ขับขี่ควบคุมเอง

### 7. ระดับการพัฒนา
- **ระดับพื้นฐาน:** ระบบขั้นต่ำที่ปลอดภัยและพิสูจน์ขั้นตอนใช้งานสำคัญได้
- **ระดับมาตรฐาน:** เพิ่มการรับรู้ ความสะดวกในการซ่อม และความทนทานหลังมีหลักฐานจากระดับพื้นฐาน
- **ระดับขั้นสูง:** เพิ่มเซนเซอร์หรือกำลังประมวลผลเมื่อมีเหตุผลด้านประโยชน์ ความเข้ากันได้ ต้นทุน และการตรวจสอบรองรับ

### 8. ขอบเขตหลักฐานและการอนุมัติ
เอกสารนี้เป็นมาตรฐานการออกแบบและการวางแผนเท่านั้น ไม่ใช่หลักฐานว่ามีต้นแบบจริงหรือผ่านการทดสอบแล้ว และไม่อนุมัติการจัดซื้อ ดาวน์โหลด ติดตั้ง ดัดแปลงฮาร์ดแวร์ หรือรวม Pull Request โดยอัตโนมัติ ต้องผ่านการตรวจสอบและอนุมัติแยกต่างหาก
