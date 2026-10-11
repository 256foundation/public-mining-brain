# LuxOS Docs — Compatible Miners

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/compatibility
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


LuxOS supports select models from both Bitmain and MicroBT. Select your manufacturer below to view compatible models.

<Tabs items="['Bitmain (Antminer)', 'MicroBT (Whatsminer)']">
  <Tab value="Bitmain (Antminer)">
    While Luxor will strive to provide support to as many machines as possible, the current makes and models supported are limited to the list below.

    ## Antminer 19 Series [#antminer-19-series]

    | S19 Model     | Control Board                         |                                  Hashboard Model Number                                  | Power Targeting | On-die Chip Temps |
    | :------------ | :------------------------------------ | :--------------------------------------------------------------------------------------: | :-------------: | :---------------: |
    | S19           | Xilinx                                |                                            All                                           |        —        |         —         |
    | T19           | Xilinx                                |                                            All                                           |        —        |         —         |
    | S19a          | Xilinx                                |                                         BHB28611                                         |        —        |         —         |
    | S19a Pro      | Xilinx                                |                                         BHB28501                                         |        —        |         —         |
    | S19j          | Xilinx                                |                                         BHB42701                                         |        —        |         —         |
    | S19 Pro       | Xilinx, BeagleBone, AMLogic           |                                            All                                           |        —        |         —         |
    | S19j Pro      | Xilinx, BeagleBone, AMLogic, \*CVITEK | BHB42601, BHB42603, BHB42621, BHB42631, BHB42641, BHB42651, BHB42821, BHB42831, BHB42841 |        —        |         —         |
    | S19j Pro+     | Xilinx, BeagleBone, AMLogic, \*CVITEK |                                         BHB42612                                         |        —        |         —         |
    | S19k Pro      | Xilinx, BeagleBone, AMLogic, \*CVITEK |                               BHB56902, BHB56903, BHB56907                               |        —        |         —         |
    | S19 XP        | Xilinx, BeagleBone, AMLogic, \*CVITEK |                                    BHB56801, BHB56802                                    |        ✓        |         —         |
    | S19 XP+       | Xilinx, BeagleBone, AMLogic, \*CVITEK |                                         BHB68707                                         |        ✓        |         ✓         |
    | S19j XP       | AMLogic, \*CVITEK                     |                                         BHB56804                                         |        ✓        |         —         |
    | S19 XP Hydro  | Xilinx                                |                                         HHB56601                                         |        —        |         —         |
    | S19 XP+ Hydro | Xilinx                                |                                         HHB68701                                         |        ✓        |         ✓         |

    ## Antminer 21 Series [#antminer-21-series]

    | S21 Model        | Control Board     |      Hashboard Model Number     | Power Targeting | On-die Chip Temps |
    | :--------------- | :---------------- | :-----------------------------: | :-------------: | :---------------: |
    | S21              | AMLogic, \*CVITEK |   BHB68601, BHB68603, BHB68606  |        ✓        |         ✓         |
    | S21 Pro          | AMLogic           | A3HB70601, A3HB70602, A3HB70603 |        ✓        |         —         |
    | S21 XP           | AMLogic           |       A3HB70501, A3HB70503      |        ✓        |         —         |
    | S21+             | AMLogic           |            A3HB70701            |        ✓        |         —         |
    | T21              | AMLogic, \*CVITEK |        BHB68701, BHB68703       |        ✓        |         ✓         |
    | S21 Hydro        | Xilinx            |             HHB68501            |        —        |         ✓         |
    | S21e Hydro       | Xilinx            |            H6HB70801            |        —        |         —         |
    | S21 XP Hydro     | Xilinx            |            H6HB70501            |        ✓        |         —         |
    | S21+ Hydro       | Xilinx            | H6HB70701, H6HB70702, H6HB70704 |        ✓        |         —         |
    | U3 S21e XP Hydro | Xilinx            |            H1HB70602            |        ✓        |         —         |

    ## Antminer Equihash (Zcash) [#antminer-equihash-zcash]

    | Model   | Control Board | Hashboard Model Number | Power Targeting | On-die Chip Temps |
    | :------ | :------------ | :--------------------: | :-------------: | :---------------: |
    | Z15 Pro | Xilinx        |        BEZ36501        |        —        |         ✓         |

    <Callout type="warn" title="Remote Install Required">
      Remote Install is required for:

      * Machines with CVITEK control boards
      * Any machine with Bitmain Firmware dated March 2024 or newer

      Please schedule a remote install by [contacting us](https://luxor.tech/contact). Visit our [Remote Install](./kb/remoteinstall) document to learn more about setting up a VPN for this case.
    </Callout>
  </Tab>

  <Tab value="MicroBT (Whatsminer)">
    While Luxor will strive to provide support to as many machines as possible, the current makes and models supported are limited to the list below.

    <Accordions type="single">
      <Accordion title="M50 — 1 supported miner type">
        | Miner Type | Control Board | Power Targeting | On-die Chip Temps |
        | :--------- | :-----------: | :-------------: | :---------------: |
        | M50\_VK40  |      H616     |        ✓        |         ✓         |
      </Accordion>

      <Accordion title="M50S — 3 supported miner types">
        | Miner Type | Control Board | Power Targeting | On-die Chip Temps |
        | :--------- | :-----------: | :-------------: | :---------------: |
        | M50S\_VK20 |      H616     |        ✓        |         ✓         |
        | M50S\_VK30 |      H616     |        ✓        |         ✓         |
        | M50S\_VK80 |      H616     |        ✓        |         ✓         |
      </Accordion>

      <Accordion title="M50S+ — 3 supported miner types">
        | Miner Type  | Control Board | Power Targeting | On-die Chip Temps |
        | :---------- | :-----------: | :-------------: | :---------------: |
        | M50S+\_VK10 |      H616     |        ✓        |         ✓         |
        | M50S+\_VK20 |      H616     |        ✓        |         ✓         |
        | M50S+\_VK30 |      H616     |        ✓        |         ✓         |
      </Accordion>

      <Accordion title="M50S++ — 1 supported miner type">
        | Miner Type   | Control Board | Power Targeting | On-die Chip Temps |
        | :----------- | :-----------: | :-------------: | :---------------: |
        | M50S++\_VK50 |      H616     |        ✓        |         ✓         |
      </Accordion>

      <Accordion title="M60 — 1 supported miner type">
        | Miner Type | Control Board | Power Targeting | On-die Chip Temps |
        | :--------- | :-----------: | :-------------: | :---------------: |
        | M60\_VK20  |      H616     |        ✓        |         ✓         |
      </Accordion>

      <Accordion title="M60S — 1 supported miner type">
        | Miner Type | Control Board | Power Targeting | On-die Chip Temps |
        | :--------- | :-----------: | :-------------: | :---------------: |
        | M60S\_VK20 |      H616     |        ✓        |         ✓         |
      </Accordion>
    </Accordions>
  </Tab>
</Tabs>
