---
title: "Current PhD students"
permalink: /education/phd-students/
---

# Current PhD students

Current PhD students reported by the participating ISP-supported mathematics environments. Research topics are included where available.

{% assign phd_institutions = "Addis Ababa University|Makerere University|University of Nairobi|University of Rwanda|University of Dar es Salaam|University of Zambia" | split: "|" %}

{% for institution in phd_institutions %}
## {{ institution }}

{% assign students = site.data.phd_students | where: "institution", institution %}
{% for student in students %}
**{{ student.name }}**{% if student.topic %}  
*{{ student.topic | newline_to_br }}*{% endif %}{% if student.start_year %}  
Started {{ student.start_year }}{% endif %}{% if student.research_group %}  
Research group: {{ student.research_group }}{% endif %}{% if student.collaboration %}  
Collaboration: {{ student.collaboration }}{% endif %}

{% endfor %}
{% endfor %}
