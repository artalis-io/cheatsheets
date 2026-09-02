#!/usr/bin/env python3
"""Validate and build structured Typst cheat sheets."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
TEMPLATE = ROOT / "templates" / "cheatsheet.typ"
DIST = ROOT / "dist"
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
BLOCK_TYPES = {"entries", "text", "note", "code", "table"}
NOTE_KINDS = {"info", "tip", "warning"}


class ValidationError(Exception):
    pass


@dataclass(frozen=True)
class Sheet:
    path: Path
    data: dict[str, Any]

    @property
    def id(self) -> str:
        return self.data["id"]


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def load_sheet(path: Path) -> Sheet:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise ValidationError(f"{path}: cannot parse YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: document must be a mapping")
    return Sheet(path, data)


def validate_sheet(sheet: Sheet) -> list[str]:
    d, errors = sheet.data, []
    where = sheet.path.name
    for key in ("id", "title"):
        if not _nonempty(d.get(key)):
            errors.append(f"{where}: {key} must be a non-empty string")
    sheet_id = d.get("id")
    if _nonempty(sheet_id):
        if not ID_RE.fullmatch(sheet_id):
            errors.append(f"{where}: id must match {ID_RE.pattern}")
        if sheet.path.stem != sheet_id:
            errors.append(f"{where}: filename must match id '{sheet_id}'")
    for key in ("subtitle", "version", "updated", "intro", "footer", "category"):
        if key in d and not _nonempty(d[key]):
            errors.append(f"{where}: {key} must be a non-empty string when present")
    tags = d.get("tags", [])
    if not isinstance(tags, list) or any(not _nonempty(x) for x in tags):
        errors.append(f"{where}: tags must be a list of non-empty strings")
    verified = d.get("verified_on")
    if verified is not None:
        if not isinstance(verified, dict):
            errors.append(f"{where}: verified_on must be a mapping")
        else:
            for key in ("date", "software", "host"):
                if key in verified and not _nonempty(str(verified[key])):
                    errors.append(f"{where}: verified_on.{key} must not be empty")
            if "date" not in verified:
                errors.append(f"{where}: verified_on.date is required")
    sections = d.get("sections")
    if not isinstance(sections, list) or not sections:
        errors.append(f"{where}: sections must be a non-empty list")
        return errors
    for si, section in enumerate(sections):
        loc = f"{where}: sections[{si}]"
        if not isinstance(section, dict):
            errors.append(f"{loc} must be a mapping")
            continue
        if not _nonempty(section.get("title")):
            errors.append(f"{loc}.title must be a non-empty string")
        blocks = section.get("blocks")
        if not isinstance(blocks, list) or not blocks:
            errors.append(f"{loc}.blocks must be a non-empty list")
            continue
        for bi, block in enumerate(blocks):
            bloc = f"{loc}.blocks[{bi}]"
            if not isinstance(block, dict):
                errors.append(f"{bloc} must be a mapping")
                continue
            kind = block.get("type")
            if kind not in BLOCK_TYPES:
                errors.append(f"{bloc}.type unsupported: {kind!r}")
                continue
            if kind == "entries":
                items = block.get("items")
                if not isinstance(items, list) or not items:
                    errors.append(f"{bloc}.items must be a non-empty list")
                else:
                    for ii, item in enumerate(items):
                        if not isinstance(item, dict) or not _nonempty(item.get("command")) or not _nonempty(item.get("description")):
                            errors.append(f"{bloc}.items[{ii}] requires non-empty command and description")
            elif kind in {"text", "code"} and not _nonempty(block.get("text")):
                errors.append(f"{bloc}.text must be a non-empty string")
            elif kind == "note":
                if block.get("kind", "info") not in NOTE_KINDS:
                    errors.append(f"{bloc}.kind must be one of {sorted(NOTE_KINDS)}")
                if not _nonempty(block.get("text")):
                    errors.append(f"{bloc}.text must be a non-empty string")
            elif kind == "table":
                headers, rows = block.get("headers"), block.get("rows")
                if not isinstance(headers, list) or not headers or any(not _nonempty(x) for x in headers):
                    errors.append(f"{bloc}.headers must be non-empty strings")
                if not isinstance(rows, list) or not rows:
                    errors.append(f"{bloc}.rows must be a non-empty list")
                elif isinstance(headers, list) and any(not isinstance(r, list) or len(r) != len(headers) for r in rows):
                    errors.append(f"{bloc}.rows must match header column count")
    return errors


def discover(content_dir: Path = CONTENT) -> list[Sheet]:
    sheets = [load_sheet(p) for p in sorted(content_dir.glob("*.yaml"))]
    if not sheets:
        raise ValidationError(f"no YAML files found in {content_dir}")
    ids: dict[str, Path] = {}
    duplicate_errors = []
    for sheet in sheets:
        sheet_id = sheet.data.get("id")
        if isinstance(sheet_id, str) and sheet_id in ids:
            duplicate_errors.append(f"duplicate id '{sheet_id}': {ids[sheet_id].name}, {sheet.path.name}")
        elif isinstance(sheet_id, str):
            ids[sheet_id] = sheet.path
    if duplicate_errors:
        raise ValidationError("\n".join(duplicate_errors))
    return sheets


def validate_all(sheets: list[Sheet]) -> None:
    errors = [error for sheet in sheets for error in validate_sheet(sheet)]
    if errors:
        raise ValidationError("\n".join(errors))


def select(sheets: list[Sheet], names: list[str]) -> list[Sheet]:
    if not names:
        return sheets
    by_id = {s.id: s for s in sheets}
    unknown = sorted(set(names) - by_id.keys())
    if unknown:
        raise ValidationError(f"unknown cheat sheet(s): {', '.join(unknown)}")
    return [by_id[name] for name in names]


def typst_binary() -> str:
    binary = shutil.which("typst")
    if not binary:
        raise ValidationError("Typst not found; install version from .typst-version")
    return binary


def build(sheets: list[Sheet]) -> None:
    compiler = typst_binary()
    DIST.mkdir(exist_ok=True)
    for sheet in sheets:
        output = DIST / f"{sheet.id}.pdf"
        print(f"BUILD    {sheet.id}")
        subprocess.run(
            [compiler, "compile", "--root", str(ROOT), "--input", f"sheet={sheet.id}", str(TEMPLATE), str(output)],
            cwd=ROOT,
            check=True,
        )
    print(f"OK       {len(sheets)} PDF(s) in {DIST.relative_to(ROOT)}/")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    build_parser = sub.add_parser("build", help="validate and build PDFs")
    build_parser.add_argument("names", nargs="*", help="sheet IDs (default: all)")
    sub.add_parser("validate", help="validate all YAML sources")
    sub.add_parser("check", help="run validation and unit tests")
    sub.add_parser("clean", help="remove generated PDFs")
    args = parser.parse_args(argv)
    try:
        if args.command == "clean":
            shutil.rmtree(DIST, ignore_errors=True)
            print("CLEAN    dist/")
            return 0
        sheets = discover()
        validate_all(sheets)
        print(f"VALID    {len(sheets)} sheet(s)")
        if args.command == "build":
            build(select(sheets, args.names))
        elif args.command == "check":
            subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=ROOT, check=True)
        return 0
    except (ValidationError, subprocess.CalledProcessError) as exc:
        print(f"ERROR    {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

