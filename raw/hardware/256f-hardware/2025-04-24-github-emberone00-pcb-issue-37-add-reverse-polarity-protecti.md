# 256foundation/emberone00-pcb issue #37: Add reverse polarity protection?

> Source: https://github.com/256foundation/emberone00-pcb/issues/37
> Collected: 2026-10-07
> Published: 2025-04-24

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 37
- State: open
- Author: skot
- Opened: 2025-04-24
- Closed: n/a
- Labels: enhancement

## Description

Right now the emberOne is unprotected from reverse polarity power connections. I kinda think that's fine, but it would be nice to not destroy your computer too.. maybe we need reverse polarity protection on the USB port? for the upstream host?

## Comments

### zbomz on 2025-05-02

Based on my experience with Loki plebs tinkering with Loki rigs and seeing about half of them blow up at least one hash board while tinkering, I'm a huge proponent of adding reverse polarity protection.

As discussed in the "Ember One Schematic Review Video," reverse polarity protection could be added to either the USB port to at least protect the host PC or to the hash board's main power terminals. Adding reverse polarity protection to the USB port presents a challenge given that both power (VBUS) and data are connected. VBUS can be protected fairly easily with a simple shottky diode given the sub 500mA current draw, but protecting the high speed data lines is harder. It would likely require expensive isolation components/circuitry, and after all that, the hash board would still be vulnerable.    

On the other hand, adding reverse protection polarity to the hash board's main power terminals should protect both the hash board and the host PC, and robust reverse polarity protection can be achieved relatively simply and cheap. 

The design shown below implements an "ideal diode" circuit using an N-type MOSFET on the high side rail and a dedicated charge pump driver. This design offers reverse polarity protection while limiting the forward voltage drop to no more than 35mV at 10 amps. Components were selected specifically to support the max 24V input voltage. The component cost at 1K quantities is about $1.10. 

![Image](https://github.com/user-attachments/assets/e0fe07b5-d6a6-420d-8015-98fd8ddd1124)

### skot on 2025-06-09

U1: AP74700QW6-7 [DK: [31-AP74700QW6-7CT-ND](https://www.digikey.com/en/products/detail/diodes-incorporated/ap74700qw6-7/16680522)]
Q1: NVMFS5C645NL [DK: [488-NVMFS5C645NLAFT1GCT-ND](https://www.digikey.com/en/products/detail/onsemi/NVMFS5C645NLAFT1G/7220982)]
C_CP: CC0805KRX7R9BB104
CIN: GRM155R71H223KA12J
COUT: GRM21BR61H475ME51L
TVS: SMBJ30CA [DK: [SMBJ30CALFCT-ND](https://www.digikey.com/en/products/detail/littelfuse-inc/SMBJ30CA/286005)]

### skot on 2025-06-09

<img width="697" alt="Image" src="https://github.com/user-attachments/assets/da5ebba4-3408-485f-8c62-500604480bb6" />
