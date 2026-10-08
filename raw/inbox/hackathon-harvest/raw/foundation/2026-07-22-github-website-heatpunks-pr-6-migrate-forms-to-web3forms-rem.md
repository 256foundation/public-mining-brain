# 256foundation/website-heatpunks pull request #6: Migrate forms to Web3Forms, remove SMTP backend

> Source: https://github.com/256foundation/website-heatpunks/pull/6
> Collected: 2026-10-07
> Published: 2026-07-22

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 6
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-22
- Closed: 2026-07-22
- Labels: none

## Description

## Summary
- Contact form and summit waitlist now submit directly from the browser to Web3Forms (each with its own access key) instead of through a Nodemailer/SMTP backend, with an embedded hCaptcha widget and honeypot field for spam protection.
- Removed `lib/email.ts`, `/api/contact`, `/api/summit-invitation`, and the `nodemailer` dependency — no server-side email path remains.
- Updated the site's contact email everywhere (footer, FAQ, sponsor links) from `admin@heatpunks.org` to `tyler@256foundation.org` via `siteConfig.contact.email`.
- Refreshed `.env.example`, `CLAUDE.md`, `README.md`, `Dockerfile`, and `docker-compose.yml` for the new setup, and cleaned up stale SMTP/Proton Mail references (`docker-compose.yml` had dead `CONTACT_EMAIL`/`GRANTS_EMAIL`/`SUMMIT_EMAIL` vars that no code ever read).
- Added 2027 summit travel guidance to the event details section (fly in Thursday/leave Sunday, or Wednesday for the optional ski day).

## Test plan
- [x] `npm run build`, `npm run lint`, `npm run test` all pass
- [x] Verified both forms in the browser: contact form and waitlist modal each render their hCaptcha widget and submit with the correct dedicated Web3Forms access key
- [x] `NEXT_PUBLIC_WEB3FORMS_CONTACT_ACCESS_KEY` / `NEXT_PUBLIC_WEB3FORMS_WAITLIST_ACCESS_KEY` already added to Vercel project settings
- [ ] Confirm on production after merge: submit both forms live, confirm hCaptcha completes (couldn't fully validate on localhost due to domain restriction) and notification emails land in `tyler@256foundation.org`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-22

[vc]: #5iFoKl2orncnyHOIi5PPlGdlpYmSg1jnhMnyTJhRYWM=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS1oZWF0cHVua3MvQnlGdVBNdDJoTVEyWVo1ZUZEblg1YVE1Sm5XaCIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWhlYXRwdW5rcy1naXQtY29uc29saWQtNzJmZGVhLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJQRU5ESU5HIiwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtaGVhdHB1bmtzLWdpdC1jb25zb2xpZC03MmZkZWEtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn19XX0=
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Building](https://vercel.com/static/status/building.svg) [Building](https://vercel.com/256-foundation-s-projects/website-heatpunks/ByFuPMt2hMQ2YZ5eFDnX5aQ5JnWh) | [Preview](https://website-heatpunks-git-consolid-72fdea-256-foundation-s-projects.vercel.app), [Comment](https://vercel.live/open-feedback/website-heatpunks-git-consolid-72fdea-256-foundation-s-projects.vercel.app?via=pr-comment-feedback-link) | Jul 22, 2026 2:35am |
