---
layout: default
title: "Arithmetic Geometry Summer School"
project_id: "arithmetic-geometry-summer-school-2026"
programme: "core-math-schools"
location: "Addis Ababa, Ethiopia"
year: 2026
---

# Arithmetic Geometry Summer School

{% assign programme = site.programmes | where: "programme_id", page.programme | first %}
**Programme:** [{{ programme.title }}]({{ programme.url | relative_url }})

**Location:** {{ page.location }}

**Year:** {{ page.year }}
