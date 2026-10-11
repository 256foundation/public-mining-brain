# Avalon (Canaan) miners

> Sources: Canaan product/shop/news pages via dated Wayback Machine snapshots (2025-10-06 → 2026-06-11; live canaan.io 403s this sandbox — see park note); ASIC Miner Value + MiningNow cross-check snapshots (values as of 2026-10-10); Canaan IR mirror (investor.canaan-creative.com, live corroboration); Heatpunks forum threads on Avalon Q / Avalon Mini integration
> Raw: [Miner index (2026-04-12 snapshot)](../../raw/hardware/canaan/2026-04-12-wayback-canaan-miner-index.md); [A15 series page (2026-06-11 snapshot)](../../raw/hardware/canaan/2026-06-11-wayback-canaan-miner-a15-series.md); [A15Pro+ 240T shop page (2026-04-21 snapshot)](../../raw/hardware/canaan/2026-04-21-wayback-shop-canaan-a15pro-240t.md); [A1566HA-500T shop page (2025-10-06 snapshot)](../../raw/hardware/canaan/2025-10-06-wayback-shop-canaan-a1566ha-500t.md); [A14 series page (2026-05-12 snapshot)](../../raw/hardware/canaan/2026-05-12-wayback-canaan-miner-a14-series.md); [A16XP launch news (2025-10-29)](../../raw/hardware/canaan/2025-10-29-wayback-canaan-news-a16xp-launch.md); [AMV Canaan snapshot](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-canaan.md); [MiningNow Canaan snapshot](../../raw/hardware/miningnow/2026-10-10-miningnow-canaan.md); [Avalon Q duct thread](../../raw/history/heatpunks-forum/2025-11-10-forum-avalon-q-integration-w-forced-air-ducts.md); [Avalon Mini 3 / Home Assistant thread](../../raw/history/heatpunks-forum/2025-10-28-forum-send-commands-to-canaan-avalon-mini-3-via-home-assistant.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Live-capture park note (As-Of 2026-10-10)

www.canaan.io and shop.canaan.io serve HTTP 403 (Akamai) from the capture sandbox — tested with plain GET, full browser headers, http:// and https://, and the apex→www redirect chain. All manufacturer-side numbers on this page and its model articles come from **dated Wayback Machine snapshots** (each model article records its snapshot URL and date). The IR mirror investor.canaan-creative.com was reachable live and used only to corroborate numbers. Re-capture from live pages remains parked (→ B5).

## Current lineup (nav, per 2026-04-12 snapshot)

- Flagship generation: **Avalon Miner A16XP-300T** and **Avalon Miner A16-282T** — the A16 series "supersedes the A15 series as Canaan's flagship air-cooled generation as of Oct 2025" (launch news, below).
- A15 generation: A15Pro-221T (plus shop refresh A15Pro+ 240T), A15XP, A15; hydro offering is the **A1566HA** rack unit (440T/460T/480T/500T variants seen in Wayback URL inventory).
- Boxes: Avalon Immersion/Air Cooling Mining Box-40ft, Hydro Cooling Mining Box-20/40ft. Clearance at the 2026-04 snapshot: A1366I-122T immersion, A15-200T. Home line: AvalonQ, Avalon Nano 3S, Avalon Mini 3.
- Hero pricing per index snapshot: A15 "From $15.80/T", A1466 "From $9.90/T", A1326 "From $5.30/T".
- Lineup rotates frequently: the June 2026 A15-page snapshot had already dropped A15Pro/A15XP cards and moved "Avalon Miner A15-200T" to Clearance ([A15 series page](../../raw/hardware/canaan/2026-06-11-wayback-canaan-miner-a15-series.md) Notes).

## Efficiency ladder (manufacturer figures, snapshot-dated)

- A16XP-300T: **12.8 J/TH ±5%** at 300 TH/s (series claim, launch news); AMV/MiningNow list wall power 3850 W → 12.83 j/Th computed.
- A15Pro+ 240T: **15.5 J/TH** at 240 T (shop); A15Pro-221T: **16.8 J/TH** at 221 T; A15XP: **17.8 J/TH** at 209 T; A15: **18.8 J/TH** at 194 T ([A15 series page](../../raw/hardware/canaan/2026-06-11-wayback-canaan-miner-a15-series.md)).
- A1566HA-500T hydro: **16.8 J/TH** at 500 TH/s ([shop page](../../raw/hardware/canaan/2025-10-06-wayback-shop-canaan-a1566ha-500t.md)).
- A14 series: 1466 at **23.3 J/TH**, 1446 at **27.1 J/TH** — prior generation ([A14 series page](../../raw/hardware/canaan/2026-05-12-wayback-canaan-miner-a14-series.md)).
- Series branding note: Canaan markets the A15/A1566 line as the "1xJ/T series" — the series page says "the power efficiency has reached 1xJ/T!" (sic, [A15 series page](../../raw/hardware/canaan/2026-06-11-wayback-canaan-miner-a15-series.md)).

## DB attribution confusion: "A4 Ultra Hyd"

ASIC Miner Value's efficiency ladder places an "A4 Ultra Hyd" at "9.45J/T" in Canaan context, but 9.45J/T at 886T is **Bitdeer's SEALMINER A4 Ultra Hydro** ([Bitdeer product page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md)); Canaan's own lineup has no A4 series. Any efficiency comparison must attribute that datapoint to Bitdeer, not Canaan.

## Heat-reuse notes

- The A15-generation hydro flagship **A1566HA** is a 2U rack unit (556×482.6×86 mm, 20 kg, hydro, operating "10℃~50℃") — commercial-loop hardware, 8064 W heat class ([shop page](../../raw/hardware/canaan/2025-10-06-wayback-shop-canaan-a1566ha-500t.md)).
- The home line is where the heatpunks community actually runs Canaan hardware: an Avalon Q owner planned duct integration — "I’ve been using it as a space heater in my office" and "that thing really pumps out some heat", with Tyler Stevens replying the units go "plumbed in on the supply side of the duct, right before the filter and circulator fan on the furnace" ([Avalon Q duct thread](../../raw/history/heatpunks-forum/2025-11-10-forum-avalon-q-integration-w-forced-air-ducts.md)); Avalon Mini 3 accepts control commands via Home Assistant ([HA thread](../../raw/history/heatpunks-forum/2025-10-28-forum-send-commands-to-canaan-avalon-mini-3-via-home-assistant.md)).

## See Also

- Model pages: [A16XP](avalon-a16xp.md), [A15Pro](avalon-a15pro.md), [A15Pro+](avalon-a15pro-plus.md), [A15XP](avalon-a15xp.md), [A15](avalon-a15.md), [A1566HA-500T](avalon-a1566ha-500t.md), [A14 series](avalon-a14-series.md)
- [Bitmain ASIC reference](bitmain-asic-reference.md), [Whatsminer overview](whatsminer-overview.md), [SEALMINER overview](sealminer-overview.md), [Teraflux overview](teraflux-overview.md)
