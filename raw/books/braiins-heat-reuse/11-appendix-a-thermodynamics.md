# Bitcoin Mining Heat Reuse — appendix A: Energy & Thermodynamics for Bitcoiners (extract)

> Source: https://braiins.com/books/bitcoin-mining-heat-reuse?lang=en (Braiins Publishing, free distribution; authored by Tyler Stevens; foreword by Paul Jin Li)
> Collected: 2026-10-11
> Published: 2025
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source)
> Note: text extracted via pdftotext from the author's final per-chapter production PDFs; the typeset font's space glyph extracts as "!" and is normalized to spaces in quotes; typography otherwise verbatim.

## Key points (appendix A)

- Framing: "everything discussed in this bitcoin heat reuse book is grounded in physics. This is what makes bitcoin the first thermodynamically sound money." (p. 166)
- Energy and work: Energy can be defined as "the capacity to do work"; work "W=F*d" — lifting example: "100 N * 1 m = 100 Nm", and "1 Nm is equal to 1 J." (p. 166)
- Electrical work: "W=q * E * d" — charge through an electric field over a distance. (p. 167)
- Proof-of-work pun: "Bitcoin mining requires electrical work to perform the logic operations of the SHA-256 hash functions, hence the appropriately named proof-of-work description for the process!" (p. 168)
- Heat doing work: "When heat is added to a system, such as a gas, it increases the gas's pressure and volume, enabling it to do work" — "W=P * ∆V" — "The exact amount of work that can be performed by bitcoin miner heat energy is related to the temperature difference between the hot exhaust and the cold surroundings." (p. 168)
- Power: "Power is a measure of energy usage over time, denoted joules per second (J/s), also known as the watt W." — "A bitcoin miner drawing 3000 watts of electric power consumes 3000 joules of energy every second! Over an hour, this consumption amounts to 10.8 million joules (since 1 hour = 3600 seconds)." (pp. 168–169)
- Unit definitions: "1 BTU is the energy required to raise the temperature of 1 pound of water by 1 degree Fahrenheit"; "1 Therm = 100,000 BTU"; "1 hp is approximately equal to 746 W." (pp. 169–170)
- Heat-unit conversions: "1 kWh = 3,412 BTU" and "1 kW = 3,412 BTU/h" — "most heating infrastructure is rated in BTU/h, while bitcoin mining hardware is rated in kW." (p. 171)
- Watts vs watt-hours: "Watts measure power, which is the rate at which energy is used or generated. On the other hand, watt-hours measure the total amount of energy consumed or generated in a time period." Worked: "3000 Wh / 1 h = 3000 W / 6000 Wh / 2 h = 3000 W." (pp. 170–171)
- Temperature vs thermal energy: "Temperature is not a direct measure of energy. It is a measure of the average kinetic energy of particles in a substance." Thermal energy depends on "temperature, mass, and specific heat capacity" — specific heat capacity is "how resistant a substance is to changing temperature." (p. 172)
- First Law: "The First Law of Thermodynamics, also known as the Law of Energy Conservation, states that energy cannot be created or destroyed, only transformed from one form to another." — "Electric circuits are highly efficient at converting electric energy into heat... The result is a near-perfect conversion of electricity to heat." Example: "A 3000 W bitcoin miner exhausts approximately 3000 W of heat." (p. 173)
- Entropy humor: "If your hash boards start glowing, making noise or moving around, you've got a big problem on your hands!" (p. 173)
- Second Law: "for any energy transfer, the total entropy - a measure of disorder or randomness - of a system will always increase... energy transformations are inherently irreversible, and cannot be undone with perfect efficiency." Applied to mining: "entropy is generated when electricity is converted into heat throughout hash operations. This conversion is an irreversible process... The sum of all heat energy cannot be perfectly captured and converted back into electricity." (pp. 174–175)
- Third Law: "The Third Law of Thermodynamics defines absolute zero as the temperature at which the kinetic motion of particles approaches zero. Absolute zero is defined as -459.67°F, -273.15°C, or 0°K on the Kelvin scale." (p. 175)
- Quantity vs quality: "The amount of electric energy consumed by the bitcoin miners is equal to the heat energy they output... A one megawatt bitcoin mine must reject one-megawatt of heat. The quantity is conserved." — "The quality of energy, however, is not conserved... Electricity is high-quality... thermal heat energy is much lower in quality than electric energy." (p. 176)
- Exergy: "Exergy quantifies the portion of energy that can be converted into useful work, considering both its quality and the surrounding environment... Higher exhaust temperatures correspond to higher exergy, meaning the waste heat has greater potential for useful applications such as heating, boiling water, or even driving a heat engine." (p. 177)
- Carnot efficiency: "η max = 1 - (Tcold, ambient temp / Thot, fluid temp )" — "Here you can see the dependency of energy conversion efficiency on the temperature difference." (p. 178)
- Low-grade classification: "The output fluid temperatures from bitcoin miners typically range from 40-70°C. This range is commonly referred to as low-grade heat... Generally, temperatures below 150°C (302°F) are classified as low-grade. Bitcoin miner heat exhaust falls into the specific category of ultra low-grade heat, with temperatures below 100°C (212°F) – the boiling point of water." (p. 178)
- Work limitation: "low-grade heat is extremely inefficient at converting into work compared to energy transfer from higher quality (temperature) heat sources. As a result, bitcoin miners are generally not suitable for industrial processes where heat energy is converted back into useful work." (p. 178)
- Direct-use thesis: "the best application of hashrate heat is to use this waste energy directly for system heating, rather than convert the heat back into work... we lose efficiency with each step of energy conversion." (p. 179)
- Closing credo: "Mining bitcoin is the most thermodynamically sound method for heating. Not a single joule of energy is put to waste. Instead, each one serves a dual purpose." (p. 179)
- Section flow: ENERGY & WORK (mechanical / electrical / W=P*∆V) → POWER → UNITS (Units of Energy / Units of Power / Common Units in Bitcoin Mining) → TEMPERATURE VS THERMAL ENERGY → LAWS OF THERMODYNAMICS (1st / 2nd / 3rd) → QUANTITY VS QUALITY (exergy, Carnot) → LOW GRADE HEAT → HEAT FOR HEATING (pp. 166–179)
