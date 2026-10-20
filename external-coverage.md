---
title: "External Coverage"
permalink: /news/external-coverage/
news_events: true
---

# External Coverage

[← News & Events]({{ '/news-events/' | relative_url }})

Articles about CoRE-Math published by universities, research organisations, media and other external sources.

<div class="external-coverage-list">
{% assign coverage_items = site.data.external_coverage | sort: "date" | reverse %}
{% for item in coverage_items %}
  <article class="external-coverage-item" id="{{ item.id }}">
    <div class="external-coverage-date">{{ item.date | date: "%-d %B %Y" }}</div>
    <div class="external-coverage-title">
      {% if item.archive_pdf %}
      <a href="{{ item.archive_pdf | relative_url }}">{{ item.title }}</a>
      <p><a class="action-link" href="{{ item.original_url }}">Original publication<span class="link-arrow">&nbsp;→</span></a></p>
      {% else %}
      <a href="{{ item.original_url }}">{{ item.title }}</a>
      {% endif %}
    </div>
    <div class="external-coverage-source">
      <span>{{ item.source }}</span>
      {% if item.author %}<span>{{ item.author }}</span>{% endif %}
    </div>
  </article>
{% endfor %}
</div>
