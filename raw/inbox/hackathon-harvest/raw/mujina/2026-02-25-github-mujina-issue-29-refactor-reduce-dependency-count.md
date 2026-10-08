# 256foundation/mujina issue #29: refactor: reduce dependency count

> Source: https://github.com/256foundation/mujina/issues/29
> Collected: 2026-10-07
> Published: 2026-02-25

- Repository: 256foundation/mujina
- Type: issue
- Number: 29
- State: closed
- Author: rkuester
- Opened: 2026-02-25
- Closed: 2026-08-31
- Labels: contributor-friendly

## Description

An audit in [discussion #8][discussion] identified dependencies that can be removed or replaced with small amounts of custom code. Taken together, these changes could cut roughly half of our transitive crates.

Each removal is independent and makes a good self-contained PR. Pick a dependency from the audit, remove it (replacing with custom code if needed), run `just checks`, and open a PR. The dead dependencies are trivial and could all go in a single PR.

For removals that are debatable (e.g., replacing `num-traits` with manual IEEE 754 bit extraction), check in on the discussion first so we can agree it's worth doing before you write code.

[discussion]: https://github.com/256foundation/mujina/discussions/8#discussioncomment-12740989

## Comments

### jayrmotta on 2026-03-12

Should this now be considered resolved?

### rkuester on 2026-03-13

I left it open for now, because only the lowest hanging fruit from discussion #8 was picked in PR #32. There's still some left on the middle branches for those looking for a good first issue.
