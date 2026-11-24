# CoRE-Math instructions for Codex

## Authoritative storage

Permanent storage conventions:

- **GitHub:** Website content, code, maintenance instructions and publicly
  downloadable resources. Commit public deliverables to the existing repository
  folders, respecting publication limits and redistribution rights.
- **Dropbox `/0. CoRE-Math/`:** Main CoRE-Math document archive.
- **Dropbox `/CoRE-Math Archive – Restricted/`:** Source materials retained
  for internal reference, not for public distribution. Its existing subfolders
  are `Conference documentation` and `External coverage`.

On 24 November 2026, the owner confirmed that they had manually checked the
restricted archive's sharing settings and no other users had been granted
access. This is an owner-confirmed access record, not an automated verification.

For restricted archival material, link from the website to the original external
source, never to the archived copy. Do not create public sharing links, upload
restricted copies to GitHub, or expose them through website download fields.
The main Dropbox archive must not be treated as a restricted destination.

Local Codex folders are temporary working space, not a permanent archive.
Reuse existing folders and file-naming conventions. Do not create additional
folders, change sharing permissions, or move, delete or reorganise existing
documents as a side effect of maintenance. These storage rules do not authorise
such changes. See [website administration](docs/website-administration.md#storage-and-archiving).

## Where files belong

| Material | Storage location |
|---|---|
| Website pages and structured content | Existing root pages, `universities/`, `_posts/`, `_events/`, `_programmes/`, `_projects/`, `_research_groups/` and `_data/`, according to the current content type. |
| Website code, styling and configuration | `_layouts/`, `_includes/`, `assets/css/`, `assets/js/`, `scripts/`, `tests/`, `_config.yml` and `.github/workflows/`. |
| Design principles and implementation guidance | `docs/design-principles.md`, `docs/design-system.md` and the existing related design/editorial documents. |
| Public-safe website communications: posts, graphics, editable sources and supporting documentation | `_communications/`; reuse `_communications/linkedin/` and its existing post-specific folders. The central mention reference is `_communications/linkedin/organisation-ids.md`. Undeployed final work may live on a named GitHub branch; report that branch. |
| Website photographs and originals supplied for new website work | The applicable existing `assets/images/` subject folder, preserving originals separately from derivatives and retaining established names/IDs. Do not replace an original with an export. Existing externally stored originals are not migrated by this policy. |
| Photograph attribution and provenance | Existing `_data/member_photographs.yml`, relevant page/post image metadata, `photo-credits.md`, and associated communications attribution files. Retain creators, sources, licences, copyright notices and modification records; keep public-safe evidence in GitHub alongside the relevant documentation. |
| Website maintenance documentation | `docs/`, linked from `docs/README.md` where useful. |
| General CoRE-Math documents | Dropbox `/0. CoRE-Math/`; use the appropriate existing archive folder. |
| Internal source materials not for public distribution | Dropbox `/CoRE-Math Archive – Restricted/Conference documentation/` or `/CoRE-Math Archive – Restricted/External coverage/`, according to the material. |
| Publicly downloadable resources | Existing appropriate `assets/documents/` folders in GitHub, only where public redistribution is permitted. |

## Photographs and existing archives

Website photographs and their attribution records remain in GitHub. Do not
assume that an optimised website image is an archival original. For new
originals, check redistribution rights and repository size constraints before
committing; report a concrete constraint rather than silently creating a new
external archive. Do not commit confidential correspondence, credentials or
restricted originals to the public repository. Record public-safe provenance
and the limitation instead.

The location and tooling for a broader, visually browsable photographic library
are undecided. Do not assume the existing Dropbox collection is complete.
Do not move, delete or reorganise photographs in Dropbox or elsewhere without
an explicit task to do so. Preserve existing archive references and records;
this policy does not authorise migration, catalogue regeneration or cleanup.
Existing recovery backups are not authoritative working archives and do not
justify new parallel collections of deliverables.

## Workflow and completion reporting

Read `docs/README.md` and the relevant existing authoring/design guidance.
Follow `docs/website-administration.md` for GitHub publishing. A push to `main`
publishes the website. For routine website updates, work directly on `main` and
deploy without creating review branches or requesting additional approval.
Use a separate branch when the user explicitly requests review-only work or
withholds deployment authorisation.
Keep temporary build outputs out of commits. Report exact final repository
paths, branch and whether files were committed and pushed (including commit
ID), plus any remaining publication or storage limitation.

These permanent storage conventions supersede conflicting earlier storage
guidance. Historical archive procedures describe existing records and do not
authorise new folders, migrations or sharing changes.
