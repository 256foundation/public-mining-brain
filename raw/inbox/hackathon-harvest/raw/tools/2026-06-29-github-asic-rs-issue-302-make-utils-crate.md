# 256foundation/asic-rs issue #302: make utils crate

> Source: https://github.com/256foundation/asic-rs/issues/302
> Collected: 2026-10-07
> Published: 2026-06-29

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 302
- State: closed
- Author: cfilipescu
- Opened: 2026-06-29
- Closed: 2026-06-29
- Labels: none

## Description

for functions such as the following:

```rust
    fn parse_number_string(value: &str) -> Option<f64> {
        value.trim().replace(',', "").parse::<f64>().ok()
    }

    fn parse_f64(value: &Value) -> Option<f64> {
        value
            .as_f64()
            .or_else(|| value.as_str().and_then(Self::parse_number_string))
    }

    fn parse_fan_rpm(value: &Value) -> Option<f64> {
        Self::parse_f64(value).or_else(|| {
            value
                .as_str()
                .filter(|s| s.contains("Socket connect failed"))
                .map(|_| 0.0)
        })
    }

    fn parse_u64(value: &Value) -> Option<u64> {
        value.as_u64().or_else(|| {
            value
                .as_str()
                .map(|s| {
                    s.trim()
                        .chars()
                        .take_while(|ch| ch.is_ascii_digit() || *ch == ',')
                        .collect::<String>()
                        .replace(',', "")
                })
                .filter(|s| !s.is_empty())
                .and_then(|s| s.parse::<u64>().ok())
        })
    }

    fn parse_number_tokens(value: &str) -> Vec<f64> {
        value
            .split(|c: char| !(c.is_ascii_digit() || c == '.' || c == '-' || c == ','))
            .filter_map(Self::parse_number_string)
            .filter(|value| *value > 0.0)
            .collect()
    }

    fn parse_temperature(value: &Value) -> Option<Temperature> {
        let temps = match value {
            Value::Array(values) => values
                .iter()
                .filter_map(Self::parse_f64)
                .collect::<Vec<_>>(),
            Value::String(value) => Self::parse_number_tokens(value),
            _ => Self::parse_f64(value).into_iter().collect(),
        }
        .into_iter()
        .filter(|value| *value > 0.0)
        .collect::<Vec<_>>();

        if temps.is_empty() {
            return None;
        }

        Some(Temperature::from_celsius(
            temps.iter().sum::<f64>() / temps.len() as f64,
        ))
    }
```

move these to a util file (on all firmwares), since that functionality should be pretty consistent across versions, and it helps clean up these miner implementation (which is only going to get more complex).

## Comments

### b-rowan on 2026-06-29

I think better to have this inside each firmware backend, such as `firmwares/antminer/utils.rs`
