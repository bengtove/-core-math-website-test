---
title: "Research"
permalink: /research/
---

# Research

Research activities and collaborations within CoRE-Math.

## Research groups

{% for research_group in site.research_groups %}
- [{{ research_group.title }}]({{ research_group.url | relative_url }})
{% endfor %}

## Research projects

{% assign research_projects = site.projects | where: "section", "research" %}
{% for project in research_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}
