---
title: "Education"
permalink: /education/
---

# Education

Education and postgraduate training within CoRE-Math.

## Projects

{% for project in site.projects %}
  {% if project.sections contains "education" %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
  {% endif %}
{% endfor %}
