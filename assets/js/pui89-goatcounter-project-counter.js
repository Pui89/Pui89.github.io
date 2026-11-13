/* PUI89 per-page GoatCounter display. One compact counter; no visitor-level data is shown. */
(function () {
  "use strict";

  var target = document.getElementById("pui89-project-view-count");
  if (!target || target.dataset.pui89CounterStarted === "true") return;
  target.dataset.pui89CounterStarted = "true";

  var panel = target.closest(".pui89-project-views");
  if (panel) {
    var stage = document.querySelector(".pui89-progress--hero");
    if (stage && stage.parentNode) {
      // Keep the view count directly beneath the development-stage card,
      // right-aligned with the project hero rather than floating over the page.
      var row = document.createElement("div");
      row.className = "pui89-project-views-row";
      row.setAttribute("aria-label", "Project view count");
      row.style.display = "flex";
      row.style.justifyContent = "flex-end";
      row.style.alignItems = "center";
      row.style.width = "100%";
      row.style.maxWidth = "100%";
      row.style.margin = "8px 0 0";
      row.style.flex = "0 0 100%";
      row.style.gridColumn = "1 / -1";
      stage.insertAdjacentElement("afterend", row);
      row.appendChild(panel);
    }

    panel.style.position = "relative";
    panel.style.top = "auto";
    panel.style.right = "auto";
    panel.style.zIndex = "2";
    panel.style.margin = "0";
    panel.style.maxWidth = "calc(100vw - 24px)";
    panel.style.padding = "6px 10px";
    panel.style.borderRadius = "999px";
    panel.style.border = "1px solid #293b50";
    panel.style.background = "rgba(16,27,43,.94)";
    panel.style.color = "#a8b7c9";
    panel.style.boxShadow = "0 6px 20px rgba(0,0,0,.22)";
    panel.style.backdropFilter = "blur(12px)";
    panel.style.webkitBackdropFilter = "blur(12px)";
    panel.style.fontSize = ".78rem";
    panel.style.lineHeight = "1.3";
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
