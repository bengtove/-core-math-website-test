---
layout: default
title: "APREA – Applied Probability Research in Eastern Africa"
type: research-group
research_group_id: aprea
---

# APREA – Applied Probability Research in Eastern Africa

Applied Probability Research in Eastern Africa (APREA) is a regional research group focused on using applied probability and statistics to address problems in health, economics and the environment.

The network has included researchers from the University of Nairobi, Kenyatta University, the Technical University of Kenya, Makerere University, Kyambogo University and Eduardo Mondlane University. Its principal collaborating institutions in Sweden have been KTH Royal Institute of Technology and Linköping University.

APREA was supported by the International Science Programme (ISP) through 2025.

## Selected publications

The publications below are records in the CoRE-Math publication dataset explicitly reported under APREA.

{% assign group_publications = site.data.publications | where_exp: "publication", "publication.research_groups contains 'APREA'" %}
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

- Patrick Weke — University of Nairobi<br>
  [pweke@uonbi.ac.ke](mailto:pweke@uonbi.ac.ke)
