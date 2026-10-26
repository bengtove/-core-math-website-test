# CoRE-Math technical design specification

This reference describes the implementation on `main` as of October 2026. It documents the approved warm-neutral and terracotta palette, not the earlier experimental palette studies. It is a maintenance reference: it does not create new design rules. For open consistency decisions, see [the design-consistency audit](design-consistency-audit.md).

## CSS architecture

`_layouts/default.html` loads the GitHub Pages `jekyll-theme-primer` stylesheet first, followed by the shared custom styles:

- `assets/css/navigation.css` — site frame, header, navigation rail, mobile menu and footer.
- `assets/css/content.css` — shared palette, typography, editorial-grid primitives, focus styles, detail-page context, related content and common content treatments.
- Page stylesheets — loaded conditionally for homepage, About, Network & Partnerships, Research, Education, Outreach, Programmes & Projects, News & Events, Opportunities and Contact.

The Primer dependency is explicit in `_config.yml` (`theme: jekyll-theme-primer`). Page-specific CSS extends the shared rules rather than replacing the global frame.

## Layout and widths

| Element | Implemented value | Use |
| --- | --- | --- |
| Site shell | `min(1180px, calc(100% - 48px))` | General shell and footer container. |
| Desktop site frame | `71.25rem` / 1140px maximum | White/warm content frame containing the desktop rail and page content. |
| Desktop navigation rail | `10.75rem` / 172px | Persistent left navigation column at `1280px` and above. |
| Rail-to-content gap | `2.5rem` | Space between rail and main column in the desktop frame. |
| Structured-page inset | `2.75rem` desktop; `1.5rem` tablet | Research, Education, Programmes & Projects and Network & Partnerships use these inner content insets. |
| Sustained prose | `52rem` | Long-form paragraphs, explanatory copy, news and comparable detail-page reading content. |
| Wide structured content | commonly `64rem` | About, Outreach, Contact and selected structured sections. |

The outer canvas is visible at wide desktop widths. The header, its lower rule and the desktop frame share the `71.25rem` working width. This is deliberate: generic prose remains comfortably bounded, while editorial grids and directories can use a wider structured area.

## Typography

Primer provides the base type stack. Custom styles set `--body-text-size: 17px` for ordinary sustained copy while `.site-main.markdown-body` has an 18px (`1.125rem`) base for components that retain their own type scale.

| Level or role | Implemented value | Notes |
| --- | --- | --- |
| H1 | `2rem` / 32px | Reduced to `1.875rem` / 30px at `767px` and below. |
| H2 | `1.5rem` / 24px | Landing-page section styles sometimes use a responsive `clamp()` between `1.55rem` and `2rem`. |
| H3 | `1.25rem` / 20px | Editorial-entry headings commonly use `1.15em` and `1.35` line-height. |
| Sustained prose | 17px, `1.6` line-height | Constrained to `52rem` where it is continuous reading copy. |
| Hero title | `clamp(2rem, 4vw, 3.5rem)` | White on the dark blue image overlay. |
| Orientation labels | `.8rem`, uppercase, `700`, `.09em` tracking | Homepage labels; terracotta accent. |
| Metadata | `.9rem` | Muted colour for dates, locations, funders and similar secondary facts. |

Headings use `--editorial-heading` (`#302b28`) unless a component intentionally specifies a different treatment. The homepage hero title has an explicit, scoped white rule so the shared heading colour cannot override it.

## Colour palette

The production palette is declared mainly in `assets/css/content.css`.

| Token / colour | Value | Intended use |
| --- | --- | --- |
| `--site-outer` / `--site-footer` | `#e8e4dd` | Warm-neutral outer canvas and footer. |
| `--site-surface` | `#fcfaf6` | Main working surface and mobile page background. |
| `--site-rail` | `#f0ece5` | Desktop navigation rail. |
| `--site-rail-rule` | `#d9d3c9` | Rail separator. |
| `--content-surface` | `#f4f0e9` | Subtle supporting surfaces, placeholders and dialog headers. |
| `--site-text` / `--editorial-heading` | `#302b28` | Primary dark neutral text and headings. |
| `--editorial-muted` | `#625d57` | Secondary text and metadata. |
| `--content-rule` | `#d4cec4` | Quiet 1px section/list dividers. |
| `--brand-blue-deep` | `#164c74` | Hero overlay and dark CoRE-Math blue surfaces. |
| `--editorial-blue` | `#1f5f8b` | Header rule, active navigation marker and focus outline. |
| `--editorial-link` | `#315d7b` | Standard links and linked entry headings. |
| `--editorial-accent` | `#874432` | Terracotta editorial labels and entry rules. |

