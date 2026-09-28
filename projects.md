---
title: "Programmes & Projects"
permalink: /projects/
---

# Programmes & Projects

Explore CoRE-Math programmes and projects.

{% assign core_math_schools = site.programmes | where: "programme_id", "core-math-schools" | first %}
{% assign core_math_fellowships = site.programmes | where: "programme_id", "core-math-fellowships" | first %}
{% assign industry_mathematics = site.programmes | where: "programme_id", "study-groups-with-industry" | first %}
{% assign women_in_math = site.projects | where: "title", "Women in Math" | first %}
{% assign lake_victoria = site.projects | where: "project_id", "lake-victoria" | first %}
{% assign math4sdg = site.projects | where: "project_id", "math4sdg" | first %}
{% assign fame = site.projects | where: "project_id", "fame" | first %}
{% assign sida_collaboration = site.projects | where: "project_id", "sida-supported-collaboration" | first %}
{% assign spirit = site.projects | where: "project_id", "spirit" | first %}
{% assign earth_observation = site.projects | where: "project_id", "applied-mathematics-for-earth-observation" | first %}

## Programmes

### [{{ core_math_schools.title }}]({{ core_math_schools.url | relative_url }})

### [{{ core_math_fellowships.title }}]({{ core_math_fellowships.url | relative_url }})

### [{{ industry_mathematics.title }}]({{ industry_mathematics.url | relative_url }})

Industrial Mathematics connects mathematics with problems from industry and society through contact workshops, Modelling Weeks, Study Groups with Industry and follow-up research.

### [{{ women_in_math.title }}]({{ women_in_math.url | relative_url }})

Women in Math is a cross-cutting area of work within CoRE-Math, aiming to increase participation and opportunities for women in the mathematical sciences and strengthen inclusion across CoRE-Math activities.

## Projects

### [{{ lake_victoria.title }}]({{ lake_victoria.url | relative_url }})

A developing CoRE-Math research collaboration around Lake Victoria.

### [{{ math4sdg.title }}]({{ math4sdg.url | relative_url }})

Math4SDG was funded through Norad’s NORHED II programme, with its closing conference held in Arusha in August 2026.

### [FAME]({{ fame.url | relative_url }})

An applied mathematics flagship programme supporting research collaboration between Finland and Africa, including doctoral and postdoctoral collaboration.

### [{{ sida_collaboration.title }}]({{ sida_collaboration.url | relative_url }})

Long-term bilateral and regional collaboration in mathematics, postgraduate education and research capacity development involving universities in Eastern Africa and Sweden.

### [{{ spirit.title }}]({{ spirit.url | relative_url }})

A University of Geneva–University of Rwanda research collaboration developing statistical methods for Small Area Estimation, with applications to gender disparities in Rwanda.

### [{{ earth_observation.title }}]({{ earth_observation.url | relative_url }})

A Finland–Rwanda collaboration in applied mathematics for Earth observation involving LUT University, the University of Rwanda and AIMS Rwanda.
