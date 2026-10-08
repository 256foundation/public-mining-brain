# 256foundation/asic-rs pull request #44: feature: Add ePIC FW and Model support

> Source: https://github.com/256foundation/asic-rs/pull/44
> Collected: 2026-10-07
> Published: 2025-08-13

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 44
- State: closed
- Author: jpcomps
- Opened: 2025-08-13
- Closed: 2025-08-14
- Labels: none

## Description

This pull request adds support for EPic miners to the codebase and refactors string formatting for better readability and maintainability. The most significant changes include the introduction of new types and logic for handling EPic miner models and APIs, as well as consistent usage of Rust's inline string interpolation.

**EPic miner support:**

* Added the `EPicModel` enum (with variants `BM520i` and `S19JProDual`) in `src/data/device/models/epic.rs` to represent EPic miner models.
* Updated the `MinerModel` and related factory logic to support the new `EPicModel`, including parsing, display, and conversion to hardware types. [[1]](diffhunk://#diff-324bf494b51cb278010eb581625eab5439106042d6258c5845c6a64f36a6bfd3R5-R13) [[2]](diffhunk://#diff-324bf494b51cb278010eb581625eab5439106042d6258c5845c6a64f36a6bfd3R61-R77) [[3]](diffhunk://#diff-324bf494b51cb278010eb581625eab5439106042d6258c5845c6a64f36a6bfd3R87) [[4]](diffhunk://#diff-324bf494b51cb278010eb581625eab5439106042d6258c5845c6a64f36a6bfd3R138-R146) [[5]](diffhunk://#diff-6f222f75b3d2ddaace5c01f80b7939650ef49bf12d8bd44ef39ae14e4934770dR98)
* Added a new `EPicWebAPI` client in `src/miners/backends/epic/web.rs` to communicate with EPic miners via HTTP, including error handling and API command execution.

**General improvements and refactoring:**

* Refactored string formatting throughout the BTMiner2 and BTMiner3 backend modules to use Rust's inline `{}` formatting for improved readability and maintainability. [[1]](diffhunk://#diff-1137d3f28c53f91727c84f89db2a71f67dbae802987ae0bfb5a8e7f28e07959eL273-R273) [[2]](diffhunk://#diff-1137d3f28c53f91727c84f89db2a71f67dbae802987ae0bfb5a8e7f28e07959eL285-R285) [[3]](diffhunk://#diff-1137d3f28c53f91727c84f89db2a71f67dbae802987ae0bfb5a8e7f28e07959eL297-R322) [[4]](diffhunk://#diff-1137d3f28c53f91727c84f89db2a71f67dbae802987ae0bfb5a8e7f28e07959eL377-R377) [[5]](diffhunk://#diff-1137d3f28c53f91727c84f89db2a71f67dbae802987ae0bfb5a8e7f28e07959eL450-R476) [[6]](diffhunk://#diff-ce9cd319bfcd9bc730017ab982f49fa5d2ddf3e1411eeb045b6f4ecfd780ef83L271-R271) [[7]](diffhunk://#diff-ce9cd319bfcd9bc730017ab982f49fa5d2ddf3e1411eeb045b6f4ecfd780ef83L280-R280) [[8]](diffhunk://#diff-ce9cd319bfcd9bc730017ab982f49fa5d2ddf3e1411eeb045b6f4ecfd780ef83L289-R312) [[9]](diffhunk://#diff-ce9cd319bfcd9bc730017ab982f49fa5d2ddf3e1411eeb045b6f4ecfd780ef83L361-R361) [[10]](diffhunk://#diff-ce9cd319bfcd9bc730017ab982f49fa5d2ddf3e1411eeb045b6f4ecfd780ef83L430-R446)
* Minor update to use inline formatting in error messages in the `RPCError` display implementation.

**Other:**

* Added an `Unknown` variant to the `MinerMake` enum to better handle unknown device makes.

## Comments

### jpcomps on 2025-08-14

Think i hit most of the comments, would appreciate a re-review. Let me know if theres anything else you see that can be improved.
