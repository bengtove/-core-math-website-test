(function () {
  "use strict";

  document.querySelectorAll("a[href]").forEach(function (link) {
    var url;

    try {
      url = new URL(link.getAttribute("href"), window.location.href);
    } catch (error) {
      return;
    }

    if (!/^https?:$/.test(url.protocol) || url.origin === window.location.origin) {
      return;
    }

    var rel = new Set((link.getAttribute("rel") || "").split(/\s+/).filter(Boolean));
    rel.add("noopener");
    rel.add("noreferrer");

    link.setAttribute("target", "_blank");
    link.setAttribute("rel", Array.from(rel).join(" "));
  });
}());
