# 256foundation/asic-rs pull request #94: bug: fix wm V1 having newlines in some responses

> Source: https://github.com/256foundation/asic-rs/pull/94
> Collected: 2026-10-07
> Published: 2025-10-20

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 94
- State: closed
- Author: b-rowan
- Opened: 2025-10-20
- Closed: 2025-10-21
- Labels: none

## Description

Example response which was causing this - 
```
&response = "{\"STATUS\":\"S\",\"When\":1760998397,\"Code\":131,\"Msg\":{\"api_ver\":\"whatsminer v1.4.0\",\"fw_ver\":\"20210322.22.REL\n\"},\"Description\":\"whatsminer v1.4.0\"}"
```

Specifically the newline in `fw_ver`.
