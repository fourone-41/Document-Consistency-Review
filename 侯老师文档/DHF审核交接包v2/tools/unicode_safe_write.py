#!/usr/bin/env python3
"""Write text files through a single UTF-8-safe channel.

Why this exists:
- Windows PowerShell and command-line argument passing can replace CJK text with
  question marks before Python receives it.
- This script avoids that by accepting content from UTF-8 files, JSON files with
  escaped Unicode, or base64 payloads.

Recommended use:
  python tools/unicode_safe_write.py --path out.md --json payload.json --key content
  python tools/unicode_safe_write.py --path out.md --base64-file payload.b64
  python tools/unicode_safe_write.py --path out.md --text-file source.utf8.txt
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import sys
from pathlib import Path


BAD_RE = re.compile(r"\?{3,}|\ufffd")


def has_bad_text(text: str) -> bool:
    return bool(BAD_RE.search(text))


def load_text(args: argparse.Namespace) -> str:
    sources = [
        bool(args.text_file),
        bool(args.json),
        bool(args.base64_file),
        args.stdin_base64,
    ]
    if sum(sources) != 1:
        raise SystemExit("Choose exactly one input source.")

    if args.text_file:
        return Path(args.text_file).read_text(encoding="utf-8")

    if args.json:
        data = json.loads(Path(args.json).read_text(encoding="utf-8"))
        value = data
        for key in args.key.split("."):
            value = value[key]
        if not isinstance(value, str):
            raise SystemExit("Selected JSON value is not a string.")
        return value

    if args.base64_file:
        raw = Path(args.base64_file).read_text(encoding="ascii").strip()
        return base64.b64decode(raw).decode("utf-8")

    raw_stdin = sys.stdin.read().strip()
    return base64.b64decode(raw_stdin).decode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Output file path")
    parser.add_argument("--text-file", help="UTF-8 source text file")
    parser.add_argument("--json", help="JSON source file; Unicode escapes are safe")
    parser.add_argument("--key", default="content", help="JSON key path, default: content")
    parser.add_argument("--base64-file", help="Base64 source file")
    parser.add_argument("--stdin-base64", action="store_true", help="Read base64 from stdin")
    parser.add_argument("--allow-suspicious", action="store_true")
    args = parser.parse_args()

    text = load_text(args)
    if has_bad_text(text) and not args.allow_suspicious:
        raise SystemExit("Refusing to write suspicious replacement markers.")

    out = Path(args.path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="")

    reread = out.read_text(encoding="utf-8")
    if reread != text:
        raise SystemExit("Write verification failed: read-back content differs.")
    if has_bad_text(reread) and not args.allow_suspicious:
        raise SystemExit("Write verification failed: suspicious text after write.")

    print(json.dumps({"status": "ok", "path": str(out), "chars": len(text)}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
