# bitaxeorg/legitlist pull request #13: Add TikTok and Nostr social support with stricter slug validation

> Source: https://github.com/bitaxeorg/legitlist/pull/13
> Collected: 2026-10-10
> Published: 2026-03-20
> Registry ID: legitlist

- Repository: bitaxeorg/legitlist
- Type: pull request
- Number: 13
- State: closed, MERGED 2026-03-20T15:12:40Z
- Author: DerekLoadout
- Opened: 2026-03-20
- Files: .github/pull_request_template.md (+1/-1), .github/workflows/validate-vendor.yml (+2/-2), MAINTAINERS.md (+4/-3), README.md (+3/-1), VENDOR_GUIDE.md (+17/-5), scripts/sync-to-framer.mjs (+4/-0), scripts/validate-all.mjs (+2/-2), vendors/_example.json (+3/-1), vendors/_schema.json (+32/-4)

## Body (excerpt)

> ## Summary
> - add `tiktok` and `nostr` social keys to vendor schema and example JSON
> - map new social fields in Framer sync (`socialTt`, `socialNostr`)
> - tighten slug/filename/logo conventions to lowercase single-hyphen format and align CI + docs
> - align contributor and maintainer docs with supported social keys and validation behavior
>
> ## Validation
> `npm run validate` → "🎉 All valid! passes locally"; documentation and enforcement rules were coherence-reviewed and aligned

## Key patches

vendors/_schema.json — schema change defining the canonical social keys and slug/logo patterns (verbatim hunks):

```json
-      "pattern": "^[a-zA-Z0-9_-]+$",
-      "description": "URL-safe identifier, must match filename — letters, numbers, hyphens, underscores (e.g. \"pivotal-mining\" or \"pivotal_mining\")"
+      "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$",
+      "description": "URL-safe identifier, must match filename — lowercase letters, numbers, and hyphens only (e.g. \"pivotal-mining\")"
```

```json
+        "tiktok": {
+          "description": "Full HTTPS URL to TikTok profile, or empty string to omit",
+          "oneOf": [
+            { "type": "string", "format": "uri", "pattern": "^https://" },
+            { "type": "string", "maxLength": 0 }
+          ]
+        },
+        "nostr": {
+          "description": "Full HTTPS URL to Nostr profile page, or empty string to omit",
+          "oneOf": [
+            { "type": "string", "format": "uri", "pattern": "^https://" },
+            { "type": "string", "maxLength": 0 }
+          ]
+        }
```

scripts/sync-to-framer.mjs — Framer CMS field mapping (verbatim):

```js
+  { id: "socialTt",     type: "link",    name: "TikTok" },
+  { id: "socialNostr",  type: "link",    name: "Nostr" },
```

scripts/validate-all.mjs — stricter slug regex (verbatim):

```js
-  if (!/^[a-zA-Z0-9_-]+\.json$/.test(file)) {
+  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*\.json$/.test(file)) {
```

.github/workflows/validate-vendor.yml — CI filename check tightened to match (same regex).

VENDOR_GUIDE.md — nostr usage rule (verbatim): "for `nostr`, use an HTTPS profile page URL (not a raw `npub...` or `nostr:` identifier)"; "only these social keys are allowed in JSON (do not add custom keys like `discord`)".
