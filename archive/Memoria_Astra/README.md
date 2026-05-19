# Memoria Astra Archive

This folder preserves the full Memoria Astra publishing set: manuscripts, covers, Apple metadata, KDP/Google/Apple working notes, and the two series-specific manuscript assembly helpers.

The root PixelPacific Publishing workflow skips anything under `archive/` by default. Use these only when you intentionally need to inspect or rebuild the archived series:

```bash
python3 scripts/publish.py inventory --include-archived
python3 scripts/publish.py build --book archive/Memoria_Astra/16_The_Second_Spiral
python3 scripts/publish.py build --all --include-archived
```

Do not use `--include-archived` in the normal GitHub push workflow; active publishing work should live in a new series folder or standalone book folder at the repository root.
