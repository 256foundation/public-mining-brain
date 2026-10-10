# 256foundation/emberone00-pcb issue #3: Ramp Capacitors need better tolerance

> Source: https://github.com/256foundation/emberone00-pcb/issues/3
> Collected: 2026-10-07
> Published: 2024-10-29

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 3
- State: open
- Author: skot
- Opened: 2024-10-29
- Closed: n/a
- Labels: bug

## Description

C6 and C10 (Cramp1 and Cramp2 in Webench) need to be 5% C0G NP0 capacitors. I failed to pick those. `399-C0805C821J5GAC7800CT-ND` seems like a good choice

> The value of ramp capacitor (CRAMP) must be less than 2 nF to allow full discharge between cycles by the discharge switch internal to the LM25119 device . A good-quality, thermally-stable ceramic capacitor with 5% or less tolerance is recommended. For this design the value of CRAMP was set at the standard capacitor value of 820 pF.
