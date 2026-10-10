# 256foundation/asic-rs pull request #268: feat(epic): parse summary status messages

> Source: https://github.com/256foundation/asic-rs/pull/268
> Collected: 2026-10-07
> Published: 2026-06-05

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 268
- State: closed
- Author: cfilipescu
- Opened: 2026-06-05
- Closed: 2026-06-05
- Labels: none

## Description

## Summary
- collect ePIC summary data for messages
- parse non-empty Status/Last Error as an error message
- print get_messages output in the ignored live ePIC test
- add regression coverage for summary status Last Error parsing

## Tests
- cargo test -p asic-rs-firmwares-epic
- cargo check

## Comments

### cfilipescu on 2026-06-05

> PR is good, but definitely not ideal design for how I would like to read errors. Would like to look into improving it on the firmware side if possible. One noticeable issue is that the timestamp is linked to when the data was queried, not when the error was generated, and we don't actually know if that error is still active or not.

agreed this should be improved and we can talk about it next week just to brainstorm ideas.
