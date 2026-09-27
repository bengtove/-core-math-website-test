---
layout: default
title: "NORHED II"
programme_id: "norhed-ii"
---

# NORHED II

NORHED II is a Norad funding programme.

## Projects

{% assign related_projects = site.projects | where: "programme", page.programme_id %}
{% for project in related_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}
