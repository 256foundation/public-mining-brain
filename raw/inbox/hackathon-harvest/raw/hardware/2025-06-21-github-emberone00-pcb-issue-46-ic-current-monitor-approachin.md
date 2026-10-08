# 256foundation/emberone00-pcb issue #46: IC Current Monitor approaching end of life

> Source: https://github.com/256foundation/emberone00-pcb/issues/46
> Collected: 2026-10-07
> Published: 2025-06-21

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 46
- State: open
- Author: econoalchemist
- Opened: 2025-06-21
- Closed: n/a
- Labels: documentation

## Description

In the v4 Bill Of Materials there is an IC Current Monitor called out for reference number U3, with manufacturer part number: INA260AIPW. According to the Texas Instrument website, this component is flagged for "Last Time Buy", meaning they are in the process of discontinuing production. See [this page](https://www.ti.com/product/INA260/part-details/INA260AIPW) for reference. 

There is another IC which seems identical in specification to my un-trained eye. The part number is appended with an "R" though: INA260AIPWR. Could someone with an engineering background please confirm this replacement is suitable? Or if not, which one is a suitable replacement? I think the "R" just relates to the packaging used and perhaps nothing has changed with the actual component. See [this page](https://www.ti.com/product/INA260/part-details/INA260AIPWR) for reference.




## Comments

### skot on 2025-06-22

The "R" suffix in this case means the chips are sold on a reel vs. a tube. (This kind of naming is traditional for TI, but unfortunately buried in the end of the datasheet) It seems like TI is discontinuing the tube. The parts are exactly the same.

I'll change the BOM