Terracotta is intentionally limited to editorial orientation labels and entry rules; large section headings remain dark neutral. Blue remains the principal functional/identity colour for logos, navigation, links, focus and the homepage hero panel. The white hero foreground uses `#fff` on the dark blue overlay. The news lightbox has self-contained dark overlay and control colours because it is an image-viewing interaction rather than a page surface.

## Spacing and rules

- Sustained prose line-height is `1.6`; specific introductions may use `1.65`.
- Major structured landing-page sections generally use `3rem` to `3.75rem` vertical separation. Page-specific styles retain purposeful variations.
- The shared two-column editorial grid has a `2.25rem` column gap and `1.5rem` row gap (`--editorial-grid-gap`). Components may use a different row gap when their content needs it.
- A quiet section divider is `1px solid var(--content-rule)`. It appears beneath selected structured-section headings through shared selectors; narrative headings and headings that immediately introduce an editorial grid do not automatically receive a rule.
- An editorial entry rule is `2px solid var(--editorial-accent)` with `.9rem` opening padding. It is terracotta in the current palette, despite older documentation referring to it as blue.
- In multi-row editorial grids, entry rules normally appear only on the first row of the component's widest standard layout. Later rows use whitespace. The original entry assignment persists at narrower breakpoints. Full details are in [editorial-grid conventions](editorial-grid-conventions.md).

## Links and interactive states

- General content links use `--editorial-link` (`#315d7b`).
- Linked news, event, school and research-item titles are visually identifiable as links and underline on hover/focus where their component style specifies it.
- Editorial cards that introduce an area use plain headings plus a separate action link rather than duplicate heading and action links to the same destination.
- Action links use meaningful labels such as `About the programme →`, `About the project →`, `About the research group →`, `Event details →` and `Read the report →`. A `span.link-arrow` keeps the arrow with the final word without disabling normal wrapping.
- Keyboard-focusable anchors, buttons, summaries, selects, inputs and textareas receive a `3px` blue outline with a `3px` offset via `:focus-visible`.
- External destinations are described in their label where that adds useful context. The shared external-links script handles the established external-link behaviour.

## Navigation, header and footer

At `1280px` and above, the desktop navigation rail is present as part of the site frame. The navigation itself is sticky (`top: 2.25rem`), while the rail remains in normal document layout. It has a warm-neutral surface, 14px left inset and a blue current-page marker.

Below `1280px`, the rail is removed and a `Menu` button controls an in-header navigation panel. The panel is a three-column grid from `768px` to `1279px`, and a single column below `768px`. The mobile interface has no desktop rail or outer canvas margins.

The header uses the 1140px frame, a CoRE-Math identity at left, the Africa–Europe CoRE logo at right where space allows, and a 2px blue lower rule on desktop. The Africa–Europe logo is a labelled link. The footer is a three-column identity / Connect / Explore layout on desktop and a single column below `768px`; it uses the warm outer/footer surface and a quiet top divider.

## Reusable components and conventions

| Pattern | Shared hook / implementation | Appropriate use |
| --- | --- | --- |
| Open editorial grid | Shared `display: grid` selectors and `--editorial-grid-*` variables in `content.css` | Comparable two-column activity, programme, project, partner and research grids. |
| Editorial entry rule | `--editorial-entry-rule` and `--editorial-entry-padding` | First-row entries in a multi-row editorial grid. |
| Section rule | `--editorial-section-rule` | Selected structured landing-page headings. |
| Parent context | `_includes/detail-context.html`, `.parent-context` | Automatic return links on collection detail pages; standalone pages opt in through front matter. |
| Related events/content | `_includes/related-events.html`, `.related-content` | Collection metadata relationships and supporting material. |
| Local contents | `.local-contents`, `.local-contents__columns` | Long-form pages only; two content-sized columns desktop, one column mobile. |
| Directory/profile dialog | `.node-grid`, `.node-card`, `.member-portrait-dialog` | Member universities; deliberately specialised rather than an editorial grid. |
| Opportunities catalogue | `.opportunity-list`, filters and metadata classes | Filterable, deadline-oriented catalogue; deliberately list-based. |

Do not treat every repeated item as an editorial grid. Tables, chronological event lists, image directories, filters, profile dialogs and publication lists have separate information tasks and retain their specialised presentations.

## Page-type conventions

### Homepage

The homepage combines a full-width photograph with a dark-blue identity overlay, introductory copy, and a sequence of editorial entry points. At desktop widths the overlay is translucent (`rgba(22, 76, 116, .92)`); at `760px` and below it becomes an opaque `--brand-blue-deep` panel. It uses:

