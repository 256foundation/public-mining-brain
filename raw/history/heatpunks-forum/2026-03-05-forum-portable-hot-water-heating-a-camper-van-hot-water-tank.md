# Portable hot water: heating a camper van hot water tank

> Source: https://forum.heatpunks.org/t/portable-hot-water-heating-a-camper-van-hot-water-tank/256
> Collected: 2026-10-10
> Published: 2026-03-05
> Registry ID: heatpunks-forum

josh | 2026-03-05 02:52:10 UTC | #1

# Hydro Single19

[![IMG_6171](https://forum.heatpunks.org/uploads/default/optimized/1X/90904d2ac9bfdb049fbecfea2352ed184595acbb_2_560x500.jpeg)IMG_61711920×1714 879 KB](https://forum.heatpunks.org/uploads/default/original/1X/90904d2ac9bfdb049fbecfea2352ed184595acbb.jpeg)

1kW of quiet, portable water or air heating from 120v. APW12 enables under/overclocking.

Use for:

- RV water heater. Power with alternator via inverter or power station. Use existing RV plumbing/pump (hot hose on low → heat exchanger → fill port)

- Heat water at a job or camp site

- Add to a sidearm loop on an existing water heater

- Attach via a circulation pump to a kids pool (use a different heat exchanger if its chlorinated…)

- Dunk the heat exchanger in a bucket of water for sous vide

- Stock tank ice melter

- Etc.

# Parts:

| Part | Supplier |
|---|---|
| S19J Pro board | Upcycled e-waste |
| APW12 (with 120v mod) | Upcycled e-waste + resistors |
| Bitmain control board | Upcycled e-waste |
| Zeus water block | [zeusbtc.com](http://zeusbtc.com) |
| Heat exchanger 3" x 7.5" x 30 plate | [vevor.com](http://vevor.com) |
| Hydro pump/reservoir | Amazon |
| 240mm PC radiator | Amazon |
| Arctic P12 Max fans x2 (Radiator) | Amazon |
| Noctua 60mm fans x3 (PSU) | Amazon |
| Hydro tubing | Amazon |
| Hydro fittings | Amazon |
| Misc wiring components | Amazon |
| Mine4heat enclosure + furniture | 3DFuel Pro-PCTG filament |
| Sentinel X100 corrosion inhibitor | [supplyhouse.com](http://supplyhouse.com) |

# Build

I used an APW12 with the 120v mod completed. APW3 would be fine but I figured since i could cool it well I should leave the potential for overclocking (provided I have sufficient power). To power the pump, I spliced in to the 6-pin wires from the PSU to the control board. So one end has the 6-pin connector and the other end has a 6-pin connector, barrel jack for Vonets, and Molex connector for the hydro pump. For the Hashboard I cut the stock bus bars down to size.

I started with the mine4heat enclosure but realized I didn’t need the “flared” fan mounts but did need a place to attach the radiator, so I designed (hacked together) some [custom parts](https://github.com/jnswtf/Hydro-mine4heat.):

- Fanless grille for the back

- Fanless grille for the front

- Control board cover with radiator mount

- Shorter carry handle

I replaced the heat sink on the hashboard with a Zeus Mining water block and used the Zeus mining push to fit adapters and 8mm OD corrugated tubing they included. I did need to find [these fittings](https://www.amazon.com/dp/B07KT7B5ZP) to go from the Zeus tubing to the standard g1/4 fittings that the PC hydro stuff uses.

The hydro loop is:

Pump/reservoir → Hashboard (in lower port, out top port) → Plate heat exchanger → radiator → back to Pump

I put the heat exchanger closest to the hashboard outlet so it gets the most heat. Then if our exchanger isn’t pulling enough heat out, the radiator takes care of the rest. This also lets you use this as a basic space heater without having to change anything. Using LuxOS to manage the fans, they will only turn on once the board temp is high enough (I set target temp to 60c).

# Operation

The main use case is in my camper van. I power the miner from a portable power station that is being charged by the alternator/solar when we’re driving or shore power if we’re plugged in. Starlink or mobile hotspot for data. I set the target temp in LuxOS to 60 and adjust power draw to about 450-500w. Could go much higher depending on your power source.

On the van side, I hook our sprayer hose (blue) up to the heat exchanger inlet and connect the outlet to the water fill port on the van. Then I crack the hot faucet on very low. I also had to figure out the non-standard configuration of the van water panel that let me pump water back in the fill port while in “dry camping” mode.

[![IMG_5740](https://forum.heatpunks.org/uploads/default/optimized/1X/8c081473907459c99f06020e096b2f5d6ea3fe8e_2_690x498.jpeg)IMG_57401920×1386 687 KB](https://forum.heatpunks.org/uploads/default/original/1X/8c081473907459c99f06020e096b2f5d6ea3fe8e.jpeg)
[![IMG_6176](https://forum.heatpunks.org/uploads/default/optimized/1X/f2b54238aa4929f7173720baf95825e69a94f9ff_2_582x499.jpeg)IMG_61761920×1649 895 KB](https://forum.heatpunks.org/uploads/default/original/1X/f2b54238aa4929f7173720baf95825e69a94f9ff.jpeg)

So now the water is slowly circulating from the hot water tank. I have found that it takes 2 hours of this for the 10L tank to get up to temp.

Why don’t van manufacturers use an electric heater to warm up the water tank while you’re driving?

Another fun way to operate is to just dunk the heat exchanger into a container of water (put it in a plastic bag first). It will gradually bring it up to the temp you set your target chip temp to. I did an experiment to cook some eggs sous vide and it worked pretty well.
[![IMG_6037](https://forum.heatpunks.org/uploads/default/optimized/1X/bbfbde2b14e5dfa92cdc1149312c85ecf811a536_2_666x500.jpeg)IMG_60371920×1440 704 KB](https://forum.heatpunks.org/uploads/default/original/1X/bbfbde2b14e5dfa92cdc1149312c85ecf811a536.jpeg)
[![IMG_6039](https://forum.heatpunks.org/uploads/default/optimized/1X/1c37aa7cc9ad05f61a19a75639b5c2b53726c0b4_2_375x500.jpeg)IMG_60391920×2560 787 KB](https://forum.heatpunks.org/uploads/default/original/1X/1c37aa7cc9ad05f61a19a75639b5c2b53726c0b4.jpeg)
[![IMG_6040](https://forum.heatpunks.org/uploads/default/optimized/1X/88f4ae12dca1e423ae1dae88f891c9d089a65f49_2_375x500.jpeg)IMG_60401920×2560 530 KB](https://forum.heatpunks.org/uploads/default/original/1X/88f4ae12dca1e423ae1dae88f891c9d089a65f49.jpeg)

-------------------------

beefyfish | 2026-03-05 20:22:17 UTC | #2

thanks for posting this! i was fascinated watching it at the heatpunk summit.  i would love to try to build it to learn.  great meeting you too.
