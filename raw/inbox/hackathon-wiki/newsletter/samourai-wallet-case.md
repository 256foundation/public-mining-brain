# Samourai Wallet Case and Developer Liability

> Sources: 256 Foundation (newsletter #5, May 2025), 2025-05-05; 256 Foundation (newsletter #6, June 2025), 2025-06-19; 256 Foundation (newsletter #7, July 2025), 2025-07-15; 256 Foundation (newsletter #8, August 2025), 2025-08-18; 256 Foundation (newsletter #9, September 2025), 2025-09-25; 256 Foundation (Assembling Freedom #12), 2025-12-22; 256 Foundation (Assembling Freedom #13), 2026-01-14; 256 Foundation (Assembling Freedom #17), 2026-02-19; 256 Foundation (POD256 Episode 108 newsletter), 2026-03-18
> Raw: [Newsletter May 2025](../../raw/newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md); [Newsletter June 2025](../../raw/newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md); [Newsletter July 2025](../../raw/newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md); [Newsletter August 2025](../../raw/newsletter/2025-08-18-is-open-source-communism.md); [Newsletter September 2025](../../raw/newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md); [Assembling Freedom #12](../../raw/newsletter/2025-12-22-assembling-freedom-12.md); [Assembling Freedom #13](../../raw/newsletter/2026-01-14-assembling-freedom-13.md); [Assembling Freedom #17](../../raw/newsletter/2026-02-19-assembling-freedom-17-unpacking-pod256-episode-105-chips-cha.md); [POD256 Episode 108 newsletter](../../raw/newsletter/2026-03-18-pod256-episode-108-breakdown-from-mixers-to-miners-why-samou.md)
> Updated: 2026-10-07

## Overview

The prosecution of the Samourai Wallet developers, Keonne Rodriguez and William (Bill) Hill, is the story the newsletter followed most closely outside mining. The newsletter called it the most important case facing Bitcoiners. Its worry is the legal theory: that people who write non-custodial software can be treated as money transmitters and held liable for what users do. The author argues that the same reasoning could reach wallet makers, node operators and miners. This page follows the case as the newsletters reported it, from the Justice Department memo of April 2025 to the prison sentences discussed in March 2026. The newsletters are openly on the developers' side, and their descriptions of prosecutors and judges are advocacy.

## Why a mining foundation cares

- Samourai Wallet was a non-custodial mobile wallet with privacy tools. Whirlpool was its CoinJoin implementation. The March 2026 issue also lists Dojo (a user-run full node backend), Ricochet (extra hops) and Stonewall.
- The author used Whirlpool as a miner. It stops a pool operator from tracking how rewards are spent, and stops the people a miner pays from learning that they mine.
- Prosecutors compared a non-custodial wallet to a frying pan that transfers heat without controlling it. The newsletter reads that as saying any way of helping funds move counts as money transmission. It quotes the phrase prosecutors used: "to facilitate the transfer of funds by any and all means".
- The March 2026 issue draws the line to mining directly. If developers can be jailed for privacy code, it asks what stops the next attack on open mining tools.

## Timeline

Dates without a year are in 2025.

| When | What the newsletters report |
|---|---|
| April 2024 | Samourai's infrastructure is seized and the Whirlpool coordinator goes offline. April 24 is given as the date of the developers' arrest. |
| April 7 | Deputy Attorney General Todd Blanche issues a memo titled "Ending Regulation By Prosecution". It says the Department will no longer target mixing services and wallets for the acts of their users. The Southern District of New York (SDNY) does not drop the case. |
| April 29 | Prosecution and defense jointly ask for more time for prosecutors to decide their position. |
| May 5 | A defense letter says prosecutors had asked FinCEN whether Samourai would need a money transmitter license, FinCEN said no, and prosecutors did not disclose this for almost a year. |
| May 9 | Prosecutors reply: "There is no basis for a hearing, nor is there anything to remedy". |
| May 14 | Judge Berman suggests the defense raise the issue in pretrial motions. |
| May 29 | The defense files motions, including a motion to dismiss and a motion for separate trials. |
| June 3 | Judge Berman declines an amicus brief as "not needed at this time". Matt Corallo and Save Our Wallets push the Blockchain Regulatory Certainty Act (BRCA). |
| June 6 | The DeFi Education Fund publishes its amicus brief anyway. |
| June 8 | The BRCA language is reported as included in the CLARITY Act under Section 110. |
| June 23 | Ashigaru, a fork of the Samourai app made by former users, announces a new Whirlpool coordinator. |
| June 24 | Prosecutors file an updated indictment. It drops the allegation that Samourai failed to get a license and adds emphasis on "transferring funds on behalf of the public". |
| June 26 | Prosecutors file an 83-page letter opposing the defense's pre-trial motions. |
| July 14 | The trial of Tornado Cash developer Roman Storm starts in the SDNY. |
| July 30 | The Samourai developers plead guilty to conspiracy to operate an unlicensed money transmitting business. Prosecutors drop the money laundering conspiracy charge. |
| August 6 | The Storm trial ends. The jury convicts on the unlicensed money transmitting conspiracy count and cannot agree on the other two. |
| November 6 & 7, 2025 | Scheduled sentencing hearings, as stated in the August issue. |
| November | Keonne Rodriguez appears on POD256 #96. |
| March 2026 | The newsletter reports Keonne Rodriguez sentenced to 5 years and Bill Hill to 4 years. Keonne is serving time in Morgantown, WV. Bill is in an undisclosed prison. |

## The plea

Before the plea the developers faced 25-years in prison. The laundering charge carried a maximum of 20-years and the money transmitting charge a maximum of 5-years. The August issue calls the plea the right decision in hindsight, given the Storm verdict. A trial would have cost more and risked 20 more years, and a jury would likely have convicted on the transmitting charge anyway. It also says no precedent was set, because the case ended in a plea.

The August issue describes the fight as lasting 462 days. In the same passage it says the developers had been under house arrest for nearly 500 days.

> **Status: Disputed**
> The money figures differ. The August 2025 issue says the developers need to pay a $6m fine by sentencing. The March 2026 issue gives a forfeiture figure that is garbled in the saved text (`6.3Mpaid+250k in fines each`). The two issues are months apart and may describe different stages, but neither explains the difference.

## The newsletter's argument

- **Custody is the test.** A money transmitter moves other people's money, so it must control that money. Samourai never held user funds. In the Storm case prosecutors argued that custody is not required under Section 1960. The September issue calls that argument misleading, because bitcoin cannot be moved without control of the keys.
- **FinCEN had already answered.** FinCEN's 2019 guidance says developers of non-custodial software do not need a license, and FinCEN told prosecutors the same about Samourai.
- **Legislation may not help.** The July issue doubts the CLARITY Act would do anything for developers already charged.
- **Mixers and CoinJoins differ.** A mixer takes custody of coins. A CoinJoin never does. The July issue criticizes a Secret Service post for blurring the two.
- **Precedent on conspiracy.** The December issue cites the Falcone case. There the Supreme Court found that a merchant who sold sugar to a bootlegger during prohibition was not a conspirator, even with vague knowledge of how the sugar would be used.
- **Treasury's later view.** The March 2026 issue says the U.S. Treasury told Congress that month that lawful users may use mixers for financial privacy. It argues this undercuts the prosecution's theory.

## Related events

- **Ashigaru.** The July issue welcomed the new Whirlpool coordinator as proof that open code outlives its authors' arrest. The August issue reports criticism that a malicious coordinator could link CoinJoin participants. It says there is no evidence this ever happened and that the Ashigaru developers shipped a fix.
- **Google Play.** In August 2025 a Google Play policy seemed to require licenses from wallet developers. Google then said non-custodial wallets were not in scope.
- **Roman Storm.** The August issue expected an appeal after sentencing.

## What the newsletters ask readers to do

- Sign the pardon petition at `change.org/billandkeonne`. The request appears from the December 2025 issue onward and heads issue #13. Issue #17 repeats it.
- Donate to the legal defense fund through `p2prights.org` (2025 issues).
- Write to Keonne Rodriguez in prison. The March 2026 issue gives the address and the rules: three pages or fewer and no artwork.
- Keep using the tools. The March 2026 issue suggests recovering Samourai seeds in Sparrow or Electrum, running a Ronin Dojo node, and testing Ashigaru Whirlpool.

## See Also

- [Editorial Essays and Arguments, 2025](editorial-essays-2025.md)
- [Foundation Progress Timeline, 2025](foundation-progress-2025.md)
- [Foundation Progress Timeline, 2026](foundation-progress-2026.md)
- [256 Foundation: Mission and Organization](../foundation/mission-and-organization.md)
