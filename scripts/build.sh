#!/bin/bash

set -euo pipefail

# Compatibility wrapper. The root publisher now owns discovery, packaging,
# platform folders, and validation checklists.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$SCRIPT_DIR/publish.py" build --book "$(pwd)"
