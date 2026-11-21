#!/usr/bin/env python3
"""Lint GitHub-compatible inline and displayed math in maintained Part I Markdown.

Run: python "Part I - Algebra And Geometry/check_markdown_style.py"
This does not rewrite files. Archived Gemini source files are intentionally exempt.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
FENCE = chr(96)*3
BACKTICK = chr(96)

def lint(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    errors = []
    inside = False
    in_math = False
    count_math = 0
    count_inline = 0
    for i,line in enumerate(lines):
        n = i+1
        if line.lstrip().startswith(FENCE):
            if line != line.lstrip():
                errors.append(f"{path}:{n}: indented code fence")
            if not inside:
                inside = True
                in_math = line == FENCE+"math"
                if in_math:
                    count_math += 1
                    if not (i>=2 and lines[i-1]=="" and lines[i-2]!=""):
                        errors.append(f"{path}:{n}: require exactly one blank line above math")
                    if not (i+4 < len(lines) and lines[i+2]==FENCE
                            and lines[i+3]=="" and lines[i+4]!=""):
                        errors.append(f"{path}:{n}: math must be one line with exactly one blank below")
            else:
                if line != FENCE:
                    errors.append(f"{path}:{n}: unexpected closing fence")
                inside = False
                in_math = False
            continue
        if inside:
            if in_math and ("\\operatorname{" in line or "\\boxed" in line or "$" in line):
                errors.append(f"{path}:{n}: prohibited LaTeX command or delimiter inside math block")
            continue
        j = 0
        while j < len(line):
            if line[j] == BACKTICK:
                k = j
                while k<len(line) and line[k]==BACKTICK:
                    k+=1
                marker = line[j:k]
                end = line.find(marker,k)
                j = end+len(marker) if end!=-1 else k
                continue
            if line[j]=="$" and (j==0 or line[j-1]!="\\"):
                if j+1>=len(line) or line[j+1]!=BACKTICK:
                    errors.append(f"{path}:{n}: use dollar-backtick inline math")
                    j+=1
                    continue
                end=line.find(BACKTICK+"$",j+2)
                if end==-1:
                    errors.append(f"{path}:{n}: unterminated inline math")
                    j+=2
                    continue
                if not line[j+2:end].strip():
                    errors.append(f"{path}:{n}: empty math")
                if "\\operatorname{" in line[j+2:end] or "\\boxed" in line[j+2:end]:
                    errors.append(f"{path}:{n}: prohibited math command")
                count_inline += 1
                j=end+2
                continue
            if line.startswith("\\operatorname{",j) or line.startswith("\\boxed",j) or line.startswith("$$",j):
                errors.append(f"{path}:{n}: prohibited math command or delimiter")
            j+=1
    if inside:
        errors.append(f"{path}: unclosed code fence")
    return errors, count_math, count_inline

def main():
    errors=[]
    counts=[0,0,0]
    for file in sorted(ROOT.rglob("*.md")):
        if "gemini" in file.name.lower():
            continue
        fail,display,inline=lint(file)
        counts[0]+=1
        counts[1]+=display
        counts[2]+=inline
        errors.extend(fail)
    if errors:
        print("\n".join(errors))
        print(f"FAIL: {len(errors)} issue(s)")
        return 1
    print(f"PASS: {counts[0]} files, {counts[2]} inline expressions, {counts[1]} math blocks")
    return 0

if __name__=="__main__":
    sys.exit(main())
