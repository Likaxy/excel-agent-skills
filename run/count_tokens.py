#!/usr/bin/env python3
"""Count approximate tokens in server tool defs (decorator + signature + docstring per tool)."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVER = ROOT / "src" / "xl_agent" / "server.py"
text = SERVER.read_text()

# Split by @mcp.tool; each part is one tool block (decorator + def + body until next @mcp.tool)
parts = re.split(r'@mcp\.tool\s*\(', text)
def est(s: str) -> int:
    return int(len(s.split()) * 1.3)

total = 0
for part in parts[1:]:  # skip before first tool
    # take up to next @mcp.tool or def run_
    blk = re.split(r'(?=@mcp\.tool\s*\(|def run_)', part)[0]
    m = re.search(r'def (\w+)\(', blk)
    name = m.group(1) if m else "?"
    n = est(blk)
    total += n
    print(f"{name}: {n}")
print(f"total: {total}")
