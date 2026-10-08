# 256foundation/asic-rs pull request #408: feat(antminer): add S21/S23 hydro models and aliases

> Source: https://github.com/256foundation/asic-rs/pull/408
> Collected: 2026-10-07
> Published: 2026-10-07

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 408
- State: closed
- Author: dtyg0d
- Opened: 2026-10-07
- Closed: 2026-10-07
- Labels: none

## Description

Superseded by #409, which carries the identical model-only diff on a clean commit history. This PR remains available as the review record.

Stock S21 XP Hyd, S21j XP Hyd and S23 Hyd labels previously fell back to unknown models. This change adds distinct SHA256 model identities and exact aliases, with regression tests that preserve unknown identities for unconfirmed variants. Existing model parsing behavior is unchanged.

S21 XP Hyd records the three hashboards documented in BITMAIN's user guide, with chip counts left unknown. S21j XP Hyd and S23 Hyd board/chip counts remain unknown until supported by real telemetry or manufacturer documentation. No telemetry parser, schema, binding, packaging or control changes are included in this PR; those changes are retained separately in the fork.

Validation: 11 Antminer model/hardware tests passed; Rust formatting and generated supported-device documentation checks passed. These checks do not establish live telemetry or control compatibility.

Hardware reference: https://file12.bitmain.com/shop-product-s3/firmware/6ced87e3-bfee-4525-ab66-4ac67d342398/2025/02/27/17/S21%20XP%20Hyd.%20User%20Guide-V4.0.17.pdf (section 1.2).
