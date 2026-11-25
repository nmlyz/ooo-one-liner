#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a one-line out-of-office reply.

The line was picked from 36 candidates by pairwise judging against the
brief — a real away message whose joke is the message itself: the chair
has been promoted to the sender's position. The program checks the result
against the entry gate (1-160 characters, single line, no leading or
trailing space) before writing it, then reads the file back to confirm
the bytes match.
"""

import os
import sys

LINE = "Out of office. My chair has been promoted to my position."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 160):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-160")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
