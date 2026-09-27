---
title: "News & Events"
permalink: /news-events/
---

# News & Events

Updates and events from across CoRE-Math.

{% for post in site.posts %}
## [{{ post.title }}]({{ post.url | relative_url }})

**{{ post.date | date: "%-d %B %Y" }}{% if post.location %} · {{ post.location }}{% endif %}**

{{ post.excerpt }}
{% endfor %}
