---
title: "Research"
permalink: /research/
---

# Research

Research within CoRE-Math brings together researchers across African and European universities through research groups, collaborative projects and international partnerships. Several regional research groups provide established platforms for collaboration in areas including algebra, combinatorics, applied probability and partial differential equations. Research collaboration is developed through workshops, research visits, joint publications and postgraduate research, strengthening existing research environments and creating opportunities for new collaborations across institutions and countries.

## Research groups

{% for research_group in site.research_groups %}
- [{{ research_group.title }}]({{ research_group.url | relative_url }})
{% endfor %}

## Publications

[Selected publications from CoRE-Math nodes]({{ '/research/publications/' | relative_url }}) — mathematical-sciences publications reported through the CoRE-Math annual surveys, with links to research groups, projects and collaborations where known.
