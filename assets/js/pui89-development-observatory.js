/* PUI89 Development Observatory: evidence-led project stages, without readiness scores. */
(function(){
"use strict";
const DATA_URL="/data/pui89-progress.json";
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const lang=(document.documentElement.lang||"en").toLowerCase().startsWith("th")?"th":"en";
const t=o=>typeof o==="string"?o:(o?.[lang]||o?.en||"");
const formatDate=value=>{if(!/^\d{4}-\d{2}-\d{2}$/.test(String(value||"")))return value||"";const d=new Date(value+"T12:00:00Z");return new Intl.DateTimeFormat(lang==="th"?"th-TH-u-ca-buddhist":"en-GB",{day:"numeric",month:"long",year:"numeric",timeZone:"UTC"}).format(d);};
const el=(tag,cls,txt)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(txt!==undefined)n.textContent=txt;return n;};
const stageLevel=project=>{const value=String(project.stageLabel?.en||t(project.stageLabel)).trim().toLowerCase();const levels={"proposed":1,"specified":2,"implemented":3,"simulated":4,"software-tested":5,"bench-tested":6,"field-tested":7,"validated":8,"certified":9,"unknown":10};return levels[value]||10;};
const addStageIndicator=(parent,project,compact=false)=>{const level=stageLevel(project);const stageName=t(project.stageLabel);const wrap=el("div",compact?"pui89-observatory__stage-indicator pui89-observatory__stage-indicator--level-"+level:"pui89-global-status__stage pui89-global-status__stage--level-"+level);const badge=el("span",compact?"pui89-observatory__stage-badge pui89-observatory__stage-badge--level-"+level:"pui89-global-status__stage-tab",stageName);badge.setAttribute("aria-label",(lang==="th"?"ขั้นการพัฒนา: ":"Development stage: ")+stageName);wrap.append(badge);parent.append(wrap);};
function addField(card,label,value){
 if(!value)return;
 card.append(el("span","pui89-observatory__label",label));
 card.append(el("p","",t(value)));
}
function projectCard(p){
 const card=el("article","pui89-observatory__card");
 card.append(el("h3","",p.number+". "+t(p.name)));
 card.append(el("span","pui89-observatory__label",lang==="th"?"ขั้นการพัฒนา":"DOCUMENTED DEVELOPMENT STAGE"));
 addStageIndicator(card,p,true);
 const readiness=el("div","pui89-observatory__readiness");
 const readinessHead=el("div","pui89-observatory__readiness-head");
 readinessHead.append(el("span","pui89-observatory__label",lang==="th"?"ความพร้อมโดยรวม":"OVERALL READINESS"));
 readinessHead.append(el("strong","pui89-observatory__percent",String(p.progressPercent??"—")+"%"));
 readiness.append(readinessHead);
 const track=el("div","pui89-observatory__progress-track");track.setAttribute("role","progressbar");track.setAttribute("aria-valuemin","0");track.setAttribute("aria-valuemax","100");track.setAttribute("aria-valuenow",String(p.progressPercent??0));
 const fill=el("span","pui89-observatory__progress-fill");fill.style.width=String(p.progressPercent??0)+"%";track.append(fill);readiness.append(track);card.append(readiness);
 if(p.progressAsOf)addField(card,lang==="th"?"ข้อมูลเปอร์เซ็นต์ ณ":"READINESS BASELINE",p.progressAsOf.slice(0,7));
 card.append(el("p","",t(p.summary)));
 addField(card,lang==="th"?"หลักฐานที่มี":"DOCUMENTED EVIDENCE",p.evidence);
 if(p.evidenceDate)addField(card,lang==="th"?"วันที่ทบทวนหลักฐาน":"EVIDENCE REVIEW DATE",p.evidenceDate);
 if(Array.isArray(p.evidenceLinks)&&p.evidenceLinks.length){
  card.append(el("span","pui89-observatory__label",lang==="th"?"ลิงก์หลักฐาน":"EVIDENCE LINKS"));
  const evidenceLinks=el("div","pui89-observatory__links");
  p.evidenceLinks.forEach(item=>{
   const evidenceLink=el("a","",t(item.label));
   evidenceLink.href=item.url;
   evidenceLink.target="_blank";
   evidenceLink.rel="noopener noreferrer";
   evidenceLinks.append(evidenceLink);
  });
  card.append(evidenceLinks);
 }
 addField(card,lang==="th"?"ข้อจำกัดและสิ่งที่ยังไม่ยืนยัน":"LIMITATIONS & UNVALIDATED CAPABILITIES",p.blockers);
 addField(card,lang==="th"?"เป้าหมายถัดไป":"NEXT MILESTONE",p.next);
 const links=el("div","pui89-observatory__links");
 const urls={coconut:["coconut.html","coconut-th.html"],sentinel:["sentinel.html","sentinel-th.html"],"ai-home":["home.html","home-th.html"],"ai-nomad":["nomad.html","nomad-th.html"],"robot-car":["ai-global-suv.html","ai-global-suv-th.html"],motorcycle:["ai-robot-motorcycle.html","ai-robot-motorcycle-th.html"]};
 const pair=urls[p.id]||["#","#"],page=lang==="th"?pair[1]:pair[0];
 const a=el("a","",lang==="th"?"เปิดหน้าโครงการ ↗":"Project page ↗");a.href="/"+page;links.append(a);
 const gh=el("a","","GitHub ↗");gh.href="https://github.com/"+p.repo;gh.target="_blank";gh.rel="noopener noreferrer";links.append(gh);
 if(p.history?.length){const h=p.history[p.history.length-1];links.append(el("span","pui89-observatory__empty",(lang==="th"?"บันทึกล่าสุด: ":"Latest evidence record: ")+formatDate(h.date)));}
 card.append(links);return card;
}
function renderTopStatus(project){
 const old=document.getElementById("pui89-global-project-status");
 if(old)old.remove();
 document.querySelectorAll(".pui89-progress--hero").forEach(node=>node.remove());
 const history=(project.history||[]).slice().sort((a,b)=>a.date.localeCompare(b.date));
 const last=history.length?history[history.length-1].date:"";
 const panel=el("aside","pui89-global-status");
 panel.id="pui89-global-project-status";
 panel.setAttribute("aria-label",lang==="th"?"สถานะและระดับการพัฒนาโครงการ":"Project development status and maturity");
 const name=el("div","pui89-global-status__name",t(project.name));
 panel.append(name);
 const status=el("div","pui89-global-status__status",lang==="th"?"กำลังพัฒนา":"IN DEVELOPMENT");
 panel.append(status);
 const readiness=el("div","pui89-global-status__readiness");
 const readinessHead=el("div","pui89-global-status__readiness-head");
 readinessHead.append(el("span","pui89-global-status__readiness-label",lang==="th"?"ความพร้อมโดยรวม":"OVERALL READINESS"));
 readinessHead.append(el("strong","pui89-global-status__percent",String(project.progressPercent??"—")+"%"));
 readiness.append(readinessHead);
 const track=el("div","pui89-global-status__progress-track");track.setAttribute("role","progressbar");track.setAttribute("aria-valuemin","0");track.setAttribute("aria-valuemax","100");track.setAttribute("aria-valuenow",String(project.progressPercent??0));
 const fill=el("span","pui89-global-status__progress-fill");fill.style.width=String(project.progressPercent??0)+"%";track.append(fill);readiness.append(track);panel.append(readiness);
 addStageIndicator(panel,project,false);
 const stageValue=el("span","pui89-global-status__stage-value",(lang==="th"?"ระดับ ":"LEVEL ")+stageLevel(project));
 panel.lastElementChild.append(stageValue);
 const stageHistory=(project.history||[]).slice().sort((a,b)=>a.date.localeCompare(b.date));
 const stagePeriod=stageHistory.length?stageHistory[stageHistory.length-1].period:"";
 const periodLabel=stagePeriod?new Intl.DateTimeFormat(lang==="th"?"th-TH-u-ca-buddhist":"en-GB",{month:"long",year:"numeric",timeZone:"UTC"}).format(new Date(stagePeriod+"-01T12:00:00Z")):"";
 if(periodLabel)panel.append(el("div","pui89-global-status__date",(lang==="th"?"เดือนที่บันทึกขั้น: ":"STAGE RECORDED: ")+periodLabel));
 const evidenceDate=last?new Intl.DateTimeFormat(lang==="th"?"th-TH-u-ca-buddhist":"en-GB",{day:"numeric",month:"short",year:"numeric",timeZone:"UTC"}).format(new Date(last+"T12:00:00Z")):"";
 panel.append(el("div","pui89-global-status__date",(lang==="th"?"หลักฐานล่าสุด · ":"LATEST EVIDENCE · ")+evidenceDate));
 const nav=document.querySelector("nav.nav")||document.querySelector("nav");
 if(nav)nav.insertAdjacentElement("afterend",panel);
 else {const main=document.querySelector("main");if(main)main.insertAdjacentElement("beforebegin",panel);else document.body.prepend(panel);}
}
function render(root,data){
 const portfolio=root.dataset.view==="portfolio",id=root.dataset.projectId;
 const projects=id?data.projects.filter(p=>p.id===id):data.projects;
 if(!projects.length){root.textContent=lang==="th"?"ไม่พบข้อมูลโครงการ":"Project data unavailable";return;}
 const section=el("section","pui89-observatory"+(portfolio?"":" pui89-observatory__individual"));
 section.id=portfolio?"development-observatory":"project-development-record";
 section.append(el("div","pui89-observatory__eyebrow",portfolio?"PUI89 · EVIDENCE-LED PORTFOLIO":"PUI89 · PROJECT DEVELOPMENT RECORD"));
 section.append(el("h2","",portfolio?t(data.title):t(projects[0].name)+" — "+(lang==="th"?"บันทึกการพัฒนา":"Development record")));
 section.append(el("p","pui89-observatory__intro",portfolio?(lang==="th"?"แสดงเปอร์เซ็นต์ความพร้อม ขั้นการพัฒนา หลักฐาน ข้อจำกัด และเป้าหมายถัดไปของผลิตภัณฑ์ทั้ง 6 รายการ โดยแยกความพร้อมออกจากระดับหลักฐาน":"Shows readiness percentages, documented development stages, evidence, limitations and next milestones across all six active products. Readiness and evidence maturity are reported separately."):(lang==="th"?"สรุปสถานะตามหลักฐานที่บันทึกไว้ พร้อมข้อจำกัดและงานถัดไป":"A concise record of documented work, limitations and the next milestone.")));
 const meta=el("div","pui89-observatory__meta");
 meta.append(el("span","pui89-observatory__chip",(lang==="th"?"ทบทวนข้อมูลล่าสุด: ":"Last reviewed: ")+formatDate(data.asOf)));
 meta.append(el("span","pui89-observatory__chip",lang==="th"?"ข้อมูลชุดเดียวกันสำหรับเว็บไซต์ภาษาไทยและอังกฤษ":"One shared source for English and Thai pages"));
 section.append(meta);
 if(data.maturityFramework?.note){
  const method=el("p","pui89-observatory__method",t(data.maturityFramework.note));
  section.append(method);
 }
 if(data.maturityFramework?.labels?.length){
  const labels=el("div","pui89-observatory__meta");
  labels.append(el("span","pui89-observatory__label",lang==="th"?"ป้ายสถานะตามหลักฐาน":"EVIDENCE MATURITY LABELS"));
  data.maturityFramework.labels.forEach(item=>labels.append(el("span","pui89-observatory__chip",t(item))));
  section.append(labels);
 }
 if(data.platform){
  const platform=el("article","pui89-observatory__platform");
  platform.append(el("span","pui89-observatory__eyebrow",lang==="th"?"โครงสร้างพื้นฐานร่วม":"SHARED FOUNDATION"));
  platform.append(el("h3","",t(data.platform.name)));
  platform.append(el("p","",t(data.platform.summary)));
  platform.append(el("p","",t(data.platform.next)));
  const link=el("a","",data.platform.url?(lang==="th"?"ภาพรวมสาธารณะ ↗":"Public overview ↗"):"GitHub ↗");link.href=data.platform.url||("https://github.com/"+data.platform.repo);link.target="_blank";link.rel="noopener noreferrer";platform.append(link);
  section.append(platform);
 }
 const grid=el("div","pui89-observatory__grid");projects.forEach(p=>grid.append(projectCard(p)));section.append(grid);
 // Keep the single page-authored status tile; do not inject a second floating status card.
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
 document.querySelectorAll("[data-pui89-observatory]").forEach(root=>{
  if(root.dataset.projectId){
   const project=data.projects.find(p=>p.id===root.dataset.projectId);
   if(project)renderTopStatus(project);
   // Individual project pages show only the compact status square.
   // Full evidence cards and timelines remain on the central portfolio page.
   root.remove();
  }else{
   render(root,data);
  }
 });
}).catch(()=>{
 document.querySelectorAll("[data-pui89-observatory]").forEach(root=>{
  if(root.dataset.projectId){root.remove();return;}
  root.textContent=lang==="th"?"ไม่สามารถโหลดข้อมูลการพัฒนาได้ในขณะนี้":"Development records are temporarily unavailable.";
  root.classList.add("pui89-observatory__empty");
 });
});
})();