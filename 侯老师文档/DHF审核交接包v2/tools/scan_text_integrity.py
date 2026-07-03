#!/usr/bin/env python3
"""Scan text files for likely mojibake or destructive replacement.

This is intentionally conservative. It flags:
- repeated question marks, usually created when Unicode was replaced by ASCII;
- U+FFFD replacement characters;
- common UTF-8-as-CP1252 mojibake markers.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


BAD_RE = re.compile(
    r"\?{3,}|\ufffd|\u00c3.|\u00c2.|\u00e2[\u0080-\u009f]"
)
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".csv",
    ".json",
    ".html",
    ".htm",
    ".py",
    ".mdc",
    ".yaml",
    ".yml",
}


def iter_files(root: Path):
    if root.is_file():
        yield root
        return
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def scan_file(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return {
            "path": str(path),
            "line": 0,
            "match": "UnicodeDecodeError",
            "snippet": str(exc),
        }

    for index, line in enumerate(text.splitlines(), start=1):
        match = BAD_RE.search(line)
        if match:
            return {
                "path": str(path),
                "line": index,
                "match": match.group(0),
                "snippet": line[:240],
            }
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    findings = []
    for raw in args.paths:
        root = Path(raw)
        for path in iter_files(root):
            finding = scan_file(path)
            if finding:
                findings.append(finding)

    if args.json:
        print(json.dumps(findings, ensure_ascii=True, indent=2))
    else:
        for finding in findings:
            print(
                f"{finding['path']}:{finding['line']}: "
                f"{finding['match']} :: {finding['snippet']}"
            )

    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
