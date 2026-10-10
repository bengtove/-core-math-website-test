---
homepage: true
---

<section class="home-hero">
  <div class="home-hero-image">
    <img src="{{ '/assets/images/news/560c14_574ae92fac3f4e6da79ed0326d46f997~mv2.jpeg.avif' | relative_url }}" alt="Young people taking part in a mathematics competition">
    <div class="home-hero-identity">
      <h1 class="home-hero-name">CoRE-Math</h1>
      <p class="home-hero-fullname">Africa–Europe Cluster of Research Excellence in Mathematics</p>
    </div>
  </div>
  <div class="home-hero-intro">
    <p class="home-lead">CoRE-Math brings together universities, research groups, networks and partner organisations in Africa and Europe to strengthen research, postgraduate education and the contribution of mathematics to society.</p>
    <p><a class="home-text-link action-link" href="{{ '/about/' | relative_url }}">About CoRE-Math<span class="link-arrow">&nbsp;→</span></a></p>
  </div>
</section>

<section class="home-section home-focus">
  <div class="home-section-heading">
    <p class="home-eyebrow">What we do</p>
    <h2>Mathematics across universities, countries and generations</h2>
  </div>
  <div class="home-focus-grid">
    <article class="home-editorial-entry">
      <h3><a href="{{ '/research/' | relative_url }}">Research</a></h3>
      <p>Connecting research groups and researchers across Africa and Europe through collaboration, projects, seminars and scientific exchange.</p>
      <a class="home-text-link action-link" href="{{ '/research/' | relative_url }}">Explore research<span class="link-arrow">&nbsp;→</span></a>
    </article>
    <article class="home-editorial-entry">
      <h3><a href="{{ '/education/' | relative_url }}">Education</a></h3>
      <p>Strengthening postgraduate education through doctoral collaboration, schools, fellowships, mobility and shared supervision.</p>
      <a class="home-text-link action-link" href="{{ '/education/' | relative_url }}">Explore education<span class="link-arrow">&nbsp;→</span></a>
    </article>
    <article class="home-editorial-entry">
      <h3><a href="{{ '/outreach/' | relative_url }}">Outreach</a></h3>
      <p>Connecting mathematics with young people, teachers, competitions, industry and wider society.</p>
      <a class="home-text-link action-link" href="{{ '/outreach/' | relative_url }}">Explore outreach<span class="link-arrow">&nbsp;→</span></a>
    </article>
  </div>
</section>

<section class="home-section">
  <div class="home-section-intro">
    <div class="home-section-heading">
      <p class="home-eyebrow">Across Africa and Europe</p>
      <h2>One network, 17 universities</h2>
    </div>
  </div>
  <p class="home-network-copy">CoRE-Math connects eight African and nine European universities, building on long-standing partnerships and creating new connections in research, postgraduate education, mobility and engagement with society.</p>
  <p class="home-section-link"><a class="home-text-link action-link" href="{{ '/network-partnerships/' | relative_url }}">Meet the network<span class="link-arrow">&nbsp;→</span></a></p>
</section>

<section class="home-section home-news">
  <div class="home-section-intro">
    <div class="home-section-heading">
      <p class="home-eyebrow">From the network</p>
      <h2>Latest news</h2>
    </div>
  </div>
  <div class="home-news-grid">
    {% for post in site.posts limit:3 %}
    <article class="home-news-item home-editorial-entry">
      {% if post.image %}
      <a class="home-news-image" href="{{ post.url | relative_url }}"><img src="{{ post.image | relative_url }}" alt=""></a>
      {% endif %}
      <p class="home-news-meta">{{ post.date | date: "%-d %B %Y" }}{% if post.location %} · {{ post.location }}{% endif %}</p>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      {% assign post_summary = post.home_excerpt | default: post.excerpt %}
      <p>{{ post_summary | strip_html | truncatewords: 28 }}</p>
    </article>
    {% endfor %}
  </div>
  <p class="home-section-link"><a class="home-text-link action-link" href="{{ '/news-events/' | relative_url }}">More news<span class="link-arrow">&nbsp;→</span></a></p>
</section>

<section class="home-section home-upcoming">
  <div class="home-section-intro">
    <div class="home-section-heading">
      <p class="home-eyebrow">Looking ahead</p>
      <h2>Upcoming events</h2>
    </div>
  </div>
  <div class="home-event-grid">
    <article class="home-editorial-entry">
      <p class="home-news-meta">19–30 July 2027 · Lusaka, Zambia</p>
      <h3><a href="{{ '/events/2027-topological-data-analysis-lusaka/' | relative_url }}">Summer School on Topological Data Analysis and Applications</a></h3>
      <p>An intensive two-week school introducing topological data analysis and its applications, bringing together postgraduate students and researchers.</p>
    </article>
    <article class="home-editorial-entry">
      <p class="home-news-meta">19–30 July 2027 · Kampala, Uganda</p>
      <h3><a href="{{ '/events/2027-algebraic-enumerative-combinatorics/' | relative_url }}">School on Algebraic and Enumerative Combinatorics</a></h3>
      <p>A two-week school exploring algebraic and enumerative combinatorics, with lectures and opportunities for interaction among postgraduate students and researchers.</p>
    </article>
  </div>
  <p class="home-section-link"><a class="home-text-link action-link" href="{{ '/news-events/' | relative_url }}">More events<span class="link-arrow">&nbsp;→</span></a></p>
</section>

<section class="home-section home-projects">
  <p class="home-eyebrow">Working together</p>
  <div class="home-projects-grid">
    <div class="home-projects-column home-editorial-entry">
      <h2>Programmes &amp; Projects</h2>
      <p>Schools, fellowships, industrial mathematics, research projects and institutional collaborations turn the network into concrete activity.</p>
      <a class="home-text-link action-link" href="{{ '/projects/' | relative_url }}">Explore programmes and projects<span class="link-arrow">&nbsp;→</span></a>
    </div>
    <div class="home-projects-column home-editorial-entry">
      <h2>Opportunities</h2>
      <p>Explore funding opportunities, fellowships, research visits and other possibilities for collaboration and professional development.</p>
      <a class="home-text-link action-link" href="{{ '/opportunities/' | relative_url }}">Explore opportunities<span class="link-arrow">&nbsp;→</span></a>
    </div>
  </div>
</section>
