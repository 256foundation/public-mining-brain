# Hashrate Heating vs Heat Pumps - Calculate COP with BTC

> Source: https://forum.heatpunks.org/t/hashrate-heating-vs-heat-pumps-calculate-cop-with-btc/233
> Collected: 2026-10-10
> Published: 2025-12-15
> Registry ID: heatpunks-forum

tylerkstevens | 2025-12-15 21:04:24 UTC | #1

Some fudsters say hashrate heating makes no sense when heat pumps exist.

Here’s why I disagree

Heat pumps don’t generate heat. They move heat. Say you spend 1 unit of electricity on a heat pump. You could get 3 units of heat energy in return. How? Because they capture heat from the ambient air and bring it inside. Even when it’s cold outside, there’s technically still some energy to extract from those air molecules.

This is measured by a metric called the Coefficient of Performance (COP). 1 watt in, 3 watts of heat out. 3:1 = 3.0, or 300% efficient.

The colder it gets, the worse heat pumps perform (less energy in the air to bring inside as heat). Lower COP.

Hashrate heating has a thermodynamic efficiency of near 100%. 1 watt of electricity = 1 watt of heat. COP = 1.0. (Resistive heating).

But that misses the point. The real value of a high COP is that you only need to purchase 1 watt of heat for every 3 watts that are delivered as warmth. Effectively, a heat pump cost 1/3 as much as an electric resistive heater.

But hashrate heaters earn revenue, so the thermodynamic COP of 1.0 is not the full story. What really matters, is how much heat do I get for how much I spend? And bitcoin mining heaters give you money back…

What I’m getting at is that there’s an “effective” COP of a hashrate heater that takes into account the money you get back after paying 1-1 for the heat.

Here’s the equation I drafted:

COP_eff = 1 / (1-R)

where

R = Daily Mining Revenue / Daily Elect Heat Cost

Ex)

You spend $15.00 on electricity for hashrate heating and earn $10.00 back from mining. That means mining pays for 66.6% of your electricity. You’re only truly “paying” for 33.3% of it. (10/15=0.667)

Therefore, the COP_eff = 3.0.

You get three watts of heat for every 1 watt you truly purchase and don’t earn revenue back for.

That’s the same economic COP as a heat pump.

What’s interesting is that the COP of your hashrate heating system depends on multiple factors:

- Miner Efficiency (W/TH/s)

- Electricity Rate ($/kWh)

- Network Hashprice ($/TH/s/day)

Whereas, the efficiency of your Heatpump only depends on the machine efficiency.

Here’s how COP_eff breaks down for a Whatsminer M64 (228 TH/s, 22 J/TH, 5000 W) at various electric utility rates, with 0.037 $/TH/s/day hashprice (all-time low…)

The kicker: at 0.07 $/kWh electric rate, the device COP approaches infinity, because the heat is free. (Again, at all-time low hashprice, mind you).

---

My Takeaway: COP isn’t just about thermodynamic efficiency. In my view, the energy doomers use this sole metric to poo-poo anything that doesn’t have “physics that checks out”. They’re missing the point. People want to save money. Not have the thermodynamically most efficient gadget.

In summary - using energy is not bad. Harnessing energy to do good is not immoral. And flowing electrons through the bitcoin network as they’re converted to heat is for some, the best and most efficient thing you could possibly do.

And I didn’t even map out the economics when you hold the bitcoin for the long term while fiat dissolves to nothing.

Take a look at how COP_eff changes with various electric rates. Where do you fall on the chart?

[![Screenshot 2025-12-15 at 14.03.47](https://forum.heatpunks.org/uploads/default/original/1X/0553b0e6cacf3b2a2f0ecccdaf3dadf6ba0c862c.png)Screenshot 2025-12-15 at 14.03.47950×882 15.9 KB](https://forum.heatpunks.org/uploads/default/original/1X/0553b0e6cacf3b2a2f0ecccdaf3dadf6ba0c862c.png)

| Electricity Rate | Daily Elec Cost | Daily BTC Revenue | Net Heat Cost | Revenue Ratio (R) | Effective COP |
|---|---|---|---|---|---|
| $0.07/kWh | $8.40 | $8.41 | **-$0.01** | 100.1% | ∞ (profitable!) |
| $0.08/kWh | $9.60 | $8.41 | $1.19 | 87.6% | **8.1** |
| $0.09/kWh | $10.80 | $8.41 | $2.39 | 77.9% | **4.5** |
| $0.10/kWh | $12.00 | $8.41 | $3.59 | 70.1% | **3.3** |
| $0.11/kWh | $13.20 | $8.41 | $4.79 | 63.7% | **2.8** |
| $0.12/kWh | $14.40 | $8.41 | $5.99 | 58.4% | **2.4** |
| $0.13/kWh | $15.60 | $8.41 | $7.19 | 53.9% | **2.2** |
| $0.14/kWh | $16.80 | $8.41 | $8.39 | 50.1% | **2.0** |
| $0.15/kWh | $18.00 | $8.41 | $9.59 | 46.7% | **1.9** |

-------------------------

Cody | 2025-12-16 01:10:57 UTC | #2

Awesome post!  I have long been expressing Hashrate heating systems as having higher than 100% efficiency.  So the calcs I’ve been running show an S19kpro on 9 cent power having ~170% efficiency,  of course it doesn’t from a thermodynamic perspective, but it does from a “how much heat for how much money” perspective.  I think you should just adopt a (Coefficient of Performance Economically) or COPE :rofl:  metric to explain this simply.   Getting this stuff across simply to the masses is key.
