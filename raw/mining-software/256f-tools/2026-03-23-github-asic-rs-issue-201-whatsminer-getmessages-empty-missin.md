# 256foundation/asic-rs issue #201: WhatsMiner: GetMessages empty/missing message text for V2 and V3 backends

> Source: https://github.com/256foundation/asic-rs/issues/201
> Collected: 2026-10-07
> Published: 2026-03-23

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 201
- State: closed
- Author: ankitgoswami
- Opened: 2026-03-23
- Closed: 2026-04-01
- Labels: none

## Description

## Problem

WhatsMiner V3 and V2 backends do not return useful error messages from `GetMessages`, making it impossible for consumers to classify or display miner errors properly.

### WhatsMiner V3

`GetMessages` is an empty impl that returns no messages at all:

```rust
impl GetMessages for WhatsMinerV3 {}
```

### WhatsMiner V2

`parse_messages` extracts error codes and timestamps but sets the `message` field to an empty string:

```rust
messages.push(MinerMessage {
    timestamp: ts,
    code: code.parse::<u64>().unwrap_or(0),
    message: "".to_string(),  // always empty
    severity: MessageSeverity::Error,
})
```

## Impact

Consumers relying on `MinerData.messages` to classify errors (e.g. fan failure, PSU fault, over-temperature) get either no messages (V3) or messages with empty text (V2). This means error UIs show "Unknown error" instead of actionable descriptions like "Power input voltage is lower than 230V for high power mode."

For reference, pyasic handles this by maintaining a lookup table that maps WhatsMiner numeric error codes to human-readable descriptions.

## Expected behavior

- V3: `GetMessages` should parse error data from the V3 API response (the API does return error information)
- V2: `parse_messages` should map known error codes to descriptive message strings, or at minimum include the raw error code in the message text so consumers can display something useful

## V1 reference

WhatsMiner V1 also has a `parse_messages` impl. Worth checking if it has the same empty-message issue.
