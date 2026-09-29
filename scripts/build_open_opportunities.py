#!/usr/bin/env python3
"""Build deterministic public opportunity data from the restricted Coda table."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://coda.io/apis/v1"
DOCUMENT_ID = "twgdrEvtAq"
TABLE_ID = "grid-DWbBoJPU0E"

COLUMNS = {
    "programme": "c-hgesZqt97J",
    "funder": "c-UOTvWcWqhw",
    "description": "c-OrIOg9CUPE",
    "status": "c-w_COF9nRww",
    "deadline": "c-PCA_1hp23U",
    "deadline_note": "c-EAm7jWk5aP",
    "support_type": "c-eKVKLI88t_",
    "career_stage": "c-dJzcLWwGR8",
    "region": "c-xiaIgEGf9",
}
INTERNAL_URL_COLUMN = "c-wzYiAIeRZO"
PUBLISHED_STATUSES = {"Open", "Rolling"}
REQUIRED_KEYS = tuple(COLUMNS)
OPTIONAL_KEYS = {"url"}

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^\s)]+)\)")
RAW_URL_RE = re.compile(r"https?://[^\s<>\]\[\]\"'()`]+")


class BuildError(RuntimeError):
    """Raised when retrieval or validation cannot safely complete."""


def api_get(token: str, path: str, params: dict[str, Any]) -> dict[str, Any]:
    query = urllib.parse.urlencode(params)
    url = f"{BASE_URL}{path}"
    if query:
        url = f"{url}?{query}"
    request = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        raise BuildError(f"Coda API returned HTTP {error.code} for {path}") from None
    except urllib.error.URLError as error:
        raise BuildError(f"Could not reach the Coda API: {error.reason}") from None
    except json.JSONDecodeError:
        raise BuildError("Coda API returned invalid JSON") from None
    if not isinstance(payload, dict):
        raise BuildError("Coda API returned an unexpected response structure")
    return payload


def fetch_all_rows(token: str, value_format: str) -> list[dict[str, Any]]:
    path = f"/docs/{DOCUMENT_ID}/tables/{TABLE_ID}/rows"
    params: dict[str, Any] = {
        "limit": 500,
        "useColumnNames": "false",
        "valueFormat": value_format,
    }
    rows: list[dict[str, Any]] = []
    while True:
        payload = api_get(token, path, params)
        items = payload.get("items")
        if not isinstance(items, list):
            raise BuildError("Coda row response did not contain an items array")
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get("id"), str):
                raise BuildError("Coda returned a row without an immutable row ID")
            if not isinstance(item.get("values"), dict):
                raise BuildError(f"Coda row {item['id']} did not contain a values object")
            rows.append(item)
        next_token = payload.get("nextPageToken")
        if not next_token:
            break
        if not isinstance(next_token, str):
            raise BuildError("Coda returned an invalid pagination token")
        params["pageToken"] = next_token
    return rows


def public_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        items = [public_text(item) for item in value]
        return ", ".join(item for item in items if item)
    raise BuildError(f"Unsupported public cell value type: {type(value).__name__}")


def normalized_url(candidate: str) -> str | None:
    candidate = candidate.strip().rstrip(".,;:")
    parsed = urllib.parse.urlparse(candidate)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None
    hostname = (parsed.hostname or "").casefold()
    if hostname == "coda.io" or hostname.endswith(".coda.io"):
        return None
    if hostname == "docs.superhuman.com":
        return None
    return urllib.parse.urlunparse(parsed)


def extract_urls(value: Any) -> set[str]:
    candidates: set[str] = set()
    if isinstance(value, str):
        strings = MARKDOWN_LINK_RE.findall(value) + RAW_URL_RE.findall(value)
        for item in strings:
            url = normalized_url(item)
            if url:
                candidates.add(url)
    elif isinstance(value, list):
        for item in value:
            candidates.update(extract_urls(item))
    elif isinstance(value, dict):
        for key in ("url", "href", "browserLink"):
            if key in value:
                candidates.update(extract_urls(value[key]))
        for key in ("value", "values", "text", "content"):
            if key in value:
                candidates.update(extract_urls(value[key]))
    return candidates


def warning(programme: str, issue: str) -> None:
    safe_programme = programme.replace("\n", " ").replace("\r", " ")
    print(f"::warning title=Opportunity URL omitted::{safe_programme}: {issue}")


def resolve_url(
    programme: str, rich_values: dict[str, Any]
) -> tuple[str | None, str]:
    programme_urls = extract_urls(rich_values.get(COLUMNS["programme"]))
    internal_urls = extract_urls(rich_values.get(INTERNAL_URL_COLUMN))

    if len(programme_urls) > 1 or len(internal_urls) > 1:
        warning(programme, "one or both URL sources contained multiple candidates")
        return None, "multiple"

    programme_url = next(iter(programme_urls), None)
    internal_url = next(iter(internal_urls), None)
    if programme_url and internal_url:
        if programme_url == internal_url:
            return programme_url, "matching_both"
        warning(programme, "the rich Programme link and URLs (internal) conflicted")
        return None, "conflict"
    if programme_url:
        return programme_url, "programme_rich"
    if internal_url:
        return internal_url, "urls_internal"

    warning(programme, "no unambiguous HTTP/HTTPS URL was returned")
    return None, "missing"


def record_sort_key(record: dict[str, str]) -> tuple[str, ...]:
    return tuple(record.get(key, "").casefold() for key in (*REQUIRED_KEYS, "url"))


def validate_records(records: list[dict[str, str]]) -> None:
    previous_key: tuple[str, ...] | None = None
    for index, record in enumerate(records):
        keys = set(record)
        if not set(REQUIRED_KEYS).issubset(keys):
            missing = sorted(set(REQUIRED_KEYS) - keys)
            raise BuildError(f"Generated record {index} is missing fields: {missing}")
        if keys - set(REQUIRED_KEYS) - OPTIONAL_KEYS:
            raise BuildError(f"Generated record {index} contains unexpected fields")
        if any(not isinstance(value, str) for value in record.values()):
            raise BuildError(f"Generated record {index} contains a non-string value")
        if not record["programme"]:
            raise BuildError(f"Generated record {index} has no Programme value")
        if record["status"] not in PUBLISHED_STATUSES:
            raise BuildError(f"Generated record {index} has an unpublished Status")
        if "url" in record and normalized_url(record["url"]) != record["url"]:
            raise BuildError(f"Generated record {index} has an invalid URL")
        sort_key = record_sort_key(record)
        if previous_key is not None and sort_key < previous_key:
            raise BuildError("Generated records are not deterministically sorted")
        previous_key = sort_key


def build(token: str) -> list[dict[str, str]]:
    simple_rows = fetch_all_rows(token, "simple")
    rich_rows = fetch_all_rows(token, "rich")
    rich_by_id = {row["id"]: row for row in rich_rows}

    simple_ids = {row["id"] for row in simple_rows}
    if simple_ids != set(rich_by_id):
        raise BuildError("Simple and rich API reads returned different row sets")

    records: list[dict[str, str]] = []
    url_sources = {
        "programme_rich": 0,
        "urls_internal": 0,
        "matching_both": 0,
        "multiple": 0,
        "conflict": 0,
        "missing": 0,
    }
    for row in simple_rows:
        values = row["values"]
        status = values.get(COLUMNS["status"])
        if status not in PUBLISHED_STATUSES:
            continue

        record = {
            key: public_text(values.get(column_id))
            for key, column_id in COLUMNS.items()
        }
        rich_values = rich_by_id[row["id"]]["values"]
        url, source = resolve_url(
            record["programme"] or "<unnamed opportunity>", rich_values
        )
        url_sources[source] += 1
        if url:
            record["url"] = url
        records.append(record)

    records.sort(key=record_sort_key)
    validate_records(records)
    print(
        "URL source summary: "
        f"rich Programme only={url_sources['programme_rich']}, "
        f"URLs (internal) only={url_sources['urls_internal']}, "
        f"matching both={url_sources['matching_both']}, "
        f"omitted={url_sources['multiple'] + url_sources['conflict'] + url_sources['missing']}."
    )
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    token = os.environ.get("CODA_API_TOKEN", "")
    if not token:
        print("ERROR: The required repository secret is unavailable.", file=sys.stderr)
        return 1

    try:
        records = build(token)
        rendered = json.dumps(records, ensure_ascii=False, indent=2) + "\n"
        json.loads(rendered)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    except (BuildError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Generated {len(records)} open or rolling opportunities.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
