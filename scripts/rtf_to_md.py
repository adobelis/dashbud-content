"""Convert RTF files to Markdown using striprtf."""
import sys
from pathlib import Path
from striprtf.striprtf import rtf_to_text

def convert(rtf_path: str, md_path: str):
    raw = Path(rtf_path).read_text(encoding="utf-8", errors="replace")
    text = rtf_to_text(raw)
    Path(md_path).write_text(text, encoding="utf-8")
    print(f"Wrote {md_path}")

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
