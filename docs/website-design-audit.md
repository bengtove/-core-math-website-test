# CoRE-Math website design and consistency audit

**Date:** 13 October 2026  
**Scope:** published site and the `main`-equivalent source tree in this repository.  
**Method:** source inventory of every public record, inspection of the shared layouts and all scoped stylesheets, and rendered checks of every page/layout family at 1440px, 1024px and 390px. No site files were changed as part of this audit.

## A. Executive summary

The site now has a strong and recognisable institutional character. Its centred desktop frame, restrained blue, pale navigation rail, quiet footer, 17px body type and predominantly open editorial grids work together well. The recent move away from cards and heavy containers is the right direction: Research, Education, Outreach, Programmes & Projects, About and Network & Partnerships now share a legible vocabulary of section headings, thin rules, blue entry rules and generous white space.

The main remaining issue is not a lack of visual direction but **consolidation**. Similar content is implemented with several near-equivalent, page-specific grids and several different interpretations of when a blue rule begins an entry. The result is visually coherent in broad terms but harder to maintain and occasionally uneven in detail. The next phase should formalise a small set of reusable editorial patterns rather than redesigning pages again.

The rendered checks found no horizontal page overflow in the representative desktop, tablet or 390px mobile samples. The 1140px desktop frame and mobile gutters behave reliably. Two asset failures were observed on the published Network & Partnerships page; these should be corrected separately from any visual work.

## B. Complete inventory

### Public output

The source inventory contains **92 public output pages**:

| Family | Count | Source / output pattern | Layout or main component |
| --- | ---: | --- | --- |
| Root and informational pages | 23 | `index.md`, `about*.md`, `contact.md`, thematic landing/archive/directory pages | `default` |
| News posts | 44 | `_posts/*.md` → `/news/:year/:title/` | `post` |
| Events | 6 | `_events/*.md` → `/events/:name/` | `event` |
| Programmes | 5 | `_programmes/*.md` → `/programmes/:name/` | `default` |
| Projects | 10 | `_projects/*.md` → `/projects/:name/` | `default` |
| Research groups | 4 | `_research_groups/*.md` → `/research-groups/:name/` | `default` |

The additional `_publications` collection has **78 records**, is configured with `output: false`, and supplies the selected-publications gateway rather than 78 public pages.

The root/page inventory includes the homepage; About, Development and Organisation; Contact; Education, Schools and PhD students; Network & Partnerships; Research and Publications; Outreach and Schools & young people; Programmes & Projects and Previous projects; Opportunities; News & Events and three yearly archives; and two detailed fellowship pages. The collections provide the programme, project, research-group, event and post pages listed above. This is an appropriate content model: programmes, projects, groups and dated activities have distinct authoring homes.

### Shared templates and interface components examined

- `_layouts/default.html` — header, desktop rail, mobile menu, main frame, footer and conditional stylesheet loading.
- `_layouts/post.html` — news article header and lightbox script.
- `_layouts/event.html` — dated event header and content.
- `_includes/site-navigation.html` and `_data/navigation.yml` — shared primary navigation.
- Homepage editorial grids; About activity/gateway grids; Network member/dialog and partner grids; Research, Education, Outreach and Programmes/Projects catalogue grids; News & Events lists; Opportunities filters/list; Contact directory; news lightbox; footer.

### Rendered QA sample

At 1440px, source/rendered checks covered the homepage; About; Organisation; Development; Network & Partnerships; Research; Education; Outreach; Programmes & Projects; Opportunities; News & Events; Contact; a programme, project, research-group, event and image-bearing news post; a news archive; and the PhD directory. Responsive checks at 1024px and 390px covered the homepage and every main landing-page family, Opportunities, News & Events, Contact and a post. The source inventory covers all other collection records.

## C. Existing design system

### Frame, widths and responsive structure

- Desktop uses a centred **1140px** white site frame (`--site-frame-width: 71.25rem`) over an outer `#edf0f2` canvas.
- The desktop rail is **172px** (`--navigation-rail-width: 10.75rem`), with a pale `#f5f7f8` field and subtle `#e1e7ea` separator. It is structurally part of the frame, not a floating sidebar.
- The frame uses a 3rem site gutter on desktop and a 2.5rem narrow-screen gutter; the 390px sample rendered a 342px content width, i.e. 24px gutters, with no overflow.
- Continuous narrative content is deliberately constrained by `--prose-measure: 52rem`; page structures, headings and grids use wider available content widths. This distinction is one of the strongest decisions in the current system.
- At `1279px` the desktop rail gives way to the compact mobile navigation. This is a deliberate architecture change, not merely a grid collapse.

