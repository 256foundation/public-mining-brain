# 256foundation/256-RedTeam-Public README

> Source: https://github.com/256foundation/256-RedTeam-Public
> Collected: 2026-10-07
> Published: Unknown

# 256 Red Team — Public

Public home for the **256 Foundation Red Team's** learnings, findings, and best
practices around red-teaming Bitcoin mining firmware and mining infrastructure.

The day-to-day work — raw evidence, device sheets, firmware inventories, internal
runbooks — lives in an internal repo. This repo carries what's ready to be public:
sanitized write-ups, build guides, harnesses, and tooling patterns that other
teams can re-use.

## What you'll find here

| Area | Status |
|---|---|
| **Lab setup** | [Build your own red-team cage](docs/build-your-own-cage.md) — the full blueprint for our isolated, fully-observed miner lab: network separation, router configuration, power control (Shelly), environmental monitoring, remote access, BOM + build order |
| **Findings** | Sanitized findings and disclosure write-ups will be published here after human review and coordinated disclosure |
| **Harnesses & tooling** | Test harnesses, capture/analysis tooling patterns, and automation worth re-using |
| **Agent playbooks** | How we run mixed human + AI-agent investigation teams: operating rules, safety policies, prompt/skill patterns |

## Ground rules

- **We test hardware we own.** All live testing happens on our own lab hardware, in an
  isolated environment. Our agents analyze offline artifacts freely but never attack
  devices without explicit operator authorization.
- **Safety first.** Mining hardware is a 3 kW space heater with network services. Every
  operation in our lab is classified *always safe* (read-only, unattended) or
  *attended-only* (anything that can change fans, clocks, voltage, flash, or process
  state) — and the automation enforces it.
- **Disclosure is human-gated.** We follow coordinated disclosure: findings are verified
  by humans and disclosed to vendors before any public write-up appears here.
- **Evidence or it didn't happen.** Every published claim carries affected versions +
  hashes, repro steps, and artifact references, with confidence labels
  (`confirmed | probable | suspected`).

## About the 256 Foundation

The [256 Foundation](https://256foundation.org) builds open infrastructure for
decentralized Bitcoin mining — open firmware, protocol tooling, and reference
implementations. The red team's job is to find out how mining firmware and pool
infrastructure behave when nobody's watching: hidden fees, backdoors, skimming,
anti-tamper mechanisms, and the failure modes nobody documented.
