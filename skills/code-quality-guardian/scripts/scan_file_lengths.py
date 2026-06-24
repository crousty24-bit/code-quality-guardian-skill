#!/usr/bin/env python3
"""Read-only scan for long files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from _project_detection import is_excluded
from _rendering import inline_code, table_cell, untrusted_note


LOCKFILES = {"package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb", "poetry.lock", "uv.lock"}
TEXT_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".json", ".md", ".css", ".scss",
    ".html", ".yml", ".yaml", ".toml", ".txt", ".sh", ".rb", ".rake", ".erb", ".rs",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Find long files without modifying anything.")
    parser.add_argument("--root", default=".", help="Project root to inspect.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="Output format.")
    parser.add_argument("--exclude", action="append", default=[], help="Path segment or text to skip.")
    parser.add_argument("--max-lines", type=int, default=400, help="Line threshold.")
    return parser.parse_args()


def should_skip(path: Path, root: Path, extra: list[str]) -> bool:
    if path.name in LOCKFILES:
        return True
    return is_excluded(path, root, extra)


def count_lines(path: Path) -> int:
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        return sum(1 for _ in handle)


def scan(root: Path, max_lines: int, exclude: list[str]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in root.rglob("*"):
        if not path.is_file() or should_skip(path, root, exclude):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        lines = count_lines(path)
        if lines > max_lines:
            findings.append({"path": str(path.relative_to(root)), "lines": lines, "threshold": max_lines})
    return sorted(findings, key=lambda item: item["lines"], reverse=True)


def render_markdown(root: Path, findings: list[dict[str, Any]], max_lines: int) -> str:
    lines = [
        "# Long File Scan",
        "",
        f"- Root: {inline_code(root)}",
        f"- Threshold: {inline_code(max_lines)} lines",
        f"- {untrusted_note()}",
        "",
    ]
    if not findings:
        lines.append("No files exceeded the threshold.")
        return "\n".join(lines) + "\n"
    lines.append("| File | Lines | Threshold |")
    lines.append("|---|---:|---:|")
    for item in findings:
        lines.append(
            f"| {inline_code(item['path'])} | "
            f"{table_cell(item['lines'])} | {table_cell(item['threshold'])} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Invalid --root: {root}", file=sys.stderr)
        return 2
    findings = scan(root, args.max_lines, args.exclude)
    result = {"root": str(root), "threshold": args.max_lines, "findings": findings}
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_markdown(root, findings, args.max_lines), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
