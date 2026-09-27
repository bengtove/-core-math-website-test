---
title: "Projects"
permalink: /projects/
---

# Projects

Explore CoRE-Math programmes and projects.

## Programmes

{% for programme in site.programmes %}
- [{{ programme.title }}]({{ programme.url | relative_url }})
{% endfor %}

## Projects

{% for project in site.projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}
