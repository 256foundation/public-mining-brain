# 256foundation/website pull request #5: copy: retire the "100% passthrough" claim sitewide

> Source: https://github.com/256foundation/website/pull/5
> Collected: 2026-10-07
> Published: 2026-08-04

- Repository: 256foundation/website
- Type: pull request
- Number: 5
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-04
- Closed: 2026-08-04
- Labels: none

## Description

Retires the "100% passthrough" claim and replaces it with direct-funding language everywhere it appeared.

Scoped as five locations; it turned out to be **seven**. Two places made the same claim without using the word, so a `grep passthrough` alone would have passed while the claim was still live on the site.

## What changed

| File | Change |
|---|---|
| [`app/mission/page.tsx`](app/mission/page.tsx) | "💯 100% Passthrough" value card → "🔧 Direct Funding" |
| [`app/donate/page.tsx`](app/donate/page.tsx) | Hero rewritten to a single sentence naming the four pillar projects (was two sentences) |
| [`components/home/AllocationStats.tsx`](components/home/AllocationStats.tsx) | Trailing "100% passthrough to developers" note deleted, not replaced — the adjacent "View All Funded Projects" link already carries the section |
| [`components/home/DonateCards.tsx`](components/home/DonateCards.tsx) | Replaces "every satoshi goes directly to developers" |
| [`data/faq.ts`](data/faq.ts) | **Not in original scope.** "How much of my donation goes towards open-source contributors?" was built around a figure we no longer publish, so the question was reframed to "What does my donation fund?" rather than leaving it paired with a non-quantified answer |
| [`content/newsroom/mara-foundation-tier1-supporter.mdx`](content/newsroom/mara-foundation-tier1-supporter.mdx) | Body sentence, plus the closing boilerplate at the end of the article (**also not in original scope**) |

Two notes for reviewers:

- The FAQ answer previously bundled two claims. The second — **no board member is compensated** — is separate, still accurate, and was kept.
- Editing a published press release that names MARA is a visible change. Direct edit was chosen over appending an editor's note.

## Verification

- `grep -ri "passthrough" app components data content` → nothing
- Paraphrase sweep (`every dollar|sat|satoshi|cent`, `100% of`, `no percentage`, `no cut taken`, `overhead`, `administrat`) → nothing. Solo-mining copy on `/donate`, `/telehash`, and `faq.ts:52` stating that block reward proceeds go to the foundation is a different and accurate claim, deliberately left alone.
- `npm run build` clean (19 routes, `tsc` included) · `npm test` 11/11
- `npm run lint` **could not run** — the repo has no ESLint config, so `next lint` hangs on its interactive setup prompt. Reproduced on a clean tree, so it is pre-existing and not from this branch. Changed files were linted directly via a temporary flat config importing `eslint-config-next`: exit 0. Worth its own chore PR, especially since Next 16 drops `next lint`.
- Browser-checked in **light and dark mode**: `/mission`, `/donate`, `/faq` (accordion expanded), the home page, and the MARA post. No console errors. The DonateCards copy is longer now; both cards stay equal height with no overflow.

Copy-only — no logic, dependency, or design-system changes.

Roadmap item 1 (`website-roadmap-2026-Q3.md`, `organization-spec`).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-08-04

[vc]: #Psnw3ZrKoDvcBITnKJV9XV2dzTLmzbnHE62PGhfnwaw=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLTI1Ni1mIiwicHJvamVjdElkIjoicHJqX3h4bkVLbGJrM2RYdlFMbTF2N25JUUN3UkVmT1YiLCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vdHlsZXJrc3RldmVucy1wcm9qZWN0cy93ZWJzaXRlLTI1Ni1mL0FwSmNlcDFDdnp6Mk1kRFJ5Zldob2JCV3pabWgiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS0yNTYtZi1naXQtY29weS1yZXRpcmUtcGFzLTBlODc0ZC10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQiLCJsaXZlRmVlZGJhY2siOnsicmVzb2x2ZWQiOjAsInVucmVzb2x2ZWQiOjAsInRvdGFsIjowLCJsaW5rIjoid2Vic2l0ZS0yNTYtZi1naXQtY29weS1yZXRpcmUtcGFzLTBlODc0ZC10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAifSwicm9vdERpcmVjdG9yeSI6bnVsbH0seyJuYW1lIjoid2Vic2l0ZSIsInByb2plY3RJZCI6InByal9Ec09RanhuVUtmMGxpQ2pwV3dGRFR3OTRJYXhXIiwicm9vdERpcmVjdG9yeSI6bnVsbCwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtZ2l0LWNvcHktcmV0aXJlLXBhc3N0aHJvdWdoLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCJ9LCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy93ZWJzaXRlL1Z2a2VYRWZQZnBReWc2eWY2eW9FYVdZWDI5bzYiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS1naXQtY29weS1yZXRpcmUtcGFzc3Rocm91Z2gtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIiwibmV4dENvbW1pdFN0YXR1cyI6IkRFUExPWUVEIn1dfQ==
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/256-foundation-s-projects/website"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_DsOQjxnUKf0liCjpWwFDTw94IaxW&teamId=team_4m4Hz1Tn7d5LJFeztgvbd2CS&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website](https://vercel.com/256-foundation-s-projects/website) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website/VvkeXEfPfpQyg6yf6yoEaWYX29o6) | [Preview](https://website-git-copy-retire-passthrough-256-foundation-s-projects.vercel.app) | Aug 4, 2026 7:00pm |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_4m4Hz1Tn7d5LJFeztgvbd2CS&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/tylerkstevens-projects/website-256-f/ApJcep1Cvzz2MdDRyfWhobBWzZmh) | [Preview](https://website-256-f-git-copy-retire-pas-0e874d-tylerkstevens-projects.vercel.app) | Aug 4, 2026 7:00pm |
