# 256foundation/website-heatpunks pull request #3: Fix missing top padding on 2026 summit hero (mobile)

> Source: https://github.com/256foundation/website-heatpunks/pull/3
> Collected: 2026-10-07
> Published: 2026-07-21

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 3
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-21
- Closed: 2026-07-21
- Labels: none

## Description

## Problem

On the 2026 summit archive hero, the "PAST EVENT" badge sat flush against the archive banner on small screens.

**Root cause:** the hero content container relied on `py-16 md:py-20`, but the `.section-container` class in `globals.css` sets padding via the shorthand (`padding: 0 1.5rem`), which zeroes vertical padding and beats the Tailwind utility layer (non-layered rule wins). On small screens the content is taller than `min-h-[68vh]`, so the section grew to fit it and the badge pinned to the top with no gap.

- **Desktop** looked fine regardless: `min-h-[68vh] items-end` pushes the content down, leaving space above.
- **Mobile** broke because the content overflowed 68vh.

## Fix

Add `pt-16 md:pt-20` to the `<section>` itself (which is not a `.section-container`, so the utility applies cleanly).

- **Mobile:** proper top gap above "PAST EVENT".
- **Desktop:** unchanged — the extra top padding is absorbed into the already-empty area above the flex-end content; bottom spacing untouched.

Verified in the dev preview at mobile (375px) and desktop; no console errors.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-21

[vc]: #xh3W3K5oBiBKlMXD3Acc5eUgSy5shPdqd/LEhJUBx/0=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtaGVhdHB1bmtzLWdpdC1maXgtMjAyNi01OTMxN2QtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn0sImluc3BlY3RvclVybCI6Imh0dHBzOi8vdmVyY2VsLmNvbS8yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzL3dlYnNpdGUtaGVhdHB1bmtzLzloYmI2NnFKZUpGQTF5cXdKRGVqVTdSQ2pmWjgiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS1oZWF0cHVua3MtZ2l0LWZpeC0yMDI2LTU5MzE3ZC0yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQifV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website-heatpunks/9hbb66qJeJFA1yqwJDejU7RCjfZ8) | [Preview](https://website-heatpunks-git-fix-2026-59317d-256-foundation-s-projects.vercel.app), [Comment](https://vercel.live/open-feedback/website-heatpunks-git-fix-2026-59317d-256-foundation-s-projects.vercel.app?via=pr-comment-feedback-link) | Jul 21, 2026 6:51pm |
