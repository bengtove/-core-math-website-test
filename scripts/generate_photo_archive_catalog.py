#!/usr/bin/env python3
"""Build a portable CoRE-Math photo catalogue from XMP/IPTC and activity records.

The archive itself lives in Dropbox. Run this script against the synced
`Pictures` folder after ExifTool has added metadata to working masters or
sidecar XMP files. It does not alter photographs.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
from pathlib import Path


FIELDS = [
    "asset_id", "activity_id", "activity_title", "activity_date", "source_post_date",
    "activity_location", "activity_institutions", "activity_programmes",
    "file", "file_role", "title", "description", "date_photographed",
    "location", "photographer", "copyright_holder", "credit_line", "source",
    "rights_status", "rights_evidence", "usage_terms", "keywords",
]


def value(record: dict, *keys: str) -> str:
    for key in keys:
        item = record.get(key)
        if isinstance(item, list):
            return " | ".join(str(entry) for entry in item)
        if item not in (None, ""):
            return str(item)
    return ""


def activity_records(root: Path) -> dict[Path, dict]:
    records: dict[Path, dict] = {}
    for path in root.rglob("activity.json"):
        try:
            records[path.parent] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise SystemExit(f"Cannot read {path}: {error}") from error
    return records


def parent_activity(path: Path, activities: dict[Path, dict]) -> dict:
    for folder in (path.parent, *path.parents):
        if folder in activities:
            return activities[folder]
    return {}


def image_files(root: Path) -> list[Path]:
    extensions = {".jpg", ".jpeg", ".tif", ".tiff", ".png", ".webp", ".avif", ".heic"}
    ignored = {"00-Inbox", "rights", "IPMS pictures"}
    return sorted(
        path for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in extensions and not any(part in ignored for part in path.parts)
    )


def metadata(paths: list[Path]) -> dict[str, dict]:
    if not paths:
        return {}
    exiftool = os.environ.get("EXIFTOOL", "exiftool")
    if not shutil.which(exiftool) and not Path(exiftool).is_file():
        raise SystemExit("ExifTool is required. Install it, then run this command again.")
    sidecars = [path.with_suffix(".xmp") for path in paths if path.with_suffix(".xmp").is_file()]
    command = [exiftool, "-j", "-G1", "-a", "-s", *(str(path) for path in [*paths, *sidecars])]
    output = subprocess.run(command, check=True, capture_output=True, text=True).stdout
    extracted = {str(Path(item["SourceFile"]).resolve()): item for item in json.loads(output)}
    merged: dict[str, dict] = {}
    for path in paths:
        main = extracted.get(str(path.resolve()), {})
        sidecar = extracted.get(str(path.with_suffix(".xmp").resolve()), {})
        merged[str(path.resolve())] = {**main, **sidecar}
    return merged


def role(path: Path) -> str:
    for part in path.parts:
        if part in {"originals", "masters", "web"}:
            return part
    return "unclassified"


def row(path: Path, root: Path, item: dict, activity: dict) -> dict:
    return {
        "asset_id": value(item, "XMP-xmp:Identifier", "XMP-photoshop:TransmissionReference"),
        "activity_id": value(activity, "activity_id"),
        "activity_title": value(activity, "title"),
        "activity_date": value(activity, "date"),
        "source_post_date": value(activity, "source_post_date"),
        "activity_location": value(activity, "location"),
        "activity_institutions": value(activity, "institutions"),
        "activity_programmes": value(activity, "programmes"),
        "file": str(path.relative_to(root)),
        "file_role": role(path),
        "title": value(item, "XMP-dc:Title", "IPTC:ObjectName"),
        "description": value(item, "XMP-dc:Description", "IPTC:Caption-Abstract"),
        "date_photographed": value(item, "EXIF:DateTimeOriginal", "XMP-xmp:CreateDate", "XMP-photoshop:DateCreated"),
        "location": value(item, "XMP-iptcCore:Location", "XMP-photoshop:City"),
        "photographer": value(item, "XMP-dc:Creator", "IPTC:By-line"),
        "copyright_holder": value(item, "XMP-dc:Rights", "IPTC:CopyrightNotice"),
        "credit_line": value(item, "XMP-photoshop:Credit", "IPTC:Credit"),
        "source": value(item, "XMP-photoshop:Source", "IPTC:Source"),
        "rights_status": value(activity, "rights_status") or value(item, "XMP-xmpRights:UsageTerms"),
        "rights_evidence": value(activity, "rights_evidence"),
        "usage_terms": value(item, "XMP-xmpRights:UsageTerms"),
        "keywords": value(item, "XMP-dc:Subject", "IPTC:Keywords"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="synced Dropbox Pictures folder")
    parser.add_argument("--output", type=Path, help="output CSV (default: archive-index.csv in archive)")
    args = parser.parse_args()
    root = args.archive.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Archive folder does not exist: {root}")
    destination = args.output or root / "archive-index.csv"
    activities = activity_records(root)
    paths = image_files(root)
    extracted = metadata(paths)
    rows = [row(path, root, extracted.get(str(path.resolve()), {}), parent_activity(path, activities)) for path in paths]
    missing_ids = [entry["file"] for entry in rows if not entry["asset_id"]]
    if missing_ids:
        raise SystemExit("Missing permanent asset identifier(s): " + ", ".join(missing_ids))
    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {destination} ({len(rows)} image records).")


if __name__ == "__main__":
    main()
