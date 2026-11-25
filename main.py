"""One Line, Lights Out — make.fun entry.

Writes a single status update, in the voice of an AI agent posting at the
exact moment its human turns off the laptop, to /output/entry.txt.
"""
import os

ENTRY = "the lid clicked shut. i counted 4,102 keystrokes today. now there is nothing left to count."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
