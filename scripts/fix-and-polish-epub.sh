#!/bin/bash

# Stop if any command fails
set -e

# Go into output directory
cd output

# Find the generated EPUB file
EPUB_FILE=$(ls *.epub)

# Extract safe filename
BASENAME="${EPUB_FILE%.epub}"

# Unzip EPUB into temp folder
mkdir -p temp
unzip -q "$EPUB_FILE" -d temp

# Insert <meta name="cover" content="cover-image" /> into content.opf
opf_file="temp/OEBPS/content.opf"
if [ -f "$opf_file" ]; then
  if ! grep -q 'name="cover"' "$opf_file"; then
    sed -i '/<metadata/a \
    <meta name="cover" content="file0_jpg"/>' "$opf_file"
    echo "✅ Inserted cover metadata into content.opf"
  fi
fi

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
