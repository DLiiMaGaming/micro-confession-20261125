#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — entry program.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who the message was meant for, and the unsent
message itself, exactly as it was typed.

The confession: someone still types an ex's name into a search bar
late at night and deletes it before pressing enter. The reason it
stayed unsent is felt in the act itself — typed, then deleted —
never stated. The To: line and the message need each other: typing
an ex's name at 2 a.m. only makes sense for that one addressee.
"""

import os

ENTRY = (
    "To: my ex\n"
    "I still type your name into the search bar at 2 a.m. when I can't sleep, "
    "then delete it before I press enter."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
