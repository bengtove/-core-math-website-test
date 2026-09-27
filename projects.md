---
title: "Projects"
permalink: /projects/
---

# Projects

Explore CoRE-Math programmes and projects.

{% for programme in site.programmes %}
## [{{ programme.title }}]({{ programme.url | relative_url }})

{% assign related_projects = site.projects | where: "programme", programme.programme_id %}
{% for project in related_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}
{% endfor %}

{% assign other_project_count = 0 %}
{% for project in site.projects %}
  {% assign matching_programmes = site.programmes | where: "programme_id", project.programme %}
  {% assign matching_programme_count = matching_programmes | size %}
  {% if matching_programme_count == 0 %}
    {% assign other_project_count = other_project_count | plus: 1 %}
  {% endif %}
{% endfor %}

{% if other_project_count > 0 %}
## Other projects

{% for project in site.projects %}
  {% assign matching_programmes = site.programmes | where: "programme_id", project.programme %}
  {% assign matching_programme_count = matching_programmes | size %}
  {% if matching_programme_count == 0 %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
  {% endif %}
{% endfor %}
{% endif %}
