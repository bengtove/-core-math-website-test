---
title: "Member university photograph credits"
permalink: /photo-credits/
---

# Member university photograph credits

These photographs illustrate the [CoRE-Math member universities]({{ '/network-partnerships/' | relative_url }}). Copyright remains with the named creators except for the public-domain photograph. Each image is made available under its own licence below; these image licences do not apply to unrelated website content.

{% for member in site.data.member_universities %}
{% assign photo = site.data.member_photographs[member.photo_id] %}
<section id="{{ photo.id }}">
<h2>{{ member.name | escape }}</h2>
<p><a href="{{ photo.source_url }}">{{ photo.title | escape }}</a> — {{ photo.creator | escape }}. <a href="{{ photo.licence_url }}" rel="license">{{ photo.licence | escape }}</a>.</p>
<p>{{ photo.description | escape }}</p>
{% if photo.copyright_notice != empty %}<p>{{ photo.copyright_notice | escape }}</p>{% endif %}
<p><strong>Website changes:</strong> {{ photo.modifications | escape }} The displayed crop and website derivative retain the licence stated above.</p>
<p><strong>Reuse conditions:</strong> {{ photo.conditions | escape }}</p>
<p><a href="{{ photo.source_url }}">Original photograph and source record</a> · <a href="{{ photo.website_image_path | relative_url }}">Website image</a></p>
</section>
{% endfor %}
