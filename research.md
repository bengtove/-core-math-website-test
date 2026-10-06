---
title: "Research"
permalink: /research/
research_page: true
---

# Research

Research within CoRE-Math brings together researchers across African and European universities through research groups, collaborative projects and international partnerships. Several regional research groups provide established platforms for collaboration in areas including algebra, combinatorics, applied probability and partial differential equations. Research collaboration is developed through workshops, research visits, joint publications and postgraduate research, strengthening existing research environments and creating opportunities for new collaborations across institutions and countries.

<div class="research-layout">
  <nav class="research-toc" aria-labelledby="research-toc-heading">
    <p class="research-toc-title" id="research-toc-heading">On this page</p>
    <ul>
      <li><a href="#research-groups">Research groups</a></li>
      <li><a href="#research-projects-and-collaborations">Research projects and collaborations</a></li>
      <li><a href="#seminars-and-webinars">Seminars and webinars</a></li>
      <li><a href="#publications">Publications</a></li>
    </ul>
  </nav>

  <div class="research-content">
    <section aria-labelledby="research-groups">
      <h2 id="research-groups">Research groups</h2>

      <p>CoRE-Math connects with several regional research groups that provide platforms for collaboration, postgraduate training and scientific exchange.</p>

      <ul>
      {% for research_group in site.research_groups %}
        <li><p><a href="{{ research_group.url | relative_url }}">{{ research_group.title }}</a></p></li>
      {% endfor %}
      </ul>
    </section>

    <section aria-labelledby="research-projects-and-collaborations">
      <h2 id="research-projects-and-collaborations">Research projects and collaborations</h2>

      <p>Research within CoRE-Math also develops through projects and collaborations between participating universities and their partners. These connect mathematical research with areas including statistics, Earth observation, health, sustainable development and renewable energy, while creating opportunities for postgraduate researchers and longer-term collaboration between research environments.</p>

      <ul>
        <li><strong>Applied Mathematics for Earth Observation</strong> — a Finland–Rwanda collaboration using applied mathematics and Earth observation to address environmental and societal challenges.</li>
        <li><strong>Health Data Synergy: Bridging Medicine and Mathematics</strong> — connects mathematics and medicine around the use and analysis of health data.</li>
        <li><strong>Lake Victoria project</strong> — a developing interdisciplinary research collaboration around challenges connected with the Lake Victoria region.</li>
        <li><strong>Mathematics for Sustainable Development (Math4SDG)</strong> — supports research collaboration, PhD training and mathematics education through the University of Dar es Salaam, Makerere University and the University of Bergen.</li>
        <li><strong>SPIRIT</strong> — a University of Geneva–University of Rwanda collaboration developing statistical methods for Small Area Estimation, with applications to gender disparities in Rwanda.</li>
      </ul>

      <p><a href="{{ "/projects/" | relative_url }}">View projects and collaborations →</a></p>
    </section>

    <section aria-labelledby="seminars-and-webinars">
      <h2 id="seminars-and-webinars">Seminars and webinars</h2>

      <p>Recurring online seminars and webinar series provide opportunities for researchers and postgraduate students to follow current research, present their work and build connections across institutions and countries.</p>

      <h3 id="african-mathematics-seminar-afms">African Mathematics Seminar (AfMS)</h3>

      <p>An Africa-wide online mathematics seminar established in 2020 to connect mathematicians across the continent and provide a platform for African mathematical research. The series is currently inactive.</p>

      <p><a href="https://sites.google.com/view/africa-math-seminar/home">African Mathematics Seminar →</a></p>

      <h3 id="aecc-online-seminar-series">AECC Online Seminar Series</h3>

      <p>The African Enumerative Combinatorics Community (AECC) organises an online seminar series bringing together researchers in enumerative and algebraic combinatorics.</p>

      <p><a href="https://african-enumerative-combinatorics.github.io/">AECC seminars →</a></p>

      <h3 id="nithecs-seminars-and-colloquia">NITheCS seminars and colloquia</h3>

      <p>The National Institute for Theoretical and Computational Sciences (NITheCS) runs online and hybrid seminars, webinars and colloquia across the mathematical and computational sciences.</p>

      <p><a href="https://nithecs.ac.za/events/upcoming-events">NITheCS events →</a></p>
    </section>

    <section aria-labelledby="publications">
      <h2 id="publications">Publications</h2>

      <p><a href="{{ '/research/publications/' | relative_url }}">Selected publications from CoRE-Math nodes</a> — a curated collection of mathematical-sciences publications by researchers at the African CoRE-Math nodes, with links to research groups, projects and collaborations where known.</p>
    </section>
  </div>
</div>
