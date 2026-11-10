# CoRE-Math instructions for Codex

## Authoritative storage

GitHub is the authoritative repository for final CoRE-Math website content,
communications material and related project documentation. Commit final
deliverables to the appropriate existing repository folders and push through
the established workflow, respecting any task-specific publication limits.
A local checkout or Codex working directory under Documents is temporary
working space, not a permanent archive or the sole home of a final deliverable.

Do not use Dropbox as a parallel archive for new website or communications
material. Avoid unnecessary copies, review packages, exports and intermediate
files; retain only useful final assets, editable sources and supporting records.
Preserve existing conventions; do not introduce a new folder structure or
storage system without a clear need. Do not reorganise existing material as a
side effect of ordinary work.

## Where files belong

| Material | Existing repository location |
|---|---|
| Website pages and structured content | Existing root pages, `universities/`, `_posts/`, `_events/`, `_programmes/`, `_projects/`, `_research_groups/` and `_data/`, according to the current content type. |
| Website code, styling and configuration | `_layouts/`, `_includes/`, `assets/css/`, `assets/js/`, `scripts/`, `tests/`, `_config.yml` and `.github/workflows/`. |
| Design principles and implementation guidance | `docs/design-principles.md`, `docs/design-system.md` and the existing related design/editorial documents. |
| Communications: posts, graphics, editable sources and supporting documentation | `_communications/`; reuse `_communications/linkedin/` and its existing post-specific folders. The central mention reference is `_communications/linkedin/organisation-ids.md`. Undeployed final work may live on a named GitHub branch; report that branch. |
| Website photographs and originals supplied for new website work | The applicable existing `assets/images/` subject folder, preserving originals separately from derivatives and retaining established names/IDs. Do not replace an original with an export. Existing externally stored originals are not migrated by this policy. |
| Photograph attribution and provenance | Existing `_data/member_photographs.yml`, relevant page/post image metadata, `photo-credits.md`, and associated communications attribution files. Retain creators, sources, licences, copyright notices and modification records; keep public-safe evidence in GitHub alongside the relevant documentation. |
| Other project documentation | `docs/`, linked from `docs/README.md` where useful; use the relevant communications folder for post-specific records. |

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
publishes the website; use a separate branch when deployment is not authorised.
Keep temporary build outputs out of commits. Report exact final repository
paths, branch and whether files were committed and pushed (including commit
ID), plus any remaining publication or storage limitation.

These storage instructions supersede older directions to keep new website or
communications deliverables only in Dropbox or local working folders. Historical
archive procedures describe existing records, not a new storage policy.