### Typography

- Ordinary sustained body text is **17px** with `line-height: 1.6` through `content.css`.
- The type hierarchy is clear: large page H1, editorial section H2, smaller grid-entry H3 and muted metadata/labels. The hierarchy is most successful on the homepage, Research and Education.
- The shared font baseline remains dependent on `/assets/css/style.css`, which is linked by the default layout but is not present in this repository. See the maintenance finding below.

### Colours and surfaces

The practical palette is restrained and coherent:

| Role | Values in use |
| --- | --- |
| Primary CoRE-Math blue / principal rules | `#1f5f8b` |
| Dark blue emphasis | `#315d7b` |
| Main text | `#20262b` |
| Muted text | `#596873`, `#57606a`, `#667681` |
| Light rules | `#d8e0e5`, `#cbd6dc`, `#d0d7de` |
| Pale panel / rail | `#f5f7f8`, `#f3f7f9`, `#eef3f6` |
| Outer desktop canvas | `#edf0f2` |

The focused lightbox intentionally has a separate dark surface (`#0d1117`) and focus colours (`#58a6ff`, `#0969da`); that is a justified exception for an overlay interaction.

### Repeated visual patterns currently in use

1. **Open editorial grid:** white background; 2px blue top rule at selected entries; title, description and explicit link below. Used on homepage, About, Network partners, Outreach, Research, Education and Programmes & Projects.
2. **Quiet section heading:** H2 with a thin light-grey bottom rule. Strongest on Research, Education and Programmes & Projects.
3. **Narrative page:** 52rem readable prose within the wider structural canvas. Used for programme, project, research-group, development and article-style pages.
4. **Structured catalogue/list:** dates, metadata or compact separators, rather than grid tiles. Used appropriately for News & Events, Opportunities and historic/archive content.
5. **Image-led member directory:** three-column node grid with blue top border, image and expandable profile dialog. This has a distinct function and should remain distinct.

## D. Consistency assessment

### Patterns that are consistent and should be preserved

- The header, frame, desktop rail, footer and mobile menu now read as one site system across all reviewed pages.
- The **open-column** approach is consistently replacing card-like UI: no shadows, no rounded cards and no decorative surfaces in editorial grids.
- Page-specific grids collapse cleanly to one column at mobile widths. The tested 390px pages had no horizontal overflow.
- Headings are used semantically and rendered as headings rather than literal Markdown. The previous Markdown-in-HTML failure mode is not present in the reviewed rendered output.
- External/internal calls to action are generally explicit and consistently follow the `… →` convention.
- News images retain their proportions, stay bounded in article content and have an accessible dialog-based enlargement path; this is a good, purpose-specific exception to the otherwise text-led system.

### Similar content with inconsistent treatments

| Area | Current difference | Assessment |
| --- | --- | --- |
| Blue entry rules | Homepage focus/news/events, Research groups/projects/series, Education schools/mobility, Outreach activities, programmes/projects and partners all use blue rules, but differ in whether rules appear on every item, only the first row, or the first row plus selected items. | The rule is meaningful but its rule-of-use is not yet systematised. |
| Major section headings | Research/Education use a grey rule below most H2s; the homepage removes such rules for editorial grids; Programmes & Projects mixes quiet section rules with programme-specific blue rules. | Mostly justified, but should be expressed as a documented choice: “plain section” vs “section immediately introducing editorial entries.” |
| Grid mechanics | Research, Education, Outreach, Programmes & Projects, About and Network each define a separately named two-column grid with related but not identical gaps, margins and breakpoint behaviour. | Visually close; implementation is duplicated. |
| Metadata | Events use a formal date column; Opportunities uses labels and values; news cards use muted dates above titles; school entries use date/location beneath titles. | These are functionally justified, but shared muted metadata tokens could reduce drift. |
| Call-to-action placement | Grid items generally put links after descriptions, but long-form pages, gateways and archive links vary in separation and wording. | A small authoring convention would help without forcing uniformity. |
| Rules between catalogue records | Opportunities and historic/project catalogues use thin inter-item separators; recent open grids intentionally use whitespace. | Functionally justified: dense, sortable lists need separators; short editorial grids do not. |

