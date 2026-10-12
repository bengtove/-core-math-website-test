(function () {
  "use strict";

  var events = Array.from(document.querySelectorAll("[data-home-event]"));
  if (!events.length) return;

  function dateValue(value) {
    var match = (value || "").match(/^(\d{4})-(\d{2})-(\d{2})$/);
    if (!match) return null;

    return Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3]));
  }

  var now = new Date();
  var today = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
  var upcoming = events
    .filter(function (event) {
      var endDate = dateValue(event.dataset.endDate);
      return endDate !== null && endDate >= today;
    })
    .sort(function (left, right) {
      return dateValue(left.dataset.startDate) - dateValue(right.dataset.startDate);
    });

  events.forEach(function (event) {
    event.hidden = upcoming.slice(0, 2).indexOf(event) === -1;
  });

  upcoming.slice(0, 2).forEach(function (event) {
    event.parentNode.appendChild(event);
  });

  var emptyMessage = document.querySelector("[data-home-events-empty]");
  if (emptyMessage) emptyMessage.hidden = upcoming.length !== 0;
}());
