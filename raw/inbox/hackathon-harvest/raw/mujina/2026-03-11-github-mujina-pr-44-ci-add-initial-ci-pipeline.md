# 256foundation/mujina pull request #44: ci: add initial CI pipeline

> Source: https://github.com/256foundation/mujina/pull/44
> Collected: 2026-10-07
> Published: 2026-03-11

- Repository: 256foundation/mujina
- Type: pull request
- Number: 44
- State: closed
- Author: rkuester
- Opened: 2026-03-11
- Closed: 2026-03-11
- Labels: none

## Description

Add a containerized CI pipeline that runs fmt, clippy, and test on pushes to main and pull requests.

The justfile is the source of truth for what CI does. The GitHub Actions workflow is plumbing: checkout, cache, `just ci`. A contributor can run the same checks in the same container locally.

This is a first step, enough to require passing checks before merging. Future work (release automation, hardware-in-the-loop, etc.) can layer on top.

Derived in spirit from #13 by @jbride. The approach differs (build container from source, justfile as single source of truth, smaller initial scope) but the motivation is the same.
