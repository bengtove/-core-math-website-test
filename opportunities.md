---
title: "Opportunities"
permalink: /opportunities/
opportunities_page: true
---

# Opportunities

<div class="opportunities-page" markdown="1">

## Fellowships

Fellowship programmes at Uppsala University and the University of KwaZulu-Natal support research visits and mobility within the CoRE-Math network. They provide opportunities for postgraduate students and researchers to develop research collaborations, work with colleagues at other CoRE-Math institutions and strengthen connections across the network.

<div class="fellowship-list">
  <section class="fellowship-entry">
    <h3>Uppsala University fellowships</h3>
    <p>Research visits and mobility with Uppsala University for postgraduate students and researchers from CoRE-Math universities.</p>
    <p class="entry-link"><a class="action-link" href="{{ '/programmes/core-math-fellowships/uppsala-university/' | relative_url }}" aria-label="About the Uppsala University fellowship scheme">About the fellowship scheme<span class="link-arrow">&nbsp;→</span></a></p>
  </section>
  <section class="fellowship-entry">
    <h3>University of KwaZulu-Natal fellowships</h3>
    <p>Four fully funded fellowships are available for PhD students, postdoctoral researchers and senior researchers from African CoRE-Math universities to undertake research visits of up to three months at the University of KwaZulu-Natal in 2027.</p>
    <p class="fellowship-deadline" data-fellowship-deadline="31 October 2026"><span class="fellowship-deadline-status">Application deadline:</span> <time datetime="2026-10-31">31 October 2026</time></p>
    <p class="entry-link"><a class="action-link" href="{{ '/programmes/core-math-fellowships/university-of-kwazulu-natal/' | relative_url }}" aria-label="About the University of KwaZulu-Natal fellowship scheme">About the fellowship scheme<span class="link-arrow">&nbsp;→</span></a></p>
  </section>
</div>

## Funding opportunities

The opportunities below are selected from the ISP Mathematics Funding Database and are intended for postgraduate students, researchers and institutions seeking support for research, mobility, training and collaboration. The full database also includes programmes without currently open calls.

Deadlines and conditions may change. Always verify the information on the funder's website before applying.

<p class="opportunity-database-link"><a class="action-link" href="https://docs.superhuman.com/d/_dtwgdrEvtAq/Mathematics-funding-database_su79Sp_C" target="_blank" rel="noopener noreferrer">Explore the full ISP Mathematics Funding Database<span class="link-arrow">&nbsp;→</span></a></p>

<div class="opportunity-filters" aria-label="Filter funding opportunities">
  <label for="funder-filter">
    Funder
    <select id="funder-filter">
      <option value="">All funders</option>
    </select>
  </label>
  <label for="support-type-filter">
    Support type
    <select id="support-type-filter">
      <option value="">All support types</option>
    </select>
  </label>
  <label for="career-stage-filter">
    Applicant category
    <select id="career-stage-filter">
      <option value="">All applicant categories</option>
    </select>
  </label>
</div>

{% assign open_calls = site.data.open_opportunities | where: "status", "Open" %}
{% assign rolling_opportunities = site.data.open_opportunities | where: "status", "Rolling" %}

