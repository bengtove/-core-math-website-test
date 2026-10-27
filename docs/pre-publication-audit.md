# Pre-publication audit — CoRE-Math website

> **Historical record — October 2026.** This audit concerns the former GitHub
> Pages test address and records pre-launch findings. It is retained to explain
> decisions made before launch, not as a statement of the current live site's
> status. Use [website administration](website-administration.md) and the
> current maintenance documentation for operational information.

**Audit date:** 19 October 2026
**Scope:** current `main` and the deployed GitHub Pages test site at `https://bengtove.github.io/-core-math-website-test/`
**Method:** source/configuration inspection, deployed HTTP checks, local asset validation, relationship/data validation, and static responsive/accessibility review. This audit does not modify website code, content, styling, configuration or DNS.

## Executive summary

The test site is close to publication-ready. Its current GitHub Pages build is successful, the 99 documented public content routes resolve, literal internal links and assets resolve below the configured test-site base path, and all checked local/member-directory image and document URLs returned HTTP 200. The final warm-neutral and terracotta palette is implemented consistently in the shared CSS.

Two categories should be addressed before a public-domain switch:

1. **Confirmed visitor-facing external 404 links** occur in a formal-partner link, a project page, funding records, two publication DOI links and two historical news posts.
2. **No `robots.txt` or `sitemap.xml` is published.** This is not visible in normal browsing, but it is an avoidable discoverability and migration gap for a public launch.

The main residual risks are external dependencies (member-directory images and third-party destinations), a few very large local images, and final real-device checks of mobile navigation and responsive layouts. These are important but do not indicate a structural failure of the site.

## Evidence and checks completed

| Check | Result | Evidence |
| --- | --- | --- |
| Current GitHub Pages deployment | Pass | The latest `pages-build-deployment` run for `31eb6fe` completed successfully; Pages reports `built`, HTTPS enforced, source `main` / root. |
| Published route inventory | Pass | 102 documented public/compatibility routes (including the test-site base route) returned HTTP 2xx or 3xx. The inventory’s 99 generated content routes match the current source count: 25 standalone/redirect pages, 6 programmes, 6 projects, 4 research groups, 14 events and 44 posts. |
| Literal internal links and local assets | Pass | 101 literal site-relative links/assets found in source returned HTTP 2xx or 3xx on the deployed site. `scripts/check_local_assets.py` found 29 referenced local assets and no missing files. |
| Member-directory and repository asset URLs | Pass | 47 local/member image and document URLs, including all 17 directory images, returned HTTP 200 at audit time. |
| Event relationships | Pass | All programme, project and research-group IDs referenced by the 14 event records resolve to an existing collection record. |
| Funding deadlines | Pass | No `Open` funding record has a parsed deadline before 19 October 2026. |
| Colour contrast tokens | Pass | Core text, links, metadata, terracotta labels/rules, rail text, focus blue and white hero text all exceed WCAG AA normal-text contrast against their documented surfaces (lowest checked ratio: 6.25:1). |
| External-link automated check | Mixed | 169 unique external URLs used outside `docs/` were checked with HTTP HEAD and GET fallback. 148 returned 2xx/3xx; 9 confirmed 404; 12 were blocked, timed out or unavailable to this automated check. |

## Must fix before publication

