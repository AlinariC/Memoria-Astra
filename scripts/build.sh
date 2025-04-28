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
  --css=../assets/styles.css \
  --toc \
  --output="$OUTPUT_DIR/${TITLE// /_}.epub"

# Build the Print PDF (with TOC)
pandoc Combined.md \
  --pdf-engine=xelatex \
  --lua-filter="../assets/unnumber-specials.lua" \
  --include-in-header="../assets/pdf-header.tex" \
  --toc \
  --toc-depth=1 \
  --variable documentclass=book \
  --variable classoption=oneside \
  --variable colorlinks=false \
  --variable linkcolor=black \
  --variable numbersections=true \
  --variable secnumdepth=1 \
  --output="$OUTPUT_DIR/${TITLE// /_}-Print.pdf"
  
# Cleanup
rm Combined.md