- three-column `What we do` and Latest News grids at desktop;
- two-column upcoming-events and working-together grids;
- terracotta orientation labels and editorial top rules;
- a news subgrid to align images, dates, headlines and descriptions on desktop; and
- a single-column mobile layout below `760px`.

Homepage section links sit after the relevant content. Headings introducing general sections are plain text; individual news and event titles are clickable.

### Section landing pages

About, Research, Education, Outreach, Programmes & Projects and Network & Partnerships use the shared site frame but select the component appropriate to their content. Introductory prose is narrower than the structured content area. Open editorial columns use a first-row terracotta rule and whitespace for later rows. Section heading rules appear only where the page’s established pattern calls for them; a grey rule is not a universal H2 treatment.

The About page is narrative with a two-column activity grid and gateway links. Network & Partnerships uses a three-column image directory for universities and two-column open partner grids. Research uses group, project and seminar grids, but keeps Publications quieter. Education distinguishes its school/event list and mobility entries. Programmes & Projects retains categories and metadata-rich entries. Outreach uses a concise two-column activity grid.

### Programme and project pages

Collection detail pages are long-form content pages with an automatic parent-context link back to Programmes & Projects. Use a concise introduction, relevant facts or status, related CoRE-Math material and external links when available. Associated events are generated from collection metadata, with the documented CoRE-Math Schools exception. See [detail-page authoring](detail-page-authoring.md).

### News articles and event pages

News posts and event pages are long-form articles with a parent-context link to News & Events. The heading is followed by date/location metadata. Event pages may add organiser, external link and generated related programme/project/research-group relationships. Inline news figures are centred and capped at `36rem`, use the available content width on narrow screens, and retain their natural aspect ratios. Their left-aligned captions share the figure width and use muted `0.875rem` text. News images may use the accessible lightbox; list images are optional and no placeholder image is added for a post without one.

### Research-group pages and publications

Research-group pages receive a parent-context link to Research groups, use their existing research description and may generate related events. Publications use the shared publication listing and conventional bibliography formatting; do not invent missing bibliographic fields.

### Other specialised pages

Contact uses a simple two-column directory with muted affiliations and blue email links. Opportunities combines a two-column fellowship overview with a filterable one-column funding catalogue. Strategy uses a wide, horizontally scrollable table on narrow screens rather than compressing its columns. These patterns should remain specialised.

## Responsive behaviour

| Range | Implemented behaviour |
| --- | --- |
| `1280px` and above | Desktop frame, visible outer canvas and sticky left navigation rail. |
| `768px–1279px` | Full available warm surface, compact Menu, three-column compact navigation; structured-page inner padding reduces at `861px–1279px`. |
| `768px` and above | Institutional member directories may use two columns. |
| `767px` and below | Mobile header simplification, single-column menu and footer; H1 reduces to 1.875rem. |
| Common page-grid breakpoint: `760px` | Homepage, Education, Outreach and Programmes & Projects editorial grids stack. |
| Component breakpoints | Network directory (`850px`/`560px`), partner grid (`700px`), News & Events (`600px`) and Opportunities filters (`600px`) change only when their content needs it. |
| `360px` and below | Site gutters reduce from 3rem to 2.5rem. |

Responsive collapse preserves source order. It does not add entry rules to items that did not have one in the desktop grid.

## Maintenance checklist

1. Inspect an existing comparable page and component before adding CSS.
2. Reuse declared tokens, shared editorial primitives and documented action-link patterns.
3. Do not introduce colours, arbitrary spacing values, card treatments or a new layout pattern without a demonstrated information/design need.
4. Keep content structure semantic: heading levels, lists, dates, labels, links and controls must remain accessible.
5. Check desktop and narrow mobile layouts, keyboard focus, wrapping and horizontal overflow. A successful Jekyll build is not sufficient visual verification.
6. Update this specification and the relevant focused guidance when an intentional visual system change is approved.

## Known implementation notes for later review

These are documentation/maintenance observations, not proposals for a current visual change:

- The shared editorial-entry token is terracotta, while some older comments and documentation used the word “blue.” This document and `editorial-grid-conventions.md` now describe the implemented palette.
- The news lightbox has its own high-contrast overlay/control colours (`#0969da`, `#58a6ff`, white and dark translucent surfaces). It is an interaction-specific exception to the palette tokens and should be reviewed only as part of a dedicated lightbox change.
- Some components use their own responsive thresholds (`600px`, `700px`, `850px`) and row gaps. They reflect specialised content density and should not be globally consolidated without visual verification.
- The member-university directory uses a `3px` terracotta top marker on every image card. It is a specialised image directory rather than an open editorial grid; whether that exception should remain is recorded as an unresolved design decision in [the design-consistency audit](design-consistency-audit.md).
