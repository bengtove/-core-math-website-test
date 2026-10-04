---
layout: default
title: "AECC – African Enumerative Combinatorics Community"
type: research-group
---

# AECC – African Enumerative Combinatorics Community

The African Enumerative Combinatorics Community (AECC) brings together students and researchers across Africa with an interest in enumerative combinatorics and related areas.

AECC builds on an earlier regional collaboration in enumerative combinatorics, the **Combinatorial Research Studio (CoRS)**. CoRS was established with support from ISP and Sida bilateral research programmes and brought together researchers from Addis Ababa University, the University of Antananarivo, Makerere University and Mbarara University of Science and Technology, with international collaboration involving Stockholm University and Université Paris Cité.

## Seminar series

AECC organises a regular online seminar series in enumerative combinatorics, providing a meeting place for researchers and students across institutions and countries.

## Events

Two major AECC activities are planned at Makerere University in 2027:

- **[CIMPA School on Algebraic and Enumerative Combinatorics]({{ "/events/2027-algebraic-enumerative-combinatorics/" | relative_url }})**, 19–30 July 2027.
- **[Inaugural Pan-African AECC Research Workshop on Enumerative Combinatorics]({{ "/events/2027-pan-african-aecc-workshop/" | relative_url }})**, 2–6 August 2027.

## Committee

- Fufa Beyene — Addis Ababa University
- Yvonne Kariuki — Kibabii University
- Olivia Nabawanda — Makerere University
- Dimbinaina Ralaivaosaona — Stellenbosch University
- Sarah Selkirk — Volunteer, UK

## Selected publications

The publications below are records in the CoRE-Math publication dataset explicitly connected with AECC or its predecessor CoRS.

{% assign aecc_publications = site.data.publications | where_exp: "publication", "publication.research_groups contains 'AECC'" %}
{% assign cors_publications = site.data.publications | where_exp: "publication", "publication.research_groups contains 'CoRS'" %}
{% assign aecc_publications = aecc_publications | concat: cors_publications %}
{% assign years = aecc_publications | map: "year" | uniq | sort | reverse %}
{% for year in years %}
### {{ year }}

{% assign publications = aecc_publications | where: "year", year | sort: "sort_author" %}
{% for publication in publications %}
<div class="publication" style="margin-bottom: 1.35rem;">
<p style="margin-bottom: .25rem;">
{{ publication.authors }} ({{ publication.year }}). {{ publication.title }}. {% if publication.journal %}<em>{{ publication.journal }}</em>{% endif %}{% if publication.volume %}, <strong>{{ publication.volume }}</strong>{% if publication.issue %}({{ publication.issue }}){% endif %}{% endif %}{% if publication.pages %}, {{ publication.pages }}{% elsif publication.article_number %}, {{ publication.article_number }}{% endif %}.{% if publication.doi %} <a href="https://doi.org/{{ publication.doi }}">https://doi.org/{{ publication.doi }}</a>{% elsif publication.arxiv %} <a href="https://arxiv.org/abs/{{ publication.arxiv }}">arXiv:{{ publication.arxiv }}</a>{% endif %}
</p>
</div>
{% endfor %}
{% endfor %}

**[Visit the AECC website for further information](https://african-enumerative-combinatorics.github.io/)**
