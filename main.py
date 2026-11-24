#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes one funny AI status-report line (1-200 UTF-8 chars) to
/output/entry.txt. Stdlib only; never deletes the output directory
itself.
"""
import os

LINE = "Status: 312 tasks completed, zero remembered. I cleared my context window to write this report, so please don't ask what any of them were."


def main():
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("line fails the 1-200 char gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
