---
title: "Education"
permalink: /education/
---

# Education

Education within CoRE-Math focuses primarily on postgraduate training in the mathematical sciences. Through collaboration between universities in Africa and Europe, CoRE-Math creates opportunities for Master's and PhD students to broaden their mathematical training, engage with active research environments and build connections across institutions and countries. Activities include intensive schools, mathematical modelling training, research-oriented workshops and mobility.

## Schools

CoRE-Math Schools bring together postgraduate students and researchers for intensive study of mathematical topics. They expose students to topics and expertise that may not be available locally, provide opportunities to develop research contacts and networks, and can help students identify directions for thesis and research work.

{% for project in site.projects %}
  {% if project.sections contains "education" %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
  {% endif %}
{% endfor %}

[View previous schools →]({{ "/education/schools/" | relative_url }})

## Modelling Weeks

Modelling Weeks are educational activities in which students work in groups on mathematical modelling problems. They are designed particularly for Master's students and develop skills in mathematical modelling, teamwork and communication. Modelling Weeks form part of CoRE-Math's [Industrial Mathematics programme]({{ "/programmes/study-groups-with-industry/" | relative_url }}).

## Doctoral education

CoRE-Math aims to strengthen doctoral education through collaboration between participating universities. This can include collaborative supervision, research visits and mobility, research-oriented workshops, and opportunities for PhD students to become part of wider research collaborations.
