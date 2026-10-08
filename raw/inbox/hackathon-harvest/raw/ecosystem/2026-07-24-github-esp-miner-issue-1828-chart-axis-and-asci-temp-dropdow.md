# bitaxeorg/ESP-Miner issue #1828: Chart axis and ASCI Temp dropdown panel is clipped by the chart card's overflow: hidden

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1828
> Collected: 2026-10-07
> Published: 2026-07-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1828
- State: closed
- Author: TLausZ
- Opened: 2026-07-24
- Closed: 2026-08-06
- Labels: none

## Description

**Describe the bug**
On the Home dashboard, the two chart axis dropdowns (Y1 / Y2 data source) open a panel that is cut off. When the panel flips upward (trigger near the bottom of the viewport), its top rows are hidden behind the card edge, so options like "ASIC Temp" / "Error %" become unreadable or unreachable.

**Root cause**
The chart widget card clips the overlay. In `main/http_server/axe-os/src/app/components/home/home.component.scss`:
- `.grid-stack-item-content { overflow: hidden }` (~line 35)
- `.grid-stack-item[gs-id="chart"] .grid-stack-item-content > .card { overflow: hidden }` (~line 53)

The dropdown panel is positioned within the card, so `overflow: hidden` clips it. Note: `container-type: size` on `.grid-stack-item-content` does not clip on its own (no paint containment) — only `overflow: hidden` does.

**To Reproduce**
1. Open the AxeOS Home dashboard.
2. Click either chart axis dropdown while the chart is near the bottom of the viewport.
3. The panel opens upward and its upper options are clipped at the card border.

**Expected behavior**
The dropdown panel should overflow the card and be fully visible.

**Environment**
- Device: Bitaxe Gamma
- AxeOS / ESP-Miner: v2.14.2
- Browser: Chrome 150.0.7871.130

**Proposed fix (verified on v2.14.2)**
Let the chart widget card overflow instead of clipping:
```scss
.grid-stack-item[gs-id="chart"] .grid-stack-item-content { overflow: visible; }
.grid-stack-item[gs-id="chart"] .grid-stack-item-content > .card { overflow: visible; }
```
Tested live on v2.14.2 (which still ships the PrimeNG `p-dropdown`): the full panel becomes visible, renders cleanly above the neighbouring card, and the chart canvas below is unaffected (no spill).

**Note for `master` (post PrimeNG→Tailwind rewrite)**
`master` replaced `p-dropdown` with the custom `app-dropdown`, but the two clipping rules above are unchanged, so the same `overflow: visible` fix applies. One thing I could not verify live (the released firmware still runs the PrimeNG build): the custom `app-dropdown` panel uses only `z-50`, whereas the PrimeNG overlay had a much higher z-index. On `master` the widget may need to be lifted above its neighbours while a dropdown is open, e.g.:
```scss
.grid-stack-item[gs-id="chart"]:has(app-dropdown ul) { z-index: 100; }
```
Please verify the stacking on `master`.

**Screenshot**

<img width="2000" height="1068" alt="Image" src="https://github.com/user-attachments/assets/cfd0da01-f7d2-47ac-9982-9c341cb07277" />
