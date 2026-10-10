# 256foundation/mujina pull request #118: refactor(bm13xx): remove bitvec dependency

> Source: https://github.com/256foundation/mujina/pull/118
> Collected: 2026-10-07
> Published: 2026-09-29

- Repository: 256foundation/mujina
- Type: pull request
- Number: 118
- State: open
- Author: SusanGithaigaN
- Opened: 2026-09-29
- Closed: n/a
- Labels: none

## Description

Following discussion #8 , `bitvec` was identified as a straightforward dependency that can be removed to prevent dependency inflation in Mujina. Currently, `bitvec` is only used to pack the BM13xx command type/flags byte and extract the response type from the final response byte. The bit-slice abstraction is unnecessary for these fixed fields; each operation reduces to shifts and masks

## Fix
Replace both uses with bitwise operations and remove `bitvec` from the workspace and miner manifests. Wire format and response handling are unchanged.

`bitvec` and its four supporting crates leave the active dependency graph. Their lockfile entries remain through optional transitive dependencies.

## Tests

Added `response_type_is_independent_of_crc_bits` to cover all 256 possible response byte values. It verifies that:

- Type 0 decodes as `ReadRegister`.
- Type 4 decodes as `Nonce`.
- All other types return `InvalidResponseType` with the correct value.
- The lower five CRC bits do not affect response type selection.

This test exercises response decoding directly; CRC validation remains covered by the existing frame codec tests. Existing capture-based tests continue to verify command encoding and response decoding.

Part of: #29 


## Comments

### SusanGithaigaN on 2026-09-29

> the commit message left me a bit confused & feels more verbose than it needs to be
> 
> i think we can make it much easier to digest by following the project's [commit convention](https://github.com/256foundation/mujina?tab=contributing-ov-file#commits). the commit message needs to give future readers a _quick_ idea of _what changed_ and _why_, while the detailed explanation of the test can live in the PR description
> 
> right now, there is quite a bit of detail about the test's implementation and individual cases (which are already clear from the diff), and that makes the actual change harder to pick out at a glance
> 
> refs:
> 
> * Mujina's commit log: https://github.com/256foundation/mujina/commits/main/
> * https://cbea.ms/git-commit/

Thank you for pointing this out. I accidentally replaced my commit message with the draft pr description provided. I've made the update now
