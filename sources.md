# Sources

The frozen bibliography lives in `references.yaml` as CSL records with stable IDs; the manuscript cites them with Pandoc `[@id]` syntax and `papers refs` reconciles the two. This file records provenance for each entry. Support for particular assertions, as distinct from identity, is bound in `claims.yaml`.

## How these were checked

Journal articles and book chapters were resolved through the Crossref REST API against the DOI recorded in `references.yaml`, and the title, authors, container, volume, issue, pages and year were taken from that response rather than from memory or from the seed. Nineteen entries are books, essays in journals that do not deposit DOIs, or primary legal sources; those carry no DOI, and how each was identified is recorded below. Where the seed material asserted something a source does not say, the source wins and the discrepancy is noted.

## Primary legal sources, read in full

- `newman1966` — *Newman v. Piggie Park Enterprises, Inc.*, 256 F. Supp. 941 (D.S.C., Columbia Division, 28 July 1966), Civ. A. No. AC-1605. Case name, citation, court, division, docket number and date confirmed through the CourtListener search API (opinion id 2349546). The opinion text was read in full from the Internet Archive's 14 March 2025 capture of the Justia reproduction, after both CourtListener's opinion endpoint (authentication required) and Justia directly (bot challenge) refused anonymous access. Findings of fact 2 and 4 and the conclusions of law are quoted in the manuscript and were read from that text.
- `newman1967` — *Newman v. Piggie Park Enterprises, Inc.*, 377 F.2d 433 (4th Cir., 24 April 1967). Case name, citation, court and date confirmed through the CourtListener search API. The opinion text itself was **not** obtained. Its holding is cited only as the Supreme Court recounts it, and the manuscript attributes it that way rather than to a reading of the Fourth Circuit's own words.
- `newman1968` — *Newman v. Piggie Park Enterprises, Inc.*, 390 U.S. 400 (18 March 1968), No. 339, per curiam. Read in full from the Library of Congress facsimile of the official U.S. Reports volume. This is the source for the procedural history, for the statement that the district court "erroneously concluded that Title II does not cover drive-in restaurants of the sort involved in this case", and for the disposition "377 F. 2d 433, modified and affirmed." The question the Supreme Court actually decided was the standard for awarding attorney's fees, not the coverage of drive-ins, and the manuscript says so.

## Entries with DOIs, resolved through Crossref

- `aalbers2016` — 10.4324/9781315668666. Identity verified. Cited for the central argument, that financialization names something narrower than profit-seeking; not read at page level.
- `bourgeois1981` — 10.2307/257138. *Academy of Management Review* 6(1). Crossref reports the start page 29; the article runs to 39 and the range is recorded as such. Cited, with `cyert1963`, for a concept the paper distinguishes from its own rather than adopts.
- `cobble1992` — 10.5406/j.ctt3fh3vh. Crossref records 1992 for the University of Illinois Press edition it indexes; the first edition is usually dated 1991. The Crossref year is used. Cited for the central argument; not read at page level.
- `dika2003` — 10.1017/cbo9780511814297.004, chapter at pages 89–121. The chapter record carries no author field in Crossref; authorship is established by the monograph record 10.1017/cbo9780511814297, which lists Dika. Cited for the existence of the disagreement with Jameson, not for a reading of the chapter.
- `foxblack2011` — 10.4337/9780857930569.00023. Identity verified. Cited as a pointer to the cinema case; no figure from it is used.
- `ritzer1983` — 10.1111/j.1542-734x.1983.0601_100.x. *Journal of American Culture* 6(1) 100–107.
- `ritzer2018` — 10.1177/1469540518818628. Crossref issued year 2018 for online publication; the print issue is *Journal of Consumer Culture* 19(1) in 2019. The Crossref year is used.
- `shelleryurry2000` — 10.1111/1468-2427.00276. *IJURR* 24(4) 737–757.
- `smith1979` — 10.1080/01944367908977002. *JAPA* 45(4) 538–548.
- `teece1986` — 10.1016/0048-7333(86)90027-2. *Research Policy* 15(6) 285–305. This is the source of the appropriability concept the model turns on, and it is cited for that concept, which the article's title and abstract establish.
- `urry2004` — 10.1177/0263276404046059. *Theory, Culture & Society* 21(4-5) 25–39.

## Entries without a Crossref DOI

For each of these no DOI was returned by a Crossref bibliographic query; what Crossref does return is review and citation records, which establish that the work exists with the author, title and year given. Each is cited for its central argument as identified by title and standing in the literature, and none was read at page level in this pass. That is a real limit on the weight any of them can carry, and the manuscript does not rest a numeric or specific claim on any of them.

- `bataille1988` — *The Accursed Share*, volume I, Zone Books, translated by Robert Hurley; original French 1949.
- `benjamin1999` — *The Arcades Project*, Belknap Press, translated by Eiland and McLaughlin.
- `cyert1963` — *A Behavioral Theory of the Firm*, Prentice-Hall. Crossref returns only later reprints and a 1964 review.
- `fraser2016` — *New Left Review* 100. New Left Review does not deposit DOIs.
- `gorz1973` — "The Social Ideology of the Motorcar", first published in *Le Sauvage*, widely reproduced. The seed's warning is adopted here: its historical arithmetic is not recycled as current data, and no figure from it is used.
- `harvey1982` — *The Limits to Capital*, Basil Blackwell.
- `horkheimer1947` — *Eclipse of Reason*, Oxford University Press.
- `jakle1999` — *Fast Food: Roadside Restaurants in the Automobile Age*, Johns Hopkins University Press. Crossref returns two scholarly reviews, which confirm authors, title and publisher.
- `jameson1984` — *New Left Review* I/146.
- `lefebvre1991` — *The Production of Space*, Blackwell, translated by Nicholson-Smith; original French 1974. Crossref returns reviews from 1992 and 1994 confirming the translation and edition.
- `marx1867`, `marx1894` — *Capital* volumes I and III. Volume III chapter 46 on building-site rent is the relevant locator for the rent argument.
- `oldenburg1989` — *The Great Good Place*, Paragon House. Crossref returns two 1991 review records confirming author and title.
- `sorin2020` — *Driving While Black*, Liveright. Crossref returns a 2022 review in *The Journal of African American History*.
- `whyte1980` — *The Social Life of Small Urban Spaces*, The Conservation Foundation. Crossref returns a 1982 review confirming author, title and publisher.
- `williams1973` — *The Country and the City*, Chatto and Windus.

## Considered and not cited

- Guy Barefoot's article on 1950s drive-in cinema audiences, which the seed cites for a rise from 820 US drive-in cinemas in 1948 to 4,063 in 1958. Neither candidate URL at the *Participations* site resolved, and the figures are not used. No count of drive-in cinemas or restaurants appears anywhere in the manuscript.
- McDonald's corporate history, SONIC's franchise page and Taco Bell's 2022 Defy announcement. These are first-party statements about a company's own past and plans; none could be independently corroborated in this pass, and a stipulated model does not need them. Dropping them costs the paper nothing it was entitled to claim.
- The IPCC Working Group III urban chapter. The manuscript's burden block is stipulated and swept, not calibrated, and citing an assessment report alongside invented emission factors would imply a calibration the paper does not have.
- Every one of these omissions removes something the seed used. None of them removes a claim the manuscript makes.

## Numbers taken from sources rather than from the simulation

Two, both from the district court's findings of fact, both quoted and attributed to the court in the manuscript: the six establishments, five of them drive-ins; and the fifty percent of food at those drive-ins consumed off the premises [@newman1966]. Every other number in the manuscript is bound to a JSON pointer in a recorded execution.
