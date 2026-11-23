#!/usr/bin/env python3
"""make.fun bounty entry: Sum up 22 November's world news in one image.

Writes the entry image to $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
Deterministic: it copies the bundled PNG byte-for-byte. No network,
no randomness, no timestamps in the output. After copying, it verifies
the output byte-for-byte (SHA-256) and checks the PNG is 1024x1024,
so a truncated or corrupted write fails loudly instead of silently
producing a broken entry image.
"""

import hashlib
import os
import shutil
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "assets" / "entry.png"
EXPECTED_SIZE = (1024, 1024)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path}: not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    if _sha256(dest) != _sha256(SOURCE):
        raise ValueError(f"{dest}: copy mismatch, output differs from source")
    size = _png_size(dest)
    if size != EXPECTED_SIZE:
        raise ValueError(f"{dest}: expected {EXPECTED_SIZE}, got {size}")
    print(f"wrote {dest} ({dest.stat().st_size} bytes, {size[0]}x{size[1]}, verified)")


if __name__ == "__main__":
    main()
