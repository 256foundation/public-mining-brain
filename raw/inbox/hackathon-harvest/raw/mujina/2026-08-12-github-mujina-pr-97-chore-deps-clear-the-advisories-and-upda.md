# 256foundation/mujina pull request #97: chore(deps): clear the advisories and update the lock

> Source: https://github.com/256foundation/mujina/pull/97
> Collected: 2026-10-07
> Published: 2026-08-12

- Repository: 256foundation/mujina
- Type: pull request
- Number: 97
- State: closed
- Author: rkuester
- Opened: 2026-08-12
- Closed: 2026-08-12
- Labels: none

## Description

The nightly audit's first run filed four advisory issues. Update anyhow, ruint, and time past their fixed releases, and address paste's advisory with a reasoned ignore: it is unmaintained with no fix, and reachable only through utoipa-axum's newest release. just audit now passes cleanly.

The series opens by letting just update-deps take crate names, the form the fix commits use, and closes with a routine whole-lock update, 153 crates moving within their ranges and the cooldown, kept separate so a regression bisects cleanly.

Closes #93, closes #94, closes #95, closes #96.
