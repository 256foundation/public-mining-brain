# bitaxeorg/bitaxe-raw pull request #19: docs: retire main in favor of rhapd-bitaxe-gamma

> Source: https://github.com/bitaxeorg/bitaxe-raw/pull/19
> Collected: 2026-10-07
> Published: 2026-09-26

- Repository: bitaxeorg/bitaxe-raw
- Type: pull request
- Number: 19
- State: open
- Author: rkuester
- Opened: 2026-09-26
- Closed: n/a
- Labels: none

## Description

Replace the tree on `main` with a README that points Bitaxe Gamma users at [rhapd-bitaxe-gamma](https://github.com/256foundation/rhapd-bitaxe-gamma). People still build `main` and run into its toolchain problems (see #17), and nothing on `main` tells them the work has moved.

### Suggestions for the branches

These need write access, so they are suggestions, not part of this PR:

- Rename `main` to `bitaxe-gamma`. GitHub will redirect links and retarget open PRs, including this one.
- Make one of the active board branches (`bitaxeProto` or `bonanza`) the default, so the repository's front page shows current work. A line in that branch's README pointing Gamma users to rhapd-bitaxe-gamma would help visitors who come looking for the Gamma firmware.

Resolves #17.


## Comments

### rkuester on 2026-09-26

@skot please take a look.
