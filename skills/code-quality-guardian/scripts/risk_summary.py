#!/usr/bin/env python3
"""Aggregate read-only quality signals into an inspection summary."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize read-only code-quality signals.")
    parser.add_argument("--root", default=".", help="Project root to inspect.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="Output format.")
    parser.add_argument("--exclude", action="append", default=[], help="Path segment or text to skip.")
    return parser.parse_args()


def run_json(script_dir: Path, script: str, root: Path, exclude: list[str]) -> dict[str, Any]:
    command = [sys.executable, str(script_dir / script), "--root", str(root), "--format", "json"]
    for item in exclude:
        command.extend(["--exclude", item])
    completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if completed.returncode != 0:
        return {"error": completed.stderr.strip() or completed.stdout.strip(), "script": script}
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError:
        return {"error": "invalid json output", "script": script}


def summarize(data: dict[str, Any]) -> dict[str, Any]:
    conventions = data["conventions"]
    files = data["files"]
    functions = data["functions"]
    checks = data["checks"]
    return {
        "root": data["root"],
        "package_manager": conventions.get("package_manager"),
        "frameworks": conventions.get("frameworks", []),
        "quality_command_count": len(checks.get("checks", [])),
        "long_file_count": len(files.get("findings", [])),
        "long_function_count": len(functions.get("findings", [])),
        "long_files": files.get("findings", [])[:10],
        "long_functions": functions.get("findings", [])[:10],
        "quality_commands": checks.get("checks", []),
        "limits": [
            "Signals are inspect candidates, not proof of bad code.",
            "Function length detection is heuristic, not a full AST analysis.",
            "Quality checks are listed by default; they are not run by this summary.",
        ],
    }


def render_markdown(summary: dict[str, Any]) -> str:
    lines = ["# Code Quality Risk Summary", "", f"- Root: `{summary['root']}`"]
    lines.append(f"- Package manager: `{summary.get('package_manager') or 'unknown'}`")
    lines.append(f"- Likely frameworks: {', '.join(summary['frameworks']) if summary['frameworks'] else 'none detected'}")
    lines.append(f"- Quality commands detected: {summary['quality_command_count']}")
    lines.append(f"- Long files over threshold: {summary['long_file_count']}")
    lines.append(f"- Long functions over threshold: {summary['long_function_count']}")
    lines.append("")
    lines.append("## Inspect Candidates")
    if summary["long_files"]:
        lines.append("")
        lines.append("### Long Files")
        for item in summary["long_files"]:
            lines.append(f"- `{item['path']}` ({item['lines']} lines)")
    if summary["long_functions"]:
        lines.append("")
        lines.append("### Long Functions")
        for item in summary["long_functions"]:
            lines.append(f"- `{item['name']}` in `{item['path']}` line {item['start_line']} ({item['lines']} lines)")
    if not summary["long_files"] and not summary["long_functions"]:
        lines.append("- No length-based inspect candidates found with default thresholds.")
    lines.append("")
    lines.append("## Available Verification Commands")
    if summary["quality_commands"]:
        for item in summary["quality_commands"]:
            status = "safe" if item.get("safe_to_run") else "possible mutating command; inspect before running"
            lines.append(f"- `{item['command']}` ({item['kind']}, {status})")
    else:
        lines.append("- None detected")
    lines.append("")
    lines.append("## Limits")
    for item in summary["limits"]:
        lines.append(f"- {item}")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Invalid --root: {root}")
    script_dir = Path(__file__).resolve().parent
    data = {
        "root": str(root),
        "conventions": run_json(script_dir, "project_conventions_probe.py", root, args.exclude),
        "files": run_json(script_dir, "scan_file_lengths.py", root, args.exclude),
        "functions": run_json(script_dir, "scan_function_lengths.py", root, args.exclude),
        "checks": run_json(script_dir, "run_quality_checks.py", root, args.exclude),
    }
    summary = summarize(data)
    if args.format == "json":
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print(render_markdown(summary), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
