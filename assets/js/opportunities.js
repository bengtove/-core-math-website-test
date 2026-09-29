(function () {
  "use strict";

  var page = document.querySelector(".opportunities-page");
  if (!page) return;

  var monthNumbers = {
    January: 0,
    February: 1,
    March: 2,
    April: 3,
    May: 4,
    June: 5,
    July: 6,
    August: 7,
    September: 8,
    October: 9,
    November: 10,
    December: 11
  };

  function valuesFrom(attribute) {
    return attribute
      .split(",")
      .map(function (value) { return value.trim(); })
      .filter(Boolean);
  }

  function deadlineValue(value) {
    var match = value.match(/^(\d{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December) (\d{4})$/);
    if (!match) return null;

    var day = Number(match[1]);
    var month = monthNumbers[match[2]];
    var year = Number(match[3]);
    var timestamp = Date.UTC(year, month, day);
    var date = new Date(timestamp);

    if (date.getUTCFullYear() !== year || date.getUTCMonth() !== month || date.getUTCDate() !== day) {
      return null;
    }
    return timestamp;
  }

  function programmeName(item) {
    return item.dataset.programme || "";
  }

  function sortOpportunities() {
    var openList = page.querySelector('[data-opportunity-list="open"]');
    var rollingList = page.querySelector('[data-opportunity-list="rolling"]');

    if (openList) {
      Array.from(openList.children)
        .sort(function (left, right) {
          var leftDate = deadlineValue(left.dataset.deadline || "");
          var rightDate = deadlineValue(right.dataset.deadline || "");
          if (leftDate !== null && rightDate !== null && leftDate !== rightDate) return leftDate - rightDate;
          if (leftDate !== null && rightDate === null) return -1;
          if (leftDate === null && rightDate !== null) return 1;
          return programmeName(left).localeCompare(programmeName(right));
        })
        .forEach(function (item) { openList.appendChild(item); });
    }

    if (rollingList) {
      Array.from(rollingList.children)
        .sort(function (left, right) {
          return programmeName(left).localeCompare(programmeName(right));
        })
        .forEach(function (item) { rollingList.appendChild(item); });
    }
  }

  function populateFilter(select, attribute) {
    var values = new Set();
    page.querySelectorAll("[data-opportunity]").forEach(function (item) {
      valuesFrom(item.dataset[attribute] || "").forEach(function (value) { values.add(value); });
    });

    Array.from(values)
      .sort(function (left, right) { return left.localeCompare(right); })
      .forEach(function (value) {
        var option = document.createElement("option");
        option.value = value;
        option.textContent = value;
        select.appendChild(option);
      });
  }

  var supportFilter = page.querySelector("#support-type-filter");
  var careerFilter = page.querySelector("#career-stage-filter");
  var noResults = page.querySelector("[data-opportunity-no-results]");

  function applyFilters() {
    var visibleCount = 0;

    page.querySelectorAll("[data-opportunity]").forEach(function (item) {
      var supportMatches = !supportFilter.value || valuesFrom(item.dataset.supportType || "").includes(supportFilter.value);
      var careerMatches = !careerFilter.value || valuesFrom(item.dataset.careerStage || "").includes(careerFilter.value);
      var visible = supportMatches && careerMatches;
      item.hidden = !visible;
      if (visible) visibleCount += 1;
    });

    page.querySelectorAll("[data-opportunity-section]").forEach(function (section) {
      section.hidden = !section.querySelector("[data-opportunity]:not([hidden])");
    });

    noResults.hidden = visibleCount !== 0;
  }

  sortOpportunities();
  populateFilter(supportFilter, "supportType");
  populateFilter(careerFilter, "careerStage");
  supportFilter.addEventListener("change", applyFilters);
  careerFilter.addEventListener("change", applyFilters);
}());
