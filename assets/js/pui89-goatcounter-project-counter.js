/* PUI89 view-counter shutdown. Removes legacy view widgets and prevents GoatCounter loading. */
(function () {
  "use strict";
  function removeLegacyCounters() {
    document.querySelectorAll(
      '.pui89-project-views, #pui89-project-view-count, #pui89-public-visitor-counter, [aria-label="Website views"], [aria-label="ยอดวิวเว็บไซต์"]'
    ).forEach(function (node) { node.remove(); });
    document.querySelectorAll('script[data-goatcounter], script[src*="gc.zgo.at/count.js"]').forEach(function (node) {
      node.remove();
    });
  }
  removeLegacyCounters();
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", removeLegacyCounters, { once: true });
  }
})();
