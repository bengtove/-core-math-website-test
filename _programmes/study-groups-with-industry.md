---
layout: default
title: "Industrial Mathematics"
programme_id: "study-groups-with-industry"
---

# Industrial Mathematics

The CoRE-Math Industrial Mathematics programme organises activities involving mathematicians, students and external organisations. It builds on a long history of collaboration in applied and industrial mathematics in Africa and Europe.

## How it works

**Problem identification → Study Group with Industry → Report → Follow-up research**

This is the main Study Group process. Modelling Weeks are a separate educational activity.

### Working with external partners

Mathematics–Industry Contact Workshops and other interactions provide opportunities for mathematicians and external organisations to identify problems of mutual interest and explore possible collaboration.

### Study Groups with Industry

[Study Groups with Industry](https://ecmiindmath.org/study-groups/) are intensive workshops in which mathematicians and students work on problems proposed by companies, public organisations or other external partners.

### Reports

Each CoRE-Math Study Group with Industry must produce a report for every problem studied. Reports document the problem, the mathematical work undertaken and the results, and should be deposited in [Mathematics in Industry Reports (MIIR)](https://www.cambridge.org/engage/miir/public-dashboard), the international open repository hosted by Cambridge Open Engage. They will also be linked from the relevant Study Group pages on the CoRE-Math website.

### Follow-up research

Problems investigated during a Study Group may lead to continued collaboration or further research after the workshop.

### Modelling Weeks

[Modelling Weeks](https://ecmiindmath.org/education/modelling-weeks/) are educational activities in which students work in groups on mathematical modelling problems. They are particularly aimed at developing modelling, teamwork and communication skills and are separate from the Study Group process.

## Activities

{% assign related_projects = site.projects | where: "programme", page.programme_id %}
{% for project in related_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}

## History

Study Groups with Industry originated in Oxford in 1968 as intensive workshops in which mathematicians work directly on problems brought by industry. The model subsequently spread internationally, including to South Africa, where the [Mathematics in Industry Study Group – South Africa](https://www.wits.ac.za/csam/misg/) at Wits University began in 2004 and has developed as a long-running African Study Group programme.

The [European Consortium for Mathematics in Industry (ECMI)](https://ecmiindmath.org/about-ecmi/) was formed by European universities during 1986–87 to promote mathematical modelling in industry, educate industrial mathematicians and operate on a European scale. Study Groups therefore predate ECMI: ECMI did not create the model, but it subsequently became an important institutional framework for industrial mathematics in Europe and oversees the European Study Groups with Industry. ECMI has also organised annual [Modelling Weeks](https://ecmiindmath.org/education/modelling-weeks/) for students since 1988, providing collaborative education in mathematical modelling based on real-world problems.

In Eastern Africa, collaboration in applied and industrial mathematics between regional and Nordic partners included East Africa Technomathematics (2007–2015) and Mathematics Education and Working Life Relevance in East Africa (2013–2015). This work contributed to the development of Modelling Weeks and, later, Study Groups with Industry in Eastern Africa. The South African and Eastern African developments are distinct regional traditions within the wider international industrial mathematics movement. The present CoRE-Math Industrial Mathematics programme builds on the Eastern African experience while connecting it to wider international practice through CoRE-Math's formal partnership with ECMI.

## Resources and links

- [ECMI — Study Groups with Industry](https://ecmiindmath.org/study-groups/) — information about the internationally established Study Group format.
- [ECMI — Modelling Weeks](https://ecmiindmath.org/education/modelling-weeks/) — information about the Modelling Week format for student training.
- [Mathematics in Industry Reports (MIIR)](https://www.cambridge.org/engage/miir/public-dashboard) — the international open repository in which CoRE-Math Study Group reports should be deposited.
- [Mathematics in Industry Study Group – South Africa](https://www.wits.ac.za/csam/misg/) — a long-running African Study Group programme at Wits University.
