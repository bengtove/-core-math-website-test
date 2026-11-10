# Approved university photograph installation

> Historical record of the November 2026 preparation. Storage statements describe
> that work, not instructions for new material. Follow [AGENTS.md](../AGENTS.md)
> for current storage policy; do not move or reorganise existing originals.

This change is prepared locally only. Do not push to the deployment branch or publish without approval.

## Scope

- `_data/member_universities.yml`: approved image paths, meaningful alternative text and permanent photo IDs. All other member data and ordering are retained.
- `_data/member_photographs.yml`: reusable metadata and rights records for the 17 images.
- `assets/images/members/approved/`: separate optimised JPEG derivatives; previous image files retained.
- `network-partnerships.md` and `assets/css/network-partnerships.css`: accessible per-card credit links.
- `photo-credits.md`: original titles, creators, copyright notices, licence/source links and modification statements.
- `docs/approved-university-photo-reuse.md`: conditions for website use and a future LinkedIn collage.

## Permanent archive

The existing archive is `Dropbox/0. CoRE-Math/06. Communication, Dissemination, and Visibility/Pictures/`.

The additions use `CM-PH-000030` through `CM-PH-000046`, with `originals/`, `web/`, `rights/` and `activity.json` inside the existing year/activity structure. Unknown or disputed capture dates are kept under `_unidentified/`, with both date claims recorded. Original filenames follow the permanent ID; original bytes are unchanged. Each original has a same-stem XMP sidecar. Evidence includes the Commons API record and embedded EXIF/IPTC/XMP extraction. The root registers are `approved-university-photographs.yml` and `approved-university-photographs.md`. The generated `archive-index.csv` is refreshed after installation.

Checks compare every original's SHA-1 to Commons, record SHA-256, confirm 17 unique universities/photos, validate local image references, compare all non-image member data to the base revision, and build Jekyll. Browser review and final check results are recorded in the delivery report.

## No deployment

The local branch is `approved-university-photos`. No remote push, pull request, merge, deployment or collage publication is part of this preparation.

## Catalogue exception found during installation

Full regeneration encountered two pre-existing, uncatalogued workshop files without permanent IDs in `2024/2024-11-25-eaalg-workshop-makerere/`. These files and their metadata were not changed. The existing generator produced 34 new records from the staged approved-photo additions; those rows were appended programmatically to the existing 34 catalogue rows, which were preserved exactly. The archive catalogue therefore now has 68 records. Resolving the two older workshop IDs is separate archive maintenance.
