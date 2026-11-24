"""Make the Judge Smile — entry program.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt. Deterministic: the same bytes on
every run, stdlib only, no network.
"""

import os

# One line, crafted for the judge's brief, in order:
#  1. a small good thing that happened today
#  2. warmth — a small kindness, genuinely felt
#  3. surprise — it turns where you did not expect (she predicts the rain)
#  4. concreteness — a time (6:40), a thing (fried banana), a whisper
#  5. fresh wording — no greeting-card phrasing
ENTRY = (
    "This morning at 6:40, the warung lady slipped an extra fried banana "
    "into my bag and whispered, \"for the road — the rain is coming,\" "
    "and by 6:50, right on cue, it did."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
