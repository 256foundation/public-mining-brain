# 256foundation/mujina pull request #66: docs: add BZM2 port engineering notes under docs/bzm2/

> Source: https://github.com/256foundation/mujina/pull/66
> Collected: 2026-10-07
> Published: 2026-06-10

- Repository: 256foundation/mujina
- Type: pull request
- Number: 66
- State: closed
- Author: recklessnode
- Opened: 2026-06-10
- Closed: 2026-07-22
- Labels: none

## Description

Relocates six BZM2 port engineering notes (port architecture, UART debug CLI guide, runtime control strategy, tuning planner note, reference roadmap, opcode grounding) into `docs/bzm2/` — their natural home alongside the code they describe.

These were previously published in the `bzm2-hwref` hardware-documentation repo, where they were misfiled among the ASIC hardware reference docs; they are firmware-side engineering history. File paths into the non-distributable legacy tree were scrubbed from the grounding note during the move.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### recklessnode on 2026-06-11

Heads-up: the BZM2 series #68 → #69 → #70 → #71 now carries these same six documents in #71, landing them together with the code they describe. To keep one source of truth, this PR is probably best closed in favor of #71 — leaving that call to the maintainers/author rather than closing it unilaterally.


### recklessnode on 2026-07-22

﻿Resolving per the 2026-06-15 dev call (discussion #73) and the proposal posted there:

- The three documents here that **describe mujina code** (port architecture, tuning-planner notes, opcode grounding) ride #71, next to the code they document.
- The **general hardware reference** now lives at its canonical home, [bzm2-hwref](https://github.com/Blockscale-Solutions/bzm2-hwref) - public, CC-BY-SA, maintained by Reckless Systems with access to the original collateral. The versions there are enriched beyond this PR's copies (electrical quick-reference table, 9-bit physical-layer section, ball-map CSV). #71's README links there.

That implements the principle from the call - nothing unmaintained in the main tree - so this PR has no remaining unique content. Thanks Ryan and Dylan for the careful framing; it produced a better structure than the original submission.
