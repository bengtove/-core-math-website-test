---
title: "Education"
permalink: /education/
---

# Education

Education and postgraduate training within CoRE-Math.

## Schools

{% for project in site.projects %}
  {% if project.sections contains "education" %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
  {% endif %}
{% endfor %}

[View previous schools →]({{ "/education/schools/" | relative_url }})

## Modelling Weeks

**Planned:** Modelling Weeks for MSc students will provide intensive training in mathematical modelling, including activities connected to CoRE-Math Study Groups with Industry.

## PhD pipeline

**Planned:** This section will provide an overview of PhD students and doctoral research within CoRE-Math, including collaborative supervision across participating institutions. The data have not yet been added.
