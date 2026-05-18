# Apple Books Transporter Packages

This folder contains the Apple-only metadata overlay used by
`scripts/build_apple_itmsp.py`.

Build all local `.itmsp` folders from the existing generated EPUB and cover
outputs:

```bash
python3 scripts/build_apple_itmsp.py --all
```

Override the Apple provider short name without editing the catalog:

```bash
APPLE_BOOKS_PROVIDER=YourProviderShortName python3 scripts/build_apple_itmsp.py --all
```

Generated packages are written under each existing Apple output folder:

```text
output/<book>/apple-books/<vendor_id>.itmsp/
├── metadata.xml
├── <book>.epub
└── cover.jpg
```

Account-sensitive fields to confirm before upload:

- `provider` is `AlinariCampbell`, the publication-capable provider short name
  reported by the signed-in Transporter app.
- `01-terra-in-the-mists` uses the existing Apple Books Vendor ID
  `10083606179`, visible in iTunes Connect.
- `00-the-first-spiral` has no ISBN and uses the permanent local vendor ID
  `memoria_astra_00_the_first_spiral`.
- `08-inheritance-of-song` uses the permanent local vendor ID
  `memoria_astra_08_inheritance_of_song`.
- Exact original publication dates are placeholders where the source metadata
  only provided a year.
