#!/usr/bin/env python3
"""Fail when a source reference targets a missing local asset.

External URLs are deliberately not fetched: their availability is outside the
repository's build boundary. The check covers local content assets (images and
documents) that GitHub Pages can reliably validate during every source change.
Theme-provided styles and scripts are checked by the Jekyll build itself.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SUFFIXES = {".css", ".html", ".js", ".json", ".md", ".svg", ".yaml", ".yml"}
ASSET_PATTERN = re.compile(r"/assets/(?:images|documents)/[^\s\"'`<>|})]+")
IGNORED_PARTS = {".git", "_site", "vendor"}


def source_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in SOURCE_SUFFIXES
        and not any(part in IGNORED_PARTS for part in path.parts)
    ]


def asset_references(path: Path) -> set[str]:
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return set()
    return {reference.rstrip(".,;:") for reference in ASSET_PATTERN.findall(content)}


def main() -> int:
    missing: list[tuple[Path, str]] = []
    checked = 0

    for path in source_files():
        for reference in asset_references(path):
            checked += 1
            asset_path = ROOT / reference.lstrip("/")
            if not asset_path.is_file():
                missing.append((path.relative_to(ROOT), reference))

    if missing:
        print("Missing local asset references:", file=sys.stderr)
        for source, reference in missing:
            print(f"  {source}: {reference}", file=sys.stderr)
        return 1

    print(f"Checked {checked} local asset references: all files exist.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
