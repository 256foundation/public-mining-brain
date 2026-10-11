# emberone-usbserial-fw PR #4: add adc command

> Source: https://github.com/256foundation/emberone-usbserial-fw/pull/4
> Collected: 2026-10-10
> Published: 2025-03-15
> Registry ID: emberone-usbserial-fw

State: closed | Merged: 2025-03-16 | Author: skot | Type: PR
Closed: 2025-03-16 (merged as ab005630d97cce7e49c9974d351cbf4606499f88)
Branch: 256foundation:add-adc → main

## Body

(no body)

## Comments

(none)

## Files changed (PRs only)

- src/control/adc.rs (+40/-0) — new ADC reader; control commands 0x50 `ReadVdd` and 0x51 `ReadVin`; returns raw 16-bit sample as little-endian bytes (`value.to_le_bytes()`).
- src/control/mod.rs (+14/-2) — dispatches new control-command id `ADC_COMMAND: u8 = 7` (protocol slot order: i2c=5, gpio=6, adc=7, led=8); adds `CommandInner::Adc`, `Controller.adc` field, extends `usb_task` signature.
- src/main.rs (+10/-1) — binds `ADC_IRQ_FIFO`; wires `vdd: Channel::new_pin(p.PIN_26, Pull::None)` and `vin: Channel::new_pin(p.PIN_27, Pull::None)` (board voltage sense pins).

Key hunks verbatim (command definition, src/control/adc.rs, new file):

```rust
pub struct Pins<'d> {
    pub adc: Adc<'d, embassy_rp::adc::Async>,
    pub vdd: Channel<'d>,
    pub vin: Channel<'d>,
}

#[derive(defmt::Format)]
pub enum Command {
    ReadVdd, // 0x50
    ReadVin, // 0x51
}

impl Command {
    pub fn from_bytes(buf: &[u8]) -> Result<Self, CommandError> {
        match buf {
            [0x50] => Ok(Self::ReadVdd),
            [0x51] => Ok(Self::ReadVin),
            _ => Err(CommandError::Invalid),
        }
    }
}

impl super::ControllerCommand for Command {
    async fn handle(&self, controller: &mut super::Controller) -> Result<Vec<u8, 256>, CommandError> {
        let adc = &mut controller.adc.adc;
        let value = match self {
            Command::ReadVdd => adc.read(&mut controller.adc.vdd).await,
            Command::ReadVin => adc.read(&mut controller.adc.vin).await,
        }
        .map_err(|_| CommandError::Message("ADC Read Error"))?;

        Ok(Vec::from_slice(&value.to_le_bytes()).unwrap())
    }
}
```

Dispatcher registration (src/control/mod.rs):

```diff
+pub mod adc;
+const ADC_COMMAND: u8 = 7;
```

Pin wiring (src/main.rs):

```diff
+    let adc = adc::Adc::new(p.ADC, Irqs, Default::default());
+    let adc_pins = control::adc::Pins {
+        adc,
+        vdd: adc::Channel::new_pin(p.PIN_26, gpio::Pull::None),
+        vin: adc::Channel::new_pin(p.PIN_27, gpio::Pull::None),
+    };
```
