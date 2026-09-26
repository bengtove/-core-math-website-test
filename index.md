---
---

# CoRE-Math

## Africa–Europe collaboration in the mathematical sciences

CoRE-Math brings together universities, research groups, networks and partner organisations in Africa and Europe to strengthen research collaboration, postgraduate education and the contribution of mathematics to society.

## Latest

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url | relative_url }})

**{{ post.date | date: "%-d %B %Y" }}{% if post.location %} · {{ post.location }}{% endif %}**

{{ post.excerpt }}
{% endfor %}

## About CoRE-Math

CoRE-Math is an ARUA–The Guild Cluster of Research Excellence in Mathematical Sciences.
