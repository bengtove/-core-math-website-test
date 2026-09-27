---
layout: default
title: "CoRE-Math Schools"
programme_id: "core-math-schools"
---

# CoRE-Math Schools

CoRE-Math Schools is a programme for CoRE-Math schools.

## Projects

{% assign related_projects = site.projects | where: "programme", page.programme_id %}
{% for project in related_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}
