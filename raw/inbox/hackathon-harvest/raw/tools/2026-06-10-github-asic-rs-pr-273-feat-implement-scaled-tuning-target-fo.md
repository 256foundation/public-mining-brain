# 256foundation/asic-rs pull request #273: feat: implement scaled tuning target for braiins

> Source: https://github.com/256foundation/asic-rs/pull/273
> Collected: 2026-10-07
> Published: 2026-06-10

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 273
- State: closed
- Author: b-rowan
- Opened: 2026-06-10
- Closed: 2026-06-10
- Labels: none

## Description

The current implementation for the newer REST API based backends was using scaled tuning target as the tuning target, which could cause some confusion.

For example, if the power limit was set to 3kw, and scaling had backed it off to 2.4kw, it would show the tuning target as 2.4kw, which was only partially correct.

## Comments

### b-rowan on 2026-06-10

Fixing tests then ill merge.
