# Website metadata

## Overview

Metadata is primarily YAML front matter in Markdown collection files and structured records in `_data/`. It drives URLs, dates, ordering, related-content links, page-specific styles and client-side filters. The site has no global schema validator: authors must use the field names and identifier values documented here.

This is an implementation guide, not an editorial policy. See [detail-page authoring](detail-page-authoring.md) for page-writing conventions and [automations](automations.md) for scheduled behaviour that consumes dates and opportunity data.

## Jekyll-wide configuration and defaults

`_config.yml` defines output collections and their permalink patterns:

| Collection | Output URL | Default layout |
| --- | --- | --- |
| Posts (`_posts/`) | `/news/:year/:title/` | `post` |
| Programmes (`_programmes/`) | `/programmes/:name/` | `default` |
| Projects (`_projects/`) | `/projects/:name/` | `default` |
| Research groups (`_research_groups/`) | `/research-groups/:name/` | `default` |
| Events (`_events/`) | `/events/:name/` | `event` |
| Publications (`_publications/`) | not output | no collection default needed |

Every page without a more specific default gets `layout: default`. `title`, `permalink`, `layout`, `parent_context_url` and `parent_context_label` are general page front-matter fields, not all required for every page. `title` is normally public: it becomes the page heading when the Markdown/content does not supply one and is used by SEO tooling. `permalink` replaces the default path. The parent-context fields are used by `_includes/detail-context.html` only for standalone pages; programme, project and research-group collection pages receive their standard parent link automatically.

Boolean page flags such as `homepage`, `news_events`, `education_page`, `research_page`, `programmes_projects`, `network_partnerships`, `about_page`, `contact_page` and `opportunities_page` select page-specific CSS/JavaScript in `_layouts/default.html`. They do not carry editorial information and are normally optional, but required by the corresponding landing page implementation.

## News posts (`_posts/`)

**Required in practice:** Jekyll post filename date, `title`, and `date`. Posts use the filename and/or `date` for chronology and the configured news URL. Other fields are optional.

| Field | Meaning and use | Public? |
| --- | --- | --- |
| `title` | News headline; shown on post and cards. | Yes |
| `date` | Publication date; orders `site.posts`, formats post/card dates and determines `:year:` in the URL. Use ISO date. | Yes |
| `layout` | Usually inherited as `post`; explicit `layout: post` is equivalent. | Indirectly |
| `location` | Place shown after the post date by `_layouts/post.html` and on homepage news cards. | Yes |
| `image` | Local image path for news-card thumbnails; article body must still include its own image Markdown/figure if it should appear in the article. | Yes |
| `card_excerpt` | Preferred short card text, used on homepage and News & Events. | Yes |
| `home_excerpt` | Legacy/fallback short card text; used only if `card_excerpt` is absent. | Yes |
| `project` | Project identifier for manually generated related-news lists (currently used by Math4SDG). | Indirectly |
| `category` / `type` | Editorial labels occurring in existing posts. No current template/filter uses them. | No current display |

If neither excerpt field is supplied, `_includes/news-card-excerpt.html` derives a short excerpt from post content: it prefers one or two complete sentences, then caps it at 30 words. There is no image fallback or automatic relationship extraction from body links.

## Events (`_events/`)

**Required:** `title`, `start_date`, `location`, and `type` are present on every current record. `end_date` is optional; a one-day event falls back to `start_date` for all date-based filtering. ISO dates are essential because Liquid and JavaScript compare/display them.

| Field | Meaning and use | Public? |
| --- | --- | --- |
| `title` | Event title and Event-page heading. | Yes |
| `start_date` | Start date. Sorts Events and supplies archive year, event display and homepage ordering. | Yes |
| `end_date` | Last date, if different. Determines whether an Event remains upcoming; omission means the start date is used. | Yes |
| `location` | Event location. | Yes |
| `type` | Event kind, e.g. `school`, `research-workshop`, `study-group-with-industry`, `competition`. `school` is used to select Education and Schools-programme lists. Other values are currently descriptive. | Usually not directly displayed |
| `image` | Optional local image path for a homepage Upcoming Events thumbnail. | Yes, when its permission status permits display |
| `image_alt` | Factual alternative text for the image. The current homepage presents the thumbnail as a decorative link and therefore uses empty `alt`; retain this field for the record and for any future non-decorative use. | Not currently displayed |
| `image_title` | Original or descriptive photograph title, used in the accessible label for a linked credit where supplied. | Indirectly |
| `image_credit` / `image_source` | Required together for the current public photo-credit line. `image_source` is the original source URL. | Yes |
| `image_permission` | Rights-status value. The homepage displays the image only for `approved-web`, `CC/licensed`, or `public-domain`; absence or any other value suppresses it. | Indirectly |
| `image_license` / `image_license_url` | Optional licence name and its URL. The current credit links the credit name to the source and the licence name to this URL. | Yes, when supplied |
| `image_modification` | Full internal note about a crop or contextual limitation. Keep detailed provenance in the Dropbox archive/activity record as well. | Not currently displayed |
| `image_caption_context`, `image_caption_permission`, `image_caption_modification` | Optional short public credit fragments, for example the activity actually depicted, a permission statement, and `Cropped`. | Yes, when supplied |
| `image_archive_id` | Permanent Dropbox picture-archive identifier, such as `CM-PH-000022`. | Not currently displayed |
| `organiser` | Named organiser, shown on the Event page. | Yes |
| `external_url` | Official event/site URL, rendered as an action link. | Yes |
| `external_label` | Label for that link; falls back to `External website`. | Yes |
| `programme` | Identifier matching a programme’s `programme_id`; resolves a programme link on the Event page and lets the programme show related Events. | Yes, as a relationship |
| `project` | Identifier matching a project’s `project_id`; same relationship behaviour. | Yes, as a relationship |
| `research_group` | Identifier matching a research group’s `research_group_id`; same relationship behaviour. | Yes, as a relationship |

