#!/usr/bin/env python3
"""Read-only probe for project conventions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_EXCLUDES = {".git", "node_modules", "dist", "build", ".next", "coverage", ".venv", "venv"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect project conventions without running commands.")
    parser.add_argument("--root", default=".", help="Project root to inspect.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="Output format.")
    parser.add_argument("--exclude", action="append", default=[], help="Path segment or glob-like text to skip.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def exists(root: Path, name: str) -> bool:
    return (root / name).exists()


def detect_package_manager(root: Path) -> str | None:
    lockfiles = [
        ("pnpm-lock.yaml", "pnpm"),
        ("yarn.lock", "yarn"),
        ("package-lock.json", "npm"),
        ("bun.lockb", "bun"),
        ("uv.lock", "uv"),
        ("poetry.lock", "poetry"),
        ("Pipfile.lock", "pipenv"),
    ]
    for filename, manager in lockfiles:
        if exists(root, filename):
            return manager
    if exists(root, "package.json"):
        return "npm"
    if exists(root, "pyproject.toml"):
        return "python"
    return None


def detect_configs(root: Path) -> list[str]:
    names = [
        "package.json",
        "tsconfig.json",
        "pyproject.toml",
        "requirements.txt",
        "eslint.config.js",
        ".eslintrc",
        ".eslintrc.json",
        ".prettierrc",
        "ruff.toml",
        "pytest.ini",
        "vitest.config.ts",
        "vite.config.ts",
        "next.config.js",
        "jest.config.js",
    ]
    return [name for name in names if exists(root, name)]


def detect_frameworks(root: Path, package_json: dict[str, Any]) -> list[str]:
    deps: dict[str, Any] = {}
    for key in ("dependencies", "devDependencies"):
        value = package_json.get(key)
        if isinstance(value, dict):
            deps.update(value)
    frameworks: list[str] = []
    mapping = {
        "react": "React",
        "next": "Next.js",
        "vue": "Vue",
        "svelte": "Svelte",
        "express": "Express",
        "nestjs": "NestJS",
        "vite": "Vite",
        "vitest": "Vitest",
        "jest": "Jest",
        "typescript": "TypeScript",
    }
    for package, label in mapping.items():
        if package in deps or package.startswith("@") and package in deps:
            frameworks.append(label)
    if exists(root, "pyproject.toml"):
        text = (root / "pyproject.toml").read_text(encoding="utf-8", errors="ignore").lower()
        for needle, label in (("django", "Django"), ("fastapi", "FastAPI"), ("pytest", "pytest"), ("ruff", "Ruff")):
            if needle in text:
                frameworks.append(label)
    return sorted(set(frameworks))


def quality_commands(root: Path, package_manager: str | None, package_json: dict[str, Any]) -> list[dict[str, str]]:
    commands: list[dict[str, str]] = []
    scripts = package_json.get("scripts") if isinstance(package_json.get("scripts"), dict) else {}
    for name in ("lint", "typecheck", "test", "build"):
        if name in scripts:
            runner = package_manager if package_manager in {"npm", "pnpm", "yarn", "bun"} else "npm"
            prefix = "run " if runner in {"npm", "pnpm", "bun"} else ""
            commands.append({"kind": name, "command": f"{runner} {prefix}{name}", "confidence": "high"})
    if exists(root, "pyproject.toml") or exists(root, "pytest.ini"):
        commands.append({"kind": "test", "command": "python -m pytest", "confidence": "medium"})
    if exists(root, "ruff.toml") or exists(root, "pyproject.toml"):
        commands.append({"kind": "lint", "command": "python -m ruff check .", "confidence": "medium"})
    return commands


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
        raise SystemExit(f"Invalid --root: {root}")
    package_json = load_json(root / "package.json") if exists(root, "package.json") else {}
    manager = detect_package_manager(root)
    result = {
        "root": str(root),
        "package_manager": manager,
        "configs": detect_configs(root),
        "frameworks": detect_frameworks(root, package_json),
        "quality_commands": quality_commands(root, manager, package_json),
    }
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_markdown(result), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
