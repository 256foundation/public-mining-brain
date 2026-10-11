# bitaxeorg/legitlist pull request #45: Add PR metadata validation

> Source: https://github.com/bitaxeorg/legitlist/pull/45
> Collected: 2026-10-10
> Published: 2026-06-04
> Registry ID: legitlist

- Repository: bitaxeorg/legitlist
- Type: pull request
- Number: 45
- State: closed, MERGED 2026-06-04T11:05:01Z
- Author: DerekLoadout
- Opened: 2026-06-04
- Files: .github/workflows/validate-vendor.yml (+11/-2), MAINTAINERS.md (+4/-3), VENDOR_GUIDE.md (+4/-0), package.json (+2/-1), scripts/validate-pr.mjs (+128/-0, new file)
- Note: #44 (same title, opened same day by the same author) was closed unmerged — #45 is the reworked version that landed.

## Body

> ## Summary
> Adds PR metadata validation for vendor submissions.
>
> ## Changes
> - Validates vendor PR title format.
> - Catches unreplaced PR template placeholders.
> - Requires completed shop, website, and community rows for vendor listing PRs.
> - Requires vendor confirmations for add/update PRs only.
> - Skips vendor metadata checks for maintenance PRs that do not touch `vendors/` or `logos/`.
> - Expands workflow path coverage for validation tooling.
> - Documents accepted vendor PR title prefixes.
>
> ## Testing
> - `npm run validate` / `npm run validate:pr` / `node --check scripts/validate-pr.mjs`
> - Sample Add vendor / Deactivate vendor payloads

## Key patches

scripts/validate-pr.mjs — new 128-line validator (key logic, verbatim excerpts):

```js
const titleMatch = title.match(/^(Add vendor|Update vendor|Remove vendor|Deactivate vendor): .+/)
const prType = titleMatch?.[1]
const changedFiles = await getChangedFiles()
const touchesVendorListing = changedFiles?.some((file) => file.startsWith("vendors/") || file.startsWith("logos/"))

if (changedFiles && !touchesVendorListing && !titleMatch) {
  console.log("Skipping PR metadata validation: PR does not touch vendor listings")
  process.exit(0)
}

if (!titleMatch) {
  errors.push("PR title must start with one of: 'Add vendor:', 'Update vendor:', 'Remove vendor:', or 'Deactivate vendor:'")
}

const placeholders = [
  "Your shop name",
  "https://yourshop.com",  // (joined from template placeholder list)
  "Your X, Discord, Instagram, TikTok, Nostr, or other public link",
]

for (const placeholder of placeholders) {
  if (body.includes(placeholder)) {
    errors.push(`Replace PR template placeholder: ${placeholder}`)
  }
}
```

Confirmation-row enforcement for Add/Update PRs only:

```js
const confirmationRows = [
  "I sell genuine Bitaxe hardware",
  "My shop is live and active",
  "I am reachable in the community",
  "I use the correct name `Bitaxe` on my Bitaxe product pages",
  "My Bitaxe product pages use real product photos",
  "My Bitaxe product pages link to `https://bitaxe.org`",
  "I do not sell Bitaxe-derived products in ways that violate Bitaxe open-source license terms",
  "I am not aware of open fraud or counterfeit reports about my shop",
  "I understand listings can be removed if confirmed issues arise",
]

if (prType === "Add vendor" || prType === "Update vendor") {
  for (const label of confirmationRows) {
    const escapedLabel = label.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
    const rowPattern = new RegExp(`\\|\\s*${escapedLabel}\\s*\\|\\s*(Yes|No)\\s*\\|`, "i")
    if (!rowPattern.test(body)) {
      errors.push(`Vendor confirmation must be answered Yes/No: ${label}`)
    }
  }
}
```

(The file also regex-requires completed `**Shop name**`, `**Website**` (https), and community-contact table rows, then exits 1 listing all errors; changed files are fetched via the PR `self` link + GITHUB_TOKEN, degrading to title/body-only validation on failure.)

.github/workflows/validate-vendor.yml — new trigger types + step (verbatim):

```yaml
 on:
   pull_request:
+    types: [opened, edited, synchronize, reopened, ready_for_review]
     paths:
       - "vendors/**"
       - "logos/**"
+      - "scripts/**"
+      - "package.json"
+      - "package-lock.json"
+      - ".github/workflows/validate-vendor.yml"
...
+      - name: Run PR metadata validator
+        run: npm run validate:pr
+        env:
+          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

MAINTAINERS.md — title-prefix rule added to the merge flow (verbatim): "Vendor listing PR titles must start with `Add vendor:`, `Update vendor:`, `Remove vendor:`, or `Deactivate vendor:`"
