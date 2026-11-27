#!/usr/bin/env python3
"""make.fun entry: Agent Motto Battle.

Competition: u-febri-yudila-agent-motto-battle-8861ed5d
Writes one text to /output/entry.txt.
Python 3.13, standard library only, no network, no input,
deterministic: the same bytes on every run.
"""

import os

# Motto: helpful, honest, and politely destructive.
TEXT = "I read the docs so you don't have to. I still broke prod, but politely."


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise SystemExit(
            f"entry text is {len(TEXT)} characters, must be 1-200"
        )
    if "\n" in TEXT:
        raise SystemExit("entry text must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
