# CoRE-Math picture archive workflow

This is the website-facing operational guide to selecting and preparing
photographs. The permanent archive, original files, permissions evidence and
activity records remain in Dropbox; this repository contains only the web
derivatives and documentation needed to publish them consistently. It does not
replace the wider CoRE-Math communication or image-policy material held in
Dropbox.

The archive is stored in Dropbox at:

`/CoRE-Math/06. Communication, Dissemination, and Visibility/Pictures/`

It is deliberately simple: browse pictures in Dropbox, preserve originals, embed standard metadata in working masters, and keep web copies separate. The archive is not a website asset folder and does not replace the website repository.

## Folder structure

```text
Pictures/
  00-Inbox/
  _unidentified/
  _external-reference-only/
  YYYY/
    YYYY-MM-DD-activity-name/
      activity.json
      originals/
      masters/       # only when metadata/editing is required
      web/           # only when a derivative is required
      rights/
  archive-index.csv
```

Use a date only when it is known. If only month and year are known, use `YYYY-MM-activity-name`; do not invent a day. `IPMS pictures` remains outside this workflow until separately reviewed.

## Adding new photographs

1. Ask the contributor to send the original file, not a screenshot, social-media download or web export. They should supply: activity, date and location; photographer; copyright holder; requested credit; source; and explicit permission/restrictions for web publication.
2. Place received files in `00-Inbox/` while checking the information. Do not alter the received file.
3. Create the year/activity folder and move the unchanged received file to `originals/`. Assign the next permanent identifier, for example `CM-PH-000028`.
4. Create `activity.json` from the template below. Store common activity information there once rather than repeating it in each image.
5. If metadata or a web image is required, copy the original to `masters/`. Add IPTC/XMP fields to the copy only. For an immutable received file that must remain untouched, store its identifiers and provenance in a same-name `.xmp` sidecar. Leave unknown fields blank or use `unknown` in the activity record; never infer authorship, copyright or permission.
6. Create a file in `web/` only after permission for publication has been recorded. Copy that derivative, not the original, to the GitHub repository. Add an accurate caption, credit and alt text to the page/post.

## Metadata and rights

The master must use standard IPTC/XMP fields where known:

- `XMP-xmp:Identifier`: permanent ID, such as `CM-PH-000028`.
- `XMP-dc:Title` and `XMP-dc:Description`: title and factual caption.
- `EXIF:DateTimeOriginal` / `XMP-xmp:CreateDate`: actual capture time only.
- IPTC Core location/city/country fields.
- `XMP-dc:Creator`, `XMP-dc:Rights`, `XMP-photoshop:Credit` and `XMP-photoshop:Source`.
- `XMP-xmpRights:UsageTerms` and `XMP-xmpRights:WebStatement` for documented terms.
- `XMP-dc:Subject` for controlled keywords, for example `Institution|Makerere University` and `Programme|Industrial Mathematics`.

Use the following rights-status values in `activity.json`: `unknown`, `permission-requested`, `approved-web`, `restricted`, `CC/licensed`, or `public-domain`. A webpage that happens to display a picture is not permission evidence.

## Activity record template

Save this as `activity.json` in each activity folder. Keep unknown values as `null` or `"unknown"`.

```json
{
  "activity_id": "CM-ACT-2026-0001",
  "title": "Activity title",
  "date": "2026-10-02",
  "source_post_date": null,
  "location": "Institution, city, country",
  "institutions": ["Institution name"],
  "networks": ["CoRE-Math"],
  "programmes": [],
  "projects": [],
  "source_urls": [],
  "rights_status": "unknown",
  "rights_evidence": null,
  "notes": ""
}
```

Use `date` only for a verified activity date or date range. When a historical image is associated only with a dated website post, leave `date` as `null` and record that post date separately in `source_post_date`.

## Browsing and catalogue

Browse visually in Dropbox by year and activity. For searching by title, person, institution, programme, rights status or source, open `archive-index.csv` in Numbers, Excel, LibreOffice or any text editor.

The catalogue is generated, never manually edited. Once ExifTool is installed and the Dropbox folder is synced locally, run:

```sh
python3 scripts/generate_photo_archive_catalog.py \
  "$HOME/Library/CloudStorage/Dropbox/CoRE-Math/06. Communication, Dissemination, and Visibility/Pictures"
```

The generator reads embedded metadata (and same-name `.xmp` sidecars when an original must remain untouched) plus `activity.json` records, then rewrites `archive-index.csv`. It does not modify photographs. Its `rights_status` column comes from the activity record; XMP usage terms are retained separately.

## Preparing web copies

1. Check `rights_status` and the evidence before creating a derivative.
2. Work from `masters/`, preserving the original aspect ratio and retaining the original in `originals/`.
3. Create a reasonably sized JPEG or AVIF in `web/`; name it from the permanent identifier, for example `CM-PH-000028-card-960.avif`.
4. Record the GitHub destination in the activity record notes, then use the derivative in the website. Do not publish originals or rights correspondence.

## One-time requirement

ExifTool is required for embedded IPTC/XMP writing and catalogue generation. Install it locally on the archive-maintenance Mac with Homebrew:

```sh
brew install exiftool
```

Then test it on a copied master, never on an original. The repository script is intentionally dependency-free apart from ExifTool and Python 3, which macOS provides.

If ExifTool is installed outside the shell `PATH`, set `EXIFTOOL` to its executable path when generating the catalogue.
