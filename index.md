---
---

# CoRE-Math

## Africa–Europe collaboration in the mathematical sciences

CoRE-Math brings together universities, research groups, networks and partner organisations in Africa and Europe to strengthen research collaboration, postgraduate education and the contribution of mathematics to society.

## Latest news

{% for post in site.posts limit:4 %}
### [{{ post.title }}]({{ post.url | relative_url }})

**{{ post.date | date: "%-d %B %Y" }}{% if post.location %} · {{ post.location }}{% endif %}**

{{ post.excerpt }}
{% endfor %}

[More news →]({{ "/news-events/" | relative_url }})

## Upcoming events

### [Summer School on Topological Data Analysis and Applications](https://indico.ictp.it/event/11447)

**19–30 July 2027 · Lusaka, Zambia**

### [Algebraic and Enumerative Combinatorics](https://cimpa.info/en/ecoles/algebraic-and-enumerative-combinatorics)

**19–30 July 2027 · Makerere University, Kampala, Uganda**

[More upcoming schools →]({{ "/programmes/core-math-schools/" | relative_url }})

## About CoRE-Math

CoRE-Math is an ARUA–The Guild Cluster of Research Excellence in Mathematical Sciences.
