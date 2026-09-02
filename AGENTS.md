# Cheat-sheet authoring guide for AI agents

## Canonical sources

Edit `content/*.yaml`. Never edit PDFs or generated Typst by hand. Presentation belongs in `templates/`; validation/build behavior belongs in `scripts/`. Keep topic-specific concepts out of the schema and template.

## Schema

Each document is a mapping with:

- Required: `id`, `title`, `sections`.
- Optional strings: `subtitle`, `version`, `updated`, `intro`, `footer`, `category`.
- Optional `tags`: list of non-empty strings.
- Optional `verified_on`: mapping with required string `date` and optional `software` and `host`. This means the claim/profile was actually checked in that environment on that date; it does not make volatile CLI behavior universal.
- `id` is lowercase kebab-case, equals the YAML filename, and becomes the safe PDF filename.
- Every section has a non-empty `title` and non-empty `blocks` list.

Supported blocks:

```yaml
- type: entries
  items:
    - command: command --flag
      description: Concise effect or caveat.
- type: text
  text: Short explanatory prose.
- type: note
  kind: info # info, tip, or warning
  text: Important compact callout.
- type: code
  text: |-
    command one
    command two
- type: table
  headers: [Column A, Column B]
  rows:
    - [Value A, Value B]
```

## Workflow

To add a sheet, copy the closest content example, replace all topic content, keep the generic schema, then run `python3 scripts/cheatsheets.py validate`, `make cheatsheets-check`, and either `./build.sh ID` or `make cheatsheets`. To update one, preserve its ID unless a rename is intentional and update `updated`; set or refresh `verified_on` only when the claims were genuinely checked in the named environment.

After substantive edits, inspect every changed PDF (render pages to images with `pdftoppm -png -r 120 dist/ID.pdf /tmp/ID` when available). Check page count, clipping, overlaps, code wrapping, contrast, and whether columns are balanced enough to scan. One page is a goal for compact content, not permission to use unreadably small type.

## Content rules

- Prefer short command/description pairs and split genuinely distinct topics into sections.
- Commands must be technically correct and shell-safe. Quote paths/variables and flag destructive or privileged operations.
- Separate stable concepts from version-dependent syntax. Use notes and `verified_on` for volatile CLI claims.
- Clearly label machine-specific performance numbers, topology and memory results as examples; never imply universal performance.
- Do not duplicate layout hints in YAML or insert manual page geometry controls.
- If content overflows awkwardly, edit for concision or improve a reusable template component. Do not hard-code a topic-specific template exception.

To add a reusable block, define its neutral YAML contract, extend `BLOCK_TYPES` and validation in `scripts/cheatsheets.py`, implement rendering in `templates/cheatsheet.typ` or `components.typ`, add positive and negative unit tests, document it here, then rebuild and visually inspect all sheets.

