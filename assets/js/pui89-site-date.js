(() => {
  "use strict";
  const isThai = (document.documentElement.lang || "").toLowerCase().startsWith("th");
  const footer = document.querySelector("footer");
  if (!footer) return;

  const dateParts = () => {
    const parts = new Intl.DateTimeFormat("en-CA", {
      year: "numeric", month: "2-digit", day: "2-digit", timeZone: "Asia/Bangkok"
    }).formatToParts(new Date());
    return Object.fromEntries(parts.map(part => [part.type, part.value]));
  };

  const render = () => {
    const parts = dateParts();
    const date = new Date(Number(parts.year), Number(parts.month) - 1, Number(parts.day), 12);
    const locale = isThai ? "th-TH" : "en-GB";
    const displayDate = new Intl.DateTimeFormat(locale, {
      day: "numeric", month: "long", year: "numeric", timeZone: "Asia/Bangkok"
    }).format(date);
    const year = new Intl.DateTimeFormat(locale, {
      year: "numeric", timeZone: "Asia/Bangkok"
    }).format(date);

    let stamp = footer.querySelector("[data-pui89-site-date]");
    if (!stamp) {
      stamp = document.createElement("span");
      stamp.className = "pui89-site-date";
      stamp.setAttribute("data-pui89-site-date", "");
      stamp.style.cssText = "display:inline-block;margin-inline-start:12px;color:inherit;opacity:.82;font-size:.92em";
      footer.appendChild(stamp);
    }
    footer.innerHTML = footer.innerHTML.replace(/©\\s*20\\d{2}|©\\s*25\\d{2}/g, "© " + year);
    stamp = footer.querySelector("[data-pui89-site-date]");
    if (!stamp) {
      stamp = document.createElement("span");
      stamp.className = "pui89-site-date";
      stamp.setAttribute("data-pui89-site-date", "");
      stamp.style.cssText = "display:inline-block;margin-inline-start:12px;color:inherit;opacity:.82;font-size:.92em";
      footer.appendChild(stamp);
    }
    stamp.textContent = (isThai ? "อัปเดตล่าสุด: " : "Last updated: ") + displayDate;
  };

  render();
  window.setInterval(render, 60000);
})();
