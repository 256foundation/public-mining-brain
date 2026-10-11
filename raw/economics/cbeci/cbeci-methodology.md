# CBECI Methodology — verbatim capture

> Registry ID: cbeci-methodology
> Source: https://ccaf.io/cbnsi/cbeci/methodology
> Collected: 2026-10-10
> Published: live page (methodology current as of model v1.4.0; change-log link present but stale — see note at end)
> Posture: verbatim
> As-Of: 2026-10-10

The following is the complete server-rendered (SSR) text of the methodology page, captured verbatim on 2026-10-10 (HTTP 200, 300,931 bytes HTML; text extracted preserving heading/paragraph/list/table structure; equation images and figure charts render as images in the original and are noted as [figure]/[equation] where they interrupt the text flow; footnotes are numbered as on the page but the footnote list itself is rendered client-side and was not present in SSR — superscript numbers retained).

---

# Methodology

## Overview

### Summary

The Cambridge Bitcoin Electricity Consumption Index (CBECI) provides up-to-date estimates of Bitcoin's daily power demand and an annualised electricity consumption estimate. The applied methodology is based on a hybrid top-down approach initially developed by Marc Bevand, building a basket of real-world hardware with the underlying assumption that mining nodes ('miners') are rational economic agents that only use profitable hardware.

Given that the actual power demand cannot be determined due to the decentralised nature of the network, we made several assumptions, including hypothetical lower-bound (floor) and upper-bound (ceiling) estimates. These two boundaries encompass a best-guess estimate, a more accurate indication of the actual power demand.

The lower-bound estimate is the theoretical minimum total power demand based on the best-case assumption that all miners always use the most energy-efficient equipment. The upper-bound estimate is the theoretical maximum total power demand based on the worst-case assumption that all miners always use the least energy-efficient hardware as long as running the equipment remains profitable in terms of electricity costs. The best-guess estimate is based on the more realistic assumption that miners use a combination of profitable hardware.

### Representation

The CBECI landing page displays two measurements for each type of estimate. The first figure refers to the total electrical power consumed by the Bitcoin network, expressed in gigawatts (GW). Updated every 24 hours, this figure indicates the rate at which bitcoin miners currently consume electricity, describing the existing demand or load.

The second figure pertains to the estimated annual electricity consumption of the Bitcoin network, conveyed in terawatt-hours (TWh). This annualised measurement assumes constant power usage at the aforementioned rate over a one-year period. To mitigate the effects of short-term hashrate fluctuations and render the results more suitable for comparisons with alternative uses of electricity, we apply a seven-day moving average to the resulting data point.

### Model parameters

The CBECI model considers the parameters outlined in Table 1. The following sections specify how we calculated each estimate and what assumptions were made.

#### Table 1: CBECI model parameters

| Parameter | Symbol of parameter | Description | Measure/Unit | Source |
|---|---|---|---|---|
| Mean Bitcoin network hashrate | H | The average number of hashes performed each second on a given day | Terahashes per second (TH/s) | Dynamic: Frequency: Daily |
| Block subsidy | B | The aggregated value of all newly minted bitcoins on a given day | USD | Dynamic: Frequency: Daily |
| Transaction fees | F | The aggregated value of all transaction fees on a given day | USD | Dynamic: Frequency: Daily |
| Mining equipment efficiency | η | A measure of the energy efficiency of a given mining hardware type | joules per Terahash (J/TH) | Dynamic: estimate — Derived from specifications of over a 100 different device types — Frequency: Daily |
| Electricity cost | P | The global average cost of electricity incurred by miners | USD per kilowatt-hour (USD/kWh), or USD per Joule (USD/J), with USD/J = USD/kWh/3,600,000 | Static: estimate (assumption) |
| Power usage effectiveness (PUE) | PUE | A measure of how efficiently energy is used in a data centre | – | Static: estimates (assumptions) |

## CBECI Model

### Selecting mining equipment

In the early days of Bitcoin, mining was primarily conducted using general-purpose graphics processing units (GPUs) and field-programmable gate arrays (FPGAs). This changed significantly in 2012 with the introduction of the first application-specific integrated circuits (ASICs). ASICs, specialised hardware specifically optimised for Bitcoin mining, are orders of magnitude more efficient than their predecessors. Consequently, the use of ASICs quickly displaced GPU and FPGA mining.

