# 256foundation/mujina pull request #38: Add experimental Blockscale BZM2 support and diagnostics

> Source: https://github.com/256foundation/mujina/pull/38
> Collected: 2026-10-07
> Published: 2026-03-07

- Repository: 256foundation/mujina
- Type: pull request
- Number: 38
- State: closed
- Author: recklessnode
- Opened: 2026-03-07
- Closed: 2026-06-11
- Labels: none

## Description

## Summary
- add experimental Blockscale BZM2 support for generic Gen2 hardware integrations
- add the UART/TDM mining path, PLL/DLL control, DTS/VS telemetry, startup calibration, runtime tuning, chain/engine discovery, and board/API diagnostics
- add BZM2 reference documentation under `docs/bzm2`

## Scope
- focuses on reusable ASIC, board, and API behavior rather than vendor-specific carrier implementations
- excludes the internal porting conversation log from this upstream branch
- keeps Gen1-specific work out of scope
- removes upstream-only debug and virtual transport layers from this PR branch

## Cleanup Since Initial Submission
- scrubbed references to non-public/private source documents from the public BZM2 docs
- moved the Blockscale tuning planner out of `asic/bzm2` into a general tuning module
- moved rail/reset sequencing out of `asic/bzm2` into board-level power code
- removed the `bzm2-debug` binary from the upstream-scoped branch
- removed the synthetic `virtual_device` transport layer from the upstream-scoped branch
- removed the superseded `asic/bzm2/pnp.rs` and `asic/bzm2/control.rs` files
- rebased the branch onto the current upstream `main`
- corrected the BZM2 launch path so the Rust driver now programs the legacy nonce window and timestamp control register behavior expected by the ASIC

## Review Notes
This branch is rebased onto the current upstream `main` tip (`ece3334`) and has been revalidated after the rebase.

Suggested review order:
1. initial board/protocol integration through startup calibration
2. telemetry, chain discovery, and runtime engine layouts
3. docs and module-placement cleanup for upstream scope
4. the BZM2 launch-path correctness fix for nonce-window and timestamp-control programming

## Validation
Final branch validation after rebase onto upstream `main`:
- `cargo test -p mujina-miner --message-format=human`
- result: `374 passed, 0 failed, 5 ignored`
- doctests: `3 passed, 0 failed, 2 ignored`

## Follow-up Scope
A separate follow-up branch still carries the remaining parity-only work that was intentionally kept out of this core PR, including the richer BZM2 API parity and runtime tuning state surface.

## Draft Status
This PR is intentionally kept as a draft so it can be reviewed before requesting final upstream merge consideration.

## Comments

### penguin359 on 2026-03-09

This PR is in support of the feature discussed in #28. While the basic structure is in place, there is some clean-up that can be done with the Git history. I propose marking this as a draft for the time being while that is being worked on. Once that is done, I will work on a more formal code review of the results.

@recklessnode Can you try marking this as a draft? It seems I don't have that privilege.

### rkuester on 2026-03-13

Hey guys, thanks for sharing this code! Since this is a work-in-progress shared for informational purposes or early feedback and not yet ready for review and merge, I've marked it as a draft.

### recklessnode on 2026-03-16

Sorry for the delay folks, reviewing the suggestions today after several side conversations on the state of the PR, will see if I can take some of it into the plan today.

### recklessnode on 2026-03-19

@johnny9 @rkuester PR #38 has now been rebased onto the current upstream main, revalidated, and kept in draft for your review. Core branch validation: 339 passed, 0 failed, 5 ignored. The parity follow-up branch is also rebuilt and green if you want to compare the remaining delta later.

### recklessnode on 2026-04-04

Rebased update: this draft branch now sits on current upstream main (ece3334) and has been revalidated after the rebase. In addition to the earlier scope cleanup, it now includes a BZM2 launch-path correctness fix so the Rust driver programs the legacy nonce window and timestamp control behavior expected by the ASIC. Latest validation on this branch: cargo test -p mujina-miner --message-format=human -> 374 passed, 0 failed, 5 ignored with doctests 3 passed, 0 failed, 2 ignored. The separate parity follow-up branch also stays green on the same upstream base and now carries the saved-operating-point retune safety fix (404f4ab).

### recklessnode on 2026-06-11

Superseding this PR with a rebuilt series on current main: #68 (infra) → #69 (asic core) → #70 (board + tuning) → #71 (diagnostics + docs).

Since this PR was opened, main replaced the `Board` trait with the `BackplaneConnector` factory architecture (e14f3b1) and reworked the bitaxe monitor; rather than dragging this branch through that migration, the BZM2 work was re-ported onto the new architecture from scratch, split into reviewable parts, and re-verified (each part: 0 build warnings, 0 test failures). The fork's `*State` renames and the EmberOne00 stub regression from this branch were dropped in the process. Closing in favor of the series.
