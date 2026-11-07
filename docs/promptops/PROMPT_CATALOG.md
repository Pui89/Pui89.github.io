# PUI89 PromptOps — Prompt Catalog

**Version:** 0.1.0  
**Date:** 8 November 2026  
**Status:** Draft for human review

# English

| ID | Prompt | Intended use | Main output |
|---|---|---|---|
| P89-01 | Evidence reviewer | Check claims against source evidence | Evidence-backed findings and unknowns |
| P89-02 | Systems architect | Review boundaries, interfaces and contracts | Architecture risks and staged design |
| P89-03 | Security reviewer | Review repository and workflow risks | Prioritised security findings |
| P89-04 | Test engineer | Design low-cost deterministic tests | Test matrix and reproducible commands |
| P89-05 | AI evaluation researcher | Plan valid model evaluation | Metrics, splits, uncertainty and limits |
| P89-06 | Robotics safety reviewer | Review simulation/advisory safety cases | Hazard analysis and safe holds |
| P89-07 | Data and model governance reviewer | Check provenance, rights and supply-chain details | Approval status and missing evidence |
| P89-08 | Failure analyst | Investigate defects without hiding failures | Root-cause hypotheses and corrective tests |
| P89-09 | Project maturity assessor | Score evidence-backed maturity | Transparent rubric and evidence gaps |
| P89-10 | Bilingual technical editor | Produce consistent English/Thai materials | Parallel, technically faithful text |

# ภาษาไทย

| ID | Prompt | วัตถุประสงค์ | ผลลัพธ์หลัก |
|---|---|---|---|
| P89-01 | ผู้ตรวจสอบหลักฐาน | ตรวจสอบข้อกล่าวอ้างกับหลักฐานต้นทาง | ผลตรวจสอบและสิ่งที่ยังไม่ทราบ |
| P89-02 | สถาปนิกระบบ | ตรวจสอบขอบเขต ส่วนเชื่อมต่อ และสัญญาข้อมูล | ความเสี่ยงและแผนสถาปัตยกรรม |
| P89-03 | ผู้ตรวจสอบความปลอดภัย | ตรวจสอบ Repository และ Workflow | รายการความเสี่ยงตามลำดับความสำคัญ |
| P89-04 | วิศวกรทดสอบ | ออกแบบการทดสอบที่ทำซ้ำได้และประหยัด | ตารางทดสอบและคำสั่งที่ใช้ได้จริง |
| P89-05 | นักวิจัยประเมิน AI | วางแผนประเมินโมเดลอย่างถูกต้อง | ตัวชี้วัด การแบ่งข้อมูล และข้อจำกัด |
| P89-06 | ผู้ตรวจสอบความปลอดภัยหุ่นยนต์ | ตรวจสอบความปลอดภัยใน Simulation/Advisory | การวิเคราะห์อันตรายและเงื่อนไขหยุด |
| P89-07 | ผู้ตรวจสอบธรรมาภิบาลข้อมูลและโมเดล | ตรวจสอบที่มา สิทธิ์ และห่วงโซ่อุปทาน | สถานะการอนุมัติและหลักฐานที่ขาด |
| P89-08 | นักวิเคราะห์ความล้มเหลว | วิเคราะห์ข้อผิดพลาดโดยไม่ปกปิดผลล้มเหลว | สมมติฐานสาเหตุและการทดสอบแก้ไข |
| P89-09 | ผู้ประเมินระดับความพร้อม | ประเมินจากหลักฐานตามเกณฑ์ที่เปิดเผย | คะแนนพร้อมหลักฐานและช่องว่าง |
| P89-10 | บรรณาธิการเทคนิคสองภาษา | จัดทำเอกสารภาษาอังกฤษและภาษาไทยให้สอดคล้อง | เนื้อหาคู่ภาษาที่รักษาความหมายทางเทคนิค |

## Usage rules / กติกาการใช้งาน

- Use only the prompt relevant to the task. / ใช้เฉพาะ Prompt ที่ตรงกับงาน
- Attach evidence references; do not paste secrets or unnecessary personal data. / แนบแหล่งหลักฐาน ห้ามใส่ความลับหรือข้อมูลส่วนบุคคลที่ไม่จำเป็น
- Treat outputs as recommendations until independently verified. / ถือผลลัพธ์เป็นข้อเสนอจนกว่าจะตรวจสอบยืนยัน
- No physical actuation, paid services, automatic merges or unapproved changes. / ห้ามสั่งงานฮาร์ดแวร์ ใช้บริการเสียเงิน รวม PR อัตโนมัติ หรือแก้ไขโดยไม่ได้รับอนุญาต
