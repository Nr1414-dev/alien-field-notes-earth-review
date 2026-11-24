#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — entry program.

Writes one original line (a review of planet Earth, left by an alien
tourist after a two-day visit) to /output/entry.txt as plain UTF-8 text.
The line is at most 200 characters, as the bounty requires.
"""
import os

LINE = "Pros: breathable air, friendly locals. Cons: the air is 78% filler gas and nobody warned me. Still, I inhaled."

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not LINE.strip():
        raise ValueError("entry line must not be blank")
    if len(LINE) > 200:
        raise ValueError("entry line must be at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