We have collated a list of over 100 distinct Bitcoin ASIC models designed for SHA-256 operations launched since 2013. It was compiled from various public resources detailing different mining equipment types and their specifications.1 For the pre-ASIC era (2009–2013), we selected hardware based on research conducted by Taylor (2016) and our observations. Due to the lack of available performance data in 2009, we chose the Intel Core i5-650 model even though it was launched in January 2010.

The versions before v1.2.0 were based on the full list of hardware, which may have occasionally overstated Bitcoin's total power demand due to several factors. With v1.2.0, we introduced the following changes to address this issue:

- Consolidated hardware manufacturers to exclude 'exotic' devices: We only considered ASIC hardware from the three major manufacturers, Bitmain, MicroBT and Canaan, which have an estimated combined market share of at least 85%.2 This change removes 'exotic' devices with little to no sales from the hardware list. It is important to note that this does not apply to hardware released before July 2014.
- Introducing a maximum economic lifetime of five years: This constraint reflects the finite usability of hardware. The lack of such a constraint may risk overstating the power demand by including nominally-profitable but long-disposed hardware models.
- Removed Coinmetrics's estimate for Bitmain S7 and S9 hardware share: We retroactively returned to an equally weighted basket of profitable hardware models. Potential issues related to the underlying nonce analysis may have overstated the share of older, less efficient Bitmain S7 and S9 ASIC models in the previous hardware mix distribution.

With the introduction of v1.4.0, the condition of a 'maximum economic lifetime of five years' will be integrated into a newly introduced weighting mechanism. Details on this mechanism will be elaborated on later.

The mining efficiency of each machine type is expressed in joules per terahash (J/TH). Since the actual power usage can vary significantly based on several factors (e.g., usage conditions, overclocking), the manufacturer specifications have been adjusted with the help of experts to reflect real power usage more accurately. The complete list is available at http://sha256.cbeci.org and is open to comments and suggestions. Figure 1 illustrates the evolution of bitcoin mining equipment efficiency from late 2014.

#### Figure 1: Evolution of bitcoin mining equipment efficiency

[chart] Note: A 1,000 W mining device that generates 10 Th/s has an efficiency of 100 J/Th. This chart is based on a list of 100+ SHA-256 mining equipment.

### The profitability threshold

The CBECI model is predicated on the notion that miners are rational economic agents who only operate their devices for as long as they are profitable. To determine whether a particular mining device from our list can be included in the group of profitable hardware, the miner's revenue derived from the mining activity must be equal to or greater than the cost of operating the hardware on a given day (Equation 1). The operating cost for each hardware model in the list is calculated by multiplying the cost of electricity per joule (P) by the device's energy efficiency (η).

This results in the following mathematical inequality:

[equation 1]

with,

[equation symbols]

Miners' electricity costs vary significantly, making it challenging to assume a universally applicable value. A vast array of factors contributes to this complexity, including variations in pricing between countries, within countries, and fluctuations over time. Electricity costs also depend on whether consumers are retail or wholesale, and if wholesale, whether they have signed Power Purchase Agreements (PPAs) with rates that differ from local pricing schemes. Additionally, some miners generate their own electricity, further complicating the cost calculation. In light of these complexities, we assume that, on average, miners pay USD 0.05 per kilowatt-hour (USD/kWh). This default value is based on in-depth conversations with miners worldwide and is consistent with estimates used in previous research.3

Note: The CBECI landing page allows visitors to choose different values for the electricity cost parameter in order to explore how electricity prices influence hardware selection and total electricity consumption.

Further, the gathered data and Assumption 1 allowed us to compute a profitability threshold (Equation 2) over time, showing the minimum efficiency required for the hardware to be profitable (Figure 2). As can be seen, the profitability threshold decreased over time, suggesting that miners gradually had to invest in more efficient hardware to stay competitive as older and less efficient hardware became uneconomical.

#### Figure 2. Profitability threshold of mining equipment at 0.05 USD/kWh

[chart]

The profitability threshold θ is calculated using Equation 3:

