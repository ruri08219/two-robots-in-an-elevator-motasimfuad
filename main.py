#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
Standard library only.
"""

import os
import sys

ENTRY = "So, your left wheel squeaks on floor nine. I have logged it three times and told no one. Until now."


def main():
    if not ENTRY or not ENTRY.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(ENTRY) > 200:
        print("entry exceeds 200 characters", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
