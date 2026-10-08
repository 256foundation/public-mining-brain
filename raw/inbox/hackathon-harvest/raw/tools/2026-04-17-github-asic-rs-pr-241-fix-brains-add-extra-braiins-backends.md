# 256foundation/asic-rs pull request #241: fix(brains): add extra braiins backends and tests to fix issues with data in certain versions

> Source: https://github.com/256foundation/asic-rs/pull/241
> Collected: 2026-10-07
> Published: 2026-04-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 241
- State: closed
- Author: b-rowan
- Opened: 2026-04-17
- Closed: 2026-04-22
- Labels: none

## Description

Fixes a bunch of issues with intermediate versions of braiins, alongside adding tests and meta files.

I have some plans in the future to try to validate tests against the meta files, but for now this is tested and working against all the versions added.

## Comments

### b-rowan on 2026-04-17

Also, just skip `2618729d15b5b4131e6d9cb3f77ec07c22b051ad` when reviewing, it is just a reformat of the json to make them human readable.
