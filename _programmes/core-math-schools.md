---
layout: default
title: "CoRE-Math Schools"
programme_id: "core-math-schools"
---

# CoRE-Math Schools

CoRE-Math Schools bring together postgraduate students and researchers for intensive study of mathematical topics, with international lecturers and opportunities for research interaction and networking. The schools build on a long tradition of international mathematics schools organised by the CoRE-Math network and its predecessors since 2004, in long-standing collaboration with ICTP and other partners.

{% assign lusaka_school = site.projects | where: "project_id", "topological-data-analysis-summer-school-2027" | first %}
{% assign addis_school = site.projects | where: "project_id", "arithmetic-geometry-summer-school-2026" | first %}

## Upcoming school

### [{{ lusaka_school.title }}]({{ lusaka_school.url | relative_url }})

**19–30 July 2027 · Lusaka, Zambia**

The 2027 CoRE-Math School will focus on Topological Data Analysis and its applications. The school will bring together students and researchers for intensive study of mathematical methods connecting topology, data analysis and applications.

## Previous schools

### [{{ addis_school.title }}]({{ addis_school.url | relative_url }})

**17–28 August 2026 · Addis Ababa University, Ethiopia**

The school focused on arithmetic and algebraic geometry together with computational aspects and algorithms, with topics including algebraic varieties, commutative algebra, elliptic curves, algebraic number theory, finite fields, cryptography and computer algebra systems.

[ICTP event information](https://indico.ictp.it/event/11125/)

[View earlier schools →]({{ "/education/schools/" | relative_url }})
