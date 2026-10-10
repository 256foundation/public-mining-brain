# bitaxeorg/ESP-Miner issue #1801: feat(ui): Smooth efficiency average display using Exponential Moving Average (EMA)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1801
> Collected: 2026-10-07
> Published: 2026-07-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1801
- State: open
- Author: chillingbee
- Opened: 2026-07-04
- Closed: n/a
- Labels: none

## Description

Markdown
### Problem
The `efficiencyAverage` in the web interface currently calculates the 1-minute average (or 1-hour average when modified) by dividing the live power consumption (`info.power`) by the hashrate. Because `info.power` is updated and telemetry is fetched every second, the displayed efficiency value fluctuates rapidly by ~0.15 J/TH or more due to minor real-time power draw spikes. This causes unnecessary visual flickering in the UI for a value labeled as an "average".

### Solution
This introduces a frontend-side Exponential Moving Average (EMA) filter to smooth out the real-time power fluctuations for the `efficiencyAverage` display. 

1. Added `smoothedEfficiencyAverage` to `home.component.ts` to persist the filtered state.
2. Applied a 99% historical / 1% new value split `(old * 0.99) + (new * 0.01)` to damp out the per-second noise.
3. Changed the backend data source for the average from `hashRate_1m` to `hashRate_1h` to provide a true, rock-solid long-term efficiency metric.

### Result
The efficiency average indicator is now visually stable and reflects the true hardware performance without nervous second-by-second jumping, while still accurately adapting to frequency or voltage changes over a few minutes.

```diff
diff --git a/main/http_server/axe-os/src/app/components/home/home.component.ts b/main/http_server/axe-os/src/app/components/home/home.component.ts
index b5314a74..7a5d4cdf 100644
--- a/main/http_server/axe-os/src/app/components/home/home.component.ts
+++ b/main/http_server/axe-os/src/app/components/home/home.component.ts
@@ -175,6 +175,7 @@ export class HomeComponent implements OnInit, OnDestroy {
    public asicDomainsAmount: number = 0;
    public efficiency: number = 0;
    public efficiencyAverage: number = 0;
+   public smoothedEfficiencyAverage: number = 0;
    public expectedEfficiency: number = 0;
    public activePoolUserAddressPart: string = '';
    public activePoolUserSuffixPart: string = '';
@@ -871,12 +872,24 @@ export class HomeComponent implements OnInit, OnDestroy {
 
          this.efficiency = this.calculateEfficiency(info, 'hashRate');
          
-        // MANUELLE BERECHNUNG FÜR DEN STUNDEN-DURCHSCHNITT:
+        // BERECHNUNG MIT GEGLÄTTETEM FILTER (DÄMPFUNG)
          if (info && info.power > 0 && info.hashRate_1h > 0) {
-            // Leistung (W) geteilt durch Hashrate (GH/s umgerechnet in TH/s -> durch 1000)
-            this.efficiencyAverage = (info.power * 1000) / info.hashRate_1h;
+            const currentRawAvg = (info.power * 1000) / info.hashRate_1h;
+            
+            // Wenn der Wert zum ersten Mal berechnet wird, nimm den aktuellen Wert
+            if (this.smoothedEfficiencyAverage === 0) {
+                this.smoothedEfficiencyAverage = currentRawAvg;
+            } else {
+                // FILTER: 99% alter Wert + 1% neuer Wert. 
+                this.smoothedEfficiencyAverage = (this.smoothedEfficiencyAverage * 0.99) + (currentRawAvg * 0.01);
+            }
+            
+            // Weise den geglätteten Wert der Anzeige zu
+            this.efficiencyAverage = this.smoothedEfficiencyAverage;
          } else {
             this.efficiencyAverage = 0;
+            this.smoothedEfficiencyAverage = 0;
          }
 
         this.expectedEfficiency = this.calculateEfficiency(info, 'expectedHashrate');```

## Comments

### mutatrum on 2026-07-04

Maybe it would make more sense to apply the same 1m/10m/1h statistics for power as well, so we can have efficiencies over those ranges as well? Testing with EMAs gave me a lot of trouble when changing power/frequency settings and are slow to settle after a boot.

### chillingbee on 2026-07-04

If you can implement that, by all means! 
That’s a good idea, too!
Personally, I think the current setup is just right, that’s exactly how I understand an average—but it needs to cover a period of at least 30 minutes, if not longer.
Anything shorter doesn't really count as an average to me.
But that’s just my opinion!
