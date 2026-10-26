---
layout: default
title: "PDEAPP – Partial Differential Equations and Applications"
type: research-group
research_group_id: pdeapp
---

# PDEAPP – Partial Differential Equations and Applications

Partial Differential Equations and Applications (PDEAPP) is a regional research group established to strengthen research and publication in partial differential equations and their applications in Africa.

Its objectives include developing new research projects, strengthening proposal and grant-writing capacity, supporting MSc and PhD students, and promoting North–South and South–South research collaboration through research visits.

The network has included researchers from Université Joseph Ki-Zerbo, Addis Ababa University, Eduardo Mondlane University, the University of Rwanda, Busitema University, Makerere University and the University of Zambia. ISP support to the network ran through 2025.

## Selected publications

The publications below are records in the CoRE-Math publication dataset explicitly reported under PDEAPP.

{% assign group_publications = site.data.publications | where_exp: "publication", "publication.research_groups contains 'PDEAPP'" %}
{% assign years = group_publications | map: "year" | uniq | sort | reverse %}
{% for year in years %}
### {{ year }}

{% assign publications = group_publications | where: "year", year | sort: "sort_author" %}
{% for publication in publications %}
{% include publication-listing.html publication=publication show_meta=false %}
{% endfor %}
{% endfor %}

## Contact

For enquiries about research collaboration and participation in the group’s activities, please contact:

- Banzi Wellars — University of Rwanda<br>
  [webanzi@gmail.com](mailto:webanzi@gmail.com)
- Hamidou Touré — Joseph Ki-Zerbo University<br>
  [toureh98@gmail.com](mailto:toureh98@gmail.com)
