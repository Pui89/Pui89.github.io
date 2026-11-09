/* PUI89 shared navigation — plain JavaScript, no trackers, ads, external requests or dependencies. */
(function(){
  "use strict";
  var pairs={
    "index.html":"th.html","th.html":"index.html",
    "ai-core.html":"ai-core-th.html","ai-core-th.html":"ai-core.html",
    "ai-robot-car.html":"ai-robot-car-th.html","ai-robot-car-th.html":"ai-robot-car.html",
    "ai-robot-motorcycle.html":"ai-robot-motorcycle-th.html","ai-robot-motorcycle-th.html":"ai-robot-motorcycle.html",
    "ai-vehicles.html":"ai-vehicles-th.html","ai-vehicles-th.html":"ai-vehicles.html",
    "coconut.html":"coconut-th.html","coconut-th.html":"coconut.html",
    "command-centre.html":"command-centre-th.html","command-centre-th.html":"command-centre.html",
    "company.html":"company-th.html","company-th.html":"company.html",
    "development.html":"development-th.html","development-th.html":"development.html",
    "evidence.html":"evidence-th.html","evidence-th.html":"evidence.html",
    "flood-rescue.html":"flood-rescue-th.html","flood-rescue-th.html":"flood-rescue.html",
    "growth.html":"growth-th.html","growth-th.html":"growth.html",
    "home.html":"home-th.html","home-th.html":"home.html",
    "nomad.html":"nomad-th.html","nomad-th.html":"nomad.html",
    "open-source-resources.html":"open-source-resources-th.html","open-source-resources-th.html":"open-source-resources.html",
    "screening.html":"screening-th.html","screening-th.html":"screening.html",
    "security.html":"security-th.html","security-th.html":"security.html",
    "support.html":"support-th.html","support-th.html":"support.html",
    "research.html":"research-th.html","research-th.html":"research.html"
  };
  var en=location.pathname.split("/").pop()||"index.html";
  var th=/-th\.html$/.test(en)||en==="th.html";
  var other=pairs[en]|| (th?"index.html":"th.html");
  var t=th?{
    home:"หน้าหลัก",core:"AI Core",projects:"โครงการ",mobility:"ยานยนต์",insight:"ศูนย์ข้อมูล",about:"เกี่ยวกับ",partners:"ความร่วมมือ",github:"GitHub",language:"English",
    projectItems:[["เกษตร: Coconut Harvest AI","coconut-th.html"],["กู้ภัย: Flood Rescue AI","flood-rescue-th.html"],["Sentinel Screening AI","screening-th.html"],["HOME","home-th.html"],["NOMAD","nomad-th.html"]],
    mobilityItems:[["AI Vehicles","ai-vehicles-th.html"],["AI Car","ai-robot-car-th.html"],["AI Motorcycle","ai-robot-motorcycle-th.html"]],
    insightItems:[["Command Centre","command-centre-th.html"],["Evidence & Validation","evidence-th.html"],["Development Observatory","development-th.html"]],
    aboutItems:[["Company","company-th.html"],["Growth Roadmap","growth-th.html"],["Research & Innovation","research-th.html"],["Open-source Resources","open-source-resources-th.html"],["Security & Trust","security-th.html"]],
    footer:"แนวคิดและสถานะซอฟต์แวร์นำเสนอพร้อมหลักฐาน ขีดความสามารถทางกายภาพต้องผ่านการตรวจสอบก่อนใช้งานจริง"
  }:{
    home:"Home",core:"AI Core",projects:"Projects",mobility:"Mobility",insight:"Observatory",about:"About",partners:"Partnership",github:"GitHub",language:"ไทย",
    projectItems:[["Agriculture · Coconut Harvest AI","coconut.html"],["Rescue · Flood Rescue AI","flood-rescue.html"],["Sentinel Screening AI","screening.html"],["HOME","home.html"],["NOMAD","nomad.html"]],
    mobilityItems:[["AI Vehicles","ai-vehicles.html"],["AI Car","ai-robot-car.html"],["AI Motorcycle","ai-robot-motorcycle.html"]],
    insightItems:[["Project Command Centre","command-centre.html"],["Evidence & Validation","evidence.html"],["Development Observatory","development.html"]],
    aboutItems:[["Company","company.html"],["Growth Roadmap","growth.html"],["Research & Innovation","research.html"],["Open-source Resources","open-source-resources.html"],["Security & Trust","security.html"]],
    footer:"Project concepts and software status are presented with evidence. Physical capabilities require independent validation."
  };
  function el(tag,cls,txt){var n=document.createElement(tag);if(cls)n.className=cls;if(txt)n.textContent=txt;return n;}
  function link(label,href){var a=el("a","pui89-nav-link",label);a.href=href;if(href===en)a.setAttribute("aria-current","page");return a;}
  function group(label,items){var d=el("details","");var s=el("summary","",label);d.appendChild(s);var menu=el("div","pui89-dropdown");items.forEach(function(it){var a=el("a","",it[0]);a.href=it[1];if(it[1]===en)a.setAttribute("aria-current","page");menu.appendChild(a);});d.appendChild(menu);return d;}
  function buildNav(){
    var nav=el("nav","");nav.id="pui89-global-nav";nav.setAttribute("aria-label",th?"เมนูหลัก PUI89":"PUI89 main navigation");
    var brand=el("a","pui89-brand");brand.href=th?"th.html":"index.html";var mark=el("span","pui89-brand-mark","P");brand.appendChild(mark);brand.appendChild(document.createTextNode("PUI89"));
    var links=el("div","pui89-nav-links");
    links.appendChild(link(t.home,th?"th.html":"index.html"));links.appendChild(link(t.core,th?"ai-core-th.html":"ai-core.html"));
    links.appendChild(group(t.projects,t.projectItems));links.appendChild(group(t.mobility,t.mobilityItems));links.appendChild(group(t.insight,t.insightItems));links.appendChild(group(t.about,t.aboutItems));links.appendChild(link(t.partners,th?"support-th.html":"support.html"));
    var lang=el("div","pui89-language");lang.setAttribute("role","group");lang.setAttribute("aria-label",th?"เลือกภาษา":"Choose language");
    var active=el("span","is-current",th?"ไทย":"English");active.setAttribute("aria-current","page");active.lang=th?"th":"en";
    var switcher=el("a","",t.language);switcher.href=other;switcher.lang=th?"en":"th";
    lang.appendChild(active);lang.appendChild(switcher);
    var gh=el("a","pui89-nav-link",t.github);gh.href="https://github.com/Pui89";gh.target="_blank";gh.rel="noopener noreferrer";
    nav.appendChild(brand);nav.appendChild(links);nav.appendChild(lang);nav.appendChild(gh);
    return nav;
  }
  function init(){
    if(document.getElementById("pui89-global-nav"))return;
    var oldNavs=Array.prototype.slice.call(document.querySelectorAll("nav:not(.pui89-quick-explore)"));
    var local=[];
    oldNavs.forEach(function(n){
      Array.prototype.forEach.call(n.querySelectorAll('a[href^="#"]'),function(a){var href=a.getAttribute("href"),label=(a.textContent||"").trim();if(href&&href!=="#"&&label&&!local.some(function(x){return x.href===href;}))local.push({href:href,label:label});});
    });
    var nav=buildNav();
    if(oldNavs.length){oldNavs[0].replaceWith(nav);oldNavs.slice(1).forEach(function(n){n.remove();});}
    else document.body.insertBefore(nav,document.body.firstChild);
    if(local.length>1){var localNav=el("div","");localNav.id="pui89-local-nav";localNav.setAttribute("aria-label",th?"ลิงก์ในหน้านี้":"On this page");local.forEach(function(x){var a=el("a","",x.label);a.href=x.href;localNav.appendChild(a);});nav.insertAdjacentElement("afterend",localNav);}
    var foot=el("div","pui89-site-footer-links");foot.appendChild(link(t.core,th?"ai-core-th.html":"ai-core.html"));foot.appendChild(link(t.insight,th?"evidence-th.html":"evidence.html"));foot.appendChild(link(t.about,th?"security-th.html":"security.html"));foot.appendChild(link(t.partners,th?"support-th.html":"support.html"));var gh=el("a","",t.github);gh.href="https://github.com/Pui89";gh.target="_blank";gh.rel="noopener noreferrer";foot.appendChild(gh);foot.appendChild(el("div","pui89-footer-note",t.footer));
    var existingFooter=document.querySelector("footer");if(existingFooter)existingFooter.appendChild(foot);else document.body.appendChild(foot);
  }
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init,{once:true});else init();
})();