# SRI issue #2393 — SupportedChannelTypes predates sv2-spec#162 (open, spec/impl divergence)

> Source: https://github.com/stratum-mining/stratum/issues/2393
> Collected: 2026-10-10
> Published: see body
> Registry ID: sv2-repo

NUM: 2393 STATE: open CREATED: 2026-09-16T20:05:02Z CLOSED: open COMMENTS: 2
TITLE: `handlers_sv2`: `SupportedChannelTypes` predates sv2-spec#162 — no variant expresses a group-mode connection with standard and/or extended channels
LABELS: 

## context A

I've been driving clankers to refactor [`sv2-cpu-miner`](https://github.com/plebhash/sv2-cpu-miner) to use crates from `stratum` and `sv2-apps` only (no more unmaintained/experimental deps)

but I want to keep the same UX... and amongst other functionalities I had implemented there, one particular is blocked by the current state of `handlers_sv2`

more specifically, this CPU miner is able to open multple channels under the same connection

this is a perfectly spec-compliant use-case, but `handlers_sv2` architecture currently forbids it

## context B

this motivated me to revisit https://github.com/stratum-mining/sv2-spec/pull/162 and evaluate how well `handlers_sv2` is catering for those changes at a conceptual level

## problem

The message dispatchers in `handlers_sv2` gate which per-message handlers are reachable based on a single `SupportedChannelTypes` value per connection (`get_channel_type_for_server` / `get_channel_type_for_client`).

The current gating table for the messages where variants disagree:

| message | `Standard` | `Extended` | `Group` | `GroupAndExtended` |
|---|---|---|---|---|
| `OpenStandardMiningChannel(.Success)` | ✅ | ❌ | ✅ | ✅ |
| `OpenExtendedMiningChannel(.Success)` | ❌ | ✅ | ❌ | ✅ |
| `NewMiningJob` | ✅ | ❌ | ❌ | ❌ |
| `NewExtendedMiningJob` | ❌ | ✅ | ✅ | ✅ |
| `SubmitSharesStandard` | ✅ | ❌ | ✅ | ✅ |
| `SubmitSharesExtended` | ❌ | ✅ | ❌ | ✅ |
| `SetGroupChannel` | ❌ | ❌ | ✅ | ✅ |

This variant set encodes the **pre**-[sv2-spec#162](https://github.com/stratum-mining/sv2-spec/pull/162) model of the protocol, where Group Channels could only contain Standard Channels — that is precisely the distinction `Group` vs `GroupAndExtended` was built around. Since https://github.com/stratum-mining/sv2-spec/pull/162 was merged, that model is outdated:

- **Group Channels contain Standard and/or Extended Channels.** Every mining channel is a group member: `OpenExtendedMiningChannel.Success` now carries a `group_channel_id` field, and `SetGroupChannel` regroups "a sequence of opened standard or extended channel IDs".
- **Group-addressed `NewExtendedMiningJob` is broadcast to *all* channels in the group**, Standard and Extended alike — it is the normative mechanism for distributing work to any mix of channels on one connection.
- **The `REQUIRES_STANDARD_JOBS` setup flag is what selects the connection mode.** Per-channel `NewMiningJob` translation of group jobs is tied to the flag, and `SetGroupChannel` "can be sent only to connections that don't have `REQUIRES_STANDARD_JOBS`".

So post https://github.com/stratum-mining/sv2-spec/pull/162 there are really only **two connection modes** on the wire:

1. **standard jobs mode** (`REQUIRES_STANDARD_JOBS` set): Standard Channels only, per-channel `NewMiningJob`, no regrouping. The SRI pool enforces the "only" part by rejecting `OpenExtendedMiningChannel` on such connections (`extended-channels-not-supported-for-standard-jobs`).
2. **group mode** (flag not set): any mix of Standard and/or Extended Channels, all members of a Group Channel; ongoing work distributed as group-addressed `NewExtendedMiningJob`; per-channel jobs still legal (the SRI pool sends a per-channel `NewMiningJob` to each Standard Channel at channel-open time); `SetGroupChannel` may regroup any of the channels.

`SupportedChannelTypes` can express mode 1 (`Standard`) but **no variant expresses mode 2 in full**: `Extended`, `Group` and `GroupAndExtended` are each partial views of it, and in particular none of them admits the per-channel `NewMiningJob` that a group-mode Standard Channel legitimately receives. A `handlers_sv2` client that opens a Standard Channel on a group-mode connection hits `unexpected_message` on a spec-compliant message; a client operating both channel kinds cannot be written at all.
### TOP COMMENTS #2393

--- @plebhash (2026-09-18T13:38:25Z):
@bit-aloo curious to hear your thoughts on this issue

more specifically, here's the patch my clanker came up with, which `sv2-cpu-miner` currently uses from my fork of `handlers_sv2`:

https://github.com/plebhash/stratum/commit/e4db109420a802443a70e645e8c50ef0a684a899

https://github.com/plebhash/sv2-cpu-miner/blob/df247e45e6212e6e32971ba33c6900b399c9dc25/Cargo.toml#L23-L28

--- @xyephy (2026-10-02T05:30:29Z):
reviewed e4db109 against sv2-spec#162. Some observations:

  1. the root cause seems to be in the existing variants rather than a missing one. [05-Mining-Protocol.md L388](https://github.com/stratum-mining/sv2-spec/blob/d8bf5b85399553762f57a0e26fa7e1a5cb72f965/05-Mining-Protocol.md#L388) makes `NewMiningJob` the mandatory first message on every standard channel, and the SRI pool sends it in group mode too. client-side `Group` and `GroupAndExtended` reject it, so with the provided dispatchers neither can host a standard channel against a compliant server. reproduced on `main` with `sv2-cpu-miner` switched to `GroupAndExtended` and `REQUIRES_STANDARD_JOBS` unset: the pool's first job fails with `unexpected message: extension_type 0, message_type 21` and nothing gets mined.

  2. widening the existing arms instead (`NewMiningJob` for `Group`/`GroupAndExtended`, and `SetGroupChannel` for `Ex
