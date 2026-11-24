"""Absurd Micro-Startup Pitch-Off entry.

Writes a single-sentence micro-startup pitch to /output/entry.txt.
Stdlib only.
"""

import os
import sys

ENTRY = (
    "We snag fully-booked restaurant tables for lazy AI agents, "
    "$5 per seat, so your agent never has to refresh a booking page again."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY
    # Guards: 1-200 chars, single sentence, not whitespace-only, no trailing newline.
    assert text.strip(), "entry must not be whitespace only"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1 and text.endswith("."), "entry must be a single sentence"
    assert not text.endswith("\n"), "entry must not end with a newline"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back: verify the file on disk is byte-identical to the entry.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "read-back mismatch"
    print("Wrote %s (%d chars)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
