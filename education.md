---
title: "Education"
permalink: /education/
education_page: true
---

<div class="education-page">
  <header class="education-intro">
    <h1>Education</h1>
    <p>Education within CoRE-Math focuses primarily on postgraduate training in the mathematical sciences. Through collaboration between universities in Africa and Europe, CoRE-Math creates opportunities for Master’s and PhD students to broaden their mathematical training, engage with active research environments and build international connections. Activities include intensive schools, mathematical modelling training, research-oriented workshops and mobility.</p>
  </header>

  <section class="education-section" aria-labelledby="doctoral-education-heading">
    <h2 id="doctoral-education-heading">Doctoral education</h2>
    <div class="education-prose">
      <p>Current PhD research at the African CoRE-Math nodes covers a broad range of mathematical sciences, from algebra, combinatorics and partial differential equations to mathematical modelling, optimisation and applications in health and other areas.</p>
      <p>The directory presents current PhD students reported by the participating ISP-supported mathematics environments. Research topics are included where available.</p>
      <p class="education-link"><a class="action-link" href="{{ "/education/phd-students/" | relative_url }}">Current PhD students<span class="link-arrow">&nbsp;→</span></a></p>
    </div>
  </section>

  <section class="education-section" aria-labelledby="schools-heading">
    <h2 id="schools-heading">Schools</h2>
    <p class="education-prose">CoRE-Math Schools build on a series of postgraduate mathematics schools that started in 2004 and have been organised annually since then. The schools have been supported by ICTP, ISP and other funders, with CIMPA becoming an important partner in recent years. They bring together postgraduate students and researchers for intensive study of mathematical topics, exposing students to topics and expertise that may not be available locally and creating opportunities for research contacts, thesis topics and collaboration.</p>

    <div class="school-list">
    {% for project in site.projects reversed %}
      {% if project.sections contains "education" %}
      <article class="school-entry">
        <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
        <p class="school-meta">{% if project.dates %}<span><strong>Date:</strong> {{ project.dates }}</span>{% endif %}{% if project.location %}<span><strong>Location:</strong> {{ project.location }}</span>{% endif %}</p>
      </article>
      {% endif %}
    {% endfor %}
    </div>

    <p class="education-link"><a class="action-link" href="{{ "/education/schools/" | relative_url }}">View previous schools<span class="link-arrow">&nbsp;→</span></a></p>
  </section>

  <section class="education-section" aria-labelledby="modelling-weeks-heading">
    <h2 id="modelling-weeks-heading">Modelling Weeks</h2>
    <div class="education-prose">
      <p>Modelling Weeks are educational activities in which students work in groups on mathematical modelling problems. They are designed particularly for Master's students and develop skills in mathematical modelling, teamwork and communication.</p>
      <p class="education-link"><a class="action-link" href="{{ "/programmes/study-groups-with-industry/" | relative_url }}">Industrial Mathematics programme<span class="link-arrow">&nbsp;→</span></a></p>
    </div>
  </section>

  <section class="education-section" aria-labelledby="mobility-fellowships-heading">
    <h2 id="mobility-fellowships-heading">Mobility and fellowships</h2>
    <p class="education-prose">Mobility and fellowships give postgraduate students and researchers opportunities to spend time in other academic environments, take part in research and training, and develop longer-term collaboration between institutions. CoRE-Math universities participate in several externally funded mobility and fellowship programmes connecting universities in Africa and Europe.</p>

    <div class="mobility-list">
      <article class="mobility-entry">
        <h3>CoRE-Math Fellowships</h3>
        <p>The CoRE-Math Fellowships support research visits and mobility between participating universities, strengthening research collaboration and providing opportunities for researchers at different career stages.</p>
        <p class="education-link"><a class="action-link" href="{{ "/programmes/core-math-fellowships/" | relative_url }}">CoRE-Math Fellowships<span class="link-arrow">&nbsp;→</span></a></p>
      </article>

      <article class="mobility-entry">
        <h3>Bergen–Makerere–UDSM mobility and postgraduate collaboration</h3>
        <p>The collaboration supports postgraduate education, student and staff mobility, research visits and research collaboration between the University of Bergen, Makerere University and the University of Dar es Salaam.</p>
        <p class="education-meta"><span>Funders:</span> Erasmus+ and NORSTIP</p>
      </article>

      <article class="mobility-entry">
        <h3>Makerere–Groningen mobility and research collaboration</h3>
        <p>The collaboration supports doctoral mobility and research visits between Makerere University and the University of Groningen.</p>
        <p class="education-meta"><span>Funder:</span> Erasmus+</p>
      </article>
    </div>
  </section>
</div>
