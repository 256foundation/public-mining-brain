# Control and Automation

> Source: https://forum.heatpunks.org/t/control-and-automation/133
> Collected: 2026-10-10
> Published: 2025-06-04
> Registry ID: heatpunks-forum

tronsington | 2025-06-04 18:22:25 UTC | #1

What are you guys using for general system control? @SoftwarmLLC has recommended Taco Controllers for zone control on a radiant system. I lean heavily towards Home Assistant for automation (sorry @Cody). I’m curious what else is being used for various heating systems.

-------------------------

tylerkstevens | 2025-06-04 19:28:49 UTC | #2

Also, do you control radiant zones with valves or with pumps on each zone loop to just stop the flow?

-------------------------

Cody | 2025-06-05 00:59:54 UTC | #3

Have limited experience with radiant, but I prefer conroling zones with a different pump on each zone as opposed to valves.  It seems like you get better flow rate control over each zone that way.

I also use Taco conrollers for the pump/thermostat communication.

The hydronic engineer that was at UnderMine said he uses a lot of Tekmar stuff in his systems.

-------------------------

SoftwarmLLC | 2025-06-07 18:56:35 UTC | #4

My systems use a central hydronic manifold with valves controlled by a Taco. Im not against other types, just have had good results with the Taco.

The way my systems are set up requires minimal API input, if at all, with the miner. Braiins OS does a good job of changing the wattage on the miner based on chip temperature. I’ve found that if you get the settings correct, you can just tie it in as an independent boiler that manages itself. I know that a lot of people are using controllers to change miner output, but where I live, I prefer to run the miner at rated power and just pull heat from the immersion fluid circuit when its needed. Basically the demand signal turns on the hydronic pump to move glycol and pull heat from a immersion fluid circuit that is always hot.

The tricky part is if you live in an area where you don’t want to mine unless you need the heat. If that’s the case, I would consider some type of relay connected to the demand signal on the controller. Basically it would just turn the miner on when there is a heat demand signal… like a boiler.