`news-events.md` selects upcoming Events whose effective end date is today or later; `events-archive.md` selects past Events whose effective end date is earlier than today. Related-event sections sort by `start_date`. The event-page layout resolves at most one programme, project and research group from the three singular fields; arrays are not supported by current templates.

Example:

```yaml
title: "Study Group with Industry in Kampala"
start_date: 2026-09-21
end_date: 2026-09-25
location: "Kampala, Uganda"
type: study-group-with-industry
programme: study-groups-with-industry
```

An Event image is optional. Do not add one merely to fill a homepage card: the
image must have a documented source and an approved `image_permission` value.
Store original files, permissions evidence and full provenance in the Dropbox
picture archive, following the [photo archive workflow](photo-archive-workflow.md).

## Programmes (`_programmes/`)

**Required:** `title` and a unique `programme_id`. Existing files explicitly specify `layout: default`, though it is inherited.

| Field | Meaning and use | Public? |
| --- | --- | --- |
| `title` | Programme name, page title and labels in lists/relationships. | Yes |
| `programme_id` | Stable machine identifier. Events use it in `programme`; landing-page Liquid finds programmes by it. Keep it unchanged if the title changes. | Indirectly |
| `type` / `section` | Present only on the Women in Math record. No current template uses either field. | No current display |
| `layout` | Standard layout override. | Indirectly |

The default layout adds a generic related-events section to programme pages, except `programme_id: core-math-schools`; that programme deliberately provides dedicated upcoming/previous-school navigation to avoid duplication. Programmes & Projects uses specific `programme_id` lookups rather than iterating every programme, so a new programme must be added to that landing page deliberately.

## Projects (`_projects/`)

**Required:** `title` and a unique `project_id`; `layout: default` is standard.

| Field | Meaning and use | Public? |
| --- | --- | --- |
| `title` | Project title and related-content label. | Yes |
| `project_id` | Stable identifier used by Event `project` and post `project` relationships. | Indirectly |
| `programme` | Optional CoRE-Math parent programme identifier; the generic layout does not automatically render a project-to-programme link. External funding programmes are recorded in project funding information, not as parent programmes. | Potentially, if page uses it |
| `type` / `section` | Present in most project records but not used by templates or automated lists. | No current display |
| `layout` | Standard layout override. | Indirectly |

The default layout adds related Events by matching Event `project` to `project_id`. The Programmes & Projects landing page is curated markup: it does not automatically list all project collection records.

## Research groups (`_research_groups/`)

**Required:** `title` and unique `research_group_id`; `layout: default` is standard.

| Field | Meaning and use | Public? |
| --- | --- | --- |
| `title` | Group name shown in Research listings and relationship links. | Yes |
| `research_group_id` | Stable identifier matched by Event `research_group`. | Indirectly |
| `render_related_events` | Defaults to showing the generic related-events include; `false` suppresses it so a page can place its own version. EAALG uses `false` and includes its own reversed "Workshops and events" list. | Indirectly |
| `type` | Present on three records; not consumed by current templates. | No current display |
| `layout` | Standard layout override. | Indirectly |

Research landing-page cards are generated by iterating `site.research_groups`; their public labels are derived by splitting the title on ` – `. Titles without that separator will not produce the intended acronym/name split.

## Publications

There are two different publication stores, and this is an important maintenance distinction.

### Visible publication data: `_data/publications.json`

`research-publications.md` and research-group pages use this JSON array. The current fields are:

| Field | Required in current data | Use |
| --- | --- | --- |
| `year`, `authors`, `title`, `publication_type`, `journal`, `volume`, `issue`, `pages`, `article_number`, `doi`, `arxiv`, `institutions`, `research_groups`, `projects_programmes`, `collaborations`, `support`, `sort_author` | Yes (empty strings/arrays are valid where information is unknown) | Year headings; alphabetical sort by `sort_author`; conventional citation and conditional DOI/article/arXiv link; optional contextual metadata. |
| `full_authors` | Present in current data | Not rendered by the current template. |

