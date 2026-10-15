---
layout: default
title: "AECC – African Enumerative Combinatorics Community"
type: research-group
research_group_id: aecc
---

# AECC – African Enumerative Combinatorics Community

The African Enumerative Combinatorics Community (AECC) brings together students and researchers across Africa with an interest in enumerative combinatorics and related areas.

AECC builds on an earlier regional collaboration in enumerative combinatorics, the **Combinatorial Research Studio (CoRS)**. CoRS was established with support from ISP and Sida bilateral research programmes and brought together researchers from Addis Ababa University, the University of Antananarivo, Makerere University and Mbarara University of Science and Technology, with international collaboration involving Stockholm University and Université Paris Cité.

## Seminar series

AECC organises a regular online seminar series in enumerative combinatorics, providing a meeting place for researchers and students across institutions and countries.

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
{% include publication-listing.html publication=publication show_meta=false %}
{% endfor %}
{% endfor %}

<p><a class="action-link" href="https://african-enumerative-combinatorics.github.io/">Visit the AECC website<span class="link-arrow">&nbsp;→</span></a></p>
