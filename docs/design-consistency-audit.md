# Design-consistency audit — October 2026

## Scope and outcome

This is a documentation review of the current `main` implementation. It compares the shared CSS, page-specific grid rules and the three current design references. No website CSS, templates, content or layout were changed.

The approved Refined D palette is implemented rather than experimental: warm-neutral surfaces are defined in `assets/css/content.css`, terracotta (`#874432`) is the editorial accent, and CoRE-Math blue remains the functional and identity colour. All current internal links among `design-principles.md`, `design-system.md`, `editorial-grid-conventions.md`, `detail-page-authoring.md` and this audit resolve to existing documentation files.

## Confirmed consistent patterns

- The shared editorial-grid primitive provides the same two-column structure, `2.25rem` column gap, `1.5rem` row gap and 2px terracotta entry rule for equivalent open grids.
- About activities, Education schools and mobility, Outreach activities, Programmes & Projects entries, Network partner entries, Research groups/projects and News & Events Latest News assign rules only to their original first wide-layout row. Later rows rely on whitespace.
- Responsive grids preserve source order and rule assignment. The second item in a two-column first row keeps its rule when it stacks below the first item on mobile.
- The Research seminars are a three-column layout at `1280px` and above. All three rules are therefore correct in that layout; they remain attached when the grid becomes two columns at a narrower width. This is a responsive consequence of the common convention, not an inconsistency.
- Grey rules consistently serve quiet structural roles: selected landing-page section boundaries, gateway headings, metadata catalogues, tables and related-content boundaries. They are not used as substitutes for editorial-entry rules.

## Differences with functional justification

| Pattern | Current treatment | Why it differs from an editorial grid |
| --- | --- | --- |
| News & Events upcoming list | One terracotta rule introduces the dated list; individual events are separated by spacing. | It is a chronological, metadata-led list rather than a grid of peer editorial summaries. |
| Opportunities funding catalogue | Quiet grey list dividers between records. | Filters, deadline data and dense metadata require scanable list structure. |
| Homepage Working Together and About gateways | Quiet grey rule beneath each gateway heading. | These are navigation gateways, not editorial entries; the rule establishes the heading/content relationship. |
| Related content, tables, footer and mobile menu | Grey boundaries appropriate to each control or content group. | These are structural or interface dividers, not editorial introductions. |
| Research seminars at tablet/mobile | Three terracotta rules may appear across more than one visible row. | The rules belong to the three entries that constitute the first row in the component's widest three-column state. |

## Remaining inconsistency or decision point

### Member-university directory markers — needs a decision (medium priority)

Every `.node-card` in the Network & Partnerships image directory has a `3px` terracotta top border. Comparable open editorial grids use 2px terracotta rules only on their first wide-layout row.

This may be a justified directory treatment: the marker helps bind each photograph and profile preview into an individual directory item. It should not, however, be treated as a general editorial-grid precedent. The decision required is whether to:

1. **Retain it explicitly as an image-directory exception** (recommended if the per-card marker is considered part of the member-profile identity); or
2. **Normalise it** to the editorial-grid pattern if visual review finds the repeated markers unnecessarily emphatic.

No change should be made until that functional distinction is confirmed.

### Historical terminology in source comments — maintenance follow-up (low priority)

The comments in `education.css`, `research.css`, `outreach.css`, `programmes-projects.css` and `news-events.css` still describe terracotta entry rules as “blue.” The rendered site and current documentation use the correct terracotta token. Updating those comments would prevent future maintenance confusion, but has no visual or functional effect and can be deferred to a dedicated CSS-maintenance change.

## Recommended conventions for approval

1. **Section boundaries:** use a 1px grey rule below a heading only where a structured page needs a section boundary. Do not make it a global H2 default, and omit it when a heading directly introduces an editorial grid whose entry rules already establish rhythm.
2. **Open editorial grids:** use a 2px terracotta top rule only for entries in the first row of the component’s widest standard layout. Use whitespace for later rows. Preserve this entry assignment when the grid collapses.
3. **Structured lists and catalogues:** use their specialised list treatment rather than entry rules when chronology, filters, tables or dense metadata drive scanning.
4. **Navigation gateways:** use a quiet grey rule beneath the gateway heading; do not present them as editorial entries.
5. **Image directories:** retain a distinct rule treatment only when the image/profile task needs it, and document the exception so it is not copied into unrelated grids.

## Priorities

| Priority | Recommendation | Reason |
| --- | --- | --- |
| P1 | Treat the five conventions above as the baseline for future changes. | This prevents new accidental variations without requiring a visual redesign. |
| P2 | Decide whether the member-university directory's repeated 3px markers are a deliberate image-directory exception. | It is the only prominent rule pattern that does not clearly follow the common editorial-grid model. |
| P3 | Update legacy CSS comments that call the terracotta entry rule blue when touching those files next. | This improves maintainability only; no rendered correction is needed. |

## Technical corrections made to documentation

- The homepage hero overlay is **translucent on desktop** (`rgba(22, 76, 116, .92)`) and becomes an **opaque** dark-blue panel at `760px` and below. The technical specification now states this accurately.
- The rules documentation now distinguishes selected section dividers from a universal heading rule and explains wide-layout rule assignment across responsive breakpoints.
- The current warm-neutral palette and terracotta editorial accent match the CSS variables in `assets/css/content.css`.
