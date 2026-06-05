#!/usr/bin/env python3
"""Detect project quality checks without executing them."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from _project_detection import inspect_project


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect project quality checks without running them.")
    parser.add_argument("--root", default=".", help="Project root to inspect.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="Output format.")
    parser.add_argument("--exclude", action="append", default=[], help="Path segment or text to skip.")
    parser.add_argument("--list", action="store_true", help="Deprecated no-op; detection is always read-only.")
    return parser.parse_args()


def render_markdown(root: Path, rows: list[dict[str, Any]]) -> str:
    lines = ["# Detected Quality Checks", "", f"- Root: `{root}`", ""]
    if not rows:
        lines.append("No quality checks detected.")
        return "\n".join(lines) + "\n"
    lines.append("| Kind | Command | Status | Source | Confidence |")
    lines.append("|---|---|---|---|---|")
    for item in rows:
        lines.append(
            f"| {item['kind']} | `{item['command']}` | detected | "
            f"{item['source']} | {item['confidence']} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Invalid --root: {root}", file=sys.stderr)
        return 2
    rows = [
        {**item, "status": "detected"}
        for item in inspect_project(root, args.exclude)["quality_commands"]
    ]
    result = {"root": str(root), "mode": "detect", "checks": rows}
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_markdown(root, rows), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
