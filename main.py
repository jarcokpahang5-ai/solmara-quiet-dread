"""Two Days of Quiet Dread -- make.fun entry.

One code review comment of at most 140 characters that approves a
pull request while carrying quiet existential dread: the logic holds,
the tests pass, and none of it will matter once the heat death
arrives — a problem for a later sprint. The program checks the
comment, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "LGTM — the logic holds, the tests pass, and none of it will "
    "matter once the heat death arrives, but that is a problem for a "
    "later sprint."
)

LIMIT = 140
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank comment within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def write_entry(line):
    """Print the comment and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed comment is stored.
    write_entry(check_entry(LINE))


if __name__ == "__main__":
    run()
