# 256foundation/mujina pull request #13: Adding github actions related functionality

> Source: https://github.com/256foundation/mujina/pull/13
> Collected: 2026-10-07
> Published: 2026-01-10

- Repository: 256foundation/mujina
- Type: pull request
- Number: 13
- State: closed
- Author: jbride
- Opened: 2026-01-10
- Closed: 2026-03-11
- Labels: none

## Description

Updated to merge cleanly into main branch.

Documentation regarding this github action related functionality found [here](https://github.com/jbride/mujina/blob/gh_actions/docs/hybrid-ci-setup.md) .

## Comments

### rkuester on 2026-03-11

Thanks for getting this started, @jbride. I decided to scale this back to a smaller initial step and build it around the justfile, which didn't exist yet when you opened this. See #44.

Between that and the other things I ended up doing differently, there was enough divergence that I started it as a separate PR rather than piling changes onto yours.

Please take a look at #44 and comment if anything jumps out. The ideas here in #13 around self-hosted runners and hardware testing are worth revisiting as future work.

I'm going to close this one in favor of #44.
