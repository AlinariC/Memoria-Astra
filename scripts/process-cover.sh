#!/bin/bash

# process-cover.sh — detects cover.png changes and regenerates JPGs

# Ensure output is consistent
set -e

# Check if cover.png exists
if [ ! -f "cover.png" ]; then
  echo "❌ No cover.png found. Skipping cover processing."
  exit 0
fi

echo "✅ Found cover.png."

# If cover.jpg already exists, rename it with date suffix
if [ -f "cover.jpg" ]; then
  DATE=$(date +%Y-%m-%d)
  mv cover.jpg cover-$DATE.jpg
  echo "📦 Archived old cover.jpg as cover-$DATE.jpg"
fi

# Convert cover.png to 72dpi cover.jpg
convert cover.png -units PixelsPerInch -density 72 cover.jpg
echo "🖼️ Generated 72dpi cover.jpg"

# Convert cover.png to 300dpi cover-300dpi.jpg
convert cover.png -units PixelsPerInch -density 300 cover-300dpi.jpg
echo "🖨️ Generated 300dpi cover-300dpi.jpg"

echo "✅ Cover processing complete."