### Differences that are justified by content

- **Opportunities** needs filters, a compact dynamic record list and explicit metadata; it should not be forced into the open editorial grid.
- **News & Events** needs chronological scanning, date-first hierarchy and image optionality; its list/card hybrid is appropriate.
- **Network member universities** needs imagery and an expandable profile interaction; its portraits should not be recast as plain text columns.
- **Publications** is a gateway to a curated, data-backed collection, not a set of peer entities; the quiet closing section is correct.
- **Long-form programme/project/research-group/news/event pages** need the 52rem reading measure and should not be widened simply to match landing-page grids.
- **Fellowship tables and directory material** legitimately need tables/lists; they should remain exceptions to the editorial-grid pattern.

## E. Visual and implementation weaknesses

### Essential

1. **Published broken member-image assets.** Rendered inspection of Network & Partnerships found five unloaded `<img>` elements, including local University of Bergen, University of Vienna and Uppsala image paths, one external Groningen image and one news AVIF asset. This is a visible quality issue, particularly in the image-led member directory. Verify published URLs and filenames/case, replace or remove only confirmed broken external sources, and add a lightweight build/deployment asset check.  
   *Relevant files:* `network-partnerships.md`, `_data`/front matter supplying member images, `assets/images/members/**`, `assets/images/news/**`.

2. **Unversioned / unavailable base stylesheet in the repository.** `_layouts/default.html` loads `/assets/css/style.css?v={{ site.github.build_revision }}`, but `assets/css/style.css` is not in the working tree. The live typography baseline therefore depends on a generator/theme artifact that cannot be examined or reproduced in a normal local source-only build. This creates avoidable visual-regression risk. Establish the origin deliberately: commit the intended base stylesheet, document the theme source/version, or change the layout to use an explicit supported theme asset.  
   *Relevant files:* `_layouts/default.html`, `_config.yml`, site build configuration.

### Consistency / maintainability

3. **Many near-duplicate page-grid definitions.** CSS is sensibly scoped but now totals approximately 2,076 lines across 13 page/global files. `about.css`, `research.css`, `education.css`, `outreach.css`, `programmes-projects.css`, `network-partnerships.css` and `home.css` repeat grid, gap, blue-rule and breakpoint concepts. A future visual tweak is likely to miss one family.  
   *Relevant files:* the seven files above, especially their grid and media-query blocks.

4. **Dormant Research TOC markup and CSS.** `research.md` retains the full `research-toc` navigation while `research.css` sets `.research-toc { display: none; }`. It is harmless visually but is dead source and could confuse future maintenance or assistive-technology review if its state changes. Remove it or restore it only through a deliberate navigation decision.  
   *Relevant files:* `research.md`, `assets/css/research.css`.

5. **Inconsistent use of blue entry rules.** The 2px blue rule is now a signature element but lacks a stable semantic contract. For example, Education upcoming schools currently places it above every displayed entry, while About uses it only above the first activity row and Network partners only above the first row. The choices can all look good; the issue is that they are not encoded as reusable variants.  
   *Relevant files:* `assets/css/home.css`, `about.css`, `research.css`, `education.css`, `outreach.css`, `programmes-projects.css`, `network-partnerships.css`.

6. **Rule colours and weights have accumulated.** `#d8e0e5`, `#cbd6dc`, `#d0d7de` and local alternatives are all used for quiet rules; their visual difference is small enough to look accidental. Consolidate to one token for ordinary rules, and keep the 2px primary blue rule as the only strong divider.

### Optional refinement

7. **Desktop-to-tablet navigation changes abruptly.** At 1279px the framed desktop/rail architecture changes to the compact/mobile menu. It works and does not overflow, but 1024px reads as a different site architecture rather than a compressed desktop. Test whether a tablet-specific compact header/menu treatment needs clearer visual continuity; do not change this merely for technical uniformity.

8. **Form-control styling is the one conspicuous rounded-UI exception.** Opportunities filter selects use 4px rounding while the rest of the visual system avoids rounded surfaces. This is not wrong for native controls, but document it as an intentional accessible form-control exception or make it visually closer to the system later.  
   *Relevant file:* `assets/css/opportunities.css`.

## F. Accessibility and responsive observations

### Strengths