<section class="opportunity-section" data-opportunity-section>
  <h3>Open calls</h3>
  <p class="opportunity-section-note">Sorted by application deadline, earliest first.</p>
  <div class="opportunity-list" data-opportunity-list="open">
    {% for opportunity in open_calls %}
      <article class="opportunity-entry"
        data-opportunity
        data-programme="{{ opportunity.programme | escape }}"
        data-funder="{{ opportunity.funder | escape }}"
        data-deadline="{{ opportunity.deadline | escape }}"
        data-support-type="{{ opportunity.support_type | escape }}"
        data-career-stage="{{ opportunity.career_stage | escape }}">
        <h4>{% if opportunity.url != empty %}<a href="{{ opportunity.url | escape }}" target="_blank" rel="noopener noreferrer">{{ opportunity.programme | escape }}</a>{% else %}{{ opportunity.programme | escape }}{% endif %}</h4>
        {% if opportunity.funder != empty %}<p class="opportunity-funder">{{ opportunity.funder | escape }}</p>{% endif %}
        {% if opportunity.description != empty %}<p class="opportunity-description">{{ opportunity.description | escape }}</p>{% endif %}
        <div class="opportunity-meta">
          {% if opportunity.deadline != empty %}<p class="opportunity-deadline"><span class="opportunity-meta-label">Deadline:</span> <span class="opportunity-deadline-value">{{ opportunity.deadline | escape }}</span></p>{% endif %}
          {% if opportunity.support_type != empty or opportunity.career_stage != empty %}<p class="opportunity-details">{% if opportunity.support_type != empty %}<span><span class="opportunity-meta-label">Support type:</span> {{ opportunity.support_type | escape }}</span>{% endif %}{% if opportunity.career_stage != empty %}{% if opportunity.support_type != empty %} <span aria-hidden="true">·</span> {% endif %}<span><span class="opportunity-meta-label">Applicant category:</span> {{ opportunity.career_stage | escape }}</span>{% endif %}</p>{% endif %}
          {% if opportunity.deadline_note != empty %}<p class="opportunity-deadline-note">{{ opportunity.deadline_note | escape }}</p>{% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<section class="opportunity-section" data-opportunity-section>
  <h3>Rolling opportunities</h3>
  <p class="opportunity-section-note">Opportunities without a fixed closing date, listed alphabetically.</p>
  <div class="opportunity-list" data-opportunity-list="rolling">
    {% for opportunity in rolling_opportunities %}
      <article class="opportunity-entry"
        data-opportunity
        data-programme="{{ opportunity.programme | escape }}"
        data-funder="{{ opportunity.funder | escape }}"
        data-deadline="{{ opportunity.deadline | escape }}"
        data-support-type="{{ opportunity.support_type | escape }}"
        data-career-stage="{{ opportunity.career_stage | escape }}">
        <h4>{% if opportunity.url != empty %}<a href="{{ opportunity.url | escape }}" target="_blank" rel="noopener noreferrer">{{ opportunity.programme | escape }}</a>{% else %}{{ opportunity.programme | escape }}{% endif %}</h4>
        {% if opportunity.funder != empty %}<p class="opportunity-funder">{{ opportunity.funder | escape }}</p>{% endif %}
        {% if opportunity.description != empty %}<p class="opportunity-description">{{ opportunity.description | escape }}</p>{% endif %}
        <div class="opportunity-meta">
          {% if opportunity.deadline != empty %}<p class="opportunity-deadline"><span class="opportunity-meta-label">Deadline:</span> <span class="opportunity-deadline-value">{{ opportunity.deadline | escape }}</span></p>{% endif %}
          {% if opportunity.support_type != empty or opportunity.career_stage != empty %}<p class="opportunity-details">{% if opportunity.support_type != empty %}<span><span class="opportunity-meta-label">Support type:</span> {{ opportunity.support_type | escape }}</span>{% endif %}{% if opportunity.career_stage != empty %}{% if opportunity.support_type != empty %} <span aria-hidden="true">·</span> {% endif %}<span><span class="opportunity-meta-label">Applicant category:</span> {{ opportunity.career_stage | escape }}</span>{% endif %}</p>{% endif %}
          {% if opportunity.deadline_note != empty %}<p class="opportunity-deadline-note">{{ opportunity.deadline_note | escape }}</p>{% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<p class="visually-hidden" data-opportunity-filter-status role="status" aria-live="polite" aria-atomic="true"></p>
<p class="opportunity-no-results" data-opportunity-no-results hidden>No opportunities match these filters.</p>

</div>

<script src="{{ '/assets/js/opportunities.js' | relative_url }}?v=deadline-filter" defer></script>
