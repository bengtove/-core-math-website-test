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

## Publications

[Selected publications from CoRE-Math nodes]({{ '/research/publications/' | relative_url }}) — mathematical-sciences publications reported through the CoRE-Math annual surveys, with links to research groups, projects and collaborations where known.
