"""Packaging failures must be detected before publishing an installable skill set."""

from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

from scripts.validate_skills import validate


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "package"
        for name in ("shared-phone", "book-table"):
            skill = self.root / "skills" / name
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: A concrete phone workflow.\n---\n\n# Workflow\n\nFollow the task.\n"
            )
            (skill / "agents" / "openai.yaml").write_text(yaml.safe_dump({"interface": {
                "display_name": name,
                "short_description": "Complete the requested phone workflow",
                "default_prompt": f"Use ${name} for this task.",
            }}))
        reference = self.root / "skills/shared-phone/references/workflow.md"
        reference.parent.mkdir()
        reference.write_text("# Shared calling instructions\n")
        entry = self.root / "skills/book-table/SKILL.md"
        entry.write_text(entry.read_text() + "\nRead [shared instructions](../shared-phone/references/workflow.md).\n")

    def test_complete_portable_package_is_valid(self):
        self.assertEqual(validate(self.root), [])

    def test_install_without_shared_dependency_is_rejected(self):
        shutil.rmtree(self.root / "skills/shared-phone")
        errors = validate(self.root)
        self.assertTrue(any("missing local reference" in error for error in errors), errors)

    def test_reference_outside_the_package_is_rejected_even_if_it_exists(self):
        outside = self.root.parent / "private.md"
        outside.write_text("private data")
        (self.root / "README.md").write_text("[instructions](../private.md)")
        self.assertTrue(any("leaves the package" in error for error in validate(self.root)))

    def test_renamed_skill_with_stale_metadata_is_rejected(self):
        (self.root / "skills/book-table").rename(self.root / "skills/book-other")
        self.assertTrue(any("name must match" in error for error in validate(self.root)))

    def test_interface_invoking_another_skill_is_rejected(self):
        metadata = self.root / "skills/book-table/agents/openai.yaml"
        value = yaml.safe_load(metadata.read_text())
        value["interface"]["default_prompt"] = "Use $unrelated for this task."
        metadata.write_text(yaml.safe_dump(value))
        self.assertTrue(any("must invoke its skill" in error for error in validate(self.root)))

    def test_malformed_frontmatter_is_rejected(self):
        (self.root / "skills/book-table/SKILL.md").write_text("---\nname: [invalid\n---\n# Broken\n")
        self.assertTrue(any("invalid frontmatter" in error for error in validate(self.root)))

    def test_real_repository_package_is_valid(self):
        self.assertEqual(validate(Path(__file__).resolve().parents[1]), [])


if __name__ == "__main__":
    unittest.main()
