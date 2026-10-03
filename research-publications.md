---
title: "Publications"
permalink: /research/publications/
---

# Selected publications

Publications in the mathematical sciences by researchers at the African CoRE-Math nodes. The collection highlights research across the nodes and, where known, connections to CoRE-Math research groups, projects and collaborations. It is not intended as a complete bibliometric record of the participating departments.

{% assign years = site.data.publications | map: "year" | uniq | sort | reverse %}
{% for year in years %}
## {{ year }}

{% assign publications = site.data.publications | where: "year", year | sort: "sort_author" %}
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
