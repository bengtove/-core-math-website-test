---
layout: default
title: "CoRE-Math Schools"
programme_id: "core-math-schools"
---

# CoRE-Math Schools

CoRE-Math Schools bring together postgraduate students and researchers for intensive study of mathematical topics, with international lecturers and opportunities for research interaction and networking. The programme builds on a tradition of international mathematics schools within the network dating back to 2004, organised in collaboration with a range of international partners.

## Upcoming schools

{% assign today = site.time | date: "%Y%m%d" %}
{% assign school_events = site.events | where: "type", "school" | sort: "start_date" %}
{% assign upcoming_school_count = 0 %}
{% for event in school_events %}
  {% assign event_end = event.end_date | default: event.start_date | date: "%Y%m%d" %}
  {% if event_end >= today %}
    {% assign upcoming_school_count = upcoming_school_count | plus: 1 %}
### [{{ event.title }}]({{ event.url | relative_url }})

**{% if event.end_date %}{{ event.start_date | date: "%-d %B %Y" }} – {{ event.end_date | date: "%-d %B %Y" }}{% else %}{{ event.start_date | date: "%-d %B %Y" }}{% endif %}{% if event.location %} · {{ event.location }}{% endif %}**

{{ event.content | markdownify | remove: '<p>' | remove: '</p>' | strip }}

{% endif %}
{% endfor %}

{% if upcoming_school_count == 0 %}
No upcoming schools have been added yet.
{% endif %}

## Previous schools

CoRE-Math and its predecessor networks have organised international mathematics schools since 2004.

[View previous schools<span class="link-arrow">&nbsp;→</span>]({{ "/education/schools/" | relative_url }})
