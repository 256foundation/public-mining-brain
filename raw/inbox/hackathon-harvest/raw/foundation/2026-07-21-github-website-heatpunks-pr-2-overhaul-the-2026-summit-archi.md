# 256foundation/website-heatpunks pull request #2: Overhaul the 2026 summit archive page

> Source: https://github.com/256foundation/website-heatpunks/pull/2
> Collected: 2026-10-07
> Published: 2026-07-21

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 2
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-21
- Closed: 2026-07-21
- Labels: none

## Description

## Summary
- Rebuilds `/summit/2026` into a polished, past-tense archive with its own yellow 2026 visual identity (thermal-camera hero, "PAST EVENT" badge), following the same pattern as the recent 2025 archive redesign. Spec: `SPEC-summit-2026-redesign.md`.
- Fixes real bugs: the stale blinking "STATUS: CONCLUDED" hero field, and the hero button opening the retired `InvitationModal` instead of `WaitlistModal`.
- New Milestones section correctly frames Hashrate Heatpunks becoming a formal 256 Foundation community project (Tyler Stevens named board president) and the first Heatpunk Innovation Award (Snorkel × Hashrate House) — also corrects the same factual error ("256 Foundation was announced at HPS 2026") that had crept into the 2027 page.
- Merges Workshops + Topics into one section with all 5 real 2026 workshops; adds a new 2026-only embedded full schedule; removes Venue & Travel per feedback; reframes Sponsors as a thank-you with a cross-year CTA.
- Deletes 9 now-orphaned components (CTASection, HighlightsSection, InfoDeckCarousel, InfoDeckSection, InvitationModal, Map, TopicsSection, VenueSection, WhyWhoSection).
- Unrelated prior polish bundled as its own commit: sequential homepage section-tag renumbering, a few homepage copy tweaks, and a header style tweak — all pre-existing uncommitted work found in the tree, unrelated to the archive overhaul.

## Test plan
- [x] `npx tsc --noEmit` clean
- [x] `npm run build` clean, all summit routes present
- [x] Verified `/summit/2026` in browser preview at mobile/tablet/desktop, light/dark mode
- [x] Confirmed `/summit`, `/summit/2025`, `/summit/schedule` render unchanged, no console errors
- [x] Clicked every link on `/summit/2026` (26 links) — all valid, footer "HPS 2027 →" CTA verified end-to-end

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-21

[vc]: #fjHS79ju+Z29RqnqI10MaT/gX4Berf4wkugxvaa0HhY=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS1oZWF0cHVua3MvOG9KYkJ5N1FYeENDWXROc1JFOXE4S0JobnBzTCIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWhlYXRwdW5rcy1naXQtc3VtbWl0LTItMWI5OTExLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJERVBMT1lFRCIsImxpdmVGZWVkYmFjayI6eyJyZXNvbHZlZCI6MCwidW5yZXNvbHZlZCI6MCwidG90YWwiOjAsImxpbmsiOiJ3ZWJzaXRlLWhlYXRwdW5rcy1naXQtc3VtbWl0LTItMWI5OTExLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCJ9LCJyb290RGlyZWN0b3J5IjpudWxsfV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website-heatpunks/8oJbBy7QXxCCYtNsRE9q8KBhnpsL) | [Preview](https://website-heatpunks-git-summit-2-1b9911-256-foundation-s-projects.vercel.app), [Comment](https://vercel.live/open-feedback/website-heatpunks-git-summit-2-1b9911-256-foundation-s-projects.vercel.app?via=pr-comment-feedback-link) | Jul 21, 2026 5:55pm |
