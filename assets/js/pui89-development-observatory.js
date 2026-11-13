/* PUI89 Development Observatory: evidence-led project stages, without readiness scores. */
(function(){
"use strict";
const DATA_URL="/data/pui89-progress.json";
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const lang=(document.documentElement.lang||"en").toLowerCase().startsWith("th")?"th":"en";
const t=o=>typeof o==="string"?o:(o?.[lang]||o?.en||"");
const formatDate=value=>{if(!/^\d{4}-\d{2}-\d{2}$/.test(String(value||"")))return value||"";const d=new Date(value+"T12:00:00Z");return new Intl.DateTimeFormat(lang==="th"?"th-TH-u-ca-buddhist":"en-GB",{day:"numeric",month:"long",year:"numeric",timeZone:"UTC"}).format(d);};
const el=(tag,cls,txt)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(txt!==undefined)n.textContent=txt;return n;};
function addField(card,label,value){
 if(!value)return;
 card.append(el("span","pui89-observatory__label",label));
 card.append(el("p","",t(value)));
}
function projectCard(p,framework){
 const card=el("article","pui89-observatory__card");
 card.append(el("h3","",p.number+". "+t(p.name)));
 card.append(el("span","pui89-observatory__label",lang==="th"?"ขั้นการพัฒนา":"DOCUMENTED DEVELOPMENT STAGE"));
 card.append(el("strong","pui89-observatory__stage",t(p.stageLabel)));
 if(Number.isInteger(p.maturityLevel)&&p.maturityLevel>=1&&p.maturityLevel<=7&&framework?.levels){
  const maturity=el("div","pui89-observatory__maturity");
  maturity.append(el("span","pui89-observatory__label",lang==="th"?"ระดับวุฒิภาวะการพัฒนา":"DEVELOPMENT MATURITY"));
  const current=framework.levels.find(x=>x.level===p.maturityLevel);
  maturity.append(el("strong","pui89-observatory__maturity-stage",(lang==="th"?"ระดับ ":"Level ")+p.maturityLevel+" / 7 · "+(lang==="th"?current?.th:current?.en)));
  const steps=el("div","pui89-observatory__maturity-steps");
  framework.levels.forEach(x=>{const step=el("span",x.level<=p.maturityLevel?"is-reached":"");step.setAttribute("aria-label",(lang==="th"?"ระดับ ":"Level ")+x.level+": "+(lang==="th"?x.th:x.en));steps.append(step);});
  maturity.append(steps);
  maturity.append(el("p","pui89-observatory__empty",lang==="th"?framework.note?.th:framework.note?.en));
  card.append(maturity);
 }
 card.append(el("p","",t(p.summary)));
 if(p.commercialReadiness&&Number.isInteger(p.commercialReadiness.percent)&&p.commercialReadiness.percent>=0&&p.commercialReadiness.percent<=100){
  const scoreline=el("div","pui89-observatory__scoreline");
  scoreline.append(el("span","pui89-observatory__label",lang==="th"?"ความพร้อมเชิงพาณิชย์โดยประมาณ":"COMMERCIAL READINESS ESTIMATE"));
  scoreline.append(el("strong","pui89-observatory__score",p.commercialReadiness.percent+"%"));
  card.append(scoreline);
  const bar=el("div","pui89-observatory__bar");
  bar.setAttribute("role","progressbar");
  bar.setAttribute("aria-label",lang==="th"?"ความพร้อมเชิงพาณิชย์โดยประมาณ":"Commercial readiness estimate");
  bar.setAttribute("aria-valuemin","0");bar.setAttribute("aria-valuemax","100");
  bar.setAttribute("aria-valuenow",String(p.commercialReadiness.percent));
  const fill=el("span","");fill.style.width=p.commercialReadiness.percent+"%";bar.append(fill);card.append(bar);
  card.append(el("p","pui89-observatory__empty",(lang==="th"?"ค่าฐาน ณ ":"Baseline: ")+formatDate(p.commercialReadiness.reviewedOn)));
 }
 addField(card,lang==="th"?"หลักฐานที่มี":"DOCUMENTED EVIDENCE",p.evidence);
 addField(card,lang==="th"?"ข้อจำกัดและสิ่งที่ยังไม่ยืนยัน":"LIMITATIONS & UNVALIDATED CAPABILITIES",p.blockers);
 addField(card,lang==="th"?"เป้าหมายถัดไป":"NEXT MILESTONE",p.next);
 const links=el("div","pui89-observatory__links");
 const urls={coconut:["coconut.html","coconut-th.html"],"flood-rescue":["flood-rescue.html","flood-rescue-th.html"],sentinel:["screening.html","screening-th.html"],"ai-home":["home.html","home-th.html"],"ai-nomad":["homeguard.html","homeguard-th.html"],"robot-car":["ai-robot-car.html","ai-robot-car-th.html"],motorcycle:["ai-robot-motorcycle.html","ai-robot-motorcycle-th.html"]};
 const pair=urls[p.id]||["#","#"],page=lang==="th"?pair[1]:pair[0];
 const a=el("a","",lang==="th"?"เปิดหน้าโครงการ ↗":"Project page ↗");a.href="/"+page;links.append(a);
 const gh=el("a","","GitHub ↗");gh.href="https://github.com/"+p.repo;gh.target="_blank";gh.rel="noopener noreferrer";links.append(gh);
 if(p.history?.length){const h=p.history[p.history.length-1];links.append(el("span","pui89-observatory__empty",(lang==="th"?"บันทึกล่าสุด: ":"Latest evidence record: ")+formatDate(h.date)));}
 card.append(links);return card;
}
function render(root,data){
 const portfolio=root.dataset.view==="portfolio",id=root.dataset.projectId;
 const projects=id?data.projects.filter(p=>p.id===id):data.projects;
 if(!projects.length){root.textContent=lang==="th"?"ไม่พบข้อมูลโครงการ":"Project data unavailable";return;}
 const section=el("section","pui89-observatory"+(portfolio?"":" pui89-observatory__individual"));
 section.id=portfolio?"development-observatory":"project-development-record";
 section.append(el("div","pui89-observatory__eyebrow",portfolio?"PUI89 · EVIDENCE-LED PORTFOLIO":"PUI89 · PROJECT DEVELOPMENT RECORD"));
 section.append(el("h2","",portfolio?t(data.title):t(projects[0].name)+" — "+(lang==="th"?"บันทึกการพัฒนา":"Development record")));
 section.append(el("p","pui89-observatory__intro",portfolio?(lang==="th"?"แสดงขั้นการพัฒนาที่มีหลักฐานรองรับ ข้อจำกัด และเป้าหมายถัดไปของทั้ง 7 โครงการ โดยไม่ใช้คะแนนความพร้อมเชิงพาณิชย์":"Documented development stages, evidence, limitations and next milestones across all seven projects. No commercial-readiness percentages are used."):(lang==="th"?"สรุปสถานะตามหลักฐานที่บันทึกไว้ พร้อมข้อจำกัดและงานถัดไป":"A concise record of documented work, limitations and the next milestone.")));
 const meta=el("div","pui89-observatory__meta");
 meta.append(el("span","pui89-observatory__chip",(lang==="th"?"ทบทวนข้อมูลล่าสุด: ":"Last reviewed: ")+formatDate(data.asOf)));
 meta.append(el("span","pui89-observatory__chip",lang==="th"?"ข้อมูลชุดเดียวกันสำหรับเว็บไซต์ภาษาไทยและอังกฤษ":"One shared source for English and Thai pages"));
 section.append(meta);
 if(data.readinessBaseline){
  const method=el("p","pui89-observatory__method",t(data.readinessBaseline.definition)+" "+t(data.readinessBaseline.note));
  section.append(method);
 }
 if(data.platform){
  const platform=el("article","pui89-observatory__platform");
  platform.append(el("span","pui89-observatory__eyebrow",lang==="th"?"โครงสร้างพื้นฐานร่วม":"SHARED FOUNDATION"));
  platform.append(el("h3","",t(data.platform.name)));
  platform.append(el("p","",t(data.platform.summary)));
  platform.append(el("p","",t(data.platform.next)));
  const link=el("a","","GitHub ↗");link.href="https://github.com/"+data.platform.repo;link.target="_blank";link.rel="noopener noreferrer";platform.append(link);
  section.append(platform);
 }
 const grid=el("div","pui89-observatory__grid");projects.forEach(p=>grid.append(projectCard(p,data.maturityFramework)));section.append(grid);
 const timeline=el("div","pui89-observatory__timeline");
 timeline.append(el("h3","",lang==="th"?"ประวัติบันทึกหลักฐาน":"Evidence record history"));
 const entries=[];projects.forEach(p=>(p.history||[]).forEach(h=>entries.push({p,h})));
 entries.sort((a,b)=>a.h.date.localeCompare(b.h.date));
 if(entries.length){
  const list=el("div","pui89-observatory__timeline-list");
  entries.forEach(({p,h})=>{const item=el("div","pui89-observatory__entry");item.append(el("strong","",h.date+" · "+t(p.name)));item.append(el("small","",t(h.note)));list.append(item);});
  timeline.append(list);
 }else timeline.append(el("p","pui89-observatory__empty",lang==="th"?"ยังไม่มีบันทึก":"No records yet."));
 section.append(timeline);
 root.replaceChildren(section);
}
fetch(DATA_URL,{cache:"no-cache"}).then(r=>{if(!r.ok)throw new Error("Progress data unavailable");return r.json();}).then(data=>{
 document.querySelectorAll("[data-pui89-observatory]").forEach(root=>render(root,data));
}).catch(()=>document.querySelectorAll("[data-pui89-observatory]").forEach(root=>{
 root.textContent=lang==="th"?"ไม่สามารถโหลดข้อมูลการพัฒนาได้ในขณะนี้":"Development records are temporarily unavailable.";
 root.classList.add("pui89-observatory__empty");
}));
})();