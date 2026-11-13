/* PUI89 per-page GoatCounter display. One compact counter; no visitor-level data is shown. */
(function () {
  "use strict";

  var target = document.getElementById("pui89-project-view-count");
  if (!target || target.dataset.pui89CounterStarted === "true") return;
  target.dataset.pui89CounterStarted = "true";

  var panel = target.closest(".pui89-project-views");
  if (panel) {
    panel.style.position = "fixed";
    panel.style.top = "max(12px, env(safe-area-inset-top))";
    panel.style.right = "max(12px, env(safe-area-inset-right))";
    panel.style.zIndex = "10000";
    panel.style.margin = "0";
    panel.style.maxWidth = "calc(100vw - 24px)";
    panel.style.padding = "8px 12px";
    panel.style.borderRadius = "999px";
    panel.style.boxShadow = "0 8px 28px rgba(0,0,0,.28)";
    panel.style.backdropFilter = "blur(12px)";
    panel.style.webkitBackdropFilter = "blur(12px)";
    panel.style.fontSize = ".82rem";
    panel.style.lineHeight = "1.35";
    panel.style.whiteSpace = "nowrap";
    panel.style.pointerEvents = "none";

    var label = panel.querySelector("span");
    if (label && !label.textContent.trim().startsWith("◉")) {
      label.textContent = "◉ " + label.textContent.trim();
    }
  }

  var attempts = 0;
  var waitForGoatCounter = window.setInterval(function () {
    var counter = window.goatcounter;

    if (counter && typeof counter.visit_count === "function") {
      window.clearInterval(waitForGoatCounter);

      try {
        counter.visit_count({
          append: "#pui89-project-view-count",
          path: window.location.pathname,
          style: "div { display: inline; color: #f2f6fc; font-weight: 800; } #gcvc-views { color: #42D9FF; font-weight: 800; } #gcvc-by { color: #a8b7c9; }"
        });

        // Public counters can be cached or unavailable; never leave "Loading…".
        window.setTimeout(function () {
          if (!target.querySelector("#gcvc-views")) {
            target.textContent = "—";
            target.setAttribute("title", "View count is temporarily unavailable");
          }
        }, 8000);
      } catch (error) {
        target.textContent = "—";
        target.setAttribute("title", "View count is temporarily unavailable");
      }
    } else if (++attempts >= 100) {
      window.clearInterval(waitForGoatCounter);
      target.textContent = "—";
      target.setAttribute("title", "View count is temporarily unavailable");
    }
  }, 100);
})();
