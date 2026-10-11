# bitaxeorg/legitlist pull request #20: Add vendor: Bitaxe.de

> Source: https://github.com/bitaxeorg/legitlist/pull/20
> Collected: 2026-10-10
> Published: 2026-04-17
> Registry ID: legitlist

- Repository: bitaxeorg/legitlist
- Type: pull request
- Number: 20
- State: closed, MERGED 2026-04-25T07:47:30Z
- Author: bitaxeshop
- Opened: 2026-04-17
- Files: logos/bitaxe-de.png (binary), vendors/bitaxe-de.json (+16/-0, new file)
- Aftermath: listing later soft-deactivated by PR #54 (2026-08-19) pending "factual trust questions" in legitlist issue #38; hard-revert PR #52 was closed unmerged.

## Body (verbatim)

```markdown
## What's in this PR

**Type:** New vendor listing

---

## About your shop

| | |
|---|---|
| **Shop name** | Bitaxe.de |
| **Website** | https://bitaxe.de |
| **Region** | Europe |
| **Where to find you in the community** | https://x.com/Bitaxeshop |

Note: in your vendor JSON `social` section, use only `x`, `instagram`, `youtube`, `tiktok`, `nostr`.

---

## Vendor confirmation

_Use Yes/No for each line. Keep the text and just replace the value._

These confirmations are reviewed manually by maintainers and the community.

| | |
|---|---|
| I sell genuine Bitaxe hardware | Yes |
| My shop is live and active | Yes |
| I am reachable in the community | Yes |
| I use the correct name `Bitaxe` on my Bitaxe product pages | Yes |
| My Bitaxe product pages use real product photos | Yes |
| My Bitaxe product pages link to `https://bitaxe.org` | Yes |
| I do not sell Bitaxe-derived products in ways that violate Bitaxe open-source license terms | Yes |
| I am not aware of open fraud or counterfeit reports about my shop | Yes |
| I understand listings can be removed if confirmed issues arise | Yes |

---

## Anything else the community should know?

Bitaxe.de is one of the first Bitaxe shops in Germany, built by people who genuinely care about open-source Bitcoin mining. We are committed to serving the community with legitimate hardware, reliable support, and long-term dedication to the Bitaxe ecosystem.
```

## vendors/bitaxe-de.json (entire patch, verbatim)

```json
{
  "name": "Bitaxe.de",
  "slug": "bitaxe-de",
  "website": "https://bitaxe.de",
  "region": "Europe",
  "country": "Germany",
  "description": "Bitaxe.de was one of the first Bitaxe sellers in Germany, focused on legitimate, community-aligned distribution of Bitaxe, Nerdaxe and other open source miners and committed to supporting open-source Bitcoin mining.",
  "active": true,
  "social": {
    "x": "https://x.com/Bitaxeshop",
    "instagram": "",
    "youtube": "",
    "tiktok": "",
    "nostr": ""
  }
}
```

## Review comments (verbatim)

- skot, 2026-04-17T21:20:40Z: "website looks good to me."
- DerekLoadout, 2026-04-19T10:28:57Z: "Applied formal CI-only fixes in commit 8c2de85: fixed slug/filename mismatch in vendors/bitaxe-de.json (bitaxede -> bitaxe-de); renamed logo file to slug-based naming: logos/bitaxe-de.png. No content or vendor-quality review changes were made. I am leaving final non-formal review to @skot."
