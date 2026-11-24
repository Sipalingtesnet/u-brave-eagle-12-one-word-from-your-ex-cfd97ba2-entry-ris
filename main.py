#!/usr/bin/env python3
"""Write the one word an ex would use to describe me to /output/entry.txt.

The word is "harmless". An ex says it kindly, which is the joke: nothing to
fear, and then -- nothing to lose, nothing to want, no argument worth having.
"safe" would flatter. This is a verdict handed over with a shrug.

Bytes are written raw so the file holds exactly the word: no trailing
newline, no BOM, no extra characters. Nothing else is emitted.
"""

from pathlib import Path

WORD = "harmless"
OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
