# Detail-page authoring conventions

This note supports consistent programme, project, research-group and event pages without requiring every page to have the same length or structure.

## Content model

- A **programme** is a continuing framework for related activity.
- A **project** is a defined collaboration with its own objectives and duration.
- An **event** is an activity taking place on particular dates.
- A **research group** is an ongoing scholarly network or community.

Dated activities belong in `_events/`. Where an event belongs to a programme, project or research group, add the corresponding identifier in its front matter. Do not duplicate an event as a project merely to give it a page.

## Detail pages

Use the available information to provide, in this order where relevant:

1. a concise introduction explaining the activity or collaboration;
2. relevant factual information, such as partners, period, location, funding or status;
3. related CoRE-Math activity, using the relevant collection metadata; and
4. external links for authoritative further information.

Existing historical content should be preserved. A short record does not need invented sections merely to match a richer page.

## Events and news posts

### Event pages

Event pages are the principal, lasting record of CoRE-Math activities. Before
an event, record its objectives, programme where available, organisers, dates,
location and other relevant factual information. After it has taken place, add
a brief factual account. When a report or other output becomes available,
incorporate it into, or link to it from, the Event page. Do not present
anticipated outcomes as established results.

### News posts

News posts should normally be short and timely, highlighting the main
development rather than reproducing the full Event description. Link to the
relevant Event or Project page for more detailed information. A post may stand
alone when no corresponding Event or Project page exists.

### Cross-linking

Where both an Event page and a News post exist, provide simple links in both
directions. Avoid unnecessary duplication: the Event page holds the durable
record, while the News post provides the timely account.

## Contextual navigation

Programme, project and research-group pages generated from their respective collections receive a parent-context link automatically. This returns visitors to Programmes & Projects or Research groups, as appropriate.

Standalone detail pages outside these collections should specify both `parent_context_url` and `parent_context_label` in their front matter so that they provide the same clear route back to their parent area.

### CoRE-Math Schools

CoRE-Math Schools is an intentional exception to the generic related-events listing. Its programme page uses dedicated Upcoming schools and Previous schools navigation instead, linking to the same Event records and to the historical schools archive. This avoids duplicating school listings on the programme page.

## Links

Use explicit action labels on their own line when linking from a catalogue or editorial entry:

- `About the programme →`
- `About the project →`
- `About the research group →`
- `Event details →`
- `Read the report →`

Use a descriptive external-link label when an external destination is the primary source, for example `Visit the FAME website →`.

## Images and permissions

Verify permission or an applicable licence before publishing a photograph,
illustration or other image. A publicly available image is not automatically
available for reuse, and an institution supplying an image must have the right
to authorise its reuse.

Record the image source, copyright holder where known, permission or licence,
and required attribution in maintainable metadata alongside the image or in the
relevant page record. If any of this is uncertain, do not publish the image
until it has been clarified. Permission for one image or publication does not
extend to other material. Before reusing an image in a report, presentation or
other publication, confirm that its permission covers that new use.

### News photographs

New or substantially revised news posts should use a `<figure>` containing an
`<img>` and `<figcaption>` for each editorial photograph. Give every image
meaningful alternative text, and use a concise caption that includes the
appropriate credit. Record the image source and permission information using
the practice above. Existing historical posts do not need to be converted
unless their caption, credit and permission information can be verified.

### Event homepage photographs

An Event may supply an optional featured image for the homepage Upcoming
events listing. Use the existing image metadata names in its front matter:

```yaml
image: "path/to/approved-event-image.jpg"
image_alt: "Factual description of the photograph"
image_title: "Photograph title, when supplied by its source"
image_credit: "Photographer or institution"
image_source: "Source URL or archive reference"
image_permission: "approved-web"
image_license: "CC BY 4.0" # when applicable
image_license_url: "https://creativecommons.org/licenses/by/4.0/"
image_modification: "Cropped to 16:9." # when applicable; also state when it depicts a different activity
image_caption_context: "Kampala SGI 2026" # optional, short public context; omit terminal punctuation
image_caption_permission: "Used with permission" # optional, short public notice; omit terminal punctuation
image_caption_modification: "Cropped" # optional, short public notice; omit terminal punctuation
image_archive_id: "CM-PH-000000"
```

The homepage renders an event thumbnail only when `image` is present and
`image_permission` is one of `approved-web`, `CC/licensed` or
`public-domain`. `image_alt` records meaningful alternative text for the
asset and later editorial reuse. On the homepage, the thumbnail itself has an
empty alternative text and is removed from the keyboard tab order because the
adjacent linked event title provides the single accessible destination.

When `image_credit` and `image_source` are supplied, the homepage renders a
short, always-visible caption directly beneath the thumbnail. Use
`image_caption_context`, `image_caption_permission`, and
`image_caption_modification` where needed to form the public caption. On
desktop, paired event cards with thumbnails share CSS Grid rows, so their
headings follow the tallest natural caption without a fixed caption height. On
small screens the cards stack and each caption takes only the space it needs.
For a Creative Commons image, the photographer name links to the source and
the licence name links to the licence. Keep fuller provenance, permission
evidence, source title and any explanation of an illustrative image in the
photograph archive and event metadata. Use `image_title` and
`image_modification` for that detailed record.

Record the source, credit, licence or permission evidence, and archive
identifier before using the image. A homepage thumbnail does not automatically
place a photograph on the Event page; that remains a separate editorial
decision.
