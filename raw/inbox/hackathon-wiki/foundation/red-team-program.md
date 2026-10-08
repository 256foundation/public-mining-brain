# Red Team Program

> Sources: 256 Foundation GitHub (256-RedTeam-Public README), collected 2026-10-07; 256 Foundation (our-work page), collected 2026-10-07; 256 Foundation (newsroom: It's Time to Commoditize Bitcoin Mining), collected 2026-10-07
> Raw: [256-RedTeam-Public README](../../raw/foundation/github-256foundation-256-redteam-public.md); [256foundation.org our work](../../raw/foundation/256foundation-org-our-work.md); [newsroom: Presidio Bitcoin fundraiser](../../raw/foundation/256foundation-org-newsroom-presidio-bitcoin-fundraiser.md)
> Updated: 2026-10-07

## Overview

The 256 Red Team reverse engineers closed mining firmware and mining infrastructure, then discloses what it finds. Its job, in its own words, is to find out how mining firmware and pool infrastructure behave "when nobody's watching": hidden fees, backdoors, skimming, anti-tamper mechanisms, and undocumented failure modes. It keeps a public GitHub repo for write-ups and tooling that are ready to share, and an internal repo for day-to-day work.

## Where it sits in the foundation

The foundation's our-work page lists the Red Team Program as one of the programs that follow the core projects. It defines it as reverse engineering closed firmware and other mining software, followed by responsible disclosure. The Presidio fundraiser post describes it as publishing what is inside the closed firmware most of the industry runs on.

## The public repo

The repo is called 256-RedTeam-Public. Raw evidence, device sheets, firmware inventories and internal runbooks stay in an internal repo. The public one carries sanitized material that other teams can reuse.

| Area | What is there |
|---|---|
| Lab setup | A guide to building your own red-team cage: an isolated, fully observed miner lab. It covers network separation, router configuration, power control, environmental monitoring, remote access, a parts list and build order. |
| Findings | Sanitized findings and disclosure write-ups. The README says these will be published after human review and coordinated disclosure. |
| Harnesses and tooling | Test harnesses and capture and analysis tooling worth reusing. |
| Agent playbooks | How the team runs mixed human and AI-agent investigations: operating rules, safety policies, and prompt and skill patterns. |

## Ground rules

- **It tests hardware it owns.** All live testing happens on the team's own lab hardware in an isolated environment. Its AI agents may analyze offline artifacts freely but never attack devices without explicit operator authorization.
- **Safety first.** The README describes a miner as "a 3 kW space heater with network services". Every lab operation is classed as either *always safe* (read-only, unattended) or *attended-only* (anything that can change fans, clocks, voltage, flash or process state). The automation enforces the split.
- **Disclosure is human-gated.** Humans verify each finding, and vendors are told before any public write-up appears.
- **Evidence or it didn't happen.** Each published claim carries affected versions and hashes, reproduction steps, artifact references, and a confidence label: `confirmed`, `probable` or `suspected`.

## See Also

- [256 Foundation: Mission and Organization](mission-and-organization.md)
- [Presidio Bitcoin Fundraiser and the Case for Commoditizing Mining](presidio-bitcoin-fundraiser.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
