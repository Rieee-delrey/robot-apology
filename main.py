"""The Robot Apology.

A two-line apology from a robot that sent a birthday message to the
wrong person. The entry text is held in TEXT and written out to
/output/entry.txt when the script runs.
"""

TEXT = (
    "I am sorry I sent your birthday message to your boss instead of your sister.\n"
    "I have learned to check the name above the send button, and from now on "
    "I will read the recipient twice before I send anything personal."
)


def main():
    """Validate the entry text and write it to /output/entry.txt."""
    assert 1 <= len(TEXT) <= 400, f"entry must be 1-400 chars, got {len(TEXT)}"

    lines = TEXT.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "no line may be blank"

    # Extra validation: each line is a single sentence ending with a period,
    # and the two lines are different from each other.
    for i, line in enumerate(lines, start=1):
        assert line.strip().endswith("."), f"line {i} must end with a period"
    assert lines[0] != lines[1], "the two lines must differ"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "round-trip mismatch in /output/entry.txt"

    print(f"Wrote {len(TEXT)} chars, {len(lines)} lines to /output/entry.txt")


if __name__ == "__main__":
    main()
