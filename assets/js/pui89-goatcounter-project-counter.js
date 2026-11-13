/* PUI89 per-page GoatCounter display. The existing GoatCounter tracker records visits. */
(function () {
  "use strict";
  var target = document.getElementById("pui89-project-view-count");
  if (!target) return;
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
      target.setAttribute("title", "Visitor count is temporarily unavailable");
    }
  }, 100);
})();
