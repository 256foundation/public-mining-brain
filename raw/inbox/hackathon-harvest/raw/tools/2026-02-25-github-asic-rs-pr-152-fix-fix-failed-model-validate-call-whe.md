# 256foundation/asic-rs pull request #152: fix: fix failed `model_validate` call when calling `get_data` from python

> Source: https://github.com/256foundation/asic-rs/pull/152
> Collected: 2026-10-07
> Published: 2026-02-25

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 152
- State: closed
- Author: b-rowan
- Opened: 2026-02-25
- Closed: 2026-02-26
- Labels: none

## Description

This occurred on any data including `HashRate`, since the latest version of maturin seems to break `BeforeValidator` from pydantic in annotations.
