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
- {{ post.date | date: "%-d %B" }} — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
