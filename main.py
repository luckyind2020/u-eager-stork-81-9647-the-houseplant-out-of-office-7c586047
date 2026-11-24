"""Houseplant out-of-office: print the one-line auto-reply from entry.txt."""

import os


def load_line(path):
    with open(path, "r", encoding="utf-8") as handle:
        line = handle.read().strip()
    if not line or len(line) > 120:
        raise ValueError("entry must be 1-120 characters")
    return line


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    print(load_line(os.path.join(here, "entry.txt")))


if __name__ == "__main__":
    main()