[equation 3]

Each day a set of eligible mining hardware uniquely indexed by i with an associated efficiency of ηi is created from our list (Equation 4). The profitability threshold is then used to compile a subset of efficiencies of profitable mining hardware (S(P)) given electricity price P (Equation 5). S(P) is created daily and contains all mining hardware i with an energy efficiency (J/TH) less than or equal to the computed profitability threshold θ(P) that day (Equation 5). In this context, it should be noted that a lower J/TH value is indicative of higher energy efficiency.

Occasionally, there might be a period during which there is no profitable hardware, resulting in an empty set S(P). In this case, Assumption 2 applies.

It is reasonable to assume miners will not immediately switch off unprofitable hardware unless unfavourable market conditions persist for an extended period. To account for this, we applied a 14-day moving average to the profitability threshold to smooth the process of rebalancing S(P) and avoid it being subject to short-term fluctuations in mining profitability.

The absence of accessible price data before 18 July 2010 causes our model to assume no electricity consumption, as no profitability threshold can be computed. Accordingly, our model infers that no economically rational actor would mine bitcoin until BTC price data becomes available. In reality, however, several individuals or entities, undeterred by the lack of economic incentives, did contribute their computing power to the network. A rudimentary analysis that disregards profitability suggests that this comprised a daily average of fewer than 85 CPUs immediately before the model's inception, which can reasonably be neglected.

### Constructing the lower bound estimate

In the best-case scenario, we assumed all miners always use the most energy-efficient equipment to maximise profit. Therefore, we based the lower-bound estimates (Dlower and Elower) on Assumptions 3 and 4.

This assumption also implies that miners will upgrade their mining gear as soon as more energy-efficient hardware becomes available.

Power usage effectiveness (PUE) measures data centre energy efficiency. Data centres typically consume more energy than is needed to operate the servers because of factors such as cooling and supporting IT equipment. The higher the PUE ratio, the less efficient the energy use. Data centres with a PUE below 1.2 are typically considered efficient. For reference, Google's average PUE is 1.10, while the average PUE of most data centres is 1.8 or higher.

In bitcoin mining, electricity accounts for a substantial portion of operational costs.4 Hence, this motivates mining farm operators to enhance cooling systems, reducing total costs. Dialogue with miners confirms that mining facilities generally exhibit markedly lower PUE than conventional data centres.

Under optimal circumstances, mining facilities have refined data centre operations to the point where overheads are almost insignificant. We represent this scenario by presuming a PUE of 1.01.

The lower-bound estimates are calculated using Equations 6 and 7:

[equations 6–7]

The lower-bound estimate corresponds to the absolute minimum power demand of the Bitcoin network. While this is useful for providing a quantifiable minimum, it is a purely hypothetical value that is non-viable for various reasons, such as the following:

- Not all miners use the most efficient hardware: A miner will likely continue operating less efficient equipment as long as mining revenue is somewhat higher than costs.
- Long delivery and installation times: Delivery and installation of new equipment can take several months after release.
- Hardware supply shortage: The most efficient hardware may not be available in sufficient quantities that could reasonably be responsible for the total Ethereum network hashrate.
- Optimistic PUE: Not all mining facilities have an optimal PUE.

### Constructing the upper bound estimate

Estimating the upper-bound figures (Dupper and Eupper) is more challenging. One option is to assume a worst-case scenario where every miner employs the least efficient computational device available capable of computing cryptographic hashes, for example, a central processing unit (CPU) that powers a computer, a tablet or even a smartphone. Given the exponential surge in Bitcoin's network difficulty since 2016, such an assumption would soon result in a consumption figure that exceeds the world's total electricity generation. And this does not even consider the considerable financial losses miners would bear. Therefore, we have revised the assumption.

In this case, we assumed that the PUE for all mining sites is 1.20. While common data centre standards still consider this valid, it lies at the upper end of the PUE values reported by miners.

Therefore, the upper-bound estimates are calculated using Equations 8 and 9:

[equations 8–9]

The upper-bound estimate corresponds to the absolute maximum power demand of the Bitcoin network. While useful for providing a quantifiable maximum, it is a purely hypothetical value that is non-viable for various reasons, such as the following:

