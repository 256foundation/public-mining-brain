# 256foundation/asic-rs pull request #47: feature: add release github action on tags

> Source: https://github.com/256foundation/asic-rs/pull/47
> Collected: 2026-10-07
> Published: 2025-08-18

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 47
- State: closed
- Author: b-rowan
- Opened: 2025-08-18
- Closed: 2025-08-18
- Labels: none

## Description

(no description)

## Comments

### b-rowan on 2025-08-18

> Approved. Just keep in mind we need to make sure to bump the version in Cargo.toml on the tag. I think we can automate this with cargo workspace

Not sure how to do this, you have any examples?

### jpcomps on 2025-08-18

So two ways I think. @s0kil and @lurkny can comment. So you want to tag the repo, but also need to bump the version inside Cargo.toml.

I believe you can run, cargo workspaces version -- this will auto walk you through updating the toml file as well as generate the git tags and push. From there this action should be valid cause will guarantee the version is different.
