# Avalon Q integration w/ forced air ducts

> Source: https://forum.heatpunks.org/t/avalon-q-integration-w-forced-air-ducts/214
> Collected: 2026-10-10
> Published: 2025-11-10
> Registry ID: heatpunks-forum

Pleb_Ed | 2025-11-10 22:47:12 UTC | #1

Hey everyone. I’m about to close on a new home and want to integrate my Avalon Q into the duct work to heat my home.

I’ve been using it as a space heater in my office (about the size of a 2 car garage) and that thing really pumps out some heat. I had seen that The Space used the Q in the duct work there. Any tips or things to consider before starting this project?

-------------------------

tylerkstevens | 2025-11-12 16:35:41 UTC | #2

It’s pretty simple. Depending on how much heat you need, you might want two of them in the duct work.

Our setup has them plumbed in on the supply side of the duct, right before the filter and circulator fan on the furnace.

We use a [Venstar T7900](https://www.supplyhouse.com/Venstar-T7900-Venstar-T7900-ColorTouch-Thermostat-7-Day-Programmable-w-WiFi-Humidity-4-Heat-2-Cool?gad_source=1&gad_campaignid=20930093472&gbraid=0AAAAAD_WAyuQRNkrXQg3W9tyZcf2fDWNU) thermostat with good public api documentation and Home Assistant to define the software logic that turns on the circulator fan and miner when we call for heat on the thermostat.

Let me know if you have any specific control questions
