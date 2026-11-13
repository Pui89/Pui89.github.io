/* PUI89 per-page GoatCounter display. View count only; no visitor-level data is shown. */
(function () {
  "use strict";
  var target = document.getElementById("pui89-project-view-count");
  if (!target) return;

  var panel = target.closest(".pui89-project-views");
  if (panel) {
    panel.style.position = "fixed";
    panel.style.top = "14px";
    panel.style.right = "18px";
    panel.style.zIndex = "10000";
    panel.style.margin = "0";
    panel.style.maxWidth = "calc(100vw - 24px)";
    panel.style.padding = "9px 13px";
    panel.style.borderRadius = "999px";
    panel.style.boxShadow = "0 8px 28px rgba(0,0,0,.28)";
    panel.style.backdropFilter = "blur(12px)";
    panel.style.fontSize = ".82rem";
    var label = panel.querySelector("span");
    if (label && !label.textContent.trim().startsWith("◉")) {
      label.textContent = "◉ " + label.textContent.trim();
    }
  }

  var attempts = 0;
  var timer = window.setInterval(function () {
    if (window.goatcounter && typeof window.goatcounter.visit_count === "function") {
      window.clearInterval(timer);
      window.goatcounter.visit_count({
        append: "#pui89-project-view-count",
        path: window.location.pathname,
        style: "div { display: inline; color: #f2f6fc; font-weight: 800; } #gcvc-views { color: #42D9FF; font-weight: 800; } #gcvc-by { color: #a8b7c9; }"
      });
    } else if (++attempts >= 100) {
      window.clearInterval(timer);
      target.textContent = "—";
      target.setAttribute("title", "View count is temporarily unavailable");
    }
  }, 100);
})();
