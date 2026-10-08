# bitaxeorg/ESP-Miner issue #1258: Proposal: Limit Effciency to theoretical maximum

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1258
> Collected: 2026-10-07
> Published: 2025-10-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1258
- State: open
- Author: adammwest
- Opened: 2025-10-03
- Closed: n/a
- Labels: none

## Description

**Problem**
Eficiency is defined by the following equation
`Efficiency = Power/Hashrate`

If calculated Hashrate is over expected hashrate, efficiency becomes too small giving the impression that it is better than is physically possible.

**Cause**
Why could hashrate be greater than expected?
Hashrate is an estimate, due to the variance of the sampling window (small) and the probabilistic nature of hashrate calculation from shares.

**Solution**
Currently the code does
```javascript
if (hashrate > 0) { 
    return power / (hashrate / 1000000000000); // Convert to J/Th 
} else { 
    return power; // in this case better than infinity or NaN return }
```



I Propose Efficiency be limited to a minimum  defined by expected hashrate
[ESP source](https://github.com/bitaxeorg/ESP-Miner/blob/819777caee1d6b90fc2ecab8b505654e10308aa5/main/http_server/axe-os/src/app/components/home/home.component.ts#L464)

```javascript
public calculateEfficiencyAverage(hashrateData: number[], powerData: number[], freq: number, cores: number): number {
  if (hashrateData.length === 0 || powerData.length === 0) return 0;

  const expHashrate = freq * cores;

  const efficiencies = hashrateData.map((hashrate, index) => {
    const power = powerData[index] || 0;
    const effectiveHashrate = hashrate > 0 
      ? Math.min(hashrate, expHashrate) 
      : expHashrate;

    return power / (effectiveHashrate / 1e12); // J/Th
  });

  return this.calculateAverage(efficiencies);
}
```
Some details about how to add freq and core data from the chip is necessary to the function

This has the property of not reporting efficiency under the theoretical (over estimation).

## Comments

### WantClue on 2025-11-03

with the move over to the hashrate register this should be obsolete because we're working with values from the chip and no longer with a time period avg calculation. Still might be a bit off but i doubt that we can get any closer to real statistics than this
