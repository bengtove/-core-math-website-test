---
title: "Kampala SGI 2026"
project_id: "kampala-sgi-2026"
programme: "study-groups-with-industry"
location: "Kampala, Uganda"
activities:
  - title: "Mathematics–Industry Contact Workshop"
    activity_type: "workshop"
    date: "June 2026"
    location: "Kampala, Uganda"
    description: "A contact workshop bringing mathematics and industry participants together ahead of the Study Group with Industry."
  - title: "Study Group with Industry"
    activity_type: "study_group"
    start_date: 2026-09-21
    location: "Kampala, Uganda"
    description: "A collaborative study group working on problems originating outside academia."
---

# Kampala SGI 2026

{% assign programme = site.programmes | where: "programme_id", page.programme | first %}
**Programme:** [{{ programme.title }}]({{ programme.url | relative_url }})

**Location:** {{ page.location }}

## Activities

{% for activity in page.activities %}
### {{ activity.title }}

**Type:** {{ activity.activity_type | replace: "_", " " | capitalize }}

{% if activity.start_date %}**Starts:** {{ activity.start_date | date: "%-d %B %Y" }}{% else %}**Date:** {{ activity.date }}{% endif %}

**Location:** {{ activity.location }}

{{ activity.description }}
{% endfor %}

## Related news

{% assign related_posts = site.posts | where: "project", page.project_id %}
{% for post in related_posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%-d %B %Y" }}
{% endfor %}
