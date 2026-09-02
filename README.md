# Typst cheat-sheet publishing

A small, reproducible publishing system for dense technical references. Human- and AI-editable YAML is canonical; reusable Typst templates render printable A4 PDFs. Generated files are never hand-edited.

## Architecture

- `content/*.yaml` — canonical structured content, one file per sheet.
- `templates/` — shared A4 layout and presentation components.
- `scripts/cheatsheets.py` — discovery, validation, selection and rendering CLI.
- `tests/` — validator and selection tests.
- `dist/` — ignored local build output; CI uploads the PDFs.

The intentionally small schema supports top-level metadata (`id`, `title`, optional `subtitle`, `version`, `updated`, `intro`, `footer`, `category`, `tags`, and `verified_on`) and titled sections containing typed blocks. Supported block types are `entries`, `text`, `note`, `code`, and `table`. See [AGENTS.md](AGENTS.md) for the field-level authoring contract.

`verified_on` records a dated observation, not an eternal guarantee:

```yaml
verified_on:
  date: "2026-09-02"
  software: llama.cpp master
  host: core-1
```

## Prerequisites and reproducibility

- Python 3.11+
- Typst **0.13.1** (also pinned in `.typst-version`)
- Python packages pinned in `requirements.txt`
- DejaVu Sans and DejaVu Sans Mono (standard open fonts on common Linux distributions)

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
make cheatsheets
```

Build one sheet with `./build.sh tmux` or `make cheatsheet NAME=tmux`. Run validation and tests with `make cheatsheets-check`; remove local output with `make cheatsheets-clean`.

## Add or update a sheet

Copy a nearby YAML file, choose a lowercase kebab-case `id` matching its filename, and express the topic with generic blocks. Keep commands short, shell-safe and technically verified. Run:

```sh
python3 scripts/cheatsheets.py validate
make cheatsheets-check
make cheatsheets
```

Small references should fit one A4 page, but the template deliberately flows longer content onto additional pages instead of shrinking it until unreadable. Inspect rendered output after substantive content or layout changes.

Suggested AI prompt:

> Update the llama.cpp inference cheat sheet with X. Preserve the existing schema and style, validate all commands, run the cheat-sheet build/tests, visually inspect the PDFs, and report any content that no longer fits cleanly on A4.

## Generated output, CI and releases

YAML and templates are source; `dist/*.pdf` and any `generated/` intermediates are ignored. This avoids stale binaries and PDF diffs in review. GitHub Actions pins Typst, installs pinned Python dependencies, validates/tests, builds every PDF, verifies page geometry, and uploads `dist/` as an artifact. A `v*` tag additionally creates a GitHub Release and attaches the PDFs. Release creation requires the repository's standard `contents: write` workflow permission.

