# Memoria Astra - Automated Book Publishing
## “Memoria Astra — A Song Woven Across the Stars.”

[![License: PPPL v1.0](https://img.shields.io/badge/license-PPPL%20v1.0-purple.svg?style=flat-square)](/LICENSE)
[![Build: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square)]()
[![EPUBs Ready](https://img.shields.io/badge/epubs-ready-blue.svg?style=flat-square)]()
[![Publisher: PixelPacific](https://img.shields.io/badge/publisher-PixelPacific-8a2be2.svg?style=flat-square)](https://pixelpacific.com)
[![Universe: Memoria Astra](https://img.shields.io/badge/universe-Memoria%20Astra-8a2be2.svg?style=flat-square)]()
[![GitHub Release](https://img.shields.io/github/v/release/AlinariC/Memoria-Astra?include_prereleases&sort=date&display_name=release&style=flat-square)](https://github.com/AlinariC/Memoria-Astra/releases)

This repository automates the EPUB generation process for the **Memoria Astra** book series.

## 📚 Repository Structure

```
/
├── 01_Terra_in_the_Mists/
│    ├── Manuscript.md
│    ├── cover.jpg
├── 02_Before_the_Mists/
│    └── (similar structure)
├── (etc.)
├── assets/
│    └── styles.css
├── scripts/
│    ├── build.sh
│    ├── fix-and-polish-epub.sh
├── output/
│    └── (temporary EPUBs before upload to Releases)
├── .github/
│    └── workflows/
│         └── build-epub.yml
├── README.md
├── LICENSE
```

## 🚀 Automation Overview

- Whenever a `Manuscript.md` or `cover.jpg` is updated in any book folder, GitHub Actions will:
  - Detect the changed book(s)
  - Run `build.sh` to compile a clean EPUB
  - Run `fix-and-polish-epub.sh` to polish and finalize the EPUB
  - Move the final `.epub` into `/output/`
  - Publish the EPUB(s) to the GitHub Releases tab for easy download

## 🛠 Scripts

- **build.sh** — Compiles Markdown + metadata + cover + styles into a `.epub`
- **fix-and-polish-epub.sh** — Ensures correct EPUB structure and cover visibility

Both scripts live inside `/scripts/`.

## 🧰 How to Run Locally

1. Install required tools:
   ```bash
   sudo apt-get install pandoc zip unzip imagemagick
   ```

2. Build manually:
   ```bash
   cd [Book_Folder]
   bash ../scripts/build.sh
   bash ../scripts/fix-and-polish-epub.sh
   ```

3. Final EPUB will be inside the `/output/` folder.

## ✨ Additional Features

- Fully mobile-first website structure in parallel (`jekyll` site under `/`)
- SEO enhancements with `robots.txt`, OpenGraph metadata
- MIT-style custom licensing with PixelPacific Public License (PPPL v1.0)

---

© 2025 Alinari Campbell | Published by [PixelPacific](https://pixelpacific.com)
