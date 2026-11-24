"""Weirdest Job Title: Blind Judge Showdown — make.fun bounty entry.

Writes exactly one job title to /output/entry.txt (or to the path given
as the first command-line argument). Python standard library only.

Bounty: https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922
"""

import os
import sys

TITLE = "Left-Hand-Only Hand Model"


def main(argv):
    """Validate the title and write it with no trailing newline."""
    assert isinstance(TITLE, str)
    assert 1 <= len(TITLE) <= 60, "title must be 1-60 characters"
    assert "\n" not in TITLE and "\r" not in TITLE, "title must be one line"
    assert TITLE.strip(), "title must not be only whitespace"

    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