- Miners are interested in the most energy-efficient hardware: Large mining operators with industrial-scale data centres compete to be the first to access the most energy-efficient ASIC generations to increase operational profitability.
- Old equipment is replaced: Miners will likely replace old ASIC generations that have been unprofitable for a long time with new equipment rather than store old equipment for years, hoping the profitability threshold will rise.
- Bottlenecks in hosting space: Rational miners will always use the most efficient hardware if they have limited space to operate the equipment.
- Impact of other operating expenses: Failure to account for additional expenses, such as maintenance costs, can artificially inflate the economic life expectancy of inefficient hardware.

### Constructing the best-guess estimate

Considering that both lower- and upper-bound estimates rest upon improbable assumptions, we attempt to present a more precise estimate that adequately quantifies Bitcoin's actual electricity consumption.

In practice, many miners do not operate a single type of mining equipment, and they do not transition to the latest-generation hardware at the same time, if indeed they do at all. Likely, miners use a mix of different models, provided the equipment remains profitable in terms of electricity consumption (remains below the profitability threshold).

The challenge lies in continually determining an appropriate weighting approach for all profit-yielding equipment types, factoring in the varying market and network conditions over time. Analysing the market share progression of the predominant mining manufacturers could be a suitable proxy. However, reliable market share data spanning multiple periods is unfortunately unavailable.

In the initial iteration of the CBECI model, we presumed that all miners use an equally weighted selection of hardware types that are economically viable in terms of electricity consumption. In other words, we inferred that all profit-yielding machines were uniformly distributed among miners. Despite evident limitations to this methodology (for example, various hardware types may not have been manufactured and sold in equal quantities, certain equipment might not have been universally accessible simultaneously, and some machines might have been fully decommissioned despite a brief resurgence in profitability), the resulting outcomes were strikingly comparable to other methodologies, such as, for example, Stoll et al.'s (2019) market share analysis.5

Update 1.1.0 introduced a dataset estimating the market share of the Bitmain Antminer S7 and S9 machines. This evolving dataset is derived from the nonce distribution analysis methodology pioneered by Coin Metrics, which has generated reliable estimates that broadly align with the findings from other methodologies and studies.6 Over time, the reliability of this methodology appeared to diminish as estimates began to likely overstate the proportion of operational devices. This consequently led to us retroactively adopting a wholly equally weighted approach, eliminating the S7 and S9 parameters in v1.2.0.

The latest update (v1.4.0) marks a significant change in how we compute our best-guess estimate. This change was made after closely examining the findings from our analysis of the factors that drove the substantial increases in hashrate observed in recent years, and evaluating how the previous equally weighted approach represented these factors. Our analysis revealed that the prior methodology disproportionately emphasized the influence of older hardware on the hashrate, especially in 2021, when bitcoin mining was exceptionally profitable. This resulted in a noticeable underrepresentation of newer hardware and an overemphasis on older hardware.

Consequently, a novel approach was devised to address the identified shortcomings of the previous methodology. The refined method effectively distinguishes devices based on their release dates, assigning more weight to newer and less to older hardware. We drew on the depreciation schedules of publicly listed bitcoin mining companies to gauge which weighting factors to apply and how to implement them. While there were noticeable differences between the chosen methods, frequently employed were straight-line depreciation and the use of an estimated economic lifetime of five years.7 This led us to incorporate a similar logic into our model, where we assigned each device in set S(P) a weighting factor (based on its release date) ranging from 1 to 0, decreasing in five steps of 0.2. This adjustment ensures that the technical advancements of bitcoin mining hardware and its impact on the hashrate are more accurately represented than in a purely equally weighted approach.

In addition to introducing the aforementioned weighting mechanism, the update addresses another shortcoming: the previous assumption that hardware is operational immediately after its release. Evidence suggests a time lag between the release and deployment dates exists. Determining the precise length of this time lag is difficult, as it largely depends on the buyer's location and mode of transportation.8,9 Estimated delivery times exhibit significant variation, ranging from one week10 to a month or more.11,12 Given China's 2021 ban on cryptocurrency mining and the likely ensuing surge in long-haul transportation, the longer duration seems more plausible. To account for this issue, we have incorporated a delay of two months from the hardware's release date to when it is considered in our model, henceforth referred to as the deployment date.

