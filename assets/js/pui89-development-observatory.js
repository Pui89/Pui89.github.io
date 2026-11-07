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
 const bar=el("div","pui89-observatory__bar");bar.setAttribute("role","img");bar.setAttribute("aria-label",lang==="th"?"ความพร้อมเชิงพาณิชย์ "+p.score+"%":"Commercial readiness "+p.score+"%");
 const fill=el("span");fill.style.width=p.score+"%";bar.append(fill);card.append(bar);
 card.append(el("p","",t(p.summary)));
 card.append(el("span","pui89-observatory__label",lang==="th"?"เป้าหมายถัดไป":"NEXT MILESTONE"));
 card.append(el("p","",t(p.next)));
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
function updateBadges(data){
 data.projects.forEach(p=>{
  document.querySelectorAll(".pui89-progress").forEach(b=>{
   const aria=b.getAttribute("aria-label")||"";
   const labels=[t(p.name),p.id,p.repo.split("/")[1]];
   const page=document.querySelector('[data-project-id="'+p.id+'"]');
   if(page && !b.dataset.progressScore){const score=el("span","pui89-progress__score",(lang==="th"?"ความพร้อมเชิงพาณิชย์ ":"Commercial readiness ")+p.score+"%");b.append(score);b.dataset.progressScore="true";}
  });
 });
}
fetch(DATA_URL,{cache:"no-cache"}).then(r=>{if(!r.ok)throw new Error("Progress data unavailable");return r.json();}).then(data=>{
 document.querySelectorAll("[data-pui89-observatory]").forEach(root=>render(root,data));
 updateBadges(data);
}).catch(()=>document.querySelectorAll("[data-pui89-observatory]").forEach(root=>{root.textContent=lang==="th"?"ไม่สามารถโหลดข้อมูลความคืบหน้าได้ในขณะนี้":"Progress data is temporarily unavailable.";root.classList.add("pui89-observatory__empty");}));
})();