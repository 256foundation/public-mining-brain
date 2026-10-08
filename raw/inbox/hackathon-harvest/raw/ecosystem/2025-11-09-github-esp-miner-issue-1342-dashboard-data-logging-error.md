# bitaxeorg/ESP-Miner issue #1342: Dashboard data logging error

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1342
> Collected: 2026-10-07
> Published: 2025-11-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1342
- State: closed
- Author: Travetown
- Opened: 2025-11-09
- Closed: 2025-11-16
- Labels: none

## Description

In the system settings, I entered “Every 14 minutes for 1 week” for data logging.
However, only the last 12 hours are displayed in the dashboard (displayed every minute). Older entries disappear.

Bitaxe Gamma 601
Software from November 7 (db1b123) - Scoreboard. 

<img width="305" height="452" alt="Image" src="https://github.com/user-attachments/assets/bcd8ada9-fd4b-4088-b439-97df76c392a3" />

<img width="1011" height="219" alt="Image" src="https://github.com/user-attachments/assets/761a5d91-9c93-4383-8525-f2e5bc44ba80" />

<img width="1028" height="387" alt="Image" src="https://github.com/user-attachments/assets/c611cb8b-59ff-43e1-bb9f-996c4b508955" />


## Comments

### mutatrum on 2025-11-10

See #1054. Live data is added every 5 seconds, up to a maximum of 720 points. This pushes out datapoints, until you reload the page, then the statistics data is loaded from the backend again. These streams need to be uniformed.

### Travetown on 2025-11-10

Even after reloading, only 12 hours are displayed. 

### mutatrum on 2025-11-11

> Even after reloading, only 12 hours are displayed.

Confirmed, I'm seeing the same thing:

1 week of statistics:
<img width="1932" height="231" alt="Image" src="https://github.com/user-attachments/assets/2d3e1ef6-c6a8-4cbc-9a89-7c10fb2b346e" />

17 hour uptime:
<img width="553" height="84" alt="Image" src="https://github.com/user-attachments/assets/39b53b3d-29b4-49d6-a587-22bdd2753f32" />

12 hours on graph:
<img width="1912" height="435" alt="Image" src="https://github.com/user-attachments/assets/60074143-7d1e-450b-9af8-410f69e6ed04" />

### terratec on 2025-11-15

I'll take a look
