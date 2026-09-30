---
layout: default
title: "Industrial Mathematics"
programme_id: "study-groups-with-industry"
---

# Industrial Mathematics

Industrial Mathematics connects mathematicians and students with companies, public organisations and other partners to identify and work on problems where mathematics can contribute. Through contact workshops, Modelling Weeks, Study Groups with Industry and follow-up research, the programme creates pathways from real-world problems to mathematical research, student training and longer-term collaboration. It builds on a long history of collaboration in applied and industrial mathematics in Africa and Europe.

## How it works

**Problem identification → Study Group with Industry → Report → Follow-up research**

This pathway connects real-world problems with intensive mathematical work, documented results and opportunities for longer-term collaboration.

### Working with external partners

Mathematics–Industry Contact Workshops and other interactions bring mathematicians together with companies, public organisations and other stakeholders to identify problems where mathematics may contribute, establish contacts and develop potential collaborations. Contact workshops are one important way of identifying and developing suitable problems and building relationships with external partners, but they are not a prerequisite for every Study Group.

### Study Groups with Industry

[Study Groups with Industry](https://ecmiindmath.org/study-groups/) bring mathematicians, students and problem owners together for intensive work on problems originating in industry, public organisations or society. Problems are presented by the participating organisations and interdisciplinary groups work on them during an intensive workshop, developing mathematical formulations, approaches and possible solutions. Study Groups are an internationally established model for collaboration between mathematics and industry, with origins going back to Oxford in 1968.

### Reports

Every CoRE-Math Study Group with Industry must produce a report for each problem studied. Reports should document the problem, the mathematical work undertaken and the results, and should be deposited in [Mathematics in Industry Reports (MIIR)](https://www.cambridge.org/engage/miir/public-dashboard), the international open repository hosted by Cambridge Open Engage. Reports will also be linked from the relevant Study Group pages on the CoRE-Math website.

### Follow-up research

Promising problems and collaborations can continue after the Study Group through MSc or PhD projects, research visits, publications and longer-term research collaboration. The aim is therefore not only to solve problems during an intensive workshop, but also to create connections that can develop into sustained collaboration between mathematics and external partners.

### Modelling Weeks

[Modelling Weeks](https://ecmiindmath.org/education/modelling-weeks/) are a related educational component of the Industrial Mathematics programme. They give MSc students intensive experience of working collaboratively on open-ended real-world problems using mathematical modelling. Students work in groups, develop mathematical approaches, communicate their results and gain experience of modelling as a process rather than simply applying predetermined techniques. Modelling Weeks complement the Study Group activities but are not an integral stage in the Study Group process.

## Activities

{% assign related_projects = site.projects | where: "programme", page.programme_id %}
{% for project in related_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}

## History

Industrial Mathematics builds on a long history of collaboration in applied and industrial mathematics between Eastern Africa and Nordic partners, including East Africa Technomathematics (2007–2015) and Mathematics Education and Working Life Relevance in East Africa (2013–2015). This work contributed to the development of Modelling Weeks and, later, Study Groups with Industry in Eastern Africa.

This regional development is part of a broader international tradition. Study Groups with Industry originated in Oxford in 1968, and the European Consortium for Mathematics in Industry (ECMI) has played a long-standing role in industrial mathematics, Study Groups and Modelling Weeks. Separately, the [Mathematics in Industry Study Group – South Africa](https://www.wits.ac.za/csam/misg/) at Wits University began in 2004 and has developed as a long-running South African Study Group programme.

## Resources and links

- [ECMI — Study Groups with Industry](https://ecmiindmath.org/study-groups/) — information about the internationally established Study Group format.
- [ECMI — Modelling Weeks](https://ecmiindmath.org/education/modelling-weeks/) — information about the Modelling Week format for student training.
- [Mathematics in Industry Reports (MIIR)](https://www.cambridge.org/engage/miir/public-dashboard) — the international open repository in which CoRE-Math Study Group reports should be deposited.
- [Mathematics in Industry Study Group – South Africa](https://www.wits.ac.za/csam/misg/) — a long-running African Study Group programme at Wits University.
