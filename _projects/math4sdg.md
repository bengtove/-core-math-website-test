---
layout: default
title: "Mathematics for Sustainable Development (Math4SDG)"
project_id: "math4sdg"
programme: "norhed-ii"
---

# Mathematics for Sustainable Development (Math4SDG)

{% assign programme = site.programmes | where: "programme_id", page.programme | first %}
**Programme:** [{{ programme.title }}]({{ programme.url | relative_url }})

Math4SDG is a NORHED II capacity-building project bringing together the University of Dar es Salaam, Makerere University and the University of Bergen. Its purpose is to strengthen mathematics research and education in Tanzania and Uganda through research, PhD training, curriculum development, mathematics education, outreach and engagement beyond the universities.

**Period:** 1 January 2021 – 31 December 2026<br>
**Funding:** Norad, NORHED II<br>
**Grant:** NOK 19,996,239<br>
**Partners:** University of Dar es Salaam, Makerere University and University of Bergen

## About the project

Math4SDG combines capacity development with research, postgraduate training and mathematics education. It is intended to strengthen mathematical research at the University of Dar es Salaam and Makerere University, support the development of relevant programmes in mathematics and mathematics education, and increase the departments’ interaction with industry and society.

## Research and PhD training

The project supports 11 PhD students at Makerere University and the University of Dar es Salaam: seven in applied mathematics or statistics and four in mathematics education. The students are trained through the universities’ existing PhD programmes and are supervised by local, regional and Norwegian researchers.

The PhD programme is connected with the project’s wider research and capacity-development work, including curriculum review, research collaboration and the dissemination of findings. The project website reports that eight of the 11 students have completed their degrees and that their research has contributed to publications in international peer-reviewed journals; the remaining three students are in the final stages of their programmes.

## Education and outreach

Beyond the PhD programme, Math4SDG has supported the review of mathematics and mathematics-education curricula, training for teachers in the use of mathematical software, and school outreach in Tanzania and Uganda. Activities have also included mathematics and science camps, work on digital materials for mathematics learning, and workshops through which researchers have presented findings to education authorities and other external stakeholders.

## African–Nordic conferences

African–Nordic conferences have formed part of the project’s regional and international research collaboration. The first conference was held at Makerere University in October 2022. The [Second African–Nordic Conference in Mathematics]({{ "/news/2026/the-second-african-nordic-conference-in-mathematics/" | relative_url }}) was held in Arusha, Tanzania, on 11–14 August 2026 under the theme “Collaborative Research in Mathematics and Mathematics Education for Sustainable Development.” Organised through Math4SDG in collaboration with CoRE-Math, the International Science Programme and Sida, it brought together 104 participants from 14 countries.

The Arusha conference was an important concluding activity, while the formal Math4SDG project period continues until 31 December 2026.

Math4SDG predates CoRE-Math and is funded and administered through NORHED II and its three partner universities. Its research collaboration, postgraduate training, mathematics education and regional activities form part of the foundation on which CoRE-Math now builds.

## Links

- [Math4SDG project website — University of Dar es Salaam](https://math4sdg.udsm.ac.tz/)
- [University of Bergen: Math4SDG](https://www4.uib.no/en/research/research-groups/fluid-mechanics)
- [Norad: NORHED II portfolio 2021–2026](https://www.norad.no/contentassets/33039772c5f340b8883c1c3147cdbd54/norhed-ii-portfolio-for-2021-2026.pdf)

## Related news

{% assign related_posts = site.posts | where: "project", page.project_id %}
{% for post in related_posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%-d %B %Y" }}
{% endfor %}
