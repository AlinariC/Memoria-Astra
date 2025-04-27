#!/bin/bash

# Stop if any command fails
set -e

# Find the generated EPUB file
EPUB_FILE=$(ls *.epub)

# Extract safe filename
BASENAME="${EPUB_FILE%.epub}"

# Unzip EPUB into temp folder
mkdir -p temp
unzip -q "$EPUB_FILE" -d temp

# Fix the content.opf metadata if needed (future automation possible)

# Rebuild the EPUB properly
cd temp
zip -X0 "../${BASENAME}-fixed.epub" mimetype
zip -rX9 "../${BASENAME}-fixed.epub" * -x mimetype
cd ..

# Clean up
rm -rf temp
rm "$EPUB_FILE"

# Rename polished version
mv "${BASENAME}-fixed.epub" "${BASENAME}.epub"

echo "✅ EPUB polished successfully: ${BASENAME}.epub"
