(function () {
  "use strict";
  var script = document.currentScript;
  if (!script) return;
  var projectId = script.dataset.projectId || "";
  var portfolio = script.dataset.portfolio === "true";
  var thai = (document.documentElement.lang || "").toLowerCase().indexOf("th") === 0;
  var text = thai ? {
    title: "จำนวนการทบทวนโครงการที่มีหลักฐาน",
    intro: "นับเฉพาะการทบทวนที่เสร็จสมบูรณ์ มีวันที่ ขอบเขต และหลักฐานอ้างอิง",
    count: "ครั้ง",
    total: "รวมทุกโครงการ",
    empty: "ยังไม่มีบันทึกการทบทวนที่ผ่านเกณฑ์",
    note: "ไม่นับคะแนนดาว ความคิดเห็น ยอดเข้าชม หรือรายการร่าง",
    unavailable: "ไม่สามารถโหลดข้อมูลจำนวนการทบทวนได้ในขณะนี้"
  } : {
    title: "Evidence-backed project reviews",
    intro: "Counts only completed reviews with a date, defined scope and supporting evidence.",
    count: "reviews",
    total: "Portfolio total",
    empty: "No qualifying review records yet",
    note: "Ratings, stars, page views, comments and draft records are excluded.",
    unavailable: "Review counts are temporarily unavailable."
  };
  function el(tag, cls, value) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (value !== undefined) node.textContent = value;
    return node;
  }
  function valid(record) {
    return record && record.status === "completed" &&
      /^\\d{4}-\\d{2}-\\d{2}$/.test(record.reviewed_on || "") &&
      !!(record.scope && record.scope.trim()) &&
      !!(record.reviewer_role && record.reviewer_role.trim()) &&
      !!(record.outcome && record.outcome.trim()) &&
      Array.isArray(record.evidence) && record.evidence.length > 0;
  }
  function count(project) {
    return Array.isArray(project.review_records) ? project.review_records.filter(valid).length : 0;
  }
  function panel() {
    var section = el("section", "pui89-review-counts");
    section.setAttribute("aria-live", "polite");
    section.setAttribute("aria-label", text.title);
    var heading = el("h2", "pui89-review-counts__title", text.title);
    section.appendChild(heading);
    section.appendChild(el("p", "pui89-review-counts__intro", text.intro));
    return section;
  }
  function mount(section) {
    var footer = document.querySelector("footer");
    if (footer && footer.parentNode) footer.parentNode.insertBefore(section, footer);
    else document.body.appendChild(section);
  }
  var css = document.createElement("link");
  css.rel = "stylesheet";
  css.href = "/assets/css/pui89-project-review-counts.css";
  document.head.appendChild(css);
  fetch("/assets/data/project-review-register.json", { cache: "no-store" })
    .then(function (response) {
      if (!response.ok) throw new Error("HTTP " + response.status);
      return response.json();
    })
    .then(function (data) {
      if (!data || !Array.isArray(data.projects)) throw new Error("Invalid register");
      var section = panel();
      if (portfolio) {
        var table = el("table", "pui89-review-counts__table");
        var body = document.createElement("tbody");
        var total = 0;
        data.projects.forEach(function (project) {
          var n = count(project); total += n;
          var row = document.createElement("tr");
          row.appendChild(el("th", "", thai ? project.name_th : project.name_en));
          row.appendChild(el("td", "pui89-review-counts__number", String(n) + " " + text.count));
          body.appendChild(row);
        });
        table.appendChild(body);
        section.appendChild(table);
        var totalRow = el("p", "pui89-review-counts__total");
        totalRow.appendChild(el("strong", "", text.total + ": "));
        totalRow.appendChild(el("strong", "", String(total) + " " + text.count));
        section.appendChild(totalRow);
      } else {
        var project = data.projects.find(function (item) { return item.id === projectId; });
        if (!project) throw new Error("Project not found");
        var n = count(project);
        section.appendChild(el("p", "pui89-review-counts__value", String(n)));
        section.appendChild(el("p", "pui89-review-counts__label", text.count));
        if (n === 0) section.appendChild(el("p", "pui89-review-counts__empty", text.empty));
      }
      section.appendChild(el("p", "pui89-review-counts__note", text.note));
      mount(section);
    })
    .catch(function () {
      var section = panel();
      section.appendChild(el("p", "pui89-review-counts__empty", text.unavailable));
      mount(section);
    });
})();
