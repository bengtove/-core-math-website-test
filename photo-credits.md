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

## CoRE-Math 17-university collage

The three-row, six-column collage “Meet the 17 universities behind CoRE-Math!” uses the 17 photographs credited above, once each, with the CoRE-Math logo in the bottom-right cell. Read left to right, top to bottom:

- Row 1: Addis Ababa, Uppsala, Makerere, Linköping, Stellenbosch, Groningen.
- Row 2: Oslo, Dar es Salaam, Vienna, Bergen, KwaZulu-Natal, Stockholm.
- Row 3: Rwanda, Amsterdam, Zambia, LUT, Nairobi, CoRE-Math logo.

**Collage modifications by CoRE-Math:** recorded EXIF orientation applied where present; photographs proportionally resized and cropped to equal rectangular cells; JPEG encoding for the editable SVG and PNG export of the collection. No retouching, generative changes, colour grading or text overlays. The source links above provide access to the originals.

Each cropped photograph retains its original licence and notices listed above, including applicable ShareAlike or Free Art License conditions. The photographs remain separate components of a collection. Any copyright in CoRE-Math’s new selection and arrangement is offered under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This does not relicense the original photographs, change the public-domain status of the Dar es Salaam image, or apply to the separate CoRE-Math logo or trademark rights. No endorsement by the photographers or people shown is implied.

When redistributing the collage, retain the photographic credits, source and licence links, and this modification notice, or a conspicuous link to this page.
