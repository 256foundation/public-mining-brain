# bitaxeorg/legitlist pull request #54: Deactivate vendor: Bitaxe.de

> Source: https://github.com/bitaxeorg/legitlist/pull/54
> Collected: 2026-10-10
> Published: 2026-08-19
> Registry ID: legitlist

- Repository: bitaxeorg/legitlist
- Type: pull request
- Number: 54
- State: closed, MERGED 2026-08-19T15:08:25Z
- Author: DerekLoadout
- Opened: 2026-08-19
- Files: vendors/bitaxe-de.json (+1/-1)
- Context: first soft-deactivation in legitlist history; refs legitlist issue #38. Revert PR #52 (WantClue, hard deletion) was closed unmerged the day before.

## Body (verbatim)

```markdown
## What's in this PR

**Type:** Removal / deactivation

| | |
|---|---|
| **Shop name** | Bitaxe.de |
| **Website** | https://bitaxe.de |
| **Region** | Europe |
| **Where to find you in the community** | https://github.com/bitaxeorg/legitlist/issues/38 |

## Rationale

This PR temporarily deactivates the Bitaxe.de listing while the factual trust questions documented in #38 are resolved. It is not a finding that Bitaxe.de is a scam or has committed fraud.

This action does not make a determination about separate legal or trademark disputes.

The listing can be reconsidered through the normal public process once the outstanding questions have been answered with verifiable evidence.

#52 used a hard deletion rather than the documented soft-deactivation path and was closed without merge.

Refs #38
```

## Patch (entire diff, verbatim)

```json
   "region": "Europe",
   "country": "Germany",
   "description": "Bitaxe.de was one of the first Bitaxe sellers in Germany, focused on legitimate, community-aligned distribution of Bitaxe, Nerdaxe and other open source miners and committed to supporting open-source Bitcoin mining.",
-  "active": true,
+  "active": false,
   "social": {
     "x": "https://x.com/Bitaxeshop",
```

## Notes

- This is the documented "soft remove" path in action: `"active": false` — file stays in repo, vendor remains in Framer CMS, site filters `vendorActive = "true"`.
- The deactivation explicitly disclaims any scam/fraud finding and points to issue #38 for the underlying "factual trust questions"; the PR title prefix `Deactivate vendor:` matches the convention codified in PR #45.
