---
title: "Publications"
permalink: /research/publications/
parent_context_url: /research/
parent_context_label: Research
---

# Selected publications

Publications in the mathematical sciences by researchers at the African CoRE-Math nodes. The collection highlights research across the nodes and, where known, connections to CoRE-Math research groups, projects and collaborations. It is not intended as a complete bibliometric record of the participating departments.

{% assign years = site.data.publications | map: "year" | uniq | sort | reverse %}
{% for year in years %}
## {{ year }}

{% assign publications = site.data.publications | where: "year", year | sort: "sort_author" %}
{% for publication in publications %}
{% include publication-listing.html publication=publication %}
{% endfor %}
{% endfor %}
