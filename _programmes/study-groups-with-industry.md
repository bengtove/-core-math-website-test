---
layout: default
title: "Industrial Mathematics"
programme_id: "study-groups-with-industry"
---

# Industrial Mathematics

Industrial Mathematics connects mathematicians and students with partners outside academia to identify and work on problems where mathematics can contribute. The programme builds on a long history of collaboration in applied and industrial mathematics in Eastern Africa and Europe.

## How it works

### Mathematics–Industry Contact Workshops

Bring mathematicians together with companies, public organisations and other stakeholders to identify problems where mathematics may contribute and to develop potential collaborations.

### Modelling Weeks

Give MSc students intensive experience of working collaboratively on open-ended real-world problems using mathematical modelling.

### Study Groups with Industry

Bring mathematicians, students and problem owners together for intensive work on selected problems originating outside academia.

### Follow-up research

Promising problems and collaborations may continue through MSc or PhD projects, research visits, publications and longer-term research collaboration.

## Activities

{% assign related_projects = site.projects | where: "programme", page.programme_id %}
{% for project in related_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}

## History

Industry Mathematics builds on a long history of collaboration in applied and industrial mathematics between Eastern Africa and Nordic partners, including East Africa Technomathematics (2007–2015) and Mathematics Education and Working Life Relevance in East Africa (2013–2015). This work contributed to the development of Modelling Weeks and, later, Study Groups with Industry in Eastern Africa.
