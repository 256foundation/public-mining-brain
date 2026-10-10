# 256foundation/mujina pull request #104: chore(deps): update h2 to 0.4.19

> Source: https://github.com/256foundation/mujina/pull/104
> Collected: 2026-10-07
> Published: 2026-08-25

- Repository: 256foundation/mujina
- Type: pull request
- Number: 104
- State: closed
- Author: j-kon
- Opened: 2026-08-25
- Closed: 2026-09-04
- Labels: none

## Description

## Summary

Updates the transitive `h2` dependency from 0.4.15 to 0.4.19 to
resolve RUSTSEC-2026-0258.

The update was performed with the project's dependency tooling after
the seven-day dependency cooldown expired.

## Exposure

The vulnerable HTTP/2 path is not reached in Mujina's default setup.
The REST API server speaks HTTP/1, while the CLI can negotiate HTTP/2
when pointed at an HTTPS URL. Mining pool connections use Stratum over
raw TCP and are unaffected.

## Verification

- reproduced RUSTSEC-2026-0258 with `just audit` before the update
- updated `h2` using `just update-deps h2`
- `just audit` passes after the update
- `just checks` passes
- `git diff --check` passes

`just ci` was not run locally because Podman is not installed.

Closes #101

## Comments

### rkuester on 2026-08-31

Thanks for this @j-kon. I'm intentionally dragging my feet on this since our intended 7-day cooldown period hasn't passed yet for h2 v0.4.19. If you ran `just update-deps h2`, you did the right thing; however, it appears there's a bug in `cargo-cooldown` which skipped the cooldown 🤦.

### j-kon on 2026-08-31

> Thanks for this @j-kon. I'm intentionally dragging my feet on this since our intended 7-day cooldown period hasn't passed yet for h2 v0.4.19. If you ran `just update-deps h2`, you did the right thing; however, it appears there's a bug in `cargo-cooldown` which skipped the cooldown 🤦.

Thanks for clarifying. Yes, I used just update-deps h2. I’ll leave the PR as-is until the full seven-day cooldown for 0.4.19 has elapsed. I’m also happy to reproduce the cargo-cooldown behavior separately and report it upstream if that would be useful.

### rkuester on 2026-08-31

>  I’m also happy to reproduce the cargo-cooldown behavior separately and report it upstream if that would be useful.

Yes, please. My guess is that it's related to `h2` being a transitive dependency instead of a direct dependency (i.e., listed in our Cargo.toml). While `h2` is about to exit our 7-day cooldown, you should be able to reproduce the behavior easily by setting a longer cooldown.

### rkuester on 2026-09-04

@j-kon, thanks again. Now that h2 0.4.19 has aged past the cooldown, I'm merging this. I force-pushed a cleanup to your branch: the lockfile edit is now built by the new `just update-dep h2` from #109, which avoids a cargo bug (rust-lang/cargo#5529) that created unnecessary windows-sys changes in the earlier diff.
