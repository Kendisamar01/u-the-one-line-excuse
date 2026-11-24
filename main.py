import os
from pathlib import Path

source = Path(__file__).resolve().parent / "entry.txt"
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(source.read_text(encoding="utf-8").strip(), encoding="utf-8")
