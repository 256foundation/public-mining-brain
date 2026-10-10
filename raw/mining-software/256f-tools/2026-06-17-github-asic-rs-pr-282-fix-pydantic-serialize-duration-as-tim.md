# 256foundation/asic-rs pull request #282: fix(pydantic): serialize Duration as timedelta, not float

> Source: https://github.com/256foundation/asic-rs/pull/282
> Collected: 2026-10-07
> Published: 2026-06-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 282
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-17
- Closed: 2026-06-18
- Labels: none

## Description

### Problem
`MinerData` fields typed `Option<Duration>` (notably `uptime`) are serialized to Python as a **bare float (seconds)**: `to_pydantic_data` calls `duration_to_seconds()` and the serialization schema is `float_schema`. Consumers that treat the value as a duration crash:

```
'float' object has no attribute 'total_seconds'
```

This is also **inconsistent within the library**:
- `from_pydantic` already accepts a `timedelta` (it's the first form in its own error message: *"Expected duration as timedelta, …"*).
- The `Miner.get_uptime()` method already returns `Optional[datetime.timedelta]` (its docstring says so).

So only the `MinerData.uptime` **field** comes through as a float, while the equivalent method returns a `timedelta`.

### Fix
Emit a `datetime.timedelta` from `to_pydantic_data` (pyo3 converts `std::time::Duration` natively) and use `timedelta_schema` for serialization. `from_pydantic` is unchanged and still accepts `timedelta`, non-negative seconds, or `{secs}` dict — so existing inputs keep working; only the output type becomes the (already-expected) `timedelta`.

### Verified
Built a wheel with this change and ran it under Home Assistant against a live miner (BraiinsOS S19k Pro). Before: the `uptime` sensor crashed every update with the `total_seconds` error. After: `uptime` populates normally (e.g. `1308 s`) and no errors in the log; other fields unaffected.

### Note
This changes the serialized type of all `Duration` fields from `float` to `timedelta`. That's the type `from_pydantic`/`get_uptime` already imply, but flagging it in case any consumer relied on the float form.

## Comments

### pos-ei-don on 2026-06-18

Quick question on direction here, since there's an internal inconsistency I'd rather you decide on than assume:

- The `uptime` **type stub** declares `timedelta | None`, and the **`get_uptime()` method** returns a `timedelta` (its docstring even says so).
- But the **pydantic field** serialized a `Duration` as a bare **float (seconds)** — and there was a test (`test_miner_data_serializes_uptime_seconds`) asserting exactly that.

So the declared/typed contract (timedelta) and the runtime serialization (float) disagree. This PR resolves it toward **timedelta** (and I updated the test accordingly), which also matches how the sibling rich types serialize as structured objects rather than bare scalars.

But it's your call — two clean options:
1. **timedelta** (this PR): field matches the stub + `get_uptime()`; consumers can use `.total_seconds()`.
2. **float seconds** (your existing test): keep the serialization, and I'll drop this PR and adjust the downstream consumer to read the float instead.

Happy to go either way — just didn't want to silently flip a behavior you'd written a test for. Which do you prefer?

### b-rowan on 2026-06-18

I think this is the right direction, time delta seems like the right way to represent it.  There may be a situation where we want to implement `model_dump_json` where this might get more difficult (because we would need to dump duration to a float there, then ensure we can still load it), but for now this makes sense.

### pos-ei-don on 2026-06-18

Thanks — agreed, `timedelta` keeps it symmetric with the stub and `get_uptime()`. Re your `model_dump_json` note: that's a separate, future concern (we'd convert the Duration to seconds on dump and parse it back on load) and doesn't block this change. I kept the small `impl` since removing it drops back to the bare-float serialization. Ready to merge whenever you're happy with it.
