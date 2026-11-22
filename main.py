#!/usr/bin/env python3
"""make.fun bounty entry: Sum up 22 November's world news in one image.

Writes the entry image to $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
Deterministic: it copies the bundled PNG byte-for-byte. No network,
no randomness, no timestamps in the output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "assets" / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
