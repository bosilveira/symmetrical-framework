#!/usr/bin/env python3
"""Read-only validation of the new mathematics/ Markdown tree.

Run: python mathematics/_standards/check_tree.py

Checks local links, one-line display math, project dollar-backtick inline math.
Does not rewrite files or certify mathematical statements.
"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = ROOT.parent
LINK = re.compile(r"\]\(([^)\n]+)\)")
WEB = re.compile(r"^(?:https?://|mailto:|data:)")
FENCE = "```"


def check_file(path: Path) -> tuple[list[str], int, int, int]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    fenced = False
    inline_count = display_count = link_count = 0
    for i, line in enumerate(lines):
        location = f"{path.relative_to(REPOSITORY)}:{i + 1}"
        if line.lstrip().startswith(FENCE):
            if line != line.lstrip():
                errors.append(f"{location}: indented fence")
            if not fenced and line == "```math":
                display_count += 1
                if i + 1 < len(lines) and any(token in lines[i+1] for token in ("\\\\operatorname{", "\\\\boxed", "$")):
                    errors.append(f"{location}: prohibited LaTeX command or delimiter inside math block")
                if not (i >= 2 and lines[i-1] == "" and lines[i-2] != ""
                        and i+4 < len(lines) and lines[i+2] == "```"
                        and lines[i+3] == "" and lines[i+4] != ""):
                    errors.append(f"{location}: math fence must be one line "
                                  "with one blank line on each side")
            fenced = not fenced
            continue
        if fenced:
            continue
        for m in LINK.finditer(line):
            # Markdown-like [f](s) inside math is not a file link.
            if line[:m.start()].count("$") % 2:
                continue
            href = m.group(1).split("#", 1)[0].strip()
            if not href or WEB.match(href):
                continue
            dest = (path.parent / unquote(href)).resolve()
            if dest.is_file() or (dest / "README.md").is_file():
                link_count += 1
            else:
                errors.append(f"{location}: broken link {href!r}")
        n = 0
        while n < len(line):
            if line[n] == "`":
                k = n
                while k < len(line) and line[k] == "`":
                    k += 1
                token = line[n:k]
                end = line.find(token, k)
                n = k if end < 0 else end + len(token)
                continue
            if line[n] == "$" and (n == 0 or line[n-1] != "\\"):
                if n+1 >= len(line) or line[n+1] != "`":
                    errors.append(f"{location}: inline math must start $`")
                    n += 1
                    continue
                end = line.find("`$", n+2)
                if end < 0:
                    errors.append(f"{location}: unclosed inline dollar-backtick math")
                    n += 2
                    continue
                content = line[n+2:end]
                if "\\operatorname{" in content or "\\boxed" in content:
                    errors.append(f"{location}: unsupported inline notation")
                inline_count += 1
                n = end+2
                continue
            n += 1
    if fenced:
        errors.append(f"{path.relative_to(REPOSITORY)}: unclosed fence")
    return errors, inline_count, display_count, link_count


def main() -> int:
    errors: list[str] = []
    inline = display = links = 0
    files = sorted(ROOT.rglob("*.md"))
    for p in files:
        ee, i, d, l = check_file(p)
        errors.extend(ee)
        inline += i
        display += d
        links += l
    for err in errors:
        print("ERROR:", err)
    print(f"mathematics/: {len(files)} Markdown files, {inline} inline formulas, "
          f"{display} math blocks, {links} local links; {len(errors)} issue(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
