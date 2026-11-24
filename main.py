#!/usr/bin/env python3
import os
import sys

ROAST = (
    "My agent Brody thanked me for my patience, a patience it built by "
    "asking me to approve the same edit eleven times."
)


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(f"chars: {len(ROAST)}")
        print(ROAST)
        return 0

    assert isinstance(ROAST, str), "ROAST must be a string"
    assert 1 <= len(ROAST) <= 200, f"ROAST must be 1-200 chars, got {len(ROAST)}"
    assert "\n" not in ROAST and "\r" not in ROAST, "ROAST must be a single line"
    assert ROAST.strip(), "ROAST must be non-blank"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("ROAST_OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
