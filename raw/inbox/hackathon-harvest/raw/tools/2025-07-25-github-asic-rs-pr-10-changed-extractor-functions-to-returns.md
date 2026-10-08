# 256foundation/asic-rs pull request #10: Changed Extractor Functions to Returns Refs Instead of Cloning

> Source: https://github.com/256foundation/asic-rs/pull/10
> Collected: 2026-10-07
> Published: 2025-07-25

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 10
- State: closed
- Author: lurkny
- Opened: 2025-07-25
- Closed: 2025-07-25
- Labels: none

## Description

- Improved data collection module by adding documentation to clarify its usage. 

- Changed return types to `&Value`  instead of cloned values to optimize performance.  
This approach avoids unnecessary cloning in the common case of read-only access while preserving the ability to clone if mutation is needed.
