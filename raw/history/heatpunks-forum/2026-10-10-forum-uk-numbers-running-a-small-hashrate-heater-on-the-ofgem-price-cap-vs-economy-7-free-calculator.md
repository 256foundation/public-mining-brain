# UK numbers: running a small hashrate heater on the Ofgem price cap vs Economy 7 (free calculator)

> Source: https://forum.heatpunks.org/t/uk-numbers-running-a-small-hashrate-heater-on-the-ofgem-price-cap-vs-economy-7-free-calculator/291
> Collected: 2026-10-10
> Published: 2026-10-10
> Registry ID: heatpunks-forum

mineshop_eu | 2026-10-10 16:51:45 UTC | #1

Hi all. Guntis here from Mineshop.eu (an EU mining hardware shop based in Ireland), so I have a commercial interest. Sharing a free tool and the UK numbers behind it, because UK electricity pricing changes the maths for hashrate heating quite a bit.

**UK numbers at the Ofgem price cap for October to December 2026** (26.32p/kWh average unit rate by Direct Debit; Ofgem also removed VAT on electricity from 1 October 2026 to 31 March 2027):

- A 140 W device (Avalon Nano 3S class) running 24/7 uses about 1,226 kWh a year, roughly

  £323

  , and nearly all of it ends up as heat in the room.

- A 17 W Bitaxe Gamma: about 149 kWh a year, roughly

  £39

  .

- On Economy 7 with seven off-peak hours, a device running around the clock only uses about

  29%

  of its energy at the night rate. Running it off-peak only cuts runtime by about 70% and the bill by more.

- Compared with a heat pump, which delivers several kWh of heat per kWh of electricity, a miner only competes with resistive heat (panel heaters, oil radiators, immersion). There, the mining income is a partial rebate on heat you would buy anyway.

**Free calculator** (no sign-up or cookies; formulas and tests are public): [Home Bitcoin Miner Running Cost Calculator (UK): Price Cap vs Economy 7 | Mineshop](https://mineshop007.github.io/uk-home-miner-running-cost/) You can enter your own single-rate or two-rate prices.

The longer UK write-up, including what UK buyers pay in import VAT when buying from the EU: [ASIC Bitcoin Mining in the UK 2026 – Legal, Cost & Setup Gui](https://mineshop.eu/blog/bitcoin-mining-machine/complete-guide-to-asic-mining-in-the-uk-regulations-costs-setup)

Two questions for UK members:

1. If you are on a half-hourly tariff such as Octopus Agile, do you schedule your heaters on price signals, and with what control stack (Home Assistant, Braiins, custom scripts)?

2. Has anyone measured how much resistive heating a miner actually displaces when a room thermostat is in the loop?
