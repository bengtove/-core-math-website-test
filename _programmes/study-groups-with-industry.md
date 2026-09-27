---
layout: default
title: "Industry Mathematics"
programme_id: "study-groups-with-industry"
---

# Industry Mathematics

The Industry Mathematics programme brings mathematicians, students and industry partners together to work on problems originating outside academia.

## Projects

{% assign related_projects = site.projects | where: "programme", page.programme_id %}
{% for project in related_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}
