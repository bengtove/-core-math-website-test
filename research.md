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
