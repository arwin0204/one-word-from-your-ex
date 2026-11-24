#!/usr/bin/env python3
"""One Word From Your Ex — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe the entrant. The program is fully deterministic: no
randomness, no time, no network, no input. It always writes the same
word, every run.

Why this word
-------------
"forgettable" — the one word an ex would use that stings precisely
because it is not angry. Anger means you mattered. Forgettable means
you did not even leave a mark. It is funny through the sharp turn
(the entrant admits it themselves), painfully honest, instantly
understood with no explanation, and relatable: everyone has feared
being the person nobody remembers.
"""

import os
import sys

# The entry: exactly one word, 11 characters, well inside the 1-24
# character gate. Lowercase, a real English word, no punctuation.
WORD = "forgettable"


def validate(word: str) -> None:
    """Mirror the competition gate locally: 1-24 chars, one word,
    not only whitespace. Fail loudly instead of writing a bad entry."""
    if not (1 <= len(word) <= 24):
        raise ValueError(f"entry must be 1-24 characters, got {len(word)}")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main() -> int:
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
