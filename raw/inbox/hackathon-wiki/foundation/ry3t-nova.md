# RY3T Nova

> Sources: 256 Foundation (newsroom: The RY3T Nova), collected 2026-10-07
> Raw: [newsroom: RY3T Nova](../../raw/foundation/256foundation-org-newsroom-ry3t-nova.md)
> Updated: 2026-10-07

## Overview

The Nova is a solar miner from RY3T, an energy hardware company in Wil, Switzerland. The 256 Foundation calls it the first commercial product built on [Mujina](../mujina/mujina-firmware.md), the open-source mining firmware the foundation funds but does not own. The Nova mines Bitcoin with surplus solar power and follows the solar generation curve within seconds. RY3T built it without a partnership, a license negotiation, or permission, which the foundation says is exactly the outcome it hoped for.

## What the Nova does

When a building's solar panels make more than it can use, or its batteries are full, the Nova uses the surplus to mine instead of selling it to the grid at poor rates. It takes its orders from the solar management system that already runs the building and ramps its power draw up and down to match what the panels are producing.

RY3T packages up to three miners as a single appliance, scaling to 9kW. You give it one power target. It spreads the load across its miners and reports combined and per-miner hashrate, power, temperature and status.

The Nova is still in development. Pre-orders are open for Switzerland and the EU first, with plans to enter the US market. Specifications, availability and timelines are RY3T's to announce.

## The problem it answers

Export rates for surplus solar have been cut repeatedly across much of Europe and the United States. In some markets midday surplus earns a couple of cents per kilowatt-hour, earns nothing, or gets curtailed. In some places building owners must pay to export.

The foundation's argument is that a miner is the one flexible load that can absorb surplus at any hour and in any quantity, with nowhere needed to store the energy afterward, and it pays you for doing so.

## Why closed firmware blocked this

The hardware was never the obstacle. Mining chips take a frequency and a voltage, and turning them down draws less power.

The obstacle was firmware. The post says manufacturer firmware (Bitmain, Whatsminer, Canaan, Bitdeer) is closed, and so are the aftermarket options (Braiins OS, LuxOS, Vnish). All of it was written for a data center running flat out at a fixed setpoint. Changing power was a maintenance event, not a control input, so nobody made it fast.

People worked around this with Home Assistant integrations, external controllers and relay hardware. That meant extra parts and a ceiling on responsiveness.

## What Mujina adds

Mujina accepts a power target and settles on it in seconds, without restarting the mining process. There is no dropped pool connection. That turns a miner into a dispatchable load that an inverter or energy management system can steer in real time. The post gives the example of setting 1,400W and then 2,900W.

Mujina is GPLv3, written in Rust, and runs on Linux. Ryan, a Core Contributor funded by the foundation, maintains it.

## What has been demonstrated

Schnitzel, a Core Contributor on the [Libre Board](../hardware/libre-board.md) design, did the Mujina integration work and showed each of these on real hardware:

- **One control board, two chip generations.** Three hashboards (one S19j Pro and two S19k Pro) hashing at once on a single control board: 280 chips, 136.70 TH/s, each board at its own frequency.
- **Stepless power tracking.** A single Nova following a power target from 1,000W to 3,000W within seconds.
- **No extra control hardware.** The stock Bitmain control board runs both Mujina and the Nova control layer. No Raspberry Pi and no Home Assistant are needed. One Nova can command others, so only one control board has to run the Nova application.

Mixing chip generations has practical consequences. An owner can upgrade one hashboard at a time, run efficient boards all the time and older boards only on surplus power, and keep "obsolete" boards useful. The post notes that nobody selling new miners has a reason to ship firmware like that.

## Why the foundation highlights it

The post describes Mujina as the most critical missing piece of the stack, "the Linux kernel equivalent for Bitcoin mining". It draws two conclusions from the Nova:

1. Open-source mining firmware is production-ready. A company is prepared to put its name behind a commercial product built on it.
2. The stack is available to everyone. Because Mujina is GPLv3, improvements that are distributed come back to the commons.

The post adds that this is not an argument against industrial mining. Mujina serves large operations too. The Nova shows the other use: mining that follows available energy can go into homes, rooftops and businesses that manufacturers never designed for.

## See Also

- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Libre Board](../hardware/libre-board.md)
- [Hashrate Heatpunks](hashrate-heatpunks.md)
- [Website and Newsroom](website-and-newsroom.md)
