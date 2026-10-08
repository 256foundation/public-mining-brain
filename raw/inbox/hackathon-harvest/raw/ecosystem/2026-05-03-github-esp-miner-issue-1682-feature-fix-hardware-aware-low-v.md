# bitaxeorg/ESP-Miner issue #1682: [Feature/Fix] Hardware-Aware Low Voltage Protection: Implementing Fixed 11.7V/4.7V Thresholds

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1682
> Collected: 2026-10-07
> Published: 2026-05-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1682
- State: closed
- Author: ghost
- Opened: 2026-05-03
- Closed: 2026-08-16
- Labels: none

## Description

Regarding mutatrum's 'open question' from last year about the 12V low voltage warning—I've done the bench testing on the GT 801 (12V) and Ultra 205 (5V). The current logic triggers too late for 12V devices. Here is a hardware-aware proposal that fixes the 12V 'silent sag' while keeping the 5V rail with it's 4.7V warning that gets triggered.

Proposal

Early warning message due to Input Voltage drop to prevent hardware getting damaged.

This updates the current percentage-based logic to hardware-validated thresholds for both 5V and 12V Bitaxe families.


Whether it’s in a struct or a ternary operator, we must use 11.7V & 4.7V as the hard line for 12V and 5V devices for the Low Input Voltage warning to be triggered, any other value fails to protect the hardware while the PSU is sagging when the user is overclocking their devices, it also detects if the user is using a poor quality PSU or one that's not fit for the job - ie 12V 5amp PSU when overclocking.


On nominal - 0.3 (The "False Alarm" Trap)
This is a bad math path. For anyone with a 12.4V PSU, this triggers a 'Danger' warning at 12.1V. That is a healthy voltage, not a danger zone. It creates false positives that will lead users to ignore the warning entirely. We need a fixed floor, not a floating formula.

The fix

*ngIf="info.voltage <= (info.nominalVoltage > 8 ? 11.7 : 4.7)

<img width="704" height="552" alt="Image" src="https://github.com/user-attachments/assets/f948a375-7298-41db-af95-d55fc2e982dc" />

Real world example

<img width="1334" height="219" alt="Image" src="https://github.com/user-attachments/assets/279e171a-2ecf-45b0-a59b-866bf7f7dd31" />



Environmental Note: Thermal Sag
It's also important to note that ambient room temperatures play a critical role here. As the operating environment heats up, internal resistance in the PSU and power cables increases. A voltage that sits at a "marginal" 11.8V in a cool room can easily sag into the 11.7V danger zone as ambient temps rise during the day.
A fixed 11.7V threshold provides a necessary safety margin that accounts for these real-world thermal fluctuations, protecting the hardware from the "dirty" power and instability that occur when a PSU is thermally throttled, the user should then change their overclock settings to counter for this.

## Comments

### mutatrum on 2026-05-04

The firmware has no idea what power brick it has, if it's rated for anything other that 5V or 12V. It doesn't know if it's a 12.4V brick. Nominal voltage is defined as 5V or 12V in `device_config.h`, based on the device type. So in the current code (`(nominalVoltage + 0.5) * 0.87`) the warning below 4.785 for 5V devices and below 10.875V for 12V devices.

It would also be good to consider #1584, as currently the warning is front-end only. When moving this to the backend, it can be exposed through the API and also be shown on the display and the swarm page.

### ghost on 2026-05-04

I agree. Moving this logic to the backend is the right move. Having these 11.7V / 4.7V thresholds exposed through the API and included in the Swarm dashboard (specifically in the Power column) would be a huge win for remote monitoring.

It makes the safety warning much more robust and allows for catching 'environmental chaos' across a whole fleet at a glance, rather than having to check local UIs individually. I'm happy to provide long-term soak testing on my GT 801 and Ultra 205 once the backend implementation is ready. I'll be overclocking the units to intentionally stress the power delivery and verify how the new thresholds and API reporting handle real-world voltage sag under load.

Note
A critical edge case to consider: Users running 12V 5A or 6A PSUs on high-performance units like the GT 801. Under the current logic, these under-powered bricks can sag significantly under load without ever triggering a warning. Implementing the 11.7V floor (based on the 80% rule for continuous load) ensures the user is proactively warned that their PSU is undersized for their overclock settings before hardware damage or thermal failure occurs.

### ghost on 2026-05-07

Thought Idea / Refinement: Time-Delayed "Safe-Mode" Reboot

To ensure the backend logic acts as true physical hardware protection, we could directly reuse the existing 75°C ASIC Overheat trigger loop framework with a continuous rolling time window:

0–10 Minutes (Warning Stage):
If input voltage drops to <=11.7V or <=4.7V due to high overclocks, poor PSU choice, or real-world ambient thermal sag, the system flags an immediate warning to the API, screen, and Swarm dashboard. This 10-minute window filters out momentary transient voltage dips and prevents user alert fatigue.

At 10 Minutes (Self-Protection Stage):
If the voltage sag persists continuously past 10 minutes—meaning a user is asleep or away and cannot manually adjust settings—the firmware calls the existing ASIC overheat routine. This forces a reboot back into the low-power safe mode state, using safe default core voltage and frequency profiles.

Why this is ideal:
It drops power consumption instantly to neutralize the thermal stress on a PSU that has started to fail and prevent damage to hardware before thermal runaway can occur.


### justnate787-lang on 2026-05-08

Can I ask why it is a good idea to put the safety of the power management on a piece of hardware not attached to the pcb? Is it possible the pcb provided doesn't contain the power management to safely or effectively maintain asic temps?

### mutatrum on 2026-05-08

> Can I ask why it is a good idea to put the safety of the power management on a piece of hardware not attached to the pcb? Is it possible the pcb provided doesn't contain the power management to safely or effectively maintain asic temps?

As I said before: please open a discussion thread instead of keep posting in this PR. You're asking a hardware related question and it is not relevant here. Furthermore, I and many other have absolutely no context on your apparent knowledge and history you have on this topic and what username you have/had on Discord and why you were banned there, so if you want to make yourself clear instead of posting questions alluding to something, you need to make yourself clear and explain more. Just  **not** on this PR, it's off topic here.
