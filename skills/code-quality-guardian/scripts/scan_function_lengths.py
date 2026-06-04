#!/usr/bin/env python3
"""Read-only heuristic scan for long functions."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_EXCLUDES = {".git", "node_modules", "dist", "build", ".next", "coverage", ".venv", "venv"}
CODE_EXTENSIONS = {".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}
PY_DEF = re.compile(r"^(\s*)(async\s+def|def)\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(")
JS_DEF = re.compile(
    r"^\s*(?:export\s+)?(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(|"
    r"^\s*(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>|"
    r"^\s*(?:async\s+)?([A-Za-z_$][\w$]*)\s*\([^)]*\)\s*\{"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Find long functions with simple read-only heuristics.")
    parser.add_argument("--root", default=".", help="Project root to inspect.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="Output format.")
    parser.add_argument("--exclude", action="append", default=[], help="Path segment or text to skip.")
    parser.add_argument("--max-lines", type=int, default=80, help="Function length threshold.")
    return parser.parse_args()


def should_skip(path: Path, root: Path, extra: list[str]) -> bool:
    rel = path.relative_to(root)
    parts = set(rel.parts)
    if parts & DEFAULT_EXCLUDES:
        return True
    text = str(rel)
    return any(pattern and pattern in text for pattern in extra)


def scan_python(path: Path, root: Path, max_lines: int) -> list[dict[str, Any]]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    findings: list[dict[str, Any]] = []
    for index, line in enumerate(lines):
        match = PY_DEF.match(line)
        if not match:
            continue
        indent = len(match.group(1))
        end = index + 1
        for cursor in range(index + 1, len(lines)):
            current = lines[cursor]
            if current.strip() and len(current) - len(current.lstrip()) <= indent:
                break
            end = cursor + 1
        length = end - index
        if length > max_lines:
            findings.append({
                "path": str(path.relative_to(root)),
                "name": match.group(3),
                "start_line": index + 1,
                "lines": length,
                "threshold": max_lines,
                "confidence": "medium",
            })
    return findings


def scan_js_like(path: Path, root: Path, max_lines: int) -> list[dict[str, Any]]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    findings: list[dict[str, Any]] = []
    for index, line in enumerate(lines):
        match = JS_DEF.match(line)
        if not match:
            continue
        name = next(group for group in match.groups() if group)
        brace_depth = 0
        seen_open = False
        end = index + 1
        for cursor in range(index, len(lines)):
            current = re.sub(r"(['\"]).*?\1", "", lines[cursor])
            brace_depth += current.count("{")
            if current.count("{"):
                seen_open = True
            brace_depth -= current.count("}")
            end = cursor + 1
            if seen_open and brace_depth <= 0:
                break
        length = end - index
        if length > max_lines:
            findings.append({
                "path": str(path.relative_to(root)),
                "name": name,
                "start_line": index + 1,
                "lines": length,
                "threshold": max_lines,
                "confidence": "low",
            })
    return findings


def scan(root: Path, max_lines: int, exclude: list[str]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in CODE_EXTENSIONS or should_skip(path, root, exclude):
            continue
        if path.suffix.lower() == ".py":
            findings.extend(scan_python(path, root, max_lines))
        else:
            findings.extend(scan_js_like(path, root, max_lines))
    return sorted(findings, key=lambda item: item["lines"], reverse=True)


def render_markdown(root: Path, findings: list[dict[str, Any]], max_lines: int) -> str:
    lines = [
        "# Long Function Scan",
        "",
        f"- Root: `{root}`",
        f"- Threshold: `{max_lines}` lines",
        "- Note: this is a heuristic signal, not a full AST analysis.",
        "",
    ]
    if not findings:
        lines.append("No functions exceeded the threshold.")
        return "\n".join(lines) + "\n"
    lines.append("| Function | File | Start | Lines | Confidence |")
    lines.append("|---|---|---:|---:|---|")
    for item in findings:
        lines.append(f"| `{item['name']}` | `{item['path']}` | {item['start_line']} | {item['lines']} | {item['confidence']} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Invalid --root: {root}")
    findings = scan(root, args.max_lines, args.exclude)
    result = {"root": str(root), "threshold": args.max_lines, "note": "heuristic signal, not full AST analysis", "findings": findings}
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_markdown(root, findings, args.max_lines), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