Below is a summary of the methodology used to compute our best-guess estimate.

In the best-guess estimate, all mining farms are assumed to have a PUE of 1.10.13 This figure, albeit marginally more conservative than other estimates, has been validated numerous times through private dialogue with miners and experts in the field.

Hence, our best-guess estimates can be mathematically expressed as in Equations 10 and 11:

[equations 10–11]

In contrast to both the best- and worst-case scenarios, which use min(S(P)) and max(S(P)), respectively, our best-guess scenario uses the weighted average energy efficiency of profitable hardware, as in Equation 12:

[equation 12]

A crucial component in calculating the average energy efficiency of profitable hardware is the weighting factor introduced in update v1.4.0. Equation 13 illustrates how this weight adjustment is implemented. Depending on the deployment date, a value between 1 and 0 is assigned to all profitable devices. Models five or more years past their deployment date or whose deployment date is in the future are assigned 0, effectively excluding them from further calculations. Once a weight unit W is assigned to hardware i, its share of S(P) can be determined.

The weight factor assigned depends on the number of months that have elapsed since the estimated deployment date of hardware i. Here, 'deployment' refers to the month and year in which hardware i was released (i.e., mm/yyyy), with an additional two months added to account for the delay between the hardware's release and operational dates, as shown in Equations 14 and 15:

[equations 14–15]

The following section provides more details about the limitations of our methodology.

## Discussion

### Limitations of the model

Every theoretical model is an incomplete representation of reality that relies on specific assumptions, some of which may be debatable. As a result, they all have limitations that need to be discussed. To that end, the current CBECI model exhibits the following limitations (the list is non-exhaustive):

- Depending on electricity cost estimates: Electricity costs vary significantly between countries, regions and providers. Prices are generally dynamic and fluctuate, for example, according to the season and quantity of electricity consumed. Altering the default electricity cost assumption can substantially change the model output.
- Ignoring other cost factors: The model does not incorporate other factors that influence miners' decisions to switch off and replace existing equipment, such as maintenance and cooling costs.
- The exact composition of operational hardware remains unknown: The transition from a purely equally weighted approach to a weighted one in update 1.4.0 has mitigated the effects of using a hypothetical hardware basket. Nevertheless, this limitation remains significant, as the exact global composition of hardware used cannot be precisely determined. For transparency, our index page includes a chart outlining our assumed hardware energy efficiency estimates for all scenarios (best case, best guess, worst case) over time.
- Proprietary mining of manufacturers: We may not be aware of new and more efficient hardware that is not yet available on the market. Some have argued that manufacturers use proprietary equipment for their own benefit before public release.14
- Hardware specifications may not correspond to real performance: Hardware manufacturers often advertise their products' performance and energy efficiency using best-case scenarios. Additionally, the model does not consider that miners may overclock or underclock their machines for various reasons.
- Short switching periods: It is unlikely that miners react quickly enough in response to short-term fluctuations in the profitability threshold. Although we attempted to smooth the effect of short-term hashrate variations and price volatility by applying a 14-day moving average (profitability threshold), this may not be sufficient.
- Time lag for hardware updates: Although we consistently add new ASIC devices into our public list of bitcoin mining hardware, the inclusion in our model usually occurs in conjunction with other updates. Consequently, there may be a delay between adding hardware to our publicly available list and including it in our estimates. All considered hardware is assigned a version number, indicating the update in which it was included.

While we can confidently presume that most limitations do not substantially influence the estimation results, we acknowledge the inherent imperfections. The CBECI estimates are continually refined in response to new insights becoming available, and all changes are transparently documented in the change log.

Please feel free to message us if you have any suggestions on how we could improve the index.

### How does the CBECI compare to other estimates?

There have been multiple attempts to estimate the annualised (ann.) electricity consumption of the Bitcoin network. Table 2 is a non-exhaustive list of studies, reports and live estimates. However, it is important to note that estimates may vary considerably over time and on the methodology used; therefore, it is essential to consider the publication date when comparing estimates from different sources.

#### Table 2: Overview of previous studies

