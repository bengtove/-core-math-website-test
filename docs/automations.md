# Website automations

## Overview

The site is a Jekyll site published from the `main` branch by GitHub Pages. Most editorial content is **manual**: adding a news post, event, programme, project, research group, publication or external-coverage entry means editing the corresponding source file or data file and committing it. The automated parts build that source into pages, keep the funding-opportunities data current, verify local asset references, and refresh date-sensitive event views.

This document describes the implementation in the repository at the time it was written. For the content relationships and detail-page conventions, see [detail-page authoring](detail-page-authoring.md). For grid presentation rather than automation, see [editorial-grid conventions](editorial-grid-conventions.md).

## Operating automations

### GitHub Pages build and deployment

| Item | Implementation |
| --- | --- |
| Purpose | Build the Jekyll site and publish the current `main` branch to GitHub Pages. This renders pages, collections, Liquid loops, the sitemap, CSS and JavaScript references. |
| Trigger | A push to the publishing branch, and an explicit Pages build request from the daily archive-refresh workflow. |
| Files/services | GitHub Pages; `_config.yml`; layouts in `_layouts/`; includes in `_includes/`; Jekyll’s GitHub Pages environment. |
| Dependencies | The supported GitHub Pages Jekyll environment; `jekyll-theme-primer`; `jekyll-sitemap`; valid Markdown/Liquid/YAML. `url` is `https://www.africaeuropecoremath.org` and `baseurl` is empty. |
| Output | The deployed production site, including generated collection pages and `sitemap.xml`. |
| Maintenance | Check the Pages deployment status after a push. Build locally when practical, and investigate invalid Liquid/YAML, missing dependencies or Pages configuration if it fails. |
| Status | Implemented. |

There is no repository workflow that performs the normal Pages build; GitHub Pages performs it. The theme’s base stylesheet is declared explicitly in `_config.yml` so that `/assets/css/style.css` is reproducible.

### Daily event-archive refresh

| Item | Implementation |
| --- | --- |
| Purpose | Rebuild date-sensitive event views without an editorial commit, so an event becomes historical after its end date. |
| Trigger | `.github/workflows/refresh-event-archives.yml`: daily at `00:17` UTC, plus manual `workflow_dispatch`. |
| Files/services | GitHub Actions, GitHub CLI (`gh api`), the GitHub Pages build API, `news-events.md`, `events-archive.md`, `index.md`, `education.md`, and event templates/includes. |
| Dependencies | GitHub Actions token with `pages: write`; an active GitHub Pages site; correctly formatted `start_date` and, where applicable, `end_date` in `_events/*.md`. |
| Output | A Pages rebuild only; it does not alter the repository or event records. |
| Maintenance | In Actions, confirm the daily run succeeds. If it fails, check the Pages API response, the workflow permission, and whether Pages is enabled. A manual run is a safe diagnostic. |
| Status | Implemented. |

The list condition is `end_date` when present, otherwise `start_date`, compared with Jekyll `site.time`. In `news-events.md` an event is upcoming when that date is today or later; in `events-archive.md` it is past when that date is earlier than today. The archive groups past events dynamically by start year and orders them reverse chronologically.

The homepage also loads `assets/js/home-events.js`. The build initially renders eligible events, then this browser-side safeguard rechecks local calendar dates, hides ended items and displays the earliest two upcoming items. This helps during the interval before the next scheduled rebuild; it is not a second data source.

Education’s upcoming-school list and the CoRE-Math Schools programme list use the same Events collection and the same end-date test at build time. They will update on the daily rebuild.

### Daily funding-opportunities import

| Item | Implementation |
| --- | --- |
| Purpose | Read the restricted ISP Mathematics Funding Database in Coda and publish a safe, deterministic subset of open and rolling opportunities. |
| Trigger | `.github/workflows/update-open-opportunities.yml`: daily at `03:00` UTC, plus manual dispatch. |
| Files/services | GitHub Actions; `scripts/build_open_opportunities.py`; Coda API; `_data/open_opportunities.json`; `opportunities.md`; `assets/js/opportunities.js`. |
| Dependencies | Repository secret `CODA_API_TOKEN`; the Coda document/table/column IDs defined at the top of the script; Python standard library; write access to `main`. |
| Output | A regenerated `_data/open_opportunities.json`; the workflow commits and pushes it only if it differs. It publishes records whose Coda status is `Open` or `Rolling`. |
| Maintenance | Review workflow logs and the generated JSON. The script fails without the secret or when Coda responses/required columns are invalid. Correct source URLs in Coda, not in the generated JSON, because the next run replaces it. |
| Status | Implemented. |

The script reads Coda in both `simple` and `rich` formats so it can preserve public text but extract an unambiguous public HTTP(S) URL. It deliberately rejects Coda/Superhuman URLs, conflicting links and ambiguous multiple links. This is a safety measure, not an external-link availability check.

At page load, `opportunities.js` hides passed fixed-deadline calls, changes fellowship status after a deadline, sorts open calls by deadline and rolling calls alphabetically, and populates the three filters from `data-*` attributes. These browser changes are not saved back to Coda or GitHub.

