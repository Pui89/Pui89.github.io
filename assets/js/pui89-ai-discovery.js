(() => {
  "use strict";
  const projects = [
    {name:"Coconut Harvest AI", href:"coconut.html", th:"Coconut Harvest AI", thHref:"coconut-th.html", desc:"Agricultural vision, coconut maturity assessment, harvest planning and robotic assistance.", terms:"coconut agriculture palm maturity fruit harvest orchard computer vision มะพร้าว เกษตร สวน การเก็บเกี่ยว ผลผลิต ระยะสุก หุ่นยนต์เกษตร"},
    {name:"Extreme Flood Rescue AI", href:"flood-rescue.html", th:"Extreme Flood Rescue AI", thHref:"flood-rescue-th.html", desc:"Flood scene understanding, terrain and drainage evidence, rescue reconnaissance and simulation-first robotics.", terms:"flood water rescue terrain drainage lidar point cloud mapping boat emergency floodwater น้ำท่วม กู้ภัย ระบายน้ำ ภูมิประเทศ แผนที่ ไลด้าร์ เรือ"},
    {name:"Multimodal Narcotics Screening AI", href:"screening.html", th:"Multimodal Narcotics Screening AI", thHref:"screening-th.html", desc:"Multimodal inspection concepts with provenance, uncertainty and authorised human review.", terms:"screening inspection multimodal image x-ray sensor provenance uncertainty human review narcotics ตรวจสอบ คัดกรอง ภาพ เอกซเรย์ เซนเซอร์ หลักฐาน ความไม่แน่นอน มนุษย์"},
    {name:"PUI89 AI HOME", href:"home.html", th:"PUI89 AI HOME", thHref:"home-th.html", desc:"Indoor home monitoring concepts for fire, water, electricity, humidity and structural change.", terms:"home safety fire water electricity humidity crack vibration mold indoor house ความปลอดภัย บ้าน ไฟไหม้ น้ำ ไฟฟ้า ความชื้น รอยร้าว เชื้อรา"},
    {name:"PUI89 AI NOMAD", href:"nomad.html", th:"PUI89 AI NOMAD", thHref:"nomad-th.html", desc:"Mobile and travel-oriented assistant concept with environmental awareness and offline resilience.", terms:"nomad mobile travel outdoor suitcase portable environment offline weather safety เดินทาง เคลื่อนที่ กลางแจ้ง กระเป๋า พกพา สภาพแวดล้อม ออฟไลน์"},
    {name:"PUI89 AI Robot Car", href:"ai-robot-car.html", th:"PUI89 AI Robot Car", thHref:"ai-robot-car-th.html", desc:"Intelligent mobility research covering road context, hazard awareness and vehicle safety.", terms:"car vehicle road mobility collision hazard weather maintenance รถยนต์ ยานพาหนะ ถนน การเดินทาง อุบัติเหตุ อันตราย สภาพอากาศ"},
    {name:"PUI89 AI Robot Motorcycle — EasyRide", href:"ai-robot-motorcycle.html", th:"PUI89 AI Robot Motorcycle — EasyRide", thHref:"ai-robot-motorcycle-th.html", desc:"Step-through intelligent mobility concept with flood-depth awareness and rider safety.", terms:"motorcycle scooter easyride flood depth road rider safety รถจักรยานยนต์ มอเตอร์ไซค์ สกู๊ตเตอร์ น้ำท่วม ความลึกถนน ความปลอดภัย ผู้ขับขี่"}
  ];
  const input=document.getElementById("pui89-project-query");
  const button=document.getElementById("pui89-project-search");
  const output=document.getElementById("pui89-project-results");
  if(!input||!button||!output)return;
  const thai=document.documentElement.lang.toLowerCase().startsWith("th");
  const run=()=>{
    const query=input.value.trim().toLocaleLowerCase();
    if(!query){output.innerHTML='<p class="pui89-ai-empty">'+(thai?'พิมพ์คำค้นก่อน':'Enter a search term first.')+'</p>';return;}
    const tokens=query.split(/[\s,，、/]+/).filter(Boolean);
    const ranked=projects.map(p=>{
      const hay=(p.name+" "+p.th+" "+p.desc+" "+p.terms).toLocaleLowerCase();
      const words=hay.split(/[\s,，、/]+/);
      const score=tokens.reduce((n,t)=>n+(hay.includes(t)?(p.name.toLowerCase().includes(t)?4:words.includes(t)?3:1):0),0);
      return {...p,score};
    }).filter(p=>p.score>0).sort((a,b)=>b.score-a.score||a.name.localeCompare(b.name));
    if(!ranked.length){output.innerHTML='<p class="pui89-ai-empty">'+(thai?'ยังไม่พบโครงการที่ตรงกัน ลองใช้คำค้นภาษาไทยหรืออังกฤษอีกแบบ':'No matching project yet. Try another English or Thai keyword.')+'</p>';return;}
    output.innerHTML=ranked.slice(0,5).map(p=>'<article class="pui89-ai-result"><h3>'+escapeHtml(thai?p.th:p.name)+'</h3><p>'+escapeHtml(p.desc)+'</p><a href="'+(thai?p.thHref:p.href)+'">'+(thai?'เปิดหน้าโครงการ ↗':'Explore project ↗')+'</a></article>').join("");
  };
  const escapeHtml=s=>String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  button.addEventListener("click",run);
  input.addEventListener("keydown",e=>{if(e.key==="Enter")run();});
})();
