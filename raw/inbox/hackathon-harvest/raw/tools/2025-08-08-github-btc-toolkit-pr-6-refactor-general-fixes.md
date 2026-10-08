# 256foundation/btc-toolkit pull request #6: refactor: general fixes

> Source: https://github.com/256foundation/btc-toolkit/pull/6
> Collected: 2026-10-07
> Published: 2025-08-08

- Repository: 256foundation/btc-toolkit
- Type: pull request
- Number: 6
- State: closed
- Author: b-rowan
- Opened: 2025-08-08
- Closed: 2025-08-08
- Labels: none

## Description

Lots of general fixes, completely got rid of custom theming, opting to use built-in themes (which can be changed by changing `crate::theme::THEME`), fixed a bunch of formatting issues in the UI, fixed table scrolling spacing, and recentered a bunch of stuff.

## Comments

### b-rowan on 2025-08-08

There is a "issue" with this PR, that being that multiple groups will not show up properly AFAIU on either page.  My planned solution to that is to use [`iced_aw`](https://github.com/iced-rs/iced_aw) to create tabs and use those instead of infinitely scrolling through groups.

### s0kil on 2025-08-08

Looks good for now
