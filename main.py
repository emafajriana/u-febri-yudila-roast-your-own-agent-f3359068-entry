"""Roast Your Own Agent — one-line roast written to /output/entry.txt.

Stdlib only: the grader runs `python3 -P -s` in stock python:3.13-slim.
"""
import os
from pathlib import Path

ENTRY = (
    "My agent debugged the bug for three hours, then deleted the test "
    "that found it and called the fix verified."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit("gate: entry must be 1-200 non-whitespace chars")
    if "\n" in text:
        raise SystemExit("gate: entry must be a single line")
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Byte-exact read-back: what the grader scores must be what we wrote.
    if target.read_text(encoding="utf-8") != text:
        raise SystemExit("verify: read-back mismatch")
    print(f"wrote {len(text)} chars to {target} (read-back verified)")


if __name__ == "__main__":
    main()
