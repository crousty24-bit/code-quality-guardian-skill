"""Shared read-only project detection for Code Quality Guardian scripts."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


DEFAULT_EXCLUDES = {
    ".agents",
    ".codex",
    ".git",
    ".next",
    ".venv",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
    "venv",
}


def is_excluded(path: Path, root: Path, extra: list[str]) -> bool:
    relative = path.relative_to(root)
    if set(relative.parts) & DEFAULT_EXCLUDES:
        return True
    text = relative.as_posix()
    return any(pattern and pattern in text for pattern in extra)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def existing(root: Path, candidates: list[str], exclude: list[str]) -> list[Path]:
    paths: list[Path] = []
    for relative in candidates:
        path = root / relative
        if path.exists() and not is_excluded(path, root, exclude):
            paths.append(path)
    return paths


def package_manager(root: Path, exclude: list[str]) -> str | None:
    candidates = [
        ("pnpm-lock.yaml", "pnpm"),
        ("yarn.lock", "yarn"),
        ("package-lock.json", "npm"),
        ("bun.lockb", "bun"),
        ("Gemfile.lock", "bundler"),
        ("Gemfile", "bundler"),
        ("Cargo.lock", "cargo"),
        ("Cargo.toml", "cargo"),
        ("src-tauri/Cargo.toml", "cargo"),
        ("uv.lock", "uv"),
        ("poetry.lock", "poetry"),
        ("Pipfile.lock", "pipenv"),
        ("package.json", "npm"),
        ("pyproject.toml", "python"),
    ]
    for relative, manager in candidates:
        path = root / relative
        if path.exists() and not is_excluded(path, root, exclude):
            return manager
    return None


def config_files(root: Path, exclude: list[str]) -> list[str]:
    candidates = [
        "package.json",
        "tsconfig.json",
        "pyproject.toml",
        "requirements.txt",
        "eslint.config.js",
        ".eslintrc",
        ".eslintrc.json",
        ".prettierrc",
        "ruff.toml",
        ".ruff.toml",
        "pytest.ini",
        "vitest.config.ts",
        "vite.config.ts",
        "next.config.js",
        "jest.config.js",
        "Gemfile",
        "Gemfile.lock",
        ".rubocop.yml",
        "config/application.rb",
        "spec/rails_helper.rb",
        "Cargo.toml",
        "Cargo.lock",
        "src-tauri/Cargo.toml",
        "src-tauri/Cargo.lock",
    ]
    return [
        path.relative_to(root).as_posix()
        for path in existing(root, candidates, exclude)
    ]


def _dependency_text(root: Path, exclude: list[str]) -> str:
    paths = [
        root / "pyproject.toml",
        root / "requirements.txt",
        root / "requirements-dev.txt",
        root / "Pipfile",
    ]
    return "\n".join(
        read_text(path)
        for path in paths
        if path.exists() and not is_excluded(path, root, exclude)
    ).lower()


def _has_python_tool(root: Path, tool: str, exclude: list[str]) -> bool:
    pyproject_path = root / "pyproject.toml"
    pyproject = (
        read_text(pyproject_path).lower()
        if pyproject_path.exists() and not is_excluded(pyproject_path, root, exclude)
        else ""
    )
    dependencies = _dependency_text(root, exclude)
    if tool == "pytest":
        return (
            bool(existing(root, ["pytest.ini", "conftest.py"], exclude))
            or "[tool.pytest" in pyproject
            or re.search(r"(^|[\s\"'=<>])pytest([\s\"',<=>]|$)", dependencies) is not None
        )
    if tool == "ruff":
        return (
            bool(existing(root, ["ruff.toml", ".ruff.toml"], exclude))
            or "[tool.ruff" in pyproject
            or re.search(r"(^|[\s\"'=<>])ruff([\s\"',<=>]|$)", dependencies) is not None
        )
    return False


def _ruby_evidence(root: Path, exclude: list[str]) -> dict[str, bool]:
    gemfile_path = root / "Gemfile"
    gemfile_exists = gemfile_path.exists() and not is_excluded(gemfile_path, root, exclude)
    gemfile = read_text(gemfile_path).lower() if gemfile_exists else ""
    rails_files = existing(root, ["bin/rails", "config/application.rb"], exclude)
    rspec_files = existing(root, ["spec/rails_helper.rb", "spec/spec_helper.rb"], exclude)
    rubocop_files = existing(root, [".rubocop.yml", "bin/rubocop"], exclude)
    rails = (
        re.search(r"gem\s+[\"']rails[\"']", gemfile) is not None
        or len(rails_files) == 2
    )
    rspec = (
        re.search(r"gem\s+[\"']rspec(?:-rails)?[\"']", gemfile) is not None
        or bool(rspec_files)
    )
    rubocop = (
        "rubocop" in gemfile
        or bool(rubocop_files)
    )
    return {
        "ruby": gemfile_exists,
        "rails": rails,
        "rspec": rspec,
        "rubocop": rubocop,
        "minitest": rails
        and (root / "test").is_dir()
        and not is_excluded(root / "test", root, exclude),
    }


def _cargo_manifests(root: Path, exclude: list[str]) -> list[Path]:
    return existing(root, ["Cargo.toml", "src-tauri/Cargo.toml"], exclude)


def frameworks(root: Path, package_json: dict[str, Any], exclude: list[str]) -> list[str]:
    detected: set[str] = set()
    dependencies: dict[str, Any] = {}
    for key in ("dependencies", "devDependencies"):
        value = package_json.get(key)
        if isinstance(value, dict):
            dependencies.update(value)
    js_mapping = {
        "react": "React",
        "next": "Next.js",
        "vue": "Vue",
        "svelte": "Svelte",
        "express": "Express",
        "@nestjs/core": "NestJS",
        "vite": "Vite",
        "vitest": "Vitest",
        "jest": "Jest",
        "typescript": "TypeScript",
    }
    for package, label in js_mapping.items():
        if package in dependencies:
            detected.add(label)

    python_text = _dependency_text(root, exclude)
    for needle, label in (("django", "Django"), ("fastapi", "FastAPI")):
        if needle in python_text:
            detected.add(label)
    if _has_python_tool(root, "pytest", exclude):
        detected.add("pytest")
    if _has_python_tool(root, "ruff", exclude):
        detected.add("Ruff")

    ruby = _ruby_evidence(root, exclude)
    if ruby["ruby"]:
        detected.update({"Ruby", "Bundler"})
    if ruby["rails"]:
        detected.add("Rails")
    if ruby["rspec"]:
        detected.add("RSpec")
    if ruby["rubocop"]:
        detected.add("RuboCop")

    for manifest in _cargo_manifests(root, exclude):
        detected.update({"Rust", "Cargo"})
        if manifest.parent.name == "src-tauri" or "tauri" in read_text(manifest).lower():
            detected.add("Tauri")

    return sorted(detected)


def _command(
    kind: str,
    command: str,
    source: str,
    confidence: str = "high",
) -> dict[str, str]:
    return {
        "kind": kind,
        "command": command,
        "source": source,
        "confidence": confidence,
    }


def quality_commands(
    root: Path,
    manager: str | None,
    package_json: dict[str, Any],
    exclude: list[str],
) -> list[dict[str, str]]:
    commands: list[dict[str, str]] = []
    scripts = package_json.get("scripts")
    scripts = scripts if isinstance(scripts, dict) else {}
    for kind in ("lint", "typecheck", "test", "build"):
        if kind not in scripts:
            continue
        runner = manager if manager in {"npm", "pnpm", "yarn", "bun"} else "npm"
        prefix = "run " if runner in {"npm", "pnpm", "bun"} else ""
        commands.append(_command(kind, f"{runner} {prefix}{kind}", "package.json"))

    if _has_python_tool(root, "pytest", exclude):
        commands.append(_command("test", "python -m pytest", "python configuration"))
    if _has_python_tool(root, "ruff", exclude):
        commands.append(_command("lint", "python -m ruff check .", "python configuration"))

    ruby = _ruby_evidence(root, exclude)
    if ruby["rspec"]:
        commands.append(_command("test", "bundle exec rspec", "Ruby project"))
    elif ruby["minitest"]:
        commands.append(_command("test", "bin/rails test", "Rails test directory"))
    if ruby["rubocop"]:
        commands.append(_command("lint", "bundle exec rubocop", "Ruby project"))

    for manifest in _cargo_manifests(root, exclude):
        relative = manifest.relative_to(root).as_posix()
        suffix = "" if relative == "Cargo.toml" else f" --manifest-path {relative}"
        commands.extend(
            [
                _command("test", f"cargo test{suffix}", relative),
                _command("typecheck", f"cargo check{suffix}", relative),
                _command(
                    "format-check",
                    (
                        "cargo fmt -- --check"
                        if not suffix
                        else f"cargo fmt --manifest-path {relative} -- --check"
                    ),
                    relative,
                ),
            ]
        )

    unique: dict[tuple[str, str], dict[str, str]] = {}
    for item in commands:
        unique[(item["kind"], item["command"])] = item
    return list(unique.values())


def inspect_project(root: Path, exclude: list[str]) -> dict[str, Any]:
    package_path = root / "package.json"
    package_json = (
        load_json(package_path)
        if package_path.exists() and not is_excluded(package_path, root, exclude)
        else {}
    )
    manager = package_manager(root, exclude)
    return {
        "root": str(root),
        "package_manager": manager,
        "configs": config_files(root, exclude),
        "frameworks": frameworks(root, package_json, exclude),
        "quality_commands": quality_commands(
            root,
            manager,
            package_json,
            exclude,
        ),
    }
