# 256foundation/hydrapool issue #40: Pplns API returns empty array

> Source: https://github.com/256foundation/hydrapool/issues/40
> Collected: 2026-10-07
> Published: 2026-02-03

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 40
- State: closed
- Author: djkazic
- Opened: 2026-02-03
- Closed: 2026-02-19
- Labels: none

## Description

Running 2.2.2 binaries.
However, I can see valid shares being submitted. Am I misunderstanding the purpose of this API endpoint?

## Comments

### pool2win on 2026-02-19

We discontinued saving the PPLNS share recently for the telehash. Just wanted to avoid any slowdowns during the event. Will be bringing them back soon. Most likely as a crate feature.
