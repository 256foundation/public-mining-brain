# bitaxeorg/bitaxeGamma issue #59: Feature Request: Metrics endpoint

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/59
> Collected: 2026-10-07
> Published: 2026-05-12

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 59
- State: closed
- Author: zenhighzer
- Opened: 2026-05-12
- Closed: 2026-05-12
- Labels: none

## Description

Hi, 

I would like to display Bitaxe´s stats like hashs, temperature, wattage, etc. in prometheus/grafana. 
I could write an prometheus-metrics-importer by myself, but
unfortunately curling/receiving the bitaxe´s webinterface with python ends up in garbage. 

Could you please provide am metrics-page which could look really basic like this: 

`curl http://bitaxe/metrics

hashrate:  1.06 Th/s 
shares: 81
error: 80%
difficulty: 8192
power: 16.2 W
etc...`

If you could format the output in prometheus-format directly it would be really cool ;-)

Thanks and Best Regads
Zen

## Comments

### zenhighzer on 2026-05-12

sorry, was in wrong repo.. nevermind. issue can be ignored/closed
