---
layout: default
title: "EAALG – Eastern Africa Algebra Research Group"
research_group_id: eaalg
render_related_events: false
---

# EAALG – Eastern Africa Algebra Research Group

The Eastern Africa Algebra Research Group (EAALG) brings together researchers in algebra, algebraic geometry and related areas from Eastern Africa and international partner institutions. The group grew out of a longer history of regional collaboration in algebra and geometry and provides a platform for collaborative research, graduate training and scientific exchange.

EAALG organises research workshops and connects researchers and graduate students across the region with international collaborators. Its activities are closely linked to broader collaborations and training initiatives in algebra and geometry, including activities supported through CoRE-Math.

<p><a class="action-link" href="https://sites.google.com/view/eaalg/home">Visit the EAALG website<span class="link-arrow">&nbsp;→</span></a></p>

## Related collaborations

Researchers in EAALG also participate in regional and international collaborations in algebra, algebraic geometry and related fields. These include the Africa-UniNet-supported Uganda–Austria Collaboration in Algebra and Geometry, running from October 2024 to September 2027.

{% include related-events.html relationship="research_group" identifier=page.research_group_id heading="Related events" reverse=true plain=true %}

## Coordinators

- Tilahun Abebaw — Addis Ababa University
- Adson Banda — University of Zambia
- Alex S. Bamunoba — Makerere University
- Iara Goncalves — Universidade Eduardo Mondlane
- Celestin Kurujyibwami — University of Rwanda
- Jared Ongaro — University of Nairobi
- Layla Sorkatti — Al Neelain University
- David Ssevviiri — Makerere University
- Alex B. Tumwesigye — Makerere University

{% include related-events.html relationship="research_group" identifier=page.research_group_id heading="Workshops and events" reverse=true %}

## Selected publications

The publications below are a selection of work by researchers associated with EAALG.

{% assign eaalg_publications = site.data.publications | where_exp: "publication", "publication.research_groups contains 'EAALG'" %}
{% assign years = eaalg_publications | map: "year" | uniq | sort | reverse %}
{% for year in years %}
### {{ year }}

{% assign publications = eaalg_publications | where: "year", year | sort: "sort_author" %}
{% for publication in publications %}
{% include publication-listing.html publication=publication suppress_research_group=true suppress_node=true %}
{% endfor %}
{% endfor %}

## Contact

For enquiries about research collaboration and participation in the group’s activities, please contact:

- David Ssevviiri — Makerere University<br>
  [ssevviiridaudi@gmail.com](mailto:ssevviiridaudi@gmail.com)
