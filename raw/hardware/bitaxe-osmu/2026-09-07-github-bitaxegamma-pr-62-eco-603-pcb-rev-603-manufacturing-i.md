# bitaxeorg/bitaxeGamma pull request #62: ECO-603: PCB rev 603 + manufacturing (impl)

> Source: https://github.com/bitaxeorg/bitaxeGamma/pull/62
> Collected: 2026-10-07
> Published: 2026-09-07

- Repository: bitaxeorg/bitaxeGamma
- Type: pull request
- Number: 62
- State: open
- Author: Gkasgd
- Opened: 2026-09-07
- Closed: n/a
- Labels: none

## Description

ECO-603: re-layout PCB rev 603 + esquematicos + fabricacion.

Hereda el intento 602 revertido y aplica fixes de hardware (ver docs/eco-603/ en PR #61):
- E0: replica exacta 602 (sin R21, U9.8->1V2, U9.9->GND); E1: SYNC/BCX->AGND
- Sin R35/C61 (redundantes); D2 USBLC6 -> 2x PESD5V0S1BL (D2+D5); C60 1210; C62 nuevo
- Re-layout: F1/D1/C60, pull-ups R30-R32, ESD D3/D4, R33/R34, USB D+/D-, 3V3 por salto F.Cu

Verificacion: kicad-cli pcb drc --refill-zones -> 5 violaciones = base preexistente, 0 nuevas, 0 unconnected. ERC 19 err (solo +PVIN benigno por F1 en serie).
Manufacturing regenerado (Gerbers/.drl/BOM/PDF). iBOM html pendiente (no regenerable con kicad-cli).

Rama base de este PR: main. Docs del ECO en PR #61 (docs-only).
