# 256foundation/website pull request #45: Grants: link the funded grant log from the announcements section

> Source: https://github.com/256foundation/website/pull/45
> Collected: 2026-10-07
> Published: 2026-10-04

- Repository: 256foundation/website
- Type: pull request
- Number: 45
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-04
- Closed: 2026-10-04
- Labels: none

## Description

## Summary
On /grants, the "Funding announcements" section now links directly to the funded grant log, while keeping the newsroom link.

## Change
- `components/grants/FundingAnnouncements.tsx` sub-line: "Every grant we've funded, newest first. See the full grant log → or see more updates on our newsroom →."
  - `See the full grant log →` → `/grants/announcements`
  - `see more updates on our newsroom →` → `/newsroom`
- On the archive itself (`/grants/announcements`) the grant-log link is omitted as a self-link, leaving only the newsroom link.

## Verification
- `npx tsc --noEmit` clean, `npm run lint` clean, `node --test tests` 51/51 pass
- Checked both renders: preview shows both links, archive shows only the newsroom link
