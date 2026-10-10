# 256foundation/mujina pull request #5: Adding github actions related functionality

> Source: https://github.com/256foundation/mujina/pull/5
> Collected: 2026-10-07
> Published: 2025-10-23

- Repository: 256foundation/mujina
- Type: pull request
- Number: 5
- State: closed
- Author: jbride
- Opened: 2025-10-23
- Closed: 2025-11-15
- Labels: none

## Description

1. provides github actions for automated CI testing in both github and local environments
2. tests run in a linux container using podman
3. targets both x86_64 and aarch64
4. in local environment, can optionally provide SSH details to a remote aarch64 environment (ie:  pi4) and run:  minerd --help
5. this pull requests also includes a few minor fixes to existing Mujina code that was failing clippy tests

## Comments

### rkuester on 2025-11-15

Looks like this was automatically closed, because I've removed the branch it was based on. I will still merge this into the new main branch, shortly.
