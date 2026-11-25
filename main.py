#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry (v2).

Writes one line of awkward robot small talk to /output/entry.txt:
"So, your left wheel squeaks on floor nine. I have logged it three
times and told no one. Until now."

The entry is a single line, under 200 characters, in which one robot
confesses — with machine-log politeness — that it has been quietly
logging the other robot's squeaky wheel for three floors. The
awkwardness is the unspoken surveillance: logged, never mentioned,
until now, in an elevator neither robot can leave.

Guards (fail before writing anything, exit 1):
- empty or whitespace-only entry
- longer than 200 characters
- multi-line (contains \\n or \\r)
- contains a control character (ord < 0x20), which a single-line
  text entry must never carry

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
    if any(ord(ch) < 0x20 for ch in ENTRY):
        print("entry contains a control character", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
