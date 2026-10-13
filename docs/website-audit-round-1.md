# Website audit — Round 1 implementation

**Date:** 13 October 2026

**Reference:** [Website design and consistency audit](website-design-audit.md)
**Scope:** technical reliability and accessibility maintenance only. No visual-design, typography, content or layout convention was redesigned.

## 1. Published image investigation

### What was investigated

The audit had reported five unloaded Network & Partnerships images:

- University of Bergen — local JPEG;
- University of Vienna — local JPEG;
- Uppsala University — local JPEG;
- University of Groningen — external JPEG; and
- University of Zambia MSc graduates — local AVIF also used by a news post.

The local source files were checked for existence, filename spelling and case. The corresponding published URLs were checked for successful image responses. A delayed live-browser check then confirmed that each image decoded with a non-zero intrinsic width, including the Groningen external image.

### Cause

The initial audit capture queried image dimensions before all remote and large local assets had completed decoding. It therefore produced false negatives; the files and published paths are valid. No image source, filename or content was changed.

### Prevention added

`scripts/check_local_assets.py` now checks every repository reference to local `/assets/images/` and `/assets/documents/` files. It deliberately does not fetch external images, whose availability is outside the repository build boundary. The `Check local assets` GitHub Actions workflow runs the check on pull requests and pushes to `main`.

### Remaining consideration

Several member portraits intentionally use third-party hosts. They were live during this check, but can change without a repository commit. The local check protects repository-managed assets; a future, separately approved link-monitoring task would be needed to monitor external providers.

## 2. Base stylesheet provenance

### What was investigated

`_layouts/default.html` loads `/assets/css/style.css`, even though that file is not in the repository. The published response was inspected and identified as the Primer base stylesheet supplied by GitHub Pages.

### Cause

GitHub Pages had selected Primer implicitly. The site therefore depended on an unrecorded default-theme decision for the baseline reset, Markdown styling and typography.

### Change

`_config.yml` now declares:

```yaml
theme: jekyll-theme-primer
```

This preserves the existing generated stylesheet and visual baseline while making the dependency explicit and reproducible by GitHub Pages.

## 3. Focused accessibility corrections

### Keyboard focus

The site had bespoke focus styling for selected controls, but no source-owned, consistent focus indicator for ordinary links, buttons, summaries and form controls. `assets/css/content.css` now provides a 3px CoRE-Math-blue `:focus-visible` outline with offset. It appears only for keyboard focus and does not change normal visual presentation.

### News-image links

Homepage news thumbnails are linked independently from their adjacent headline. Their decorative images have empty alternative text, which left those links without an accessible name. `index.md` now supplies each thumbnail link with `aria-label="Read [post title]"`; the image remains decorative because the title link provides the visible article title.

The News & Events listing already removes its redundant image links from the tab order with `aria-hidden="true"` and `tabindex="-1"`, while retaining the regular title link, so no change was required there.

### Opportunities filters

The three selects already have visible labels. Filter changes now also update a visually hidden `role="status"` live region with the resulting opportunity count. The existing visible no-results message remains unchanged. This gives screen-reader users confirmation when dynamic filtering changes the list.

### Dialogs, lightbox and mobile

The member-profile interface uses native labelled `<dialog>` elements, real buttons, backdrop interaction and focus restoration. The news lightbox uses a labelled native dialog, explicit controls, keyboard image navigation and focus restoration. No confirmed change was required to either interaction. At 390px the representative page families retain the mobile menu and a single-column flow without document-level horizontal overflow.

### Content checks

Source review found alternative text on content images and intentional empty alternatives on purely decorative/redundant thumbnail images. Heading hierarchy and labelled form controls were checked across homepage, primary landings, Contact, representative programme/project/research-group/event pages, a news article/archive, institutional profiles, fellowship tables and Opportunities. No editorial text was rewritten for automated checking.

## 4. Dormant Research table of contents

The Research page contained an entire hidden local-navigation block. `research.md` and `assets/css/research.css` no longer include this unused markup or its associated styles. The visible layout, section anchors and main navigation are unchanged.

## 5. Verification

- Local asset check: `python3 scripts/check_local_assets.py` — **29 local references checked; all exist**.
- Source validation: changed files pass `git diff --check`.
- Local Jekyll build: unavailable in this checkout because it has no `Gemfile`; GitHub Pages remains the project’s authoritative builder.
- Published image URLs: each previously reported local image returned `200` with the expected image content type; the Groningen external URL also returned `200` during the check.
- Rendered checks: representative primary and collection page families were inspected at 1440px, 1024px and 390px. No document-level horizontal overflow was found. Final GitHub Pages build/deployment status is reported with the implementation commit.

## Files changed

- `_config.yml`
- `.github/workflows/check-local-assets.yml`
- `scripts/check_local_assets.py`
- `assets/css/content.css`
- `assets/css/research.css`
- `assets/js/opportunities.js`
- `index.md`
- `opportunities.md`
- `research.md`
