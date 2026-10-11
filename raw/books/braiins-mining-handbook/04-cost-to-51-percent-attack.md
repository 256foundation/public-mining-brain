# Bitcoin Mining Handbook — ch. 32: How Much Would it Cost to 51% Attack Bitcoin? (extract)

> Source: https://braiins.com/books/bitcoin-mining-handbook (PDF: https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/63ebadbe407c5bc4621f0d2a_Handbook%20I_web%20verze_3.pdf) (Braiins Publishing, free PDF)
> Collected: 2026-10-10
> Published: 2022
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source PDF)

## Key points (ch. 32)

- A 51% attack enables censorship of transaction confirmation and double spends via "a blockchain reorganization because it replaces the most recent blocks in the chain." "So far, there have been no successful 51% attacks on Bitcoin in its history, but we have seen successful attacks on other coins like Ethereum Classic." (p. 32)
- Crypto51's "1h Attack Cost" uses the spot price for hashrate from NiceHash; "For Bitcoin, the NH-able value is under 1%, and other hashrate exchanges do not add much to the value" — the volume of SHA-256 hashrate on markets "is not nearly large enough" for an attack. (pp. 32–33)
- Key distinction: "hashrate sold on an exchange or via cloud mining contracts as synthetic hashrate, and hashrate used to mine directly as physical hashrate." (p. 33)
- Physical-attack math (January 2021 context): "With the current total network hashrate of 150 EH/s" and the most efficient ASIC, "the Antminer S19 Pro... 110 TH/s and 3250 W consumption" (p. 35)
- "150,000,000 TH/s / 110 TH/s = approximately 1.364M ASICs needed to amass 150 EH/s." (p. 35)
- "With a per-unit consumption of 3250 W, that would put the electricity capacity needed to power all those ASICs at ~4.4 GW of power." (p. 35)
- Hardware cost: "at a conservative unit price of $4000 each including power supply units, the cost of hardware would exceed $5.46 billion"; chip supply is a bottleneck via "chip manufacturers like Samsung and TSMC" (hardware makers "already sold out until May 2021"). (p. 35)
- Pool concentration (January 2021): "~97% of Bitcoin's total network hashrate goes through Chinese pools." (p. 36)
- Asymmetric vectors: "attacking with physical hashrate would cost at least $5 billion, whereas attacking with synthetic hashrate by taking over several pools would be essentially FREE" — but "miners can switch pools in a matter of seconds". (p. 37)
- Summary: physical hashrate attack costs "~$5.5 billion as a conservative estimate at the time of writing", or coordinating seizure of farms is "an extremely difficult coordination problem likely involving 100+ operations"; synthetic hashrate attack = "simultaneously take over 3-5 mining pool operations". (p. 39)
- Mitigation via Stratum V2: "miners will be able to construct blocks themselves with data from their own nodes (a process called Job Negotiation), so if they are honest they'll always reference the prevhash of the most recent block in the chain" — preventing use of their hashrate for a secret "shadow" chain reorg or for mining "a different SHA-256 chain, such as Bitcoin Cash or Bitcoin SV." (p. 38)
- Detection design: "the attack causes more damage the longer it is sustained, so it can be mitigated by ensuring that some miners would detect it within minutes and switch pools." (p. 37)
