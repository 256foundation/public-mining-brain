# Bitaxe legitlist vendor counts by region (2026-10-07)

> Source: https://github.com/bitaxeorg/legitlist (`vendors/*.json` files)
> Collected: 2026-10-07
> Published: N/A (live point-in-time snapshot)

Method: shallow clone of bitaxeorg/legitlist; counted `vendors/*.json` (excluding `_example.json`) and grouped `region` fields with `jq`. The legitlist is the community-verified list of trusted Bitaxe vendors ("miners vouching for miners"; submit-by-PR process per its README, already in raw/ecosystem).

## Totals

- **Listed vendors: 27**

| region | vendors |
|---|---|
| Europe | 17 |
| North America | 5 |
| South America | 2 |
| Asia Pacific | 2 |
| India | 1 |
| (region unknown/unspecified) | 1 |

Region taxonomy used by legitlist: Europe, North America, South America, Asia Pacific, Middle East, Africa, India.

Notes:
- This is a lower bound on Bitaxe commerce reach: only vendors that submitted a PR and passed community review are listed.
- Vendor identities (slug, website, socials) are in `vendors/{slug}.json` in the source repo; not duplicated here.
