# 256foundation/website pull request #46: Projects: tighten Mujina firmware copy

> Source: https://github.com/256foundation/website/pull/46
> Collected: 2026-10-07
> Published: 2026-10-04

- Repository: 256foundation/website
- Type: pull request
- Number: 46
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-04
- Closed: 2026-10-04
- Labels: none

## Description

## Summary
Two copy edits in the Mujina firmware section on /projects, from review annotations.

## Changes (`data/projects.ts`)
- **Closed problem**: now names the failure rather than repeating "unauditable":
  > Firmware is the operating system of a miner. Closed options are un-auditable, unmodifiable and take license fees. You cannot verify they aren't skimming hashrate, phoning home, or holding a remote kill switch.
- **Open answer**: last sentence ends on "source they can actually verify" instead of "trust".

## Verification
- `npx tsc --noEmit` clean, `npm run lint` clean, `node --test tests` 51/51 pass
- Both strings verified in the rendered /projects HTML
