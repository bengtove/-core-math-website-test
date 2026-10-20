---
title: "Past events"
permalink: /events/archive/
news_events: true
parent_context_url: /news-events/
parent_context_label: News & Events
---

# Past events

{% assign today = site.time | date: "%Y%m%d" %}
{% assign events_by_date = site.events | sort: "start_date" | reverse %}
{% assign past_event_count = 0 %}
{% assign current_year = "" %}
<div class="past-events">
{% for event in events_by_date %}
  {% assign event_end = event.end_date | default: event.start_date | date: "%Y%m%d" %}
  {% if event_end < today %}
    {% assign past_event_count = past_event_count | plus: 1 %}
    {% assign event_year = event.start_date | date: "%Y" %}
    {% if current_year != event_year %}
      {% if current_year != "" %}
      </div>
    </section>
      {% endif %}
      {% assign current_year = event_year %}
    <section class="past-events-year" aria-labelledby="past-events-{{ event_year }}">
      <h2 id="past-events-{{ event_year }}">{{ event_year }}</h2>
      <div class="event-list event-list--year">
    {% endif %}
    <div class="event-item">
      <div class="event-date">
        {% if event.end_date %}
          {% assign start_month = event.start_date | date: "%b" %}
          {% assign start_year = event.start_date | date: "%Y" %}
          {% assign end_month = event.end_date | date: "%b" %}
          {% assign end_year = event.end_date | date: "%Y" %}
          {% if start_month == end_month and start_year == end_year %}
            {{ event.start_date | date: "%-d" }}–{{ event.end_date | date: "%-d %b %Y" }}
          {% else %}
            {{ event.start_date | date: "%-d %b %Y" }} – {{ event.end_date | date: "%-d %b %Y" }}
          {% endif %}
        {% else %}
          {{ event.start_date | date: "%-d %b %Y" }}
        {% endif %}
      </div>
      <div>
        <a class="event-title" href="{{ event.url | relative_url }}">{{ event.title }}</a>
        {% if event.location %}<div class="event-location">{{ event.location }}</div>{% endif %}
      </div>
    </div>
  {% endif %}
{% endfor %}
{% if past_event_count > 0 %}
</div>
</section>
{% endif %}
</div>
{% if past_event_count == 0 %}
<p>No past events have been added yet.</p>
{% endif %}
