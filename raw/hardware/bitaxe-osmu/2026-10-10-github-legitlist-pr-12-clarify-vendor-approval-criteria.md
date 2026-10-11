# bitaxeorg/legitlist pull request #12: Clarify vendor approval criteria and review guidance

> Source: https://github.com/bitaxeorg/legitlist/pull/12
> Collected: 2026-10-10
> Published: 2026-03-20
> Registry ID: legitlist

- Repository: bitaxeorg/legitlist
- Type: pull request
- Number: 12
- State: closed, MERGED 2026-03-20T10:30:53Z
- Author: DerekLoadout
- Opened: 2026-03-20
- Files: .github/pull_request_template.md (+6/-0), MAINTAINERS.md (+19/-0), README.md (+3/-1), VENDOR_GUIDE.md (+21/-2)

## Body

> ## Summary
> - add explicit vendor approval review criteria in 
> - add a maintainer-facing vendor review checklist in 
> - update  and PR template to align wording and confirmations
>
> ## Why
> These changes turn maintainer guidance from issue feedback into clear, consistent documentation so contributors understand trust and licensing expectations before submitting.

(Body as fetched; bare backtick file references lost their inline code spans in the API payload.)

## Key patches

MAINTAINERS.md — the maintainer-facing vendor review checklist (verbatim hunk):

```markdown
+## Vendor review checklist
+
+Before merging a vendor PR, confirm:
+
+- The vendor sells genuine Bitaxe hardware and is not misrepresenting clones or counterfeit products
+- The shop is live and active
+- The vendor is reachable in public community channels
+- There are no unresolved fraud or counterfeit reports
+- `Bitaxe` is spelled correctly across the shop page and materials
+- Product photos appear real and specific to the seller
+- Each Bitaxe product page links to `https://bitaxe.org`
+- No Bitaxe-derived products are being sold in violation of Bitaxe open-source license terms
+
+Selling closed-source miners is acceptable if they are not Bitaxe derivatives sold in violation of Bitaxe open-source license terms.
+
+If there is uncertainty, leave the PR open and ask for clarification before merging.
```

VENDOR_GUIDE.md — contributor-facing approval criteria (verbatim hunk):

```markdown
+## Approval review criteria
+
+Final inclusion in the legitlist is up to the maintainers.
+
+These criteria are reviewed manually by maintainers. Meeting them improves approval likelihood but does not guarantee inclusion.
+
+- You use the correct name: `Bitaxe`, not `BitAxe`
+- Your product pages use real photos of the products you sell
+- Your Bitaxe product pages link to `https://bitaxe.org`
+- You do not sell Bitaxe-derived products in ways that violate Bitaxe open-source license terms
+
+Selling closed-source miners is fine as long as they are not Bitaxe derivatives sold in violation of Bitaxe open-source license terms.
+
+If you're unsure whether a product line is acceptable, ask the maintainers before submitting.
```

PR template — four new vendor confirmations added:

```markdown
+| I use the correct name `Bitaxe` on my Bitaxe product pages | Yes |
+| My Bitaxe product pages use real product photos | Yes |
+| My Bitaxe product pages link to `https://bitaxe.org` | Yes |
+| I do not sell Bitaxe-derived products in ways that violate Bitaxe open-source license terms | Yes |
```

README.md — "core team approved" → "maintainer-approved" plus discretion clause:

```markdown
-The legitlist is not a pay-to-play directory. It’s a public trust signal: community-reviewed, core-team approved.
+The legitlist is not a pay-to-play directory. It’s a public trust signal: community-reviewed, maintainer-approved.
+
+Final inclusion is always at maintainer discretion and based on community trust, listing quality, and alignment with the Bitaxe open-source ecosystem.
```
