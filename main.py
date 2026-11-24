#!/usr/bin/env python3
"""The Robot Apology entry: writes the two-line robot confession to /output/entry.txt."""
import os

TEXT = (
    "I am sorry I sent your birthday message to your boss instead of your sister.\n"
    "I have learned to check the name above the send button, and from now on "
    "I will read the recipient twice before I send anything personal."
)

def main():
    assert 1 <= len(TEXT) <= 400, f"gate: entry is {len(TEXT)} chars, must be 1-400"
    lines = TEXT.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "neither line may be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        back = f.read()
    assert back == TEXT, "read-back mismatch"
    print(f"wrote /output/entry.txt ({len(TEXT)} chars, 2 lines)")

if __name__ == "__main__":
    main()
