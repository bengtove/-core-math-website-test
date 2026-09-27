---
layout: default
title: "Mathematics for Sustainable Development (Math4SDG)"
project_id: "math4sdg"
programme: "norhed-ii"
---

# Mathematics for Sustainable Development (Math4SDG)

{% assign programme = site.programmes | where: "programme_id", page.programme | first %}
**Programme:** [{{ programme.title }}]({{ programme.url | relative_url }})

Math4SDG was funded through Norad’s NORHED II programme. The Second African–Nordic Conference in Mathematics, held in Arusha in August 2026, was the project’s closing conference.

## Related news

{% assign related_posts = site.posts | where: "project", page.project_id %}
{% for post in related_posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%-d %B %Y" }}
{% endfor %}
