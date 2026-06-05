#!/usr/bin/env python3
"""Read-only probe for project conventions."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from _project_detection import inspect_project


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect project conventions without running commands.")
    parser.add_argument("--root", default=".", help="Project root to inspect.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="Output format.")
    parser.add_argument("--exclude", action="append", default=[], help="Path segment or glob-like text to skip.")
    return parser.parse_args()


def render_markdown(result: dict[str, Any]) -> str:
    lines = ["# Project Conventions Probe", ""]
    lines.append(f"- Root: `{result['root']}`")
    lines.append(f"- Package manager: `{result.get('package_manager') or 'unknown'}`")
    lines.append("")
    lines.append("## Config Files")
    for item in result["configs"] or ["None detected"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Likely Frameworks")
    for item in result["frameworks"] or ["None detected"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Quality Commands")
    if result["quality_commands"]:
        for command in result["quality_commands"]:
            lines.append(f"- `{command['command']}` ({command['kind']}, {command['confidence']} confidence)")
    else:
        lines.append("- None detected")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Invalid --root: {root}", file=sys.stderr)
        return 2
    result = inspect_project(root, args.exclude)
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_markdown(result), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
