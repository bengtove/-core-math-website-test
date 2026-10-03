---
title: "News & Events"
permalink: /news-events/
---

# News & Events


{% assign current_year = "" %}
{% for post in site.posts %}
  {% assign post_year = post.date | date: "%Y" %}
  {% if post_year != current_year %}
## {{ post_year }}
    {% assign current_year = post_year %}
  {% endif %}
<div style="display:grid;grid-template-columns:7.5rem 1fr;column-gap:1rem;margin:0.55rem 0;">
  <div>{{ post.date | date: "%-d %B" }}</div>
  <div><a href="{{ post.url | relative_url }}">{{ post.title }}</a></div>
</div>
{% endfor %}
