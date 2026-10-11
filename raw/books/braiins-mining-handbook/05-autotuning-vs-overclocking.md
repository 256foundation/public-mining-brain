# Bitcoin Mining Handbook — ch. 42: Autotuning vs. Overclocking for Bitcoin Miners (SHA-256 ASICs) (extract)

> Source: https://braiins.com/books/bitcoin-mining-handbook (PDF: https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/63ebadbe407c5bc4621f0d2a_Handbook%20I_web%20verze_3.pdf) (Braiins Publishing, free PDF)
> Collected: 2026-10-10
> Published: 2022
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source PDF)

## Key points (ch. 42)

- Two ways to boost a mining operation's top line: "Buy new hardware" or "Improve the performance of their current hardware"; new hardware "typically involves a large up-front capital expenditure that will likely take many months or even years to get a positive ROI". (p. 42)
- Overclocking definition: "the ASICs consume more power, hash at higher frequencies, and produce more valid proofs of work than at stock settings" — i.e. max W/TH (more hashrate, less efficiency). (p. 42)
- Overclocking example: "an Antminer S9 that typically produces 13.5 TH/s at 1200 W consumption could be overclocked to produce 16 TH/s at 1600 W consumption instead." (pp. 42–43)
- "The hash price ($/TH of hashrate) has consistently dropped over time as difficulty has risen" — miners rush to extract revenue "before their profit margins get squeezed thin by the rising difficulty." (p. 43)
- Silicon lottery: "every individual device is unique in terms of the quality of the hashing chips... primarily due to the fact that silicon quality is not 100% uniform"; manufacturers "make the ASIC specifications much lower than the maximum performance possible" for standardization. (pp. 43–44)
- Autotuning definition: "autotuning firmware can calibrate the frequency on a per-chip basis... the firmware finds an optimal frequency for every individual chip, sending higher frequencies to higher quality chips or lower frequencies to lower quality chips" — i.e. max TH/W. (p. 44)
- Headline example: "the same Antminer S9 that typically produces 13.5 TH/s at 1150 W consumption with stock firmware could produce 15.5 TH/s at 1150 W consumption with a per-chip autotuning firmware." (p. 44)
- "For miners who have very cheap or even free electricity, overclocking + autotuning is the most effective way to maximize the amount of BTC mined." (p. 44)
- Low-power mode: "miners can set their power limit at 800 or 900 Watts for S9s and achieve an efficiency in the 70-75 W/TH with air cooled machines" (better still with immersion cooling). (p. 45)
- Value proposition (verbatim): "The key value proposition of autotuning firmware is that it will optimize ASIC efficiency at any power limit that you specify, lowering your costs for every satoshi of revenue you earn." (p. 45)
- Market trajectory: "While autotuning is still relatively uncommon today, it will likely become a standard practice among miners within 1-2 years." (p. 46)
- Strategy framing: in bull markets "autotuning and overclocking tends to be the most common combination"; at low margins "autotuning at low power limits was very useful for miners using Antminer S9s around the time of the last halving". (p. 45)