- The desktop rail has an active state with a blue left marker, and navigation stays in normal layout rather than being a disruptive fixed overlay.
- The small-screen layout uses ordinary single-column flows and preserved gutters; no overflow was found at 390px in the checked page families.
- The header marks both brand links with accessible labels; the external Africa–Europe logo is a proper link.
- The university profile interface uses a native dialog pattern and an explicit close control; the news lightbox supports close controls, backdrop/Escape behaviour and focus-visible styling.
- Content images use bounded, uncropped presentation and figures retain captions.
- Headings are structurally exposed in the rendered accessibility tree.

### Risks to address in a separate accessibility pass

- Test keyboard traversal and visible focus on every interactive family, not only navigation/lightbox/dialog controls. Generic link focus styling partly depends on the absent base stylesheet.
- Review colour contrast with an automated checker after the base stylesheet is made explicit, particularly the lightest muted metadata colours on white and pale surfaces.
- Audit image `alt` text and verify the broken Network assets before relying on the member directory as an accessible information source.
- Ensure dynamic Opportunities filter state/no-results messaging is announced appropriately to assistive technologies; the UI is functional visually but needs a focused ARIA/live-region review.
- Verify heading level progression in content-authored long-form records, where Markdown is more variable than the landing-page templates.

## G. Prioritised recommendations

### Essential

1. Repair the published Network & Partnerships image failures and add a simple deployment-time link/asset check.
2. Make the base `style.css` provenance explicit and reproducible in source/build configuration.
3. Run a focused keyboard, contrast and dynamic-filter accessibility audit after those two technical fixes.

### Consistency improvements

4. Introduce a small, scoped set of shared primitives — not a general redesign:
   - `.editorial-grid` (two/three-column responsive geometry),
   - `.editorial-entry` (title, description, optional metadata/link),
   - `.editorial-entry--first-row-rule` and `.editorial-entry--all-rules`,
   - one quiet section-rule token,
   - one muted metadata style.
   Keep page CSS responsible only for column count and genuinely page-specific geometry.
5. Document the semantic use of rules: blue rule = a group’s entry boundary; quiet grey rule = a sectional heading boundary; thin separator = records in a dense catalogue. This prevents the same visual device acquiring conflicting meanings.
6. Consolidate grid gaps/breakpoints where the content purpose is alike, while retaining justified exceptions such as members, opportunities and events.
7. Remove or intentionally re-enable the dormant Research TOC source.

### Optional refinements

8. Explore a visually continuous tablet navigation treatment only if real-device review shows the 1279px switch to be disorienting.
9. Formalise external/internal/archive link wording in a short authoring note, preserving the established `→` language.
10. Add visual regression screenshots for the homepage, About, Network, Research, Education, Opportunities and News & Events at 1440px and 390px once the CSS baseline is reproducible.

## H. Concise design principles for future work

1. **One institutional frame, many purposeful content patterns.** Preserve the 1140px desktop frame, rail, restrained header and quiet footer.
2. **Separate structure from reading measure.** Keep prose readable at 52rem; allow headings and editorial grids to use the wider structural canvas.
3. **Use open editorial columns by default.** Typography, alignment, blue entry rules and whitespace should provide hierarchy; do not reintroduce cards, shadows or decorative boxes without a functional reason.
4. **Use blue rules sparingly and semantically.** They introduce editorial entries; light-grey rules delimit ordinary sections; dense records can use separators.
5. **Choose components by information task.** Editorial grids for peer activities; chronological lists for events; metadata-rich filtered lists for opportunities; image directory/dialogs for members; tables only where comparison is essential.
6. **Keep responsive behaviour simple.** Collapse grids naturally; retain 24px mobile gutters; do not use horizontal scrolling for ordinary content.
7. **Prefer shared variants to page-specific inventions.** A new pattern needs a documented information purpose before it gets new CSS.
8. **Protect the design through content operations.** Require working images, explicit alt text, valid links and a build that includes every stylesheet needed to reproduce the published appearance.

## Verification notes

- The live site rendered the evaluated structural content at 1440px, 1024px and 390px without detected document-level horizontal overflow in the selected page families.
- A local Jekyll build was not available in this audit environment. The repository’s GitHub Pages deployment remains the authoritative renderer; source/template inspection was used alongside live rendered QA.
- This document is an audit only. It intentionally makes no visual, content, component or configuration changes.
