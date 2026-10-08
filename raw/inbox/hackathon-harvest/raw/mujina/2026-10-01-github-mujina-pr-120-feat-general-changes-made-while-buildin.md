# 256foundation/mujina pull request #120: feat: general changes made while building BZM2 support

> Source: https://github.com/256foundation/mujina/pull/120
> Collected: 2026-10-07
> Published: 2026-10-01

- Repository: 256foundation/mujina
- Type: pull request
- Number: 120
- State: open
- Author: recklessnode
- Opened: 2026-10-01
- Closed: n/a
- Labels: none

## Description

Four fixes found and made while building the BZM2 driver (#117), none of them BZM2-specific. Each
is useful with or without #117 landing first; they are only sequenced after it here because that
is the branch they were made on.

**Depends on #117. Its first 22 commits are #117's; review only the last 4.** Followed by #121.

## Commits (the last 4 are this PR's own)

| commit | title | first user |
|---|---|---|
| `f0aa130` | fix(serial): close the descriptor when a stream is dropped | every `SerialStream` consumer that reopens a port after a drop — the leak previously forced `EBUSY` on the reopen |
| `83a215e` | feat(api): route fan targets to boards through a command channel | `PATCH /boards/{name}/fans/{fan}`, which existed with nothing behind it until this commit gives it a sender |
| `35ddaff` | refactor(scheduler): assign a job one slice at a time | the scheduler's existing per-template job-assignment dispatch, which now calls `assign_template`/`assign_slice` instead of one inline loop (no behaviour change; the chain-staggering commits in PR 3 are its next callers) |
| `02820ec` | feat(daemon): add an observer mode | anyone starting the daemon with `MUJINA_OBSERVE` set — a read-only attach-and-enumerate mode with no job source and a paused scheduler |

None of the eight review findings on #117 applies to these four.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012tKbAMHoFAEgGVb8PenGTV
