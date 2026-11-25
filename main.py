#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes Zhao's own make.fun username, and nothing else, to
/output/entry.txt. The judge's first criterion is that the entry is a
real make.fun username, the entrant's own handle sent as one word, so
the entry is exactly that handle: lucky-tapir-31-2576.

Stdlib only, no network, deterministic.
"""

import os
import sys

# Zhao's own make.fun handle (@lucky-tapir-31-2576).
ENTRY = "lucky-tapir-31-2576"

# Gate from RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 30 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 30


def main() -> int:
    text = ENTRY
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} chars, outside {MIN_CHARS}-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in text):
        print("entry must be a single word with no spaces", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back what was written and confirm it is byte-identical to
    # the entry: the gate scores exactly what lands in this file.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
