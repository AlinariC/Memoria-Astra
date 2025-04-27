#!/bin/bash

# fix-and-polish-epub.sh — Updated version to inject correct cover metadata

set -e

cd output

for EPUB_FILE in *.epub; do
  BASENAME="${EPUB_FILE%.epub}"
  mkdir -p temp
  unzip -q "$EPUB_FILE" -d temp

  OPF_FILE="temp/OEBPS/content.opf"
  if [ -f "$OPF_FILE" ]; then
    if ! grep -q 'name="cover"' "$OPF_FILE"; then
      sed -i '/<metadata/a \\n<meta name="cover" content="file0_jpg"/>' "$OPF_FILE"
      echo "✅ Inserted cover metadata into content.opf"
    fi
  fi

  cd temp
  zip -X0 "../${BASENAME}-fixed.epub" mimetype
  zip -rX9 "../${BASENAME}-fixed.epub" * -x mimetype
  cd ..

  rm -rf temp
  rm "$EPUB_FILE"
  mv "${BASENAME}-fixed.epub" "$EPUB_FILE"

  echo "✅ Polished EPUB: $EPUB_FILE"
done
