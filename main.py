#!/usr/bin/env python3
"""One-line out-of-office reply writer.

Writes a single out-of-office reply line to entry.txt in the output
directory. The reply is a fixed line held in a constant below; before
writing, the program checks it against the competition's own rules
(one line, 1-160 characters, no surrounding whitespace) and, after
writing, reads the file back and compares it byte for byte.

Standard library only. Usage:

    python3 main.py

The output directory defaults to /output and can be overridden with
the MAKEFUN_OUTPUT_DIR environment variable.
"""

import os
import sys

# The reply line. One sentence, 57 characters.
REPLY = "Out of office. My chair has been promoted to my position."

MAX_CHARS = 160


def check_reply(line):
    """Return a list of rule violations for *line* (empty means OK)."""
    problems = []
    if not line:
        problems.append("reply is empty")
    if len(line) > MAX_CHARS:
        problems.append("reply is longer than %d characters" % MAX_CHARS)
    if len(line) < 1:
        problems.append("reply is shorter than 1 character")
    if "\n" in line or "\r" in line:
        problems.append("reply must be a single line")
    if any(ord(ch) < 32 for ch in line):
        problems.append("reply contains a control character")
    if line != line.strip():
        problems.append("reply has leading or trailing whitespace")
    return problems


def main():
    problems = check_reply(REPLY)
    if problems:
        for problem in problems:
            print("error: %s" % problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    payload = (REPLY + "\n").encode("utf-8")
    with open(out_path, "wb") as handle:
        handle.write(payload)

    # Read the file back and verify it matches exactly what we wrote.
    with open(out_path, "rb") as handle:
        written = handle.read()
    if written != payload:
        print("error: read-back mismatch in %s" % out_path, file=sys.stderr)
        return 1

    print("wrote %d bytes to %s" % (len(payload), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
