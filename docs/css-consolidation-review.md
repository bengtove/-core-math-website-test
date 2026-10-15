# CSS consolidation review

This review covers the current CSS architecture and the documented editorial-grid conventions. It is an analysis only; no website styles or templates were changed.

The architecture is already sensibly scoped by page family. The main maintenance opportunity is extracting repeated values and editorial-grid mechanics without erasing purposeful differences.

## A. Safe, straightforward consolidation

| Consolidation | Affected stylesheets and selectors | Identical declarations | Preserve | Benefit and risk |
| --- | --- | --- | --- | --- |
| Shared editorial tokens | `content.css`; About, Education, Outreach, Research, Programmes & Projects, Network, Opportunities, Home | `#1f5f8b`; `.9rem` opening-entry padding; `2px solid` blue rules; `2.25rem` main column gap; `1.5rem` common row gap | Page-specific aliases and differing row gaps | Define neutral variables such as `--editorial-rule`, `--editorial-entry-padding`, and `--editorial-grid-gap`. No selector or rendered change. High maintenance benefit; low risk. |
| Shared quiet-section-rule tokens | `education.css`, `research.css`, `programmes-projects.css` | `padding-bottom: .45rem` and `border-bottom: 1px solid var(--content-rule)` | Different heading font sizes and margins | Use a shared token for the rule and its offset, while retaining individual heading selectors. Medium benefit; low risk. |
| Common two-column grid values | `about.css` (`.about-activity-grid`, `.about-gateway-grid`), `research.css` (`.research-tile-grid`), `outreach.css`, `education.css` (`.mobility-list`), `programmes-projects.css` (`.projects-list`), `network-partnerships.css` (`.partner-grid`) | `display: grid`; `repeat(2, minmax(0, 1fr))`; `align-items: start`; `gap: 1.5rem 2.25rem` | Schools use a `2rem` row gap; programmes use `1.75rem`; Opportunities and Contact have different gaps | Share variables, or group only the exact selectors in one shared rule. This preserves each component’s local semantics. Moderate benefit; low risk if visual regression-tested. |
| Structured-page horizontal padding | `research.css`, `education.css`, `programmes-projects.css`, `network-partnerships.css` | The desktop `column-gap: 0` and inner `2.75rem` / tablet `1.5rem` padding rules are materially identical | Page-specific main-class names and any future exceptional page | Group the selectors by the existing 1280px and 861–1279px media queries. Good reduction of repeated responsive code; low risk. |
| Colour aliases already partly present | `education.css`, `programmes-projects.css`, `content.css` | Local aliases resolve to the same shared blue, grey rule, and muted text values | Distinct catalogue and interface greys | Move only truly shared aliases to `content.css`; leave semantically different greys local. Small benefit; very low risk. |

## B. Potentially useful, but requiring visual verification

| Consolidation | Affected stylesheets and selectors | Key issue | Safe approach | Benefit and risk |
| --- | --- | --- | --- | --- |
| Reusable editorial-grid component | About activities/gateways; Research tiles; Education schools/mobility; Outreach; Programmes/projects; Network partners; parts of Home | The visual pattern is shared, but rule placement varies: first desktop row, all visible entries, or no entry rule | Introduce opt-in classes such as `.editorial-grid`, `.editorial-grid--two`, `.editorial-entry`, and rule variants. Migrate incrementally, beginning with visually equivalent two-column pages. | High maintenance benefit; medium risk from cascade order, markup changes, and responsive rule assignment. |
| Explicit rule variants | Same pages as above | The documented convention says first-row rules survive a single-column collapse according to desktop assignment. Current Programmes & Projects and Network partner CSS remove the second opening rule on mobile, while Education and Research retain it. | First document whether the current mobile differences are intentional. Then encode only approved variants such as “first-row rules retained” and “single opening rule when stacked.” | Important design consistency benefit; medium risk because it may visibly alter mobile pages. |
| Quiet-grey rule palette | `content.css`, Navigation, About, Home, Opportunities, News & Events | `#d8e0e5`, `#cbd6dc`, `#cdd7dd`, and `#d0d7de` are close but not identical | Tokenise existing colours first; only merge colours after side-by-side visual review. Keep a distinct catalogue separator if needed. | Moderate benefit; medium risk of subtle contrast and hierarchy changes. |
| Action-link base treatment | `content.css`, Home, About, Education, Outreach, Research, Programmes & Projects, Opportunities | Most action links use bold or medium blue text and spacing, but placement and weight differ by component | Keep the existing global arrow behaviour and focus rule. A narrow `.action-link` base could cover only colour and decoration, leaving spacing and weight local. | Moderate benefit; medium risk of altering intentional hierarchy. |
| Shared breakpoint vocabulary | All page stylesheets | Several nearby breakpoints exist: 860/861, 760/761, 767/768, 700, 600, 560 | Define names or comments for established breakpoints, but do not mechanically merge them. | Documentation benefit; medium-to-high risk if behavioural values are changed. |

## C. Page-specific rules that should remain separate

- **Navigation and site frame** in `navigation.css`: the 1280px rail-to-compact-navigation change is structural, not an editorial-grid variation.
- **Homepage hero, news subgrid, and event layout** in `home.css`: the news subgrid intentionally aligns metadata and titles; the hero has its own image-overlay geometry.
- **Network member directory and profile dialog** in `network-partnerships.css`: three-column imagery, dialog styling, and the 3px member-card rule are functionally distinct.
- **News & Events chronological list** in `news-events.css`: date columns and list behaviour are not editorial peer grids.
- **Opportunities** in `opportunities.css`: filters, dynamic metadata, tables, and dense catalogue separators need their own information-dense treatment.
- **News lightbox** in `news-lightbox.css`: interaction-specific styles should remain isolated.
- **Contact directory** in `contact.css`: although two-column, it is a directory rather than an editorial-grid entry pattern.
- **Reading measures**: `48rem`, `52rem`, `55rem`, and narrower gateway measures should remain page/content-specific where they support intentional reading hierarchy.

## Recommended implementation order

1. Add shared design tokens only: editorial blue rule, opening padding, common two-column gap, and quiet-rule values.
2. Group the identical structured-page padding media queries.
3. Establish documented editorial-grid utility variants without migrating every page at once.
4. Migrate one visually equivalent family at a time, with 1440px, 1024px, and 390px comparisons.
5. Resolve the mobile blue-rule variant question before consolidating rule selectors.
6. Leave specialised directories, catalogues, events, navigation, and interactive components untouched.

The key caution is to consolidate **values and approved variants**, not to force all grids into one selector or one breakpoint.
