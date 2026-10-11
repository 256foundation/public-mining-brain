# Heat for Adsorption Chiller

> Source: https://forum.heatpunks.org/t/heat-for-adsorption-chiller/147
> Collected: 2026-10-10
> Published: 2025-06-22
> Registry ID: heatpunks-forum

jwb | 2025-06-22 22:54:20 UTC | #1

Anyone ever consider how to use miner waste heat for the heat portion of an adsorption chiller home setup. If I could figure that out I could run my miners at home all year round

-------------------------

power2bit | 2025-06-26 11:26:11 UTC | #2

Yes, we’ve looked into this for our heat reuse projects in Germany. Haven’t installed absorption cooling yet… mainly because we’re still not sure it makes economic sense. Cooling demand in summer is much lower than heating demand in winter, so only part of the mining heat could be reused.

Technically it should be doable, but whether it pays off depends on your cooling needs. Would be great to hear from anyone who’s actually running something like this!

For small setups, the **Yazaki WFC‑SC5** could be an option:

- Cooling output

  : ~17.6 kW

- Heat input

  : ~25 kW @ ~85 °C

- COP

  : ~0.7

- Used price

  : €4,000–10,000 (if you can find one)

That would require a few hydro miners (e.g. WhatsMiner M64, ~5 kW thermal each), depending on how much cooling you actually need.

-------------------------

thak777 | 2025-07-04 19:49:26 UTC | #3

I’m not an HVAC guy, so I talked with Gab.ai a bit on this (summary included at the bottom of this post.)

The questions that I ended up with:

1. Can you get the Whatsminer hydro units to 85C without a problem?

2. Does the adsorption unit actually need the 85C to work, or is it just “most efficient” when it hits that temp?

3. Could you actually start with just a couple of miners and then ramp up?

4. Why aren’t there very many adsorption options out there? I couldn’t find more than a couple of examples…seems like a wide open space for heatpunks…

I do have to say that I thought the “well, if Bitcoin will stay over $80k…” was precious.

---------- AI SUMMARY ----------

### **ROI Calculation for 4x Whatsminer M64 Hydro + Yazaki Chiller Setup**

#### **1. Upfront Costs (Estimated)**

| **Item** | **Cost (USD)** | Notes |
|---|---|---|
| 4x Used M64 Hydro Miners | $8,000–$12,000 | (~$2k–$3k/unit, used market) |
| Yazaki WFC-SC5 Chiller | $4,000–$10,000 | (Used, if available) |
| Plumbing/Pumps/Controls | $2,000–$5,000 | (Pipes, heat exchangers, etc.) |
| **Total Initial Cost** | **$14,000–$27,000** |  |

**(We’ll use $20,000 midpoint for calculations.)**

---

#### **2. Daily Profit (From Earlier, BTC at $100k)**

- Mining Profit

  :

  +$23.56/day

- Cooling Savings

  :

  +$12.07/day

- Total Daily Profit

  :

  $35.63/day

#### **3. Annual Profit (Assuming 365 Days Operation)**

- $35.63 × 365 = $13,005/year

#### **4. ROI Time (Break-Even Point)**

- $20,000 ÷ $13,005/year = ~1.54 years (18.4 months)

---

### **5. Sensitivity Analysis (What If Things Change?)**

#### **A. If Bitcoin Price Drops to $70k**

- Mining profit drops to

  ~$10.13/day

  (from earlier).

- Total Daily Profit

  :

  $10.13 + $12.07 = $22.20/day

- ROI Time

  :

  $20,000 ÷ ($22.20 × 365) = ~2.47 years (29.6 months)

#### **B. If Electricity Costs Rise to $0.12/kWh**

- Mining profit drops to

  $14.92/day

  (at $100k BTC).

- Total Daily Profit

  :

  $14.92 + $12.07 = $26.99/day

- ROI Time

  :

  ~2.03 years (24.4 months)

#### **C. Best-Case Scenario (BTC $120k, $0.08/kWh)**

- Mining profit:

  ~$38.20/day

- Cooling savings:

  $12.07/day

- Total Daily Profit

  :

  $50.27/day → ROI in ~1.09 years (13 months)

---

### **6. Additional Considerations**

:white_check_mark: **Maintenance Costs**:

- Miners (~$0.01/kWh in upkeep) →

  ~$2.56/day

  (~$935/year).

- Chiller maintenance (~$500/year).

  →

  Reduces annual profit to ~$11,570

  →

  ROI ~1.73 years (21 months)

  .

:white_check_mark: **Tax Implications**:

- Mining income is taxable (varies by country).

:white_check_mark: **Hardware Lifespan**:

- Miners last

  ~3–5 years

  (degrading efficiency over time).

- Chiller lifespan

  ~10–15 years

  if maintained.

---

### **7. Final ROI Verdict**

| **Scenario** | **ROI Time** |
|---|---|
| **Base Case ($100k BTC, $0.10/kWh)** | **~1.5 years** |
| **BTC $70k** | **~2.5 years** |
| **BTC $120k + Cheap Power** | **~1.1 years** |
| **With Maintenance Costs** | **~1.7–2 years** |

---

### **Conclusion: Is This Worth It?**

:white_check_mark: **Yes, if:**

- Bitcoin stays

  above $80k

  and your electricity is

  ≤$0.10/kWh

  .

- You

  need cooling anyway

  (otherwise, just mine without the chiller).

- You’re okay with

  1.5–2.5 year payback

  .

:cross_mark: **No, if:**

- Bitcoin crashes

  below $60k

  or electricity gets

  > $0.12/kWh

  .

- You don’t want

  hardware maintenance hassle

  .

**Next Steps?**

- Refine cost estimates (get exact quotes for used miners/chiller).

- Test if your hydro miners can

  consistently supply 85°C water

  .

- Consider

  partial deployment

  (start with 2 miners, scale up).
