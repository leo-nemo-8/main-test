#!/usr/bin/env python3
"""Sync changelogs/*.md to the ReadMe changelog (Announcements) via the ReadMe API v2.

ReadMe's native Git sync only reads changelogs from a `main` branch, which this
repository does not have (it syncs on `v2.0`). This script fills the gap.

Usage: sync_changelogs.py < "STATUS<TAB>PATH" lines (output of `git diff --name-status --no-renames`)

- A / M: create or update the entry. The slug is the file name without `.md`.
- D: delete the entry.

Front matter (flat `key: value`): title (required), date (YYYY-MM-DD), type
(Added, Fixed, Improved, Deprecated, Removed), hidden (true/false).
`hidden: true` maps to ReadMe's "anyone_with_link" visibility, otherwise "public".
"""
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

API = "https://api.readme.com/v2/changelogs"
TYPES = {"added", "fixed", "improved", "deprecated", "removed", "none"}
TTY = sys.stdout.isatty() or os.environ.get("GITHUB_ACTIONS") == "true"


def color(code, text):
    return f"\033[{code}m{text}\033[0m" if TTY else text


def call(method, url, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {os.environ['README_API_KEY']}")
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode()


def parse(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path}: missing front matter")
    _, header, body = text.split("---", 2)
    meta = {}
    for line in header.strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"').strip("'")
    if not meta.get("title"):
        raise ValueError(f"{path}: 'title' is required")
    kind = meta.get("type", "none").lower()
    if kind not in TYPES:
        raise ValueError(f"{path}: unknown type '{meta.get('type')}'")
    payload = {
        "title": meta["title"],
        "type": kind,
        "content": {"body": body.strip()},
        "privacy": {
            "view": "anyone_with_link" if meta.get("hidden", "false").lower() == "true" else "public"
        },
    }
    if meta.get("date"):
        payload["created_at"] = f"{meta['date']}T12:00:00Z"
    return payload


def upsert(path):
    slug = pathlib.Path(path).stem
    payload = parse(path)
    status, _ = call("GET", f"{API}/{slug}")
    if status == 200:
        status, resp = call("PATCH", f"{API}/{slug}", payload)
        action = "updated"
    elif status == 404:
        status, resp = call("POST", API, {**payload, "slug": slug})
        action = "created"
    else:
        raise RuntimeError(f"{slug}: lookup failed ({status})")
    if status not in (200, 201):
        raise RuntimeError(f"{slug}: {action} failed ({status}) {resp}")
    print(color("32", f"  {action}: {slug} ({payload['privacy']['view']})"))


def delete(path):
    slug = pathlib.Path(path).stem
    status, resp = call("DELETE", f"{API}/{slug}")
    if status not in (204, 404):
        raise RuntimeError(f"{slug}: delete failed ({status}) {resp}")
    print(color("33", f"  deleted: {slug}" if status == 204 else f"  already absent: {slug}"))


def main():
    changes = [line.split("\t") for line in sys.stdin.read().splitlines() if line.strip()]
    changes = [(s, p) for s, p in changes if p.startswith("changelogs/") and p.endswith(".md")]
    if not changes:
        print("No changelog change.")
        return 0
    print(color("1", f"Syncing {len(changes)} changelog file(s) to ReadMe"))
    errors = 0
    for status, path in changes:
        try:
            delete(path) if status == "D" else upsert(path)
        except Exception as exc:  # report every file, fail at the end
            errors += 1
            print(color("31", f"  error: {exc}"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
