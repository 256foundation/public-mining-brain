# emberone-usbserial-fw PR #3: add dma neopixel command

> Source: https://github.com/256foundation/emberone-usbserial-fw/pull/3
> Collected: 2026-10-10
> Published: 2025-03-15
> Registry ID: emberone-usbserial-fw

State: closed | Merged: 2025-03-15 | Author: skot | Type: PR
Closed: 2025-03-15 (merged as 3e4c60e9a6818dff1a16632d3633bd4bb8ae8c63)
Branch: 256foundation:add-neopixel → main

## Body

(no body)

## Comments

(none)

## Files changed (PRs only)

- Cargo.toml (+1/-0) — adds `smart-leds = "0.4.0"` dependency.
- Cargo.lock (+1/-0) — lockfile entry for smart-leds.
- src/control/led.rs (+52/-0) — new WS2812/neopixel driver bit-banged by PIO0 state machine 0 with DMA (not CPU timing loops); registers control command 0x10 `SetRGB { r, g, b }`; handler writes the one-pixel frame via `PioWs2812::write` and echoes the RGB triple back to the host.
- src/control/mod.rs (+13/-2) — dispatches new control-command id `LED_COMMAND: u8 = 8` (protocol slot after i2c=5, gpio=6); adds `CommandInner::Led`, `Controller.led` field, extends `usb_task` signature.
- src/main.rs (+7/-2) — binds `PIO0_IRQ_0`, constructs `Led::new(&mut common, sm0, p.PIN_1, p.DMA_CH0.into())` (neopixel data on PIN_1), passes it into `control::usb_task`.

Key hunks verbatim (command definition, src/control/led.rs, new file):

```rust
pub struct Led<'d> {
    ws2812: PioWs2812<'d, PIO0, 0, 1>,
}

impl<'d> Led<'d> {
    pub fn new(common: &mut Common<'d, PIO0>, sm: StateMachine<'d, PIO0, 0>, pin: impl PioPin, dma: embassy_rp::dma::AnyChannel) -> Self {
        let program = PioWs2812Program::new(common);
        let ws2812 = PioWs2812::new(common, sm, dma, pin, &program);
        Self { ws2812 }
    }

    pub async fn set_color(&mut self, r: u8, g: u8, b: u8) {
        let data = [RGB8::new(r, g, b)];
        self.ws2812.write(&data).await;
    }
}

#[derive(defmt::Format)]
pub enum Command {
    SetRGB { r: u8, g: u8, b: u8 }, // 0x10
}

impl Command {
    pub fn from_bytes(buf: &[u8]) -> Result<Self, CommandError> {
        match buf {
            [0x10, r, g, b] => Ok(Self::SetRGB { r: *r, g: *g, b: *b }),
            _ => Err(CommandError::Invalid),
        }
    }
}

impl super::ControllerCommand for Command {
    async fn handle(&self, controller: &mut super::Controller) -> Result<Vec<u8, 256>, CommandError> {
        match self {
            Command::SetRGB { r, g, b } => {
                controller.led.set_color(*r, *g, *b).await;
                Ok(Vec::from_slice(&[*r, *g, *b]).unwrap()) // Echo back the set color
            }
        }
    }
}
```

Dispatcher registration (src/control/mod.rs):

```diff
+pub mod led;
+const LED_COMMAND: u8 = 8;
```

```diff
+            LED_COMMAND => Ok(Self {
+                id,
+                bus: buf[1],
+                inner: CommandInner::Led(led::Command::from_bytes(&buf[3..])?),
+            }),
```

Pin bring-up (src/main.rs):

```diff
+    let pio::Pio { mut common, sm0, .. } = pio::Pio::new(p.PIO0, Irqs);
+    let led = control::led::Led::new(&mut common, sm0, p.PIN_1, p.DMA_CH0.into());
```
