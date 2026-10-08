# bitaxeorg/ESP-Miner issue #345: Efficacy not Efficiency

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/345
> Collected: 2026-10-07
> Published: 2024-09-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 345
- State: closed
- Author: AndySchroder
- Opened: 2024-09-23
- Closed: 2024-10-10
- Labels: none

## Description

The web UI presents `efficiency` in terms of `J/TH`. `Efficiency` is a unitless quantity that measures the output over the input or the maximum possible output. You could present `efficiency` in terms of [Landauer's principle](https://en.wikipedia.org/wiki/Landauer%27s_principle) if you want to present `efficiency`. However, I'd encourage you to present the metric `J/TH` as an `Efficacy` instead, since that is what it really is.

## Comments

### skot on 2024-09-24

The correct term is "performance per watt", often referred to as power efficiency. The unitless efficiency term you are talking about is mechanical efficiency, but that's not really relevant in computing.
