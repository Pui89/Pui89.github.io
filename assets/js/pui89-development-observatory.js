/* PUI89 Development Observatory: render a shared evidence-led portfolio record. */
(function(){
"use strict";
const DATA_URL="/data/pui89-progress.json";
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const lang=(document.documentElement.lang||"en").toLowerCase().startsWith("th")?"th":"en";
const t=o=>typeof o==="string"?o:(o?.[lang]||o?.en||"");
const el=(tag,cls,txt)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(txt!==undefined)n.textContent=txt;return n;};
function record(p,history){
 const card=el("article","pui89-observatory__card");
 card.append(el("h3","",p.number+". "+t(p.name)));
 const line=el("div","pui89-observatory__scoreline");
 line.append(el("span","pui89-observatory__score",p.score+"%"),el("span","pui89-observatory__stage",t(p.stageLabel)));
 card.append(line);
 const maturity=el("div","pui89-observatory__maturity");
 maturity.append(el("span","pui89-observatory__label",lang==="th"?"ระดับวุฒิภาวะ":"DEVELOPMENT MATURITY"));
 maturity.append(el("strong","pui89-observatory__maturity-stage","L"+p.maturityLevel+" · "+t(p.maturityLabel)));
 const indicators=el("div","pui89-observatory__meta");
 [["Engineering strength",p.engineeringStrength,"ความแข็งแรงทางวิศวกรรม"],["Evidence confidence",p.evidenceConfidence,"ความเชื่อมั่นของหลักฐาน"],["Implementation level",p.implementationLevel,"ระดับการพัฒนาใช้งาน"]].forEach(([enKey,value,thKey])=>{
   const item=el("div","pui89-observatory__indicator");
   item.append(el("strong","",lang==="th"?thKey:enKey));
   item.append(el("p","",t(value)));
   indicators.append(item);
 });
 maturity.append(indicators);
 maturity.append(el("span","pui89-observatory__label",lang==="th"?"เป้าหมายยกระดับวุฒิภาวะ":"NEXT MATURITY GATE"));
 maturity.append(el("p","",t(p.nextMaturityMilestone)));
 card.append(maturity);

 const bar=el("div","pui89-observatory__bar");bar.setAttribute("role","img");bar.setAttribute("aria-label",lang==="th"?"ความพร้อมเชิงพาณิชย์ "+p.score+"%":"Commercial readiness "+p.score+"%");
 const fill=el("span");fill.style.width=p.score+"%";bar.append(fill);card.append(bar);
 card.append(el("p","",t(p.summary)));
 if(p.liveReport){
  const live=el("div","pui89-observatory__meta");
  live.append(el("span","pui89-observatory__chip",(lang==="th"?"หลักฐานครอบคลุม ":"Evidence coverage ")+p.liveReport.evidence_coverage_percent+"%"));
  live.append(el("span","pui89-observatory__chip",(lang==="th"?"ความเชื่อมั่นจากความครอบคลุม: ":"Coverage-derived confidence: ")+p.liveReport.evidence_confidence_proxy));
  live.append(el("span","pui89-observatory__chip",(lang==="th"?"การเชื่อมต่อ AI Core ที่ยืนยันแล้ว: ":"Shared AI Core verified: ")+p.liveReport.shared_ai_core_integration_percent+"%"));
  live.append(el("span","pui89-observatory__chip",(lang==="th"?"ตรวจล่าสุด: ":"Report date: ")+p.liveReport.review_date));
  live.append(el("span","pui89-observatory__chip",(lang==="th"?"รูปแบบความเสี่ยงที่ตรวจพบ: ":"Secret-pattern findings: ")+p.liveReport.security_review.secret_pattern_findings.length));
  card.append(live);
 }
 card.append(el("span","pui89-observatory__label",lang==="th"?"เป้าหมายถัดไป":"NEXT MILESTONE"));
 card.append(el("p","",lang==="en"&&p.liveReport?p.liveReport.next_milestone:t(p.next)));
 card.append(el("span","pui89-observatory__label",lang==="th"?"หลักฐานและข้อจำกัด":"EVIDENCE & LIMITATIONS"));
 card.append(el("p","",t(p.evidence)));
 card.append(el("span","pui89-observatory__label",lang==="th"?"สิ่งที่ยังต้องทำ":"REMAINING BLOCKERS"));
 card.append(el("p","",t(p.blockers)));
 const links=el("div","pui89-observatory__links");
 const urls={coconut:["coconut.html","coconut-th.html"],"flood-rescue":["flood-rescue.html","flood-rescue-th.html"],sentinel:["screening.html","screening-th.html"],"ai-home":["home.html","home-th.html"],"ai-nomad":["homeguard.html","homeguard-th.html"],"robot-car":["ai-robot-car.html","ai-robot-car-th.html"],motorcycle:["ai-robot-motorcycle.html","ai-robot-motorcycle-th.html"]};
 const pair=urls[p.id]||["#","#"];const page=lang==="th"?pair[1]:pair[0];
 const a=el("a","",lang==="th"?"เปิดหน้าโครงการ ↗":"Project page ↗");a.href="/"+page;links.append(a);
 const gh=el("a","", "GitHub ↗");gh.href="https://github.com/"+p.repo;gh.target="_blank";gh.rel="noopener noreferrer";links.append(gh);
 const hist=history||p.history||[];
 if(hist.length){const latest=hist[hist.length-1];links.append(el("span","pui89-observatory__empty",(lang==="th"?"บันทึกล่าสุด: ":"Latest record: ")+latest.date));}
 card.append(links);return card;
}
function render(root,data){
 const isPortfolio=root.dataset.view==="portfolio";
 const projectId=root.dataset.projectId;
 const projects=projectId?data.projects.filter(p=>p.id===projectId):data.projects;
 if(!projects.length){root.textContent=lang==="th"?"ไม่พบข้อมูลโครงการ":"Project data unavailable";return;}
 const section=el("section","pui89-observatory"+(isPortfolio?"":" pui89-observatory__individual"));
 section.id=isPortfolio?"development-observatory":"project-progress-history";
 section.append(el("div","pui89-observatory__eyebrow",isPortfolio?"PUI89 · PORTFOLIO INTELLIGENCE":"PUI89 · PROJECT DEVELOPMENT RECORD"));
 section.append(el("h2","",isPortfolio?t(data.title):t(projects[0].name)+" — "+(lang==="th"?"ประวัติการพัฒนา":"Development history")));
 section.append(el("p","pui89-observatory__intro",isPortfolio?(lang==="th"?"ติดตามความพร้อมเชิงพาณิชย์ หลักฐาน เป้าหมายถัดไป และประวัติรายเดือน/รายปีของทั้ง 7 โครงการ":"Track commercial readiness, evidence, next milestones and monthly/yearly history across all seven projects."):t(data.method)));
 const meta=el("div","pui89-observatory__meta");
 meta.append(el("span","pui89-observatory__chip",(lang==="th"?"วันที่ทบทวนล่าสุด: ":"Last reviewed: ")+data.asOf));
 meta.append(el("span","pui89-observatory__chip",lang==="th"?"ข้อมูลจากแหล่งเดียวกันทั้งเว็บ EN/TH":"One shared source for English and Thai pages"));
 section.append(meta);
 
 if(data.platform){
  const platform=el("article","pui89-observatory__platform");
  platform.append(el("span","pui89-observatory__eyebrow",lang==="th"?"แพลตฟอร์มพื้นฐานร่วม":"SHARED FOUNDATION"));
  platform.append(el("h3","",t(data.platform.name)));
  platform.append(el("div","pui89-observatory__maturity-stage","L"+data.platform.maturityLevel+" · "+t(data.platform.maturityLabel)));
  const pmeta=el("div","pui89-observatory__meta");
  [["Engineering strength",data.platform.engineeringStrength,"ความแข็งแรงทางวิศวกรรม"],["Evidence confidence",data.platform.evidenceConfidence,"ความเชื่อมั่นของหลักฐาน"],["Implementation level",data.platform.implementationLevel,"ระดับการพัฒนาใช้งาน"]].forEach(([enKey,value,thKey])=>{const item=el("div","pui89-observatory__indicator");item.append(el("strong","",lang==="th"?thKey:enKey));item.append(el("p","",t(value)));pmeta.append(item);});
  platform.append(pmeta);platform.append(el("p","",t(data.platform.next)));
  const link=el("a","","GitHub ↗");link.href="https://github.com/"+data.platform.repo;link.target="_blank";link.rel="noopener noreferrer";platform.append(link);
  section.append(platform);
 }
const grid=el("div","pui89-observatory__grid");
 projects.forEach(p=>grid.append(record(p,p.history)));section.append(grid);
 const timeline=el("div","pui89-observatory__timeline");timeline.append(el("h3","",lang==="th"?"ประวัติรายเดือน":"Monthly development history"));
 const entries=[];
 projects.forEach(p=>(p.history||[]).forEach(h=>entries.push({p,h})));
 entries.sort((a,b)=>a.h.date.localeCompare(b.h.date));
 if(entries.length){const list=el("div","pui89-observatory__timeline-list");entries.forEach(({p,h})=>{const item=el("div","pui89-observatory__entry");item.append(el("strong","",h.period+" · "+t(p.name)+" · "+h.score+"%"));item.append(el("small","",t(h.note)));list.append(item);});timeline.append(list);}
 else timeline.append(el("p","pui89-observatory__empty",lang==="th"?"ยังไม่มีบันทึก":"No records yet."));
 timeline.append(el("h3","",lang==="th"?"ภาพรวมรายปี":"Yearly overview"));
 const years=[...new Set(entries.map(x=>x.h.date.slice(0,4)))].sort();
 years.forEach(year=>{const e=el("div","pui89-observatory__year");const count=entries.filter(x=>x.h.date.startsWith(year)).length;e.append(el("strong","",year));e.append(el("p","",lang==="th"?("มีบันทึกหลักฐาน "+count+" รายการในปีนี้"):count+" evidence record(s) recorded this year."));timeline.append(e);});
 if(!years.length)timeline.append(el("p","pui89-observatory__empty",lang==="th"?"ยังไม่มีข้อมูลรายปี":"No yearly records yet."));
 section.append(timeline);
 const method=el("div","pui89-observatory__method");method.append(el("strong","",lang==="th"?"วิธีคิดคะแนนและความหมายของ 100%":"Scoring method and the meaning of 100%"));method.append(el("p","",t(data.method)));
 const weights=el("p","",data.weights.map(w=>t(w)+" ("+w.weight+"%)").join(" · "));method.append(weights);
 method.append(el("p","",lang==="th"?"หมายเหตุ: มีเพียงค่าฐานเดือนพฤศจิกายน 2026 ในขณะนี้ ไม่มีการสร้างข้อมูลเดือนก่อนหน้าหรืออนาคตขึ้นเอง วันที่เริ่มโครงการจะแสดงเมื่อมีหลักฐานยืนยัน":"Note: November 2026 is the first recorded baseline. Earlier or future monthly entries are not invented. Project start dates will be shown only when verified."));
 section.append(method);
 root.replaceChildren(section);
}
function setScore(badge,label){
 if(!badge)return;
 let score=badge.querySelector(".pui89-progress__score");
 if(!score){score=el("span","pui89-progress__score");badge.append(score);}
 score.textContent=label;
 badge.dataset.progressScore="true";
}
function updateBadges(data){
 const projectRoot=document.querySelector('[data-view="project"][data-project-id]');
 if(projectRoot){
  const p=data.projects.find(item=>item.id===projectRoot.dataset.projectId);
  setScore(document.querySelector(".pui89-progress--hero"),p?(lang==="th"?"ความพร้อมเชิงพาณิชย์ ":"Commercial readiness ")+p.score+"%":"");
 }
 const portfolioRoot=document.querySelector('[data-view="portfolio"]');
 if(portfolioRoot){
  const cards=[...document.querySelectorAll("#projects article")];
  data.projects.forEach((p,index)=>{
   const badge=cards[index]?.querySelector(".pui89-progress--card");
   if(badge)setScore(badge,(lang==="th"?"พร้อมเชิงพาณิชย์ ":"Commercial readiness ")+p.score+"%");
  });
 }
}
async function hydrate(data){
 await Promise.all(data.projects.map(async p=>{
  const base="https://raw.githubusercontent.com/"+p.repo+"/main/docs/";
  try{
   const response=await fetch(base+"project-health-latest.json",{cache:"no-store"});
   if(response.ok){
    const report=await response.json();p.liveReport=report;p.score=report.progress_percent;
    p.stageLabel=report.progress_percent>=75?{en:"Advanced evidence stage",th:"หลักฐานอยู่ในขั้นก้าวหน้า"}:report.progress_percent>=50?{en:"Developing evidence stage",th:"กำลังพัฒนาหลักฐาน"}:report.progress_percent>=25?{en:"Foundation and prototype stage",th:"วางรากฐานและต้นแบบ"}:{en:"Early foundation stage",th:"ระยะวางรากฐานเริ่มต้น"};
    if(report.review_date&&report.review_date>data.asOf)data.asOf=report.review_date;
   }
  }catch(_){ }
  try{
   const response=await fetch(base+"project-progress-history.json",{cache:"no-store"});
   if(response.ok){
    const history=await response.json();
    if(Array.isArray(history)&&history.length){const live=history.map(h=>({date:h.date,period:h.date.slice(0,7),score:h.score_percent,note:{en:"Evidence-led "+h.cadence+" review; coverage "+h.evidence_coverage_percent+"%.",th:"บันทึกทบทวนตามหลักฐาน รอบ"+h.cadence+" ครอบคลุมหลักฐาน "+h.evidence_coverage_percent+"%"}}));const baseline=p.history||[];p.history=[...baseline.filter(b=>!live.some(h=>h.date===b.date)),...live].sort((a,b)=>a.date.localeCompare(b.date));}
   }
  }catch(_){ }
 }));
 return data;
}
fetch(DATA_URL,{cache:"no-cache"}).then(r=>{if(!r.ok)throw new Error("Progress data unavailable");return r.json();}).then(hydrate).then(data=>{
 document.querySelectorAll("[data-pui89-observatory]").forEach(root=>render(root,data));
 updateBadges(data);
}).catch(()=>document.querySelectorAll("[data-pui89-observatory]").forEach(root=>{root.textContent=lang==="th"?"ไม่สามารถโหลดข้อมูลความคืบหน้าได้ในขณะนี้":"Progress data is temporarily unavailable.";root.classList.add("pui89-observatory__empty");}));
})();