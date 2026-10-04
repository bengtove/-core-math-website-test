---
title: "News & Events"
permalink: /news-events/
news_events: true
---

# News & Events

## Upcoming Events

{% assign today = site.time | date: "%Y%m%d" %}
{% assign events_by_date = site.events | sort: "start_date" %}
{% assign upcoming_count = 0 %}
<div class="event-list">
{% for event in events_by_date %}
  {% assign event_end = event.end_date | default: event.start_date | date: "%Y%m%d" %}
  {% if event_end >= today %}
    {% assign upcoming_count = upcoming_count | plus: 1 %}
    <div class="event-item">
      <div class="event-date">
        {% if event.end_date %}
          {{ event.start_date | date: "%-d %B %Y" }} – {{ event.end_date | date: "%-d %B %Y" }}
        {% else %}
          {{ event.start_date | date: "%-d %B %Y" }}
        {% endif %}
      </div>
      <div>
        <a class="event-title" href="{{ event.url | relative_url }}">{{ event.title }}</a>
        {% if event.location %}<div class="event-location">{{ event.location }}</div>{% endif %}
      </div>
    </div>
  {% endif %}
{% endfor %}
</div>
{% if upcoming_count == 0 %}
<p>No upcoming events have been added yet.</p>
{% endif %}

## Latest News

<div class="latest-news">
{% for post in site.posts limit:6 %}
  <article class="news-card{% if post.image %} news-card--with-image{% endif %}">
    {% if post.image %}
    <a class="news-card-image-link" href="{{ post.url | relative_url }}" aria-hidden="true" tabindex="-1">
      <img class="news-card-image" src="{{ post.image | relative_url }}" alt="">
    </a>
    {% endif %}
    <div class="news-card-content">
      <div class="news-date">{{ post.date | date: "%-d %B %Y" }}</div>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p class="news-excerpt">{{ post.excerpt | strip_html | strip_newlines | truncatewords: 28 }}</p>
    </div>
  </article>
{% endfor %}
</div>

## Archive

<div class="news-archive-years">
  <a href="{{ "/news/archive/2026/" | relative_url }}">2026</a>
  <span aria-hidden="true">·</span>
  <a href="{{ "/news/archive/2025/" | relative_url }}">2025</a>
  <span aria-hidden="true">·</span>
  <a href="{{ "/news/archive/2024/" | relative_url }}">2024</a>
</div>