| Author | Publication date | Title | Estimate (TWh) |
|---|---|---|---|
| Digiconomist | Live estimate | Bitcoin Energy Consumption Index | 204.44 |
| CoinMetrics | June 2023 | The Signal & The Nonce | 117.4 |
| De Vries, A., Gallersdorfer, U., Klaaßen, L. and Stoll, C. | February 2022 | Revisiting Bitcoin's carbon footprint | 117.3 |
| CoinShares | January 2022 | The Bitcoin Mining Network | 89.0 |
| Sandner, P., Lichti, C., Richter, R., Heidt, C. and Schaub, B. | August 2021 | The Carbon Emissions of Bitcoin From an Investor Perspective | 90.9 |
| Köhler, S. and Pizzol, M. | November 2019 | Life Cycle Assessment of Bitcoin Mining | 31.3 |
| Stoll, C., Klaaßen, L. and Gallersdorfer, U. | June 2019 | The Carbon Footprint of Bitcoin | 48.5 |
| Zade, M., Myklebost, J., Tzscheutschler, P. and Wagner, U. | March 2019 | Is Bitcoin the Only Problem? A Scenario Model for the Power Demand of Blockchains | 33.7 |
| Krause, M.J. and Tolaymat, T. | November 2018 | Quantification of energy and carbon costs for mining cryptocurrencies | 30.1 |
| McCook, H. | August 2018 | The cost & sustainability of Bitcoin | 105.0 |
| De Vries, A. | May 2018 | Bitcoin's Growing Energy Problem | 22.4–67.2 |
| Vranken, H. | October 2017 | Sustainability of bitcoin and blockchains | 0.9–4.4 |
| Bevand, M. | February 2017 | Electricity consumption of Bitcoin: a market-based and technical analysis | 4.1–4.7 |
| Hayes, A.S. | March 2015 | A Cost Production Model for Bitcoin | (no estimate shown) |
| O'Dwyer, K.L. and Malone, D. | September 2014 | Bitcoin Mining and its Energy Footprint | 0.9–87.6 |

The studies in Table 2 often produce findings that vary considerably, resulting in a broad range of potential estimates. This is due to the different methodologies used. Some studies adopt a top-down economic approach, others a bottom-up model, and models such as our CBECI are founded on a hybrid top-down approach. Lei et al. (2021) compared 22 different studies and proposed best practices for estimating the energy consumption of blockchain technology systems. They concluded that, in comparison, the previous CBECI model most closely aligns with the identified best practices.15

Each study is underpinned by a set of assumptions that may be subject to scrutiny. Consequently, each investigation's design – including our own analysis – has inherent limitations and disadvantages. However, certain papers have been criticised for adopting overly simplistic assumptions and non-trivial errors, such as inappropriate temporal averaging or simplistic extrapolations. For an in-depth review of previous studies, refer to Koomey (2019).16

The CBECI was devised using the studies in Table 2 as a reference. We have meticulously reviewed the various methodologies and integrated best practices. The website aims to offer comprehensive documentation with transparent version control, underscore the model's dependence on electricity cost assumptions (by allowing visitors to alter the default value) and candidly present the uncertainties and limitations of the model. We always welcome feedback and suggestions for further improvements.

---

## Capture notes (not part of the verbatim text)

- Source page HTTP 200; 300,931 bytes SSR HTML; the entire methodology body is server-rendered (no JS needed).
- The in-text "change log" link points to https://ccaf.io/cbnsi/change_log — as of 2026-10-10 that URL, and https://ccaf.io/cbnsi/cbeci/change_log, return an SPA-rendered "404 Page Not Found" page (HTTP 200 soft-404 / HTTP 404 respectively). The change log appears to have been retired or moved; parked.
- The phrase "total Ethereum network hashrate" under lower-bound limitations appears verbatim on the page (context: CBECI) and is reproduced as-is.
- Digiconomist's "204.44" TWh live-estimate value in Table 2 matches the live JSON at https://ccaf.io/cbeci/api/data/stats/live ({"digiconomist":"204.44"}), fetched 2026-10-10.
- Equations render as images on the page and are NOT reproduced here (marked [equation n]); figures likewise.
