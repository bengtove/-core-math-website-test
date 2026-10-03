---
layout: default
title: "PDEAPP – Partial Differential Equations and Applications"
type: research-group
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
<div class="publication" style="margin-bottom: 1.35rem;">
<p style="margin-bottom: .25rem;">
{{ publication.authors }} ({{ publication.year }}). {{ publication.title }}. {% if publication.journal %}<em>{{ publication.journal }}</em>{% endif %}{% if publication.volume %}, <strong>{{ publication.volume }}</strong>{% if publication.issue %}({{ publication.issue }}){% endif %}{% endif %}{% if publication.pages %}, {{ publication.pages }}{% elsif publication.article_number %}, {{ publication.article_number }}{% endif %}.{% if publication.doi %} <a href="https://doi.org/{{ publication.doi }}">https://doi.org/{{ publication.doi }}</a>{% elsif publication.arxiv %} <a href="https://arxiv.org/abs/{{ publication.arxiv }}">arXiv:{{ publication.arxiv }}</a>{% endif %}
</p>
</div>
{% endfor %}
{% endfor %}
