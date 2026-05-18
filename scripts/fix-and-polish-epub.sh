#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "EPUB polishing is now part of scripts/publish.py."
echo "Rebuilding all source-ready packages instead."
python3 "$SCRIPT_DIR/publish.py" build --all
