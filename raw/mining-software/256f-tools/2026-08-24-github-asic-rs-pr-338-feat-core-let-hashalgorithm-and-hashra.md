# 256foundation/asic-rs pull request #338: feat(core): let HashAlgorithm and HashRateUnit compare against their names

> Source: https://github.com/256foundation/asic-rs/pull/338
> Collected: 2026-10-07
> Published: 2026-08-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 338
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-24
- Closed: 2026-08-25
- Labels: none

## Description

Second of three. **Stacked on #337** — that commit appears here until it merges. Review the second commit only.

## Problem

Both enums are exposed to Python as pyclasses with no `__eq__`, so `hashrate.unit == "TH/s"` evaluates to `False` rather than raising.

The existing test file shows the shape of the workaround, two lines apart:

```python
assert str(model.hashrate.unit) == "TH/s"   # enum -> str() required
assert model.hashrate.algo == "SHA256"      # str  -> compares directly
```

A silently false branch with no traceback is the worst version of this — the caller gets a wrong answer and no signal that anything went wrong.

## Change

Both enums now compare equal to another value of their own type *or* to their rendered name, so either idiom works and neither is a trap. `__hash__` is restored explicitly alongside, since defining `__eq__` drops the inherited hash and both are used as dict keys; `HashRateUnit` gains a `Hash` derive to support it.

## Why now

This is what makes #338 safe. Converting `HashRate.algo` from `String` to `HashAlgorithm` would otherwise silently break every Python caller comparing it to a string — with this in place, that conversion is a non-event for them.

It also fixes a wart that exists today, independent of the stack: `DeviceInfo.algo` is already a `HashAlgorithm`, and anyone comparing it to a string is already getting `False`.

## Tests

Verified by building the extension module and running the real suite, not by reasoning about pyo3 behaviour — **91 Python tests pass**, including new ones asserting `== "Scrypt"`, `!= "SHA256"`, `!= 17`, and that both types stay usable as dict keys.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ErTo1a4BgYptp5tC8r1oHR
