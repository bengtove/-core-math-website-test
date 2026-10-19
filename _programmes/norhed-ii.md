---
layout: default
title: "NORHED II"
programme_id: "norhed-ii"
---

# NORHED II

NORHED II (2021–2026) is the second phase of the Norwegian Programme for Capacity Development in Higher Education and Research for Development, funded by the Norwegian Agency for Development Cooperation (Norad).

The programme supports partnerships between universities in Norway and the Global South to strengthen higher education and research capacity. Its objectives include improving postgraduate education, strengthening research environments, promoting institutional development, and advancing gender equality and inclusion.

## Projects

{% assign related_projects = site.projects | where: "programme", page.programme_id %}
{% for project in related_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}){% if project.location %} — {{ project.location }}{% endif %}
{% endfor %}

## Further information

- [NORHED II (2021–2026) — Norad](https://www.norad.no/innsikt/tematiske-omrader/utdanning-og-forsking/hoyere-utdanning--sentralt-for-ethvert-lands-utvikling/norhed-ii-2021-2026/)
