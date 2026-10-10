---
title: "Network & Partnerships"
permalink: /network-partnerships/
network_partnerships: true
---

# Network & Partnerships

CoRE-Math consists of 17 member universities and works with mathematical organisations and networks through formal and other partnerships.

## Member universities

The 17 member universities form the nodes of CoRE-Math. The network brings together long-standing collaborations and newer connections in research, postgraduate education, mobility and engagement with society.

<div class="node-grid">

<article class="node-card node-card-network">
  <div class="node-card-image"><img src="{{ '/assets/images/branding/core-math-mark.png' | relative_url }}" alt="CoRE-Math mark"></div>
  <div class="node-card-body">
    <p class="node-card-country">Africa & Europe</p>
    <h3>One network, 17 universities</h3>
    <p>CoRE-Math connects eight African and nine European universities. Some relationships go back several decades; others are developing through the Cluster. Together they create a platform for research collaboration, postgraduate education, mobility, schools, industry engagement and joint initiatives across institutions and countries.</p>
  </div>
</article>

{% for member in site.data.member_universities %}
  {% assign member_image = member.image %}
  {% unless member_image contains '://' %}
    {% assign member_image = member_image | relative_url %}
  {% endunless %}
  <article class="node-card">
    <div class="node-card-image"><img src="{{ member_image }}" alt="{{ member.image_alt }}"></div>
    <div class="node-card-body">
      <p class="node-card-country">{{ member.country }}</p>
      <h3><a href="{{ member.url }}">{{ member.name }}</a></h3>
      <p>{{ member.introduction }}</p>
      <button class="node-card-more" type="button" aria-haspopup="dialog" aria-controls="member-portrait-{{ forloop.index }}" data-member-portrait-trigger="member-portrait-{{ forloop.index }}">Read more<span class="link-arrow">&nbsp;→</span></button>
    </div>
  </article>
{% endfor %}

</div>

{% for member in site.data.member_universities %}
  <dialog class="member-portrait-dialog" id="member-portrait-{{ forloop.index }}" aria-labelledby="member-portrait-heading-{{ forloop.index }}">
    <div class="member-portrait-dialog__surface">
      <header class="member-portrait-dialog__header">
        <div>
          <p class="member-portrait-dialog__country">{{ member.country }}</p>
          <h2 id="member-portrait-heading-{{ forloop.index }}">{{ member.name }}</h2>
        </div>
        <button class="member-portrait-dialog__close" type="button" aria-label="Close" data-member-portrait-close>&times;</button>
      </header>
      <div class="member-portrait-dialog__content">
        <p>{{ member.portrait }}</p>
        <p class="member-portrait-dialog__link"><a class="action-link" href="{{ member.url }}">Visit {{ member.name }} website<span class="link-arrow">&nbsp;→</span></a></p>
      </div>
    </div>
  </dialog>
{% endfor %}

## Formal partners

<div class="partner-grid">
  <article class="partner-card">
    <h3><a href="https://ecmiindmath.org/">European Consortium for Mathematics in Industry (ECMI)</a></h3>
    <p>ECMI and CoRE-Math collaborate in industrial mathematics, including links between mathematics and industry, Study Groups with Industry, and related education and research activities. The partnership connects CoRE-Math with European industrial mathematics networks and supports exchange among researchers, students and external partners.</p>
  </article>
  <article class="partner-card">
    <h3><a href="https://www.iciam.org/">International Council for Industrial and Applied Mathematics (ICIAM)</a></h3>
    <p>ICIAM connects CoRE-Math with the international industrial and applied mathematics community. The partnership supports the development and visibility of applied mathematics in Africa and provides an international context for CoRE-Math’s work in industrial mathematics, research and education.</p>
  </article>
  <article class="partner-card">
    <h3><a href="https://www.uu.se/en/centre/international-science-programme">International Science Programme (ISP)</a></h3>
    <p>ISP at Uppsala University is a formal partner of CoRE-Math. Through agreements with six African member universities, it supports long-term development of mathematical research and postgraduate education, building on decades of collaboration through EAUMP and support to Addis Ababa University, and contributing to CoRE-Math’s coordination and development.</p>
  </article>
</div>

## Other partners

<div class="partner-grid">
  <article class="partner-card">
    <h3><a href="https://www.cimpa.info/en">Centre International de Mathématiques Pures et Appliquées (CIMPA)</a></h3>
    <p>CoRE-Math collaborates with CIMPA through research schools that bring international researchers together with postgraduate students and early-career mathematicians in Africa. These activities support advanced study, research interaction and the development of regional mathematical communities, while strengthening links across institutions and countries.</p>
  </article>
  <article class="partner-card">
    <h3><a href="https://www.coe-mass.ac.za/">Centre of Excellence in Mathematical and Statistical Sciences (CoE-MaSS)</a></h3>
    <p>CoE-MaSS is a South African network for pure mathematics, applied mathematics and statistics, hosted by the University of the Witwatersrand. CoRE-Math is developing collaboration with CoE-MaSS in research, postgraduate education, industrial mathematics, schools and workshops, early-career development and scientific networking.</p>
  </article>
  <article class="partner-card">
    <h3><a href="https://www.ictp.it/">International Centre for Theoretical Physics (ICTP)</a></h3>
    <p>ICTP has long collaborated with universities and networks that now participate in CoRE-Math. The collaboration includes schools and other activities supporting research and postgraduate education in mathematics, bringing international researchers together with students and early-career mathematicians from across Africa and Europe.</p>
  </article>
  <article class="partner-card">
    <h3><a href="https://www.up.ac.za/nga-mass">National Graduate Academy for Mathematical and Statistical Sciences (NGA(MaSS))</a></h3>
    <p>CoRE-Math is developing collaboration with NGA(MaSS) in postgraduate education, research and networking, industrial mathematics, schools and workshops, early-career development and joint funding initiatives.</p>
  </article>
</div>
