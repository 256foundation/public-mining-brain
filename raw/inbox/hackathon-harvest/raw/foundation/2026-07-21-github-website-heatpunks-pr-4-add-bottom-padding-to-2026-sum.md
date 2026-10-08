# 256foundation/website-heatpunks pull request #4: Add bottom padding to 2026 summit hero stats on mobile

> Source: https://github.com/256foundation/website-heatpunks/pull/4
> Collected: 2026-10-07
> Published: 2026-07-21

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 4
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-21
- Closed: 2026-07-21
- Labels: none

## Description

## Problem

On small screens the hero stats bar (`150+ ATTENDEES … 6 SPONSORS`) sat flush against the bottom edge of the hero section, with no breathing room before the next section.

Same root cause as the top-gap fix (#3): `.section-container` sets padding via the shorthand (`padding: 0 1.5rem`), zeroing the vertical `py-*` utility. On mobile the content is taller than `min-h-[68vh]`, so the section grows to fit it and the stats pin to the bottom.

## Fix

Add `pb-16 md:pb-0` to the `<section>`.

- **Mobile:** 64px gap below the stats.
- **Desktop (≥768px):** `md:pb-0` keeps padding-bottom at `0`, so the flush `items-end` layout is unchanged.

Verified in the dev preview at 375px (64px gap) and 1280px (padding-bottom `0`); no console errors.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-21

[vc]: #XXjTHeKwL3PiaR7DmdtIGFvt6juJPB2U2WiTj9tT7o8=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS1oZWF0cHVua3MvM1h0aWNiWU5uWTZmcUFZREppU1ZmZnplNzViRiIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWhlYXRwdW5rcy1naXQtZml4LTIwMjYtYTNmNjUxLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJERVBMT1lFRCIsImxpdmVGZWVkYmFjayI6eyJyZXNvbHZlZCI6MCwidW5yZXNvbHZlZCI6MCwidG90YWwiOjAsImxpbmsiOiJ3ZWJzaXRlLWhlYXRwdW5rcy1naXQtZml4LTIwMjYtYTNmNjUxLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCJ9LCJyb290RGlyZWN0b3J5IjpudWxsfV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website-heatpunks/3XticbYNnY6fqAYDJiSVffze75bF) | [Preview](https://website-heatpunks-git-fix-2026-a3f651-256-foundation-s-projects.vercel.app), [Comment](https://vercel.live/open-feedback/website-heatpunks-git-fix-2026-a3f651-256-foundation-s-projects.vercel.app?via=pr-comment-feedback-link) | Jul 21, 2026 6:56pm |
