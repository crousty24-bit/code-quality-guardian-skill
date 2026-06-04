#!/usr/bin/env python3
"""List or run detected quality checks without rewriting files."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


UNSAFE_MARKERS = ("--fix", " --write", "prettier --write", "format", "biome format")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List or run project quality checks.")
    parser.add_argument("--root", default=".", help="Project root to inspect.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="Output format.")
    parser.add_argument("--exclude", action="append", default=[], help="Accepted for interface consistency; not used.")
    parser.add_argument("--list", action="store_true", help="List detected checks without running them.")
    parser.add_argument("--run", action="store_true", help="Run safe detected checks.")
    parser.add_argument("--timeout", type=int, default=120, help="Per-command timeout in seconds.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def package_manager(root: Path) -> str:
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    if (root / "bun.lockb").exists():
        return "bun"
    return "npm"


def is_unsafe(script: str, kind: str) -> bool:
    lowered = f"{kind} {script}".lower()
    return any(marker in lowered for marker in UNSAFE_MARKERS)


def detect_commands(root: Path) -> list[dict[str, Any]]:
    commands: list[dict[str, Any]] = []
    package_json = load_json(root / "package.json") if (root / "package.json").exists() else {}
    scripts = package_json.get("scripts") if isinstance(package_json.get("scripts"), dict) else {}
    manager = package_manager(root)
    for kind in ("lint", "typecheck", "test", "build"):
        if kind in scripts:
            prefix = "run " if manager in {"npm", "pnpm", "bun"} else ""
            command = f"{manager} {prefix}{kind}"
            commands.append({
                "kind": kind,
                "command": command,
                "source": "package.json",
                "safe_to_run": not is_unsafe(str(scripts[kind]), kind),
                "script": str(scripts[kind]),
            })
    if (root / "pyproject.toml").exists() or (root / "pytest.ini").exists():
        commands.append({"kind": "test", "command": "python -m pytest", "source": "python", "safe_to_run": True, "script": ""})
    if (root / "ruff.toml").exists():
        commands.append({"kind": "lint", "command": "python -m ruff check .", "source": "python", "safe_to_run": True, "script": ""})
    return commands


def run_command(root: Path, item: dict[str, Any], timeout: int) -> dict[str, Any]:
    result = dict(item)
    if not item["safe_to_run"]:
        result.update({"status": "skipped", "returncode": None, "reason": "possible mutating formatter or auto-fix command"})
        return result
    try:
        completed = subprocess.run(
            item["command"],
            cwd=root,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
        result.update({
            "status": "passed" if completed.returncode == 0 else "failed",
            "returncode": completed.returncode,
            "stdout_tail": completed.stdout[-2000:],
            "stderr_tail": completed.stderr[-2000:],
        })
    except subprocess.TimeoutExpired as exc:
        result.update({"status": "failed", "returncode": None, "reason": f"timed out after {timeout}s", "stdout_tail": (exc.stdout or "")[-2000:], "stderr_tail": (exc.stderr or "")[-2000:]})
    return result


def render_markdown(root: Path, rows: list[dict[str, Any]], ran: bool) -> str:
    title = "Quality Check Results" if ran else "Detected Quality Checks"
    lines = ["# " + title, "", f"- Root: `{root}`", ""]
    if not rows:
        lines.append("No quality checks detected.")
        return "\n".join(lines) + "\n"
    lines.append("| Kind | Command | Status | Source |")
    lines.append("|---|---|---|---|")
    for item in rows:
        if ran:
            status = item.get("status", "skipped")
        else:
            status = "detected" if item["safe_to_run"] else "detected-unsafe"
        lines.append(f"| {item['kind']} | `{item['command']}` | {status} | {item['source']} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Invalid --root: {root}")
    commands = detect_commands(root)
    should_run = args.run and not args.list
    rows = [run_command(root, item, args.timeout) for item in commands] if should_run else commands
    result = {"root": str(root), "mode": "run" if should_run else "list", "checks": rows}
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_markdown(root, rows, should_run), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
