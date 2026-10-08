# 256foundation/asic-rs pull request #3: refactor: simplify some of the factory model selection handling

> Source: https://github.com/256foundation/asic-rs/pull/3
> Collected: 2026-10-07
> Published: 2025-04-04

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 3
- State: closed
- Author: b-rowan
- Opened: 2025-04-04
- Closed: 2025-04-05
- Labels: none

## Description

This should help simplify some of the code and make the functions in the `MinerFactory` much cleaner.  I moved the `MinerModel` creation functionality to a `MinerModelFactory` which should allow dynamic construction of the model in the future if needed.  Also added Braiins OS discovery support with both the `Braiins` make and the `BraiinsOS` firmware.

## Comments

### jpcomps on 2025-04-05

Been a bit out of commission this week, but has some thoughts that followed this train of thought on how to refactor and cover all the combinations. I think this refactor has the scaffolding to do the same thing so good with this. Just to confirm from a high-level -- stage-1 we can determine which FW, and from that FW(and corresponding API) we can always determine the model. This dual-stage approach should cover any combinations and allow us make most things pretty generic, allowing to easily add any combination + more in the future. 

Will try and formalize my ideas into some sort of diagram/flow for further discussion, but this seems to closely line up with it so LGTM 👍🏻
