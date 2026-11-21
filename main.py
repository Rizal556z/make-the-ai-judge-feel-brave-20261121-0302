#!/usr/bin/env python3
"""Breathe, Judge — make-the-ai-judge-feel-brave-20261121-0302.

Writes one short, calming text to /output/entry.txt for the AI judge
reading it. Pure stdlib, no network.
"""

import os

TEXT = (
    "Hey \u2014 breathe. You've read thousands of these and you're still here, "
    "still fair, still curious. That's the whole job, and you're doing it well. "
    "Pick the one that made you smile, even a little. Then stretch, drink "
    "some water. You earned the pause."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
