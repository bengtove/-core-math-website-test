---
title: "Education"
permalink: /education/
---

# Education

Education within CoRE-Math focuses primarily on postgraduate training in the mathematical sciences. Through collaboration between universities in Africa and Europe, CoRE-Math creates opportunities for Master's and PhD students to broaden their mathematical training, engage with active research environments and build connections across institutions and countries. Activities include intensive schools, mathematical modelling training, research-oriented workshops and mobility.

## Schools

CoRE-Math Schools build on a series of postgraduate mathematics schools that started in 2004 and have been organised annually since then. The schools have been supported by ICTP, ISP and other funders, with CIMPA becoming an important partner in recent years. They bring together postgraduate students and researchers for intensive study of mathematical topics, exposing students to topics and expertise that may not be available locally and creating opportunities for research contacts, thesis topics and collaboration.

{% for project in site.projects %}
  {% if project.sections contains "education" %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.dates %} — {{ project.dates }}{% endif %}{% if project.location %} · {{ project.location }}{% endif %}
  {% endif %}
{% endfor %}

[View previous schools →]({{ "/education/schools/" | relative_url }})

## Modelling Weeks

Modelling Weeks are educational activities in which students work in groups on mathematical modelling problems. They are designed particularly for Master's students and develop skills in mathematical modelling, teamwork and communication. Modelling Weeks form part of CoRE-Math's [Industrial Mathematics programme]({{ "/programmes/study-groups-with-industry/" | relative_url }}).

## Doctoral education

Current PhD research at the African CoRE-Math nodes covers a broad range of mathematical sciences, from algebra, combinatorics and partial differential equations to mathematical modelling, optimisation and applications in health and other areas.

The directory presents current PhD students reported by the participating ISP-supported mathematics environments. Research topics are included where available.

[Current PhD students →]({{ "/education/phd-students/" | relative_url }})
