#!/usr/bin/env python3
"""Validate skill metadata and portable local references without network access."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.S)
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    skills = sorted(path for path in (root / "skills").glob("*") if path.is_dir())
    if not skills:
        return ["No skill directories found under skills/."]
    for skill in skills:
        label = skill.relative_to(root).as_posix()
        entry = skill / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{label}: missing SKILL.md")
            continue
        content = entry.read_text(encoding="utf-8")
        match = FRONTMATTER.match(content)
        if not match:
            errors.append(f"{label}: missing YAML frontmatter")
            continue
        try:
            header = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"{label}: invalid frontmatter: {exc}")
            continue
        if not isinstance(header, dict):
            errors.append(f"{label}: frontmatter must be an object")
            continue
        name = header.get("name")
        if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
            errors.append(f"{label}: invalid skill name")
        elif name != skill.name:
            errors.append(f"{label}: name must match its directory")
        description = header.get("description")
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            errors.append(f"{label}: missing or invalid description")
        elif "<" in description or ">" in description:
            errors.append(f"{label}: description contains a placeholder or angle bracket")
        body = content[match.end():].strip()
        if not body or re.search(r"(?m)^\s*\[TODO:", body):
            errors.append(f"{label}: empty or unfinished instructions")
        metadata = skill / "agents" / "openai.yaml"
        try:
            interface = yaml.safe_load(metadata.read_text(encoding="utf-8"))["interface"]
            display = interface.get("display_name")
            short = interface.get("short_description")
            prompt = interface.get("default_prompt")
            if not isinstance(display, str) or not display.strip():
                errors.append(f"{label}: missing display name")
            if not isinstance(short, str) or not 25 <= len(short) <= 64:
                errors.append(f"{label}: short description must have 25-64 characters")
            if not isinstance(prompt, str) or f"${name}" not in prompt:
                errors.append(f"{label}: default prompt must invoke its skill")
        except (OSError, KeyError, TypeError, AttributeError, yaml.YAMLError) as exc:
            errors.append(f"{label}: invalid or missing interface metadata: {exc}")
    for document in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv"} for part in document.relative_to(root).parts):
            continue
        for match in LINK.finditer(document.read_text(encoding="utf-8")):
            url = urlsplit(match.group(1).strip("<>"))
            if url.scheme or url.netloc or not url.path:
                continue
            target = (document.parent / unquote(url.path)).resolve()
            label = document.relative_to(root).as_posix()
            line = document.read_text(encoding="utf-8").count("\n", 0, match.start()) + 1
            if not target.is_relative_to(root):
                errors.append(f"{label}:{line}: local reference leaves the package: {url.path}")
            elif not target.exists():
                errors.append(f"{label}:{line}: missing local reference: {url.path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    count = sum(path.is_dir() for path in (args.root / "skills").iterdir())
    print(f"PASS: {count} skills, interface metadata and local Markdown references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
