# bitaxeorg/ESP-Miner issue #1194: Development builds -- v2.10.0b2 & v2.10.0b2-1-g36664d0 & v2.10.0b2-4-g7209c6d

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1194
> Collected: 2026-10-07
> Published: 2025-08-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1194
- State: closed
- Author: ghost
- Opened: 2025-08-15
- Closed: 2025-08-23
- Labels: none

## Description

Pool config page

Just a small issue, when moving the mouse over the text on the left the input boxes get highlighted.
Enable Extranonce Subscribe  is clickable outside the box as well.

Video showing the issue.

https://github.com/user-attachments/assets/5d9c816f-d201-4301-bb50-1a93d61352e7

## Comments

### duckaxe on 2025-08-15

This is how form labels should work. Each label is linked to its corresponding input field. Clicking on the label selects the input field. The same applies when hovering over the label.

At some point, we should adjust all form fields on other views (settings, network) so that they all work according to this pattern.

See the example (click on the label): https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label

### mutatrum on 2025-08-18

This makes a lot of sense for mobile.
