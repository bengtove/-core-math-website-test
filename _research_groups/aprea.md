---
layout: default
title: "APREA – Applied Probability Research in Eastern Africa"
type: research-group
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
<div class="publication" style="margin-bottom: 1.35rem;">
<p style="margin-bottom: .25rem;">
{{ publication.authors }} ({{ publication.year }}). {{ publication.title }}. {% if publication.journal %}<em>{{ publication.journal }}</em>{% endif %}{% if publication.volume %}, <strong>{{ publication.volume }}</strong>{% if publication.issue %}({{ publication.issue }}){% endif %}{% endif %}{% if publication.pages %}, {{ publication.pages }}{% elsif publication.article_number %}, {{ publication.article_number }}{% endif %}.{% if publication.doi %} <a href="https://doi.org/{{ publication.doi }}">https://doi.org/{{ publication.doi }}</a>{% elsif publication.arxiv %} <a href="https://arxiv.org/abs/{{ publication.arxiv }}">arXiv:{{ publication.arxiv }}</a>{% endif %}
</p>
</div>
{% endfor %}
{% endfor %}
