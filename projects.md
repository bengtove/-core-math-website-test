---
title: "Programmes & Projects"
permalink: /projects/
---

# Programmes & Projects

Programmes are continuing areas of CoRE-Math activity that bring together related activities over time. Externally funded projects are defined collaborations or initiatives supported through external project funding, sometimes combining several funding sources or developing towards larger funding applications.

{% assign core_math_schools = site.programmes | where: "programme_id", "core-math-schools" | first %}
{% assign core_math_fellowships = site.programmes | where: "programme_id", "core-math-fellowships" | first %}
{% assign industry_mathematics = site.programmes | where: "programme_id", "study-groups-with-industry" | first %}
{% assign mathematics_competitions = site.programmes | where: "programme_id", "mathematics-competitions" | first %}
{% assign women_in_math = site.projects | where: "title", "Women in Math" | first %}
{% assign lake_victoria = site.projects | where: "project_id", "lake-victoria" | first %}
{% assign math4sdg = site.projects | where: "project_id", "math4sdg" | first %}
{% assign fame = site.projects | where: "project_id", "fame" | first %}
{% assign sida_collaboration = site.projects | where: "project_id", "sida-supported-collaboration" | first %}
{% assign spirit = site.projects | where: "project_id", "spirit" | first %}
{% assign earth_observation = site.projects | where: "project_id", "applied-mathematics-for-earth-observation" | first %}

## Programmes

### {{ core_math_fellowships.title }}

CoRE-Math Fellowships support research visits by postgraduate students and researchers from CoRE-Math universities to Uppsala University and the University of KwaZulu-Natal. The fellowships provide opportunities to develop research collaborations with researchers at the two host universities and strengthen connections across the CoRE-Math network.\n\n[Read more]({{ core_math_fellowships.url | relative_url }})

### {{ core_math_schools.title }}

Annual mathematics schools have been organised without interruption since 2004, in long-standing collaboration with ICTP. The schools bring together postgraduate students and researchers for intensive study of mathematical topics, with international lecturers and opportunities for research interaction and networking.\n\n[Read more]({{ core_math_schools.url | relative_url }})

### {{ industry_mathematics.title }}

Industrial Mathematics connects mathematics with problems from industry and society through contact workshops, Modelling Weeks, Study Groups with Industry and follow-up research.\n\n[Read more]({{ industry_mathematics.url | relative_url }})

### {{ mathematics_competitions.title }}

Mathematics Competitions connects and strengthens national and regional competition activities across the CoRE-Math network, supports cooperation and capacity development, and encourages young people to continue their studies in mathematics and related disciplines.\n\n[Read more]({{ mathematics_competitions.url | relative_url }})

### {{ women_in_math.title }}

Women in Math is a cross-cutting area of work within CoRE-Math, aiming to increase participation and opportunities for women in the mathematical sciences and strengthen inclusion across CoRE-Math activities.\n\n[Read more]({{ women_in_math.url | relative_url }})

## Externally funded projects

### {{ earth_observation.title }}

A Finland–Rwanda collaboration using applied mathematics and Earth observation to address research questions connected with environmental and societal challenges. The project brings together LUT University, the University of Rwanda and AIMS Rwanda and supports research collaboration and researcher development.\n\n**Funder:** Finnish National Agency for Education (EDUFI), TFK programme\n\n[Read more]({{ earth_observation.url | relative_url }})

### FAME

FAME is a Finnish flagship programme in applied mathematics in which LUT University is a partner. Its collaboration with Africa supports joint research and the development of longer-term links between Finnish and African research environments, including doctoral and postdoctoral collaboration.\n\n**Funder:** Research Council of Finland\n\n[Visit the FAME Flagship website](https://fameflagship.fi/)

### {{ lake_victoria.title }}

A developing CoRE-Math research collaboration bringing together mathematicians and researchers from other disciplines around challenges connected with the Lake Victoria region. The project aims to develop interdisciplinary research, regional collaboration and joint funding initiatives around problems where the mathematical sciences can make a contribution.\n\n**External support:** NORHED II / Math4SDG (project-development workshop)\n\n[Read more]({{ lake_victoria.url | relative_url }})

### {{ math4sdg.title }}

Math4SDG is a NORHED II project strengthening mathematics and mathematics education through collaboration between the University of Dar es Salaam, Makerere University and the University of Bergen. It supports PhD training, research collaboration, education and regional activities, including the African–Nordic Mathematics Conference held in Arusha in August 2026.\n\n**Funder:** Norad, NORHED II\n\n[Read more]({{ math4sdg.url | relative_url }})

### {{ sida_collaboration.title }}

Long-term bilateral research programmes in Rwanda, Tanzania and Uganda have strengthened mathematical research and postgraduate education through collaboration with Swedish universities. Activities have included PhD and postdoctoral training, research collaboration, curriculum and programme development, conferences and links between the participating research environments.\n\n**Funder:** Sida\n\n[Read more]({{ sida_collaboration.url | relative_url }})

### {{ spirit.title }}

A University of Geneva–University of Rwanda research collaboration developing statistical methods for Small Area Estimation, with applications to gender disparities in Rwanda. The project combines methodological research with doctoral training, researcher mobility and the development of statistical research capacity at the University of Rwanda.\n\n**Funder:** Swiss National Science Foundation (SNSF), SPIRIT programme\n\n[Read more]({{ spirit.url | relative_url }})

## Previous projects

[View previous projects →]({{ "/projects/previous/" | relative_url }})
