# 256foundation/website-heatpunks pull request #7: Fix hCaptcha verification failure (duplicate response field)

> Source: https://github.com/256foundation/website-heatpunks/pull/7
> Collected: 2026-10-07
> Published: 2026-07-22

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 7
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-22
- Closed: 2026-07-22
- Labels: none

## Description

## Summary
- Both forms failed on the deployed site with "couldn't verify captcha" — root cause: `@hcaptcha/react-hcaptcha` auto-injects its own hidden `<textarea name="h-captcha-response">` into the form's DOM, and our submit handler additionally did `formData.append('h-captcha-response', captchaToken)`, so the request carried two values for the same field.
- Fixed by switching to `formData.set(...)`, which replaces any existing value for that key instead of adding a second one.

## Test plan
- [x] `npm run build`, `npx tsc --noEmit` pass
- [x] Confirmed via live DOM inspection on heatpunks.org that the hCaptcha widget injects its own `h-captcha-response` textarea inside the form
- [ ] After merge/redeploy: submit both forms live on heatpunks.org and confirm success (not "couldn't verify captcha")

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-22

[vc]: #Ip/LL5/rRztx+w5hjmgBBNYS2BydPATxCuuBnYrMNNs=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS1oZWF0cHVua3MvbkZQczRkdHBqQUhDSFEzd0ZwMnNFaEpianJYRyIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWhlYXRwdW5rcy1naXQtZml4LWhjYXAtNTJiMmE2LTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJQRU5ESU5HIiwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtaGVhdHB1bmtzLWdpdC1maXgtaGNhcC01MmIyYTYtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn19XX0=
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Building](https://vercel.com/static/status/building.svg) [Building](https://vercel.com/256-foundation-s-projects/website-heatpunks/nFPs4dtpjAHCHQ3wFp2sEhJbjrXG) | [Preview](https://website-heatpunks-git-fix-hcap-52b2a6-256-foundation-s-projects.vercel.app), [Comment](https://vercel.live/open-feedback/website-heatpunks-git-fix-hcap-52b2a6-256-foundation-s-projects.vercel.app?via=pr-comment-feedback-link) | Jul 22, 2026 2:46am |
