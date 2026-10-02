---
layout: default
title: "EAALG – Eastern Africa Algebra Research Group"
---

# EAALG – Eastern Africa Algebra Research Group

The Eastern Africa Algebra Research Group (EAALG) brings together researchers in algebra, algebraic geometry and related areas from Eastern Africa and international partner institutions. The group grew out of a longer history of regional collaboration in algebra and geometry and provides a platform for collaborative research, graduate training and scientific exchange.

EAALG organises research workshops and connects researchers and graduate students across the region with international collaborators. Its activities are closely linked to broader collaborations and training initiatives in algebra and geometry, including activities supported through CoRE-Math.

## EAALG workshops

- **2021 — 1st EAALG Workshop: Introduction to Homological Algebra and Discrete Geometry.** Held online, 13–16 December 2021.
- **2023 — 2nd EAALG Workshop: Some Topics in Algebra and Geometry.** Makerere University, Uganda, 14–18 August 2023.
- **2024 — 3rd EAALG Workshop: Some Topics in Algebra and Geometry.** Makerere University, Uganda, 25–29 November 2024.
- **2025 — EAALG Workshop and 10th Anniversary Nairobi Workshop in Algebraic Geometry.** Nairobi and Masai Mara, Kenya, 11–19 September 2025.

## Related collaborations and activities

Researchers in EAALG also participate in regional and international collaborations in algebra, algebraic geometry and related fields. These include the Africa-UniNet-supported Uganda–Austria Collaboration in Algebra and Geometry, running from October 2024 to September 2027, and the [Austria–Uganda workshop on geometry and representation theory](https://homepage.univie.ac.at/balazs.szendroi/?page_id=864), held at the University of Vienna on 22–23 July 2025.

The 2025 Nairobi Workshop in Algebraic Geometry was organised in partnership with EAALG. A further [Austria–Uganda Workshop on Algebra and Geometry](https://homepage.univie.ac.at/balazs.szendroi/?page_id=946) is scheduled for 4–8 January 2027.

## Coordinators

- David Ssevviiri — Makerere University
- Alex S. Bamunoba — Makerere University
- Alex B. Tumwesigye — Makerere University
- Layla Sorkatti — Al Neelain University
- Jared Ongaro — University of Nairobi
- Tilahun Abebaw — Addis Ababa University
- Iara Goncalves — Universidade Eduardo Mondlane
- Celestin Kurujyibwami — University of Rwanda
- Adson Banda — University of Zambia

## Selected publications

{% assign eaalg_publications = site.data.publications | where_exp: "publication", "publication.research_groups contains 'EAALG'" %}
{% assign years = eaalg_publications | map: "year" | uniq | sort | reverse %}
{% for year in years %}
### {{ year }}

{% assign publications = eaalg_publications | where: "year", year | sort: "sort_author" %}
{% for publication in publications %}
<div class="publication" style="margin-bottom: 1.35rem;">
<p style="margin-bottom: .25rem;">
{{ publication.authors }} ({{ publication.year }}). {{ publication.title }}. {% if publication.journal %}<em>{{ publication.journal }}</em>{% endif %}{% if publication.volume %}, <strong>{{ publication.volume }}</strong>{% if publication.issue %}({{ publication.issue }}){% endif %}{% endif %}{% if publication.pages %}, {{ publication.pages }}{% elsif publication.article_number %}, {{ publication.article_number }}{% endif %}.{% if publication.doi %} <a href="https://doi.org/{{ publication.doi }}">https://doi.org/{{ publication.doi }}</a>{% elsif publication.arxiv %} <a href="https://arxiv.org/abs/{{ publication.arxiv }}">arXiv:{{ publication.arxiv }}</a>{% endif %}
</p>
{% assign has_meta = false %}{% if publication.institutions.size > 0 or publication.research_groups.size > 0 or publication.projects_programmes.size > 0 or publication.collaborations.size > 0 or publication.support.size > 0 %}{% assign has_meta = true %}{% endif %}
{% if has_meta %}<p style="margin-top: 0; font-size: .92em; color: #555;">
{% if publication.institutions.size > 0 %}<strong>CoRE-Math node:</strong> {{ publication.institutions | join: "; " }}{% endif %}
{% if publication.research_groups.size > 0 %}<br><strong>Research group:</strong> {{ publication.research_groups | join: "; " }}{% endif %}
{% if publication.projects_programmes.size > 0 %}<br><strong>Project/programme:</strong> {{ publication.projects_programmes | join: "; " }}{% endif %}
{% if publication.collaborations.size > 0 %}<br><strong>Collaboration:</strong> {{ publication.collaborations | join: "; " }}{% endif %}
{% if publication.support.size > 0 %}<br><strong>Support/activity:</strong> {{ publication.support | join: "; " }}{% endif %}
</p>{% endif %}
</div>
{% endfor %}
{% endfor %}

Visit the [EAALG website](https://sites.google.com/view/eaalg/home) for further information and the group’s broader publication record.
