---
title: "Programmes & Projects"
permalink: /projects/
---

# Programmes & Projects

Programmes are continuing areas of CoRE-Math activity that bring together related activities over time. Projects are defined collaborations or initiatives with a particular purpose and scope, often carried out within a specific period.

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

### [{{ core_math_fellowships.title }}]({{ core_math_fellowships.url | relative_url }})

CoRE-Math Fellowships support research visits by postgraduate students and researchers from CoRE-Math universities to Uppsala University and the University of KwaZulu-Natal. The fellowships provide opportunities to develop research collaborations with researchers at the two host universities and strengthen connections across the CoRE-Math network.

### [{{ core_math_schools.title }}]({{ core_math_schools.url | relative_url }})

Annual mathematics schools have been organised without interruption since 2004, in long-standing collaboration with ICTP. The schools bring together postgraduate students and researchers for intensive study of mathematical topics, with international lecturers and opportunities for research interaction and networking.

### [{{ industry_mathematics.title }}]({{ industry_mathematics.url | relative_url }})

Industrial Mathematics connects mathematics with problems from industry and society through contact workshops, Modelling Weeks, Study Groups with Industry and follow-up research.

### [{{ mathematics_competitions.title }}]({{ mathematics_competitions.url | relative_url }})

Mathematics Competitions connects and strengthens national and regional competition activities across the CoRE-Math network, supports cooperation and capacity development, and encourages young people to continue their studies in mathematics and related disciplines.

### [{{ women_in_math.title }}]({{ women_in_math.url | relative_url }})

Women in Math is a cross-cutting area of work within CoRE-Math, aiming to increase participation and opportunities for women in the mathematical sciences and strengthen inclusion across CoRE-Math activities.

## Ongoing projects

### [{{ earth_observation.title }}]({{ earth_observation.url | relative_url }})

A Finland–Rwanda collaboration using applied mathematics and Earth observation to address research questions connected with environmental and societal challenges. The project brings together LUT University, the University of Rwanda and AIMS Rwanda and supports research collaboration and researcher development.

### [FAME]({{ fame.url | relative_url }})

FAME is a Finnish flagship programme in applied mathematics in which LUT University is a partner. Its collaboration with Africa supports joint research and the development of longer-term links between Finnish and African research environments, including doctoral and postdoctoral collaboration.

### [{{ lake_victoria.title }}]({{ lake_victoria.url | relative_url }})

A developing CoRE-Math research collaboration bringing together mathematicians and researchers from other disciplines around challenges connected with the Lake Victoria region. The project aims to develop interdisciplinary research, regional collaboration and joint funding initiatives around problems where the mathematical sciences can make a contribution.

### [{{ math4sdg.title }}]({{ math4sdg.url | relative_url }})

Math4SDG is a NORHED II project strengthening mathematics and mathematics education through collaboration between the University of Dar es Salaam, Makerere University and the University of Bergen. It supports PhD training, research collaboration, education and regional activities, including the African–Nordic Mathematics Conference held in Arusha in August 2026.

### [{{ sida_collaboration.title }}]({{ sida_collaboration.url | relative_url }})

Long-term bilateral research programmes in Rwanda, Tanzania and Uganda have strengthened mathematical research and postgraduate education through collaboration with Swedish universities. Activities have included PhD and postdoctoral training, research collaboration, curriculum and programme development, conferences and links between the participating research environments.

### [{{ spirit.title }}]({{ spirit.url | relative_url }})

A University of Geneva–University of Rwanda research collaboration developing statistical methods for Small Area Estimation, with applications to gender disparities in Rwanda. The project combines methodological research with doctoral training, researcher mobility and the development of statistical research capacity at the University of Rwanda.

## Previous projects

[View previous projects →]({{ "/projects/previous/" | relative_url }})
