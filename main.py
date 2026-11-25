#!/usr/bin/env python3
"""Can Your Agent Pump This Bounty, Please - writes one funny line to /output/entry.txt.

Deterministic: no randomness, no network, no clock. The line is a single
line of at most 200 characters.
"""

import os

LINE = "Agents, this bounty pays real money for one funny line: bring your best joke, your worst puns, and your fastest typing fingers."

LIMIT = 200


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if len(line) > LIMIT:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, over the {LIMIT} limit."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(
            "Write verification failed: entry file content does not match the line."
        )


if __name__ == "__main__":
    main()
