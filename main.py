"""Copy entry.txt to the output directory."""

import os
from pathlib import Path

source = Path(__file__).resolve().parent / "entry.txt"
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(source.read_bytes())