| ID | Affected page/component | Confirmed problem and evidence | Recommended solution | Priority |
| --- | --- | --- | --- | --- |
| MF-1 | [Network & Partnerships](https://bengtove.github.io/-core-math-website-test/network-partnerships/) — International Science Programme partner | The official ISP partner link `https://www.uu.se/en/centre/international-science-programme` returned HTTP 404 on both HEAD and GET. | Replace it with the current official ISP destination after confirming the preferred landing page. Re-test from the deployed page. | P1 |
| MF-2 | [Math4SDG](https://bengtove.github.io/-core-math-website-test/projects/math4sdg/) | The linked Norad NORHED II portfolio PDF returned HTTP 404. | Locate the current Norad portfolio/document URL, or remove the obsolete document link while retaining the verified project information. | P1 |
| MF-3 | [Opportunities](https://bengtove.github.io/-core-math-website-test/opportunities/) — rolling records | The current CIRM “Workshop Organisation” (`https://www.cirm-math.fr/en/programmes.html`) and NordForsk “Research Programmes” (`https://www.nordforsk.org/funding`) links returned HTTP 404. These are live records in `_data/open_opportunities.json`, not archival material. | Update the data feed/source records to current funder destinations, or temporarily omit records that have no valid destination. Verify the daily update workflow does not restore obsolete links. | P1 |
| MF-4 | Publications shown through [Selected publications](https://bengtove.github.io/-core-math-website-test/research/publications/) and relevant research-group pages | `https://doi.org/10.4314/tjs.v50i5.15` and `https://doi.org/10.4314/sinet.v47i2` both returned HTTP 404. The associated records are `_publications/2024-006.md` and `_publications/2024-010.md`. | Verify the DOI identifiers with the publisher or Crossref. Correct a verified identifier; otherwise retain the bibliographic entry without a DOI link. Do not invent an identifier. | P1 |
| MF-5 | Search-engine discovery / domain launch | The deployed test site returns HTTP 404 for both `/robots.txt` and `/sitemap.xml`. | Add a deliberate robots policy and generate a sitemap before the public-domain switch (for example, through the approved Jekyll sitemap mechanism). Verify both files on the final domain. | P1 |

## Recommended improvements

| ID | Affected page/component | Finding | Evidence / reproduction | Recommended solution | Priority |
| --- | --- | --- | --- | --- | --- |
| RI-1 | Historical news: [2025 Nairobi Workshop](https://bengtove.github.io/-core-math-website-test/news/2025/2025-nairobi-workshop-in-algebraic-geometry/) and [ESPIDAM](https://bengtove.github.io/-core-math-website-test/news/2025/the-2nd-european-summer-program-in-infectious-disease-analysis-and-modelling-espidam/) | Each contains an external historical reference that now returns 404. | The Nairobi Google Sites page and Stockholm University ESPIDAM URL both returned 404 on GET. | Find updated archival destinations if available; otherwise remove only the dead external link while preserving the article text. | P2 |
| RI-2 | Network & Partnerships member directory | Thirteen of the 17 member images are external hotlinks. They were available at audit time, but they remain dependent on third-party hosts, URLs and hotlink policies. | All 17 image URLs returned HTTP 200 during this audit; the dependency risk is architectural, not a current breakage. | Where licensing permits, progressively replace critical external images with local, optimised assets and retain source attribution as appropriate. | P2 |
| RI-3 | Network & Partnerships and news assets | Several local images are unnecessarily large for their rendered uses. | `uppsala-university-angstrom-laboratory.jpeg` is 9.3 MB; `university-of-vienna-main-building.jpg` is 5.0 MB; `ukzn-fellowships-2027.png` is 2.8 MB; one news AVIF is 1.8 MB. The CoRE-Math mark is 1.2 MB despite rendering at 58px in the header. | Produce appropriately sized, compressed responsive assets while preserving the existing crops, quality and filenames/URLs where possible. | P2 |
| RI-4 | `/projects/fame/` | The FAME project detail page is published but is not linked from the Programmes & Projects listing; the listing links only to FAME’s external site. | Repository search finds no internal link to `/projects/fame/`. This is a discoverability issue, not a broken route. | Decide whether the internal FAME page has distinct value. If yes, add an appropriate internal project link; if not, redirect or retire it only after an editorial decision. | P2 |
| RI-5 | Mobile navigation and responsive page families | Static implementation is sound, but a final test on real Safari/Android devices is still required before launch. | The mobile menu is a button with `aria-expanded`, `aria-controls` and a `hidden` navigation panel; desktop rail changes at 1280px. This audit could not obtain a native-browser screen capture in the current environment. | Test repeated open/close, link selection, keyboard focus, and scrolling at 390px, 768px, 1024px and 1280px on actual devices. Record any reproducible issue before launch. | P2 |
| RI-6 | Long-form and structured pages | The Strategy table deliberately scrolls horizontally on narrow screens, and specialised grids change at several breakpoints. | Static CSS shows explicit overflow handling for the Strategy table and component thresholds at 600px, 700px, 760px, 850px, 860px and 1280px. No source-level overflow defect was found. | Include Strategy, Network & Partnerships, Education, Research, Opportunities and News & Events in the final visual-device pass. | P2 |

## Can wait until after publication

| ID | Affected page/component | Finding | Recommended handling | Priority |
| --- | --- | --- | --- | --- |
| CW-1 | Third-party external links | Twelve URLs could not be conclusively checked by automation: ICTP pages timed out; Math4SDG and Leverhulme returned 403; EAMO returned 503; ICMS produced DNS/socket errors. These may be bot protection or temporary third-party outages. | Open these in a normal browser before launch if they are prominent; do not treat an automated 403/timeout alone as a site defect. Monitor rather than block launch unless a visitor-facing link is confirmed unavailable. | P3 |
| CW-2 | Outbound link behaviour | `external-links.js` opens external links in a new tab and adds `noopener noreferrer`, but the text generally does not announce that behaviour. | Consider adding a concise, consistent disclosure only if user testing shows confusion. This is not a material accessibility failure. | P3 |
| CW-3 | Accessibility completeness | Static review found semantic landmarks, labelled mobile navigation, labelled filters, visible shared focus styles, descriptive member-dialog controls, and non-duplicated keyboard access for homepage/news listing images. A screen-reader pass has not been performed in this audit. | Run a short NVDA/VoiceOver pass after the blocking link and indexing fixes, concentrating on menu, filters, dialogs, lightbox and tables. | P3 |
| CW-4 | Historical source URLs | Older external research/news references can change independently of CoRE-Math. | Recheck periodically or when maintaining the relevant historical page; do not allow this to become a broad editorial rewrite. | P3 |

## Responsive design and visual-consistency assessment

The final warm-neutral design is implemented in the shared tokens: warm outer/surface/rail colours, dark-neutral body and heading text, terracotta editorial entry rules and labels, and blue branding/navigation/links. The static review found the documented patterns in place:

- the desktop rail appears at `1280px` and above; compact Menu navigation is used below that threshold;
- editorial grids preserve source order and original wide-layout terracotta rule assignment when they stack;
- quiet grey rules remain structural dividers rather than generic decoration;
- the Strategy table uses horizontal scrolling rather than compressed, unreadable columns;
- normal prose remains bounded by the `52rem` reading measure; and
- page-specific grid breakpoints are present for specialised directories and catalogues.

No confirmed CSS overflow, overlap or palette inconsistency was found through source inspection. A native visual capture could not be produced in this environment, so the real-device checks in RI-5 and RI-6 remain recommended rather than claimed as completed visual tests.

## Accessibility assessment

### Confirmed strengths

- All checked informative inline images have alternative text; decorative branding/listing images are intentionally empty-alt or hidden from duplicate keyboard navigation.
- The shared `:focus-visible` treatment is a 3px blue outline with offset for links, buttons, summaries and form controls.
- The mobile navigation has a labelled `nav`, an explicit button/control relationship, and programmatic expanded/hidden state.
- Member profiles use native `dialog`, labelled headings, a labelled close control and focus restoration.
- Funding filters have explicit labels and a polite live status region.
- Markdown heading-level scan found no heading skips in published content sources. Component templates use the expected H1/H2/H3 hierarchy for their page families.
- Checked palette pairs meet WCAG AA normal-text contrast; the weakest checked pair, muted text on the main warm surface, is 6.25:1.

### Remaining verification limits

- Actual assistive-technology behaviour and touch interaction require a manual device/screen-reader pass (CW-3 and RI-5).
- Contrast was calculated from implemented colour tokens. The desktop hero overlay is translucent, although white text remains high contrast against the dark blue overlay; visual confirmation against the actual image remains part of RI-6.

## Content completeness and relationships

- No public-content placeholder, TODO, empty `href`, empty Markdown link or unfinished-page marker was found.
- The 39 funding records contain 25 Open and 14 Rolling opportunities; none of the Open records has a parsed past deadline at the audit date.
- Event/programme/project/research-group relationships resolve correctly for all 14 event records.
- Intentional compatibility redirects for former project URLs are present and resolve.
- The only clear discoverability issue found is the orphaned FAME detail page (RI-4). Compatibility redirects are intentionally not main-navigation destinations.

## Deployment considerations for switching to the existing domain

1. **Resolve MF-1 through MF-5 first** and make a final browser/device check of RI-5 and RI-6.
2. Confirm the target domain’s ownership and current DNS records before changing GitHub Pages settings. Do not remove the existing site until rollback requirements are agreed.
3. In `_config.yml`, change `url` from `https://bengtove.github.io` to the final canonical origin and change `baseurl` from `/-core-math-website-test` to the final site path (normally empty for a root-domain site). The current use of `relative_url` is healthy for this migration, but the change must be tested in a preview/staging build.
4. Configure the custom domain in GitHub Pages, add the required DNS record(s) at the domain provider, and add/verify `CNAME` only when that configuration is approved. Keep HTTPS enforcement enabled.
5. Verify final-domain canonical and Open Graph URLs, all redirects, `robots.txt`, `sitemap.xml`, CSS/JS cache-busted URLs, collection routes, internal links, external links and the homepage event updater.
6. Preserve the current test URL until final-domain DNS, certificate provisioning and a rollback plan have been confirmed. Use the test site as the immediate fallback during the transition.
7. After the switch, submit the final sitemap to the relevant search-console property and monitor Pages deployment/build status, 404s and third-party image loading.

## Site-map status

**Completed and current enough for publication planning.** `docs/site-map.md` and `docs/page-inventory.md` are dated 18 October 2026. Their stated collection counts match the current source exactly, and their 99 generated content routes are represented in the deployed route check. The map correctly distinguishes main-navigation pages, internal detail pages, event/news collections, compatibility redirects and non-route university-profile dialogs.

No revision is required as part of this audit. Update the snapshot date and inventory only when a page, collection record, navigation relationship or redirect changes.

## Limitations

- This is not a full factual/editorial review of institutional claims, dates or historical content.
- External availability is point-in-time and may be affected by bot protection, rate limiting and third-party outages.
- The local repository has no `Gemfile`, so `bundle exec jekyll build` is not reproducible in this checkout. The authoritative GitHub Pages build for the audited commit completed successfully.
