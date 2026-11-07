(() => {
  "use strict";
  const isThai = (document.documentElement.lang || "").toLowerCase().startsWith("th");
  const footer = document.querySelector("footer");
  if (!footer) return;

  const formatDate = (iso) => {
    const date = iso ? new Date(iso + "T12:00:00+07:00") : new Date();
    return new Intl.DateTimeFormat(isThai ? "th-TH" : "en-GB", {
      day: "numeric", month: "long", year: "numeric", timeZone: "Asia/Bangkok"
    }).format(date);
  };

  const stamp = document.createElement("span");
  stamp.className = "pui89-site-date";
  stamp.setAttribute("data-pui89-site-date", "");
  stamp.style.cssText = "display:inline-block;margin-inline-start:12px;color:inherit;opacity:.82;font-size:.92em";
  stamp.textContent = (isThai ? "อัปเดตล่าสุด: " : "Last updated: ") + formatDate();
  footer.appendChild(stamp);

  const update = async () => {
    let iso = "";
    try {
      const response = await fetch("/site-date.json", { cache: "no-store" });
      if (response.ok) {
        const data = await response.json();
        if (typeof data.date === "string" && /^\d{4}-\d{2}-\d{2}$/.test(data.date)) iso = data.date;
      }
    } catch (_) {}
    const date = iso ? new Date(iso + "T12:00:00+07:00") : new Date();
    const year = new Intl.DateTimeFormat(isThai ? "th-TH" : "en-GB", {
      year: "numeric", timeZone: "Asia/Bangkok"
    }).format(date);
    footer.innerHTML = footer.innerHTML.replace(/©\s*20\d{2}/g, "© " + year);
    stamp.textContent = (isThai ? "อัปเดตล่าสุด: " : "Last updated: ") + formatDate(iso);
    if (!stamp.isConnected) footer.appendChild(stamp);
  };

  update();
  document.addEventListener("visibilitychange", () => {
    if (!document.hidden) update();
  });
})();
