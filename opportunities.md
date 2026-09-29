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
    <h3><a href="{{ '/programmes/core-math-fellowships/' | relative_url }}">Uppsala University fellowships</a></h3>
  </div>
  <div class="fellowship-entry">
    <h3><a href="{{ '/programmes/core-math-fellowships/' | relative_url }}">University of KwaZulu-Natal fellowships</a></h3>
  </div>
</div>

## Funding opportunities

The opportunities below are current external funding opportunities selected from the ISP Mathematics Funding Database.

<div class="opportunity-filters" aria-label="Filter funding opportunities">
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
  <div class="opportunity-list" data-opportunity-list="open">
    {% for opportunity in open_calls %}
      <article class="opportunity-entry"
        data-opportunity
        data-programme="{{ opportunity.programme | escape }}"
        data-deadline="{{ opportunity.deadline | escape }}"
        data-support-type="{{ opportunity.support_type | escape }}"
        data-career-stage="{{ opportunity.career_stage | escape }}">
        <h4>{% if opportunity.url %}<a href="{{ opportunity.url | escape }}">{{ opportunity.programme | escape }}</a>{% else %}{{ opportunity.programme | escape }}{% endif %}</h4>
        {% if opportunity.funder %}<p class="opportunity-funder">{{ opportunity.funder | escape }}</p>{% endif %}
        {% if opportunity.description %}<p class="opportunity-description">{{ opportunity.description | escape }}</p>{% endif %}
        <p class="opportunity-meta">
          {% if opportunity.deadline %}<span>Deadline: {{ opportunity.deadline | escape }}</span>{% endif %}
          {% if opportunity.support_type %}<span>{{ opportunity.support_type | escape }}</span>{% endif %}
          {% if opportunity.career_stage %}<span>{{ opportunity.career_stage | escape }}</span>{% endif %}
        </p>
        {% if opportunity.deadline_note %}<p class="opportunity-deadline-note">{{ opportunity.deadline_note | escape }}</p>{% endif %}
      </article>
    {% endfor %}
  </div>
</section>

<section class="opportunity-section" data-opportunity-section>
  <h3>Rolling opportunities</h3>
  <div class="opportunity-list" data-opportunity-list="rolling">
    {% for opportunity in rolling_opportunities %}
      <article class="opportunity-entry"
        data-opportunity
        data-programme="{{ opportunity.programme | escape }}"
        data-deadline="{{ opportunity.deadline | escape }}"
        data-support-type="{{ opportunity.support_type | escape }}"
        data-career-stage="{{ opportunity.career_stage | escape }}">
        <h4>{% if opportunity.url %}<a href="{{ opportunity.url | escape }}">{{ opportunity.programme | escape }}</a>{% else %}{{ opportunity.programme | escape }}{% endif %}</h4>
        {% if opportunity.funder %}<p class="opportunity-funder">{{ opportunity.funder | escape }}</p>{% endif %}
        {% if opportunity.description %}<p class="opportunity-description">{{ opportunity.description | escape }}</p>{% endif %}
        <p class="opportunity-meta">
          {% if opportunity.deadline %}<span>Deadline: {{ opportunity.deadline | escape }}</span>{% endif %}
          {% if opportunity.support_type %}<span>{{ opportunity.support_type | escape }}</span>{% endif %}
          {% if opportunity.career_stage %}<span>{{ opportunity.career_stage | escape }}</span>{% endif %}
        </p>
        {% if opportunity.deadline_note %}<p class="opportunity-deadline-note">{{ opportunity.deadline_note | escape }}</p>{% endif %}
      </article>
    {% endfor %}
  </div>
</section>

<p class="opportunity-no-results" data-opportunity-no-results hidden>No opportunities match these filters.</p>

## Full funding database

The full ISP Mathematics Funding Database also includes programmes for which there is currently no open call and provides a broader overview of funding possibilities.

[View the full ISP Mathematics Funding Database →](https://docs.superhuman.com/d/_dtwgdrEvtAq/Mathematics-funding-database_su79Sp_C)

</div>

<script src="{{ '/assets/js/opportunities.js' | relative_url }}" defer></script>
