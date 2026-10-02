---
title: "Publications"
permalink: /research/publications/
---

# Selected publications

This collection presents mathematical-sciences publications reported through the CoRE-Math annual surveys. It highlights research across the African CoRE-Math nodes and, where known, links publications to research groups, projects and collaborations.

The list is based on reported publications and is not intended as a complete bibliometric record of the participating departments.

{% assign years = site.publications | map: "year" | uniq | sort | reverse %}
{% for year in years %}
## {{ year }}

{% assign publications = site.publications | where: "year", year | sort: "title" %}
{% for publication in publications %}
<div class="publication">
<p>
{% if publication.url %}
  {% if publication.url contains 'http' %}
    <strong><a href="{{ publication.url }}">{{ publication.title }}</a></strong>
  {% else %}
    <strong><a href="https://doi.org/{{ publication.url }}">{{ publication.title }}</a></strong>
  {% endif %}
{% else %}
  <strong>{{ publication.title }}</strong>
{% endif %}
<br>
{{ publication.authors }}{% if publication.output %}. <em>{{ publication.output }}</em>{% endif %}.
<br>
<small>
{{ publication.nodes | join: " · " }}
{% if publication.research_groups %} · Research group: {{ publication.research_groups | join: ", " }}{% endif %}
{% if publication.projects_programmes %} · Project/programme: {{ publication.projects_programmes | join: ", " }}{% endif %}
{% if publication.collaborations %} · Collaboration: {{ publication.collaborations | join: ", " }}{% endif %}
{% if publication.support %} · Support/activity: {{ publication.support | join: ", " }}{% endif %}
</small>
</p>
</div>
{% endfor %}
{% endfor %}