`_includes/publication-listing.html` omits empty bibliographic fields. It normalises DOI prefixes and creates a DOI link only if the value contains `10.`; otherwise it falls back to `url` if supplied, then `arxiv`. Note that `url` is supported by the template but is not included in the established JSON field set for every record.

### Non-output collection: `_publications/`

The `_publications/` Markdown records have fields including `title`, `year`, `authors`, `output`, `nodes`, `url`, `research_groups`, `projects_programmes`, `collaborations`, `support` and `notes`. They have `output: false` in `_config.yml` and no visible template, script, configuration value or workflow currently reads `site.publications`. `output` versus JSON `publication_type`, and `nodes` versus JSON `institutions`, are inconsistent naming. Do not assume edits here update the public Publications page.

A focused comparison in October 2026 found that all 78 `_publications/` records have a matching record in the visible JSON dataset, matched by year and title. The JSON dataset contains 30 additional records, for 108 visible records in total. The Markdown collection retains 11 non-empty editorial `notes` values that are not represented in the JSON dataset; it also has older short-form author strings and, in some cases, less complete relationship data. The JSON records generally contain fuller bibliographic metadata and are the authoritative source for the published lists. Therefore the collection is an unused legacy subset, but it should not be removed until the 11 notes have been deliberately preserved, archived or confirmed as disposable.

## Data files and specialised content

| Data source | Fields / use | Public behaviour |
| --- | --- | --- |
| `_data/navigation.yml` | `title`, `url` for each main navigation item. | `_includes/site-navigation.html` builds desktop and mobile navigation and marks the current URL. |
| `_data/open_opportunities.json` | `programme`, `funder`, `description`, `status`, `deadline`, `deadline_note`, `support_type`, `career_stage`, `region`, optional `url`. | Generated from Coda; `status` splits open/rolling lists; browser script sorts, filters and removes expired fixed-deadline calls. `career_stage` supplies the visible Applicant category label; its internal key is retained for compatibility. `region` is retained but not currently rendered or filtered. |
| `_data/external_coverage.yml` | Existing entries use `id`, `date`, `title`, `source`, optional `author`, `original_url`, optional `archive_pdf`. | External Coverage sorts by date descending. If `archive_pdf` exists, title links to the local PDF and a separate original-publication link is rendered. |
| `_data/member_universities.yml` | University directory/profile information, including identity, country, description, image and portrait/modal content where supplied. | Network & Partnerships reads it to render member cards and dialogs; the JavaScript uses generated dialog IDs/`data-member-portrait-*` attributes rather than the YAML directly. |
| `_data/phd_students.json` | Student directory records. | Used by the current-PhD-students page; field expectations should be checked against that page before editing. |

## Static and historical content

The previous-schools archive (`education-schools.md`), previous-projects page, contact list, Strategy, Resources and most landing-page cards are ordinary manually authored Markdown/HTML. They may have normal page metadata, but do not have collection schemas or automatic lifecycle behaviour.

Images in news front matter (`image`) feed card listings only. Article images, captions and alternative text are Markdown/HTML in the article body; they are not inferred from the front-matter image. Local asset paths should be checked with `scripts/check_local_assets.py`.

## Unused, inconsistent or potentially confusing metadata

1. **`type` and `section` on Programmes/Projects/Research groups** are currently unused by templates. They should not be relied upon for classification without implementing/approving a consumer.
2. **Post `type` and `category`** occur in content but do not currently drive display, filtering or archives.
3. **Two publication stores** use different field names and only `_data/publications.json` is visibly rendered. `_publications/` is a 78-record legacy subset of the 108-record JSON dataset and retains 11 editorial notes. This remains the highest maintenance risk: future editors could update `_publications/` and see no public change.
4. **`region` in opportunity records** is generated but not displayed or used by the filters.
5. **Programme/project landing pages are curated**, not generic collection indexes. An item can exist as a collection page but remain absent from a landing-page grid until its curated markup is updated.
6. **Event relationships are singular.** The existing schema supports one programme, one project and one research group per Event. A multi-valued relationship would require template changes.
7. **Dates must be complete ISO dates.** The current event rendering has no documented approximate-date representation; do not use a guessed day to represent a month-only historical date.

## Authoring checklist

1. Use stable IDs (`programme_id`, `project_id`, `research_group_id`) as the relationship keys—not titles or URLs.
2. Add exact ISO `start_date` and `end_date` to every Event where known; omit `end_date` for a one-day event.
3. Add Event `type: school` for Events intended to appear in upcoming-school lists.
4. Add concise `card_excerpt` to a news post when its opening text is not suitable for a 25–30-word card.
5. Update the relevant curated landing page when adding a programme or project that visitors should discover there.
6. Edit `_data/publications.json` for visible publication-list changes. Treat `_publications/` as a legacy reference collection until a separate, reviewed retirement preserves or resolves its 11 editorial notes.
