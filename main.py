#!/usr/bin/env python3
"""Invent a Word We Need — one fresh coinage, defined in a single line.

The entry is a single invented English word plus its definition, in one
line of at most 140 characters. The program writes that line to
``entry.txt`` inside the output directory and also prints it.

Word: wavenapped — the wave you gave away to a stranger who was waving
at the person standing behind you.
"""

import os

WORD = "wavenapped"

DEFINITION = (
    "At the school gate, you wave back warmly at a stranger, "
    "then watch them hug the person behind you."
)


def build_entry() -> str:
    """Join the coined word and its one-line definition."""
    return "{}: {}".format(WORD, DEFINITION)


def main() -> None:
    entry = build_entry()
    if not 1 <= len(entry) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(entry))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
