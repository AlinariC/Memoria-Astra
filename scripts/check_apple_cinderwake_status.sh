#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KEY_DIR="${APPLE_API_KEY_DIR:-/Users/acampbell/Documents/API-KEYS/apple}"
TRANSPORTER="${TRANSPORTER_BIN:-/Applications/Transporter.app/Contents/itms/bin/iTMSTransporter}"
VENDOR_IDS="cinderwake_audio_01_the_ash_beneath_the_crown,cinderwake_audio_02_the_moon_below_the_world,cinderwake_audio_03_the_dragon_that_dreamed_death"

if [[ ! -x "$TRANSPORTER" ]]; then
  echo "Transporter not found at: $TRANSPORTER" >&2
  exit 1
fi

KEY_ID="$(tr -d '[:space:]' < "$KEY_DIR/keyID")"
ISSUER_ID="$(tr -d '[:space:]' < "$KEY_DIR/issuerID")"
KEY_FILE="$KEY_DIR/AuthKey_${KEY_ID}.p8"

if [[ ! -f "$KEY_FILE" ]]; then
  echo "Apple private key not found at expected path." >&2
  exit 1
fi

mkdir -p "$ROOT/output/apple-transporter-logs"
RUN_DIR="$(mktemp -d /tmp/cinderwake-apple-status.XXXXXX)"
trap 'rm -rf "$RUN_DIR"' EXIT
mkdir -p "$RUN_DIR/private_keys"
ln -s "$KEY_FILE" "$RUN_DIR/private_keys/AuthKey_${KEY_ID}.p8"

LOG="$ROOT/output/apple-transporter-logs/status-api-cinderwake-$(date +%Y%m%d-%H%M%S).log"
set +e
(
  cd "$RUN_DIR"
  "$TRANSPORTER" \
    -m status \
    -vendor_ids "$VENDOR_IDS" \
    -apiIssuer "$ISSUER_ID" \
    -apiKey "$KEY_ID" \
    -apiKeyType team \
    -v informational
) > "$LOG" 2>&1
RC=$?
set -e

python3 - "$LOG" "$KEY_ID" "$ISSUER_ID" "$RC" <<'PY'
from pathlib import Path
import sys

log = Path(sys.argv[1])
key_id = sys.argv[2]
issuer_id = sys.argv[3]
rc = int(sys.argv[4])
text = log.read_text(errors="replace").replace(key_id, "[KEY_ID]").replace(issuer_id, "[ISSUER_ID]")

print("Cinderwake Apple audiobook status")
print(f"Log: {log}")
print()

started = False
printed = False
for line in text.splitlines():
    if line.startswith("Vendor identifier:"):
        started = True
    if started:
        if line.startswith("[") and "DBG-X:" in line:
            continue
        print(line)
        printed = True

if not printed:
    print("No status records were returned. Last Transporter output:")
    print()
    for line in text.splitlines()[-40:]:
        if "TransporterArguments" not in line:
            print(line)

raise SystemExit(rc)
PY
