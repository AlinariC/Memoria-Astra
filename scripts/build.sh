#!/bin/bash

# build.sh — Updated version to generate EPUB and Print PDF

set -e

TITLE="$(basename $(pwd) | tr '_' ' ' | sed 's:/: :g')"
OUTPUT_DIR="../output"
mkdir -p "$OUTPUT_DIR"

# Generate Combined.md including Manuscript.md and Colophon.md
cat Manuscript.md ../assets/Colophon.md > Combined.md

# Build the EPUB
pandoc Combined.md \
  --metadata title="$TITLE" \
  --epub-cover-image=cover.jpg \
  --toc \
  --output="$OUTPUT_DIR/${TITLE// /_}.epub"

# Build the Print PDF (no TOC)
pandoc Combined.md \
  --pdf-engine=xelatex \
  --variable papersize="6in x 9in" \
  --variable geometry=margin=0.75in \
  --output="$OUTPUT_DIR/${TITLE// /_}-Print.pdf"

# Cleanup
rm Combined.md
