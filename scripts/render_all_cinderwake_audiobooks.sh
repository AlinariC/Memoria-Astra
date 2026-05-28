#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

LOG_DIR="output/audiobooks/cinderwake/logs"
mkdir -p "$LOG_DIR"

books=(
  "book-01-the-ash-beneath-the-crown"
  "book-02-the-moon-below-the-world"
  "book-03-the-dragon-that-dreamed-death"
)

for book in "${books[@]}"; do
  log="$LOG_DIR/${book}.log"
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] starting ${book}" >> "$log"
  args=(
    "$book"
    --engine dialogue
    --jobs "${CINDERWAKE_AUDIOBOOK_JOBS:-3}"
    --seed "${CINDERWAKE_AUDIOBOOK_SEED:-30101}"
  )
  if [[ "${CINDERWAKE_AUDIOBOOK_FORCE:-0}" == "1" ]]; then
    args+=(--force)
  fi
  python3 scripts/render_cinderwake_audiobooks.py "${args[@]}" >> "$log" 2>&1
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] finished ${book}" >> "$log"
done
