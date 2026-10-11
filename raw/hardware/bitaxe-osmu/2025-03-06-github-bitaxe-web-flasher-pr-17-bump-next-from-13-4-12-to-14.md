# bitaxeorg/bitaxe-web-flasher pull request #17: Bump next from 13.4.12 to 14.2.21

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/pull/17
> Collected: 2026-10-10
> Published: 2025-03-06
> Registry ID: bitaxe-hw

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: pull request (dependabot)
- Number: 17
- State: closed, MERGED 2025-03-06T21:09:53Z (merge commit 8027c4beed)
- Author: dependabot[bot]
- Labels: dependencies, javascript
- Base: bitaxeorg:main ← Head: bitaxeorg:dependabot/npm_and_yarn/next-14.2.21
- 1 commit, 2 files changed, +86/−87

## Body (core statement, verbatim)

```markdown
Bumps [next](https://github.com/vercel/next.js) from 13.4.12 to 14.2.21.
```

The remainder of the body is standard Dependabot boilerplate: an inline list of upstream next.js commits (v14.2.21, v14.2.20 `ed78a4a`, v14.2.19 `cbc62ad`, React upgrade backport #74115, plus "Additional commits viewable in [compare view](https://github.com/vercel/next.js/compare/v13.4.12...v14.2.21)"), a dependabot compatibility-score badge, and the standard `@dependabot rebase/recreate/merge/close/ignore` command reference.

## Files

### package.json (+1/-1, patch verbatim)

The only source-relevant change — the framework version pin that defines what the flasher app builds on:

```diff
-  "next": "13.4.12",
+  "next": "14.2.21",
```

### package-lock.json (+85/-86, summarized per selective-capture policy)

Lockfile-only churn: dependency tree re-resolution for next 13.4.12 → 14.2.21 (transitive version bumps across ~85 added/removed lockfile lines, including the React runtime versions bundled by next's 14.2.x line). No manifest-affecting or behavioral changes beyond the version bump; see upstream v13.4.12...v14.2.21 compare for the full changelog.

## Context

Merged the same day it was opened (2025-03-06). This was the major-version jump of the flasher's web framework (Next 13 → 14) landing in the same week as PR #19 ("fix: selectedFirmware is needed", also 2025-03-06) during the web-flasher's early maintenance burst.
