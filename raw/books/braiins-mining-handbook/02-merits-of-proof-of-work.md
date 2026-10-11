# Bitcoin Mining Handbook — ch. 18: On the Merits of Proof of Work (extract)

> Source: https://braiins.com/books/bitcoin-mining-handbook (PDF: https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/63ebadbe407c5bc4621f0d2a_Handbook%20I_web%20verze_3.pdf) (Braiins Publishing, free PDF)
> Collected: 2026-10-10
> Published: 2022
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source PDF)

## Key points (ch. 18)

- Proof of work's "first application was not in solving for state consensus in a global monetary network" — Adam Back "first devised the scheme as a way to combat spam in Usenet and remailers" (as he recounts in a 2014 interview, Let's Talk Bitcoin - Episode #77). (p. 18)
- Hashcash genesis: the computer performs SHA1 hashes until it finds a "collision"; each collision mints "a digital 'stamp' that could be used as proof of postage paid" — "these stamps are the great ancestors of bitcoin itself." (pp. 19–20)
- "the bitcoin protocol is itself a giant communication network"; if "the cost to write to blocks were zero", spammers could fill blocks and censor legitimate transactions; one-address-one-vote consensus would enable "a Sybil attack". (pp. 19–20)
- "Because of proof of work, miners must complete trillions of hashes to find a block, which expends energy, and thereby costs money to produce." (p. 20)
- "Electricity is the highest grade energy available, and it is the currency of a digital world. When a block is secured, it can be measured in this base currency as the number of Joules (or kilowatt-hours) required to produce it." (p. 20)
- Cost formula (verbatim): "Bj (Joules to produce a block) = N (miners) x H' (avg hash exhaust rate in J/TH per miner) x G hashes (TH) required to produce a block." (p. 20)
- Monetization: "you multiply Bj by E (the electricity rate in $/kWh) to get the cost to produce a block B$"; miners "need to recoup a profit by a combination of the block reward (R), plus the user fees paid (F). That is, B$< R+F." (pp. 21–22)
- Takeaway (verbatim): "the energy expended will always be determined by the rewards available to the miners of the network, including fees for block space." (p. 22)
- On energy morality: "the electricity used is directly related to the value that users place on its block space"; bitcoin "is agnostic to the fuel source; whether it is carbon-intensive coal, or cleaner sources such as methane waste gas, hydro power, or renewables." (p. 22)
- PoS comparison: "the capital required to secure a proof of stake network is significantly higher than capital committed to PoW mining equipment (billions versus millions)." (p. 23)
- PoS centralization: "Due to the behavior of compounding, larger stakes will increase more quickly than smaller ones, which is a naturally centralizing force"; in the Ethereum 2 Beacon Chain "the top 5 validators comprise over one third of the entire stake—enough to halt or impair the network." (pp. 23–24)
- Conclusion: proof of work "has roots in defeating Sybil attacks and denial of service, and is what makes bitcoin economically unattractive to attack"; it "establishes a pay-to-use communications network, and assigns a cost to block space (bandwidth) that is directly related to the value that its users place on the ability to transact, via fees." (p. 24)
