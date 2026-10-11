# SRI issue #1983 — Extensions negotiation, TLV, Worker-Specific Hashrate Tracking (closed)

> Source: https://github.com/stratum-mining/stratum/issues/1983
> Collected: 2026-10-10
> Published: see body
> Registry ID: sv2-repo

NUM: 1983 STATE: closed CREATED: 2025-10-30T13:50:38Z CLOSED: 2025-11-25T15:41:39Z COMMENTS: 6
TITLE: Add support for extensions negotiations, `TLV`, and `Worker-Specific Hashrate Tracking` extension
LABELS: 

This PR adds support for extensions negotiations, `TLV`, and `Worker-Specific Hashrate Tracking` extension.

A new crate called `extensions_sv2` has been created, with modules defining [Extension n.1 message types](https://github.com/stratum-mining/sv2-spec/blob/main/extensions/extensions-negotiation.md#2-messages-defined-by-this-extension), TLV encoding (as defined [here](https://github.com/stratum-mining/sv2-spec/blob/main/03-Protocol-Overview.md#341-stratum-v2-tlv-encoding-model)), and [Extension n.2](https://github.com/stratum-mining/sv2-spec/blob/main/extensions/worker-specific-hashrate-tracking.md) helper functions.

To better support and handle extension messages and TLV fields appended to existing messages, some breaking changes on `handlers_sv2` have been done:
- `Extensions negotiation`:
  - created new handler traits in `extensions.rs` to manage incoming new messages defined by extensions (for now we only have the ones defined in [Extension n.1](https://github.com/stratum-mining/sv2-spec/blob/main/extensions/extensions-negotiation.md))
- `TLV` and `Extension n.2`:
  - modified all the current handlers to accept a new parameter for optional TLV fields appended to the current messages
  - added a new method to all current handlers called `get_negotiated_extensions_with_server()` which is used by the trait methods `handle_*_message_frame_from_*` internally
 
I still need to fully validate these new changes by implementing it on some apps.

Closes #1742 
Closes #1743 

PS: integration tests are failing on CI, because this PR is introducing breaking changes in handlers, so that is perfectly expected.
