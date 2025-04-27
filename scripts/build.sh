#!/bin/bash

# Stop if any command fails
set -e

# Extract title from Manuscript.md
TITLE=$(awk '/^---/{flag=1;next}/^---/{flag=0}flag && /^title:/{gsub(/^title: *"/,""); gsub(/"$/,""); print; exit}' Manuscript.md)
SAFE_TITLE=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9_-]//g')

# Build the EPUB
pandoc Manuscript.md \
  --metadata-file=metadata.yaml \
  --epub-cover-image=cover.jpg \
  --css=../assets/styles.css \
  --variable=epub-chapter-level=1 \
  --toc \
  -o "${SAFE_TITLE}.epub"

echo "✅ EPUB created successfully: ${SAFE_TITLE}.epub"