### Local-asset validation

| Item | Implementation |
| --- | --- |
| Purpose | Fail early when a source file refers to a missing local image or document under `/assets/images/` or `/assets/documents/`. |
| Trigger | `.github/workflows/check-local-assets.yml`: pushes to `main` and pull requests. It can also be run locally with `python3 scripts/check_local_assets.py`. |
| Files/services | GitHub Actions, Python standard library, `scripts/check_local_assets.py`. |
| Dependencies | Repository checkout and source files encoded as text. |
| Output | A pass/fail log; no files are generated or changed. |
| Maintenance | Run it before committing asset work. It intentionally does **not** fetch external URLs and does not validate theme-provided assets. |
| Status | Implemented. |

### Jekyll-generated listings and archives

These are automated at each Jekyll build, but are not scheduled data imports. They depend on manually maintained source records.

| Output | Source and behaviour | Status |
| --- | --- | --- |
| Latest news | `site.posts` in `index.md` (first 3) and `news-events.md` (first 6), ordered by Jekyll post date. `news-card-excerpt.html` uses a supplied card/home excerpt, otherwise produces a short sentence-boundary-aware excerpt. | Implemented |
| News archive pages | The dated post URL convention is set by `permalink: /news/:year/:title/`; archive pages and their year links are manually maintained where present. Posts themselves are automatically date ordered. | Partially automated |
| Upcoming/past events | `site.events`, dates and Liquid conditions in `news-events.md`, `events-archive.md`, homepage and Education/Schools-programme lists. See daily refresh above. | Implemented |
| Related events | `_includes/related-events.html` selects Event records whose `programme`, `project` or `research_group` equals the current detail page identifier. | Implemented |
| Related event links on Event pages | `_layouts/event.html` resolves one programme, project and research group from Event metadata. | Implemented |
| Publications lists | `research-publications.md` and research-group pages select and sort `_data/publications.json` by `year` and `sort_author`, then render `_includes/publication-listing.html`. | Implemented |
| External Coverage list | `external-coverage.md` sorts `_data/external_coverage.yml` by `date`, newest first. | Implemented |

The historical schools page (`education-schools.md`) is a manually curated archive and is deliberately not migrated wholesale into Events. Similarly, the explicit news-archive year links are not discovered dynamically.

## Client-side interface automation

These scripts improve interaction but do not create or update content:

- `assets/js/mobile-navigation.js` toggles the compact navigation button and `aria-expanded` state.
- `assets/js/member-universities.js` opens, closes and returns focus from university-profile dialogs.
- `assets/js/news-lightbox.js` turns post images into keyboard-operable dialog lightboxes.
- `assets/js/external-links.js` makes off-site HTTP(S) links open in a new tab with `noopener noreferrer`.
- `assets/js/opportunities.js` and `assets/js/home-events.js` are described above.
- Anchor.js is loaded from cdnjs in `_layouts/default.html` to add heading anchors; it is an external runtime dependency.

## Feeds, social and newsletter integrations

- **RSS/Atom:** no `jekyll-feed` plugin, feed template or feed file was found. There is no RSS automation.
- **Newsletter:** no newsletter service, mailing-list form or scheduled mailing integration was found.
- **LinkedIn:** the footer contains a normal external link to a LinkedIn group. It is not an API or publishing integration.
- **Social sharing:** no automated social-post publishing or feed import was found.

## Manual processes often mistaken for automations

- New news, Events, programmes, projects, research groups, historical-school entries and External Coverage entries are authored manually.
- Event relationships are automatic **only after** the matching identifier is entered in the Event record.
- Publication records in `_publications/` are not what the visible publication pages currently read; those pages read `_data/publications.json`.
- The Dropbox picture catalogue is outside the website build. `scripts/generate_photo_archive_catalog.py` is an archive-maintenance utility, not a site automation or GitHub Action. See [photo archive workflow](photo-archive-workflow.md).

## Concerns and planned or partial work

1. **Daily Pages rebuild is an external API trigger.** If GitHub changes Pages API permissions or the repository’s Pages configuration, date-sensitive server-rendered lists will stop advancing. The homepage browser safeguard does not update Education or the Past Events page.
2. **The opportunities workflow commits directly to `main`.** This is intentional for generated data, but a failed or malformed Coda source needs investigation in Coda rather than a local edit to the JSON.
3. **News archive year navigation is partly manual.** New years require a corresponding archive destination/link if the site continues to use discrete year archives.
4. **No feed/newsletter automation exists.** This is a current absence, not a broken feature.
5. **No automated external-link checker exists.** The local asset check correctly limits itself to repository-controlled files.

### Applicant-category terminology

The visible funding label is **Applicant category**. The importer selects Coda column `c-dJzcLWwGR8` by stable ID (`useColumnNames=false`), so renaming that display column from Career stage does not require a data migration. The JSON key `career_stage`, HTML `data-career-stage` attribute and `career-stage-filter` ID are deliberately retained together. The source Coda select column remains `Career stage filter`; its six categories and the display formula are unchanged. Filter options continue to come from the published records. The daily workflow and generated JSON format are unchanged.
