---
title: "Opportunities"
permalink: /opportunities/
---

# Opportunities

<div class="opportunities-page" markdown="1">

## Fellowships

Fellowship programmes at Uppsala University and the University of KwaZulu-Natal support research visits and mobility within the CoRE-Math network. They provide opportunities for postgraduate students and researchers to develop research collaborations, work with colleagues at other CoRE-Math institutions and strengthen connections across the network.

<div class="fellowship-list">
  <div class="fellowship-entry">
    <h3><a href="{{ '/programmes/core-math-fellowships/uppsala-university/' | relative_url }}">Uppsala University fellowships</a></h3>
  </div>
  <div class="fellowship-entry">
    <h3>University of KwaZulu-Natal fellowships</h3>
  </div>
</div>

## Funding opportunities

The opportunities below are current funding opportunities selected from the ISP Mathematics Funding Database. They are intended as a starting point for postgraduate students, researchers and institutions looking for funding for research, mobility, training and collaboration. The <a href="https://docs.superhuman.com/d/_dtwgdrEvtAq/Mathematics-funding-database_su79Sp_C" target="_blank" rel="noopener noreferrer">full ISP Mathematics Funding Database</a> also includes programmes for which there is currently no open call and provides a broader overview of funding possibilities.

For full details, eligibility requirements and application procedures, please consult the funder's website using the links below. Deadlines and other information may change, so applicants should always verify the current information with the funder.

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
    Career stage
    <select id="career-stage-filter">
      <option value="">All career stages</option>
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
          <div class="opportunity-meta-grid">
            <div class="opportunity-meta-column opportunity-meta-deadline">
              <span class="opportunity-meta-label">Deadline</span>
              <span class="opportunity-meta-value opportunity-deadline-value">{{ opportunity.deadline | escape }}</span>
            </div>
            <div class="opportunity-meta-column opportunity-meta-support">
              <span class="opportunity-meta-label">Support type</span>
              <span class="opportunity-meta-value">{{ opportunity.support_type | escape }}</span>
            </div>
            <div class="opportunity-meta-column opportunity-meta-career">
              <span class="opportunity-meta-label">Career stage</span>
              <span class="opportunity-meta-value">{{ opportunity.career_stage | escape }}</span>
            </div>
          </div>
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
          <div class="opportunity-meta-grid">
            <div class="opportunity-meta-column opportunity-meta-deadline">
              <span class="opportunity-meta-label">Deadline</span>
              <span class="opportunity-meta-value opportunity-deadline-value">{{ opportunity.deadline | escape }}</span>
            </div>
            <div class="opportunity-meta-column opportunity-meta-support">
              <span class="opportunity-meta-label">Support type</span>
              <span class="opportunity-meta-value">{{ opportunity.support_type | escape }}</span>
            </div>
            <div class="opportunity-meta-column opportunity-meta-career">
              <span class="opportunity-meta-label">Career stage</span>
              <span class="opportunity-meta-value">{{ opportunity.career_stage | escape }}</span>
            </div>
          </div>
          {% if opportunity.deadline_note != empty %}<p class="opportunity-deadline-note">{{ opportunity.deadline_note | escape }}</p>{% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<p class="opportunity-no-results" data-opportunity-no-results hidden>No opportunities match these filters.</p>

</div>

<script src="{{ '/assets/js/opportunities.js' | relative_url }}?v=funder-filter" defer></script>
