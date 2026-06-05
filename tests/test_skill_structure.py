from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
SKILL_ROOT = SKILLS_ROOT / "code-quality-guardian"
SKILL_FILE = SKILL_ROOT / "SKILL.md"
VERSION = "0.1.0-beta.1"

EXPECTED_SCRIPTS = {
    "_project_detection.py",
    "project_conventions_probe.py",
    "risk_summary.py",
    "run_quality_checks.py",
    "scan_file_lengths.py",
    "scan_function_lengths.py",
}


class PhaseThreeStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill_text = SKILL_FILE.read_text(encoding="utf-8")

    def test_skill_defines_three_intervention_levels(self) -> None:
        for label in (
            "Level 1 Local",
            "Level 2 Coordinated",
            "Level 3 Specialized",
        ):
            self.assertIn(label, self.skill_text)

    def test_skill_contains_decision_contract(self) -> None:
        required_lines = (
            "Intervention class:",
            "Decision:",
            "Reason:",
            "Unknowns:",
            "Verification:",
            "Stop condition:",
        )
        for line in required_lines:
            self.assertIn(line, self.skill_text)

    def test_levels_two_and_three_require_unknowns(self) -> None:
        self.assertRegex(
            self.skill_text,
            r"(?is)Level 2 Coordinated.*?Unknowns.*?required",
        )
        self.assertRegex(
            self.skill_text,
            r"(?is)Level 3 Specialized.*?Unknowns.*?required",
        )

    def test_skill_links_to_existing_markdown_resources(self) -> None:
        linked_paths = re.findall(
            r"`((?:references|examples)/[^`]+\.md)`",
            self.skill_text,
        )
        self.assertTrue(linked_paths)
        missing = [
            relative
            for relative in linked_paths
            if not (SKILL_ROOT / relative).is_file()
        ]
        self.assertEqual(missing, [])

    def test_skill_remains_under_five_hundred_lines(self) -> None:
        self.assertLess(len(self.skill_text.splitlines()), 500)

    def test_public_metadata_matches_beta_release(self) -> None:
        self.assertIn("license: MIT", self.skill_text)
        self.assertIn("Python 3.10+", self.skill_text)
        self.assertIn("author: crousty24-bit", self.skill_text)
        self.assertIn(f'version: "{VERSION}"', self.skill_text)

    def test_phase_three_adds_no_skill_or_script(self) -> None:
        skill_directories = {
            path.name
            for path in SKILLS_ROOT.iterdir()
            if path.is_dir()
        }
        scripts = {
            path.name
            for path in (SKILL_ROOT / "scripts").glob("*.py")
        }
        self.assertEqual(skill_directories, {"code-quality-guardian"})
        self.assertEqual(scripts, EXPECTED_SCRIPTS)

    def test_public_repository_files_exist(self) -> None:
        expected = (
            "README.md",
            "LICENSE",
            "CHANGELOG.md",
            "CONTRIBUTING.md",
            "CODE_OF_CONDUCT.md",
            "SECURITY.md",
            "SUPPORT.md",
            ".github/PULL_REQUEST_TEMPLATE.md",
            ".github/ISSUE_TEMPLATE/bug.yml",
            ".github/ISSUE_TEMPLATE/feature.yml",
            ".github/ISSUE_TEMPLATE/config.yml",
            ".github/workflows/ci.yml",
        )
        missing = [
            relative
            for relative in expected
            if not (REPO_ROOT / relative).is_file()
        ]
        self.assertEqual(missing, [])

    def test_readme_relative_links_exist(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        targets = re.findall(r"\]\((?!https?://|#)([^)]+)\)", readme)
        missing = [
            target
            for target in targets
            if not (REPO_ROOT / target.split("#", 1)[0]).exists()
        ]
        self.assertEqual(missing, [])

    def test_evaluation_material_stays_private(self) -> None:
        gitignore = (REPO_ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertRegex(gitignore, r"(?m)^evals/?$")


if __name__ == "__main__":
    unittest.main()
