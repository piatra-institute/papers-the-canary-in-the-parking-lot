# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-09-22 — prose revision

Correction of a grid-search value.
  - The multiple of the site's burden needed for the site to account for half the burden of a meal occasion was published as 21.8. The exact value is (travel + food) / site = 4.78 / 0.22 = 21.7. `simulation/analyses.py` now computes it in closed form and keeps the grid value alongside (26 invariants pass).
  - Found while auditing the collection for the grid-artifact error corrected in economics-after-cognitive-scarcity. The other thresholds in this paper (the cut rents, the closure rent by bisection, the duty rate) were checked and are exact.

## 2026-09-22 — prose revision

Prose revision against the house standards. No computation, number, quotation, citation or conclusion changed.
  - Manuscript rewritten paragraph by paragraph; prose shortened from about 4,000 to about 3,000 words. Structure is now introduction, related work, model, six results and discussion sections, and limitations.
  - Removed three references to the unpublished origin chat, twelve self-references, meta-commentary, epigrammatic closers, and contrast framing ('rather than' from fourteen instances to none).
  - Corrected a factual error in the published figure 1(c), whose title said the first removal was at the top when it is plotted at the bottom.
  - Figure titles and annotations rewritten to state quantities; figures regenerated and the execution re-recorded (26 invariants pass).
  - Claim ledger re-bound; all 52 bindings pass. README rewritten as one line per paragraph with the new abstract.

## 2026-09-08 — v1, complete

Scope: the whole paper, four mechanisms, the documentary anchor and the evidence base, from the seed chat and its 7,400-word working draft to the built PDF and the bound claim ledger.

What the seed supplied and what this adds:
  - The seed is unusually careful and does most of the conceptual work: it separates commercial return, ecological cost and lived use; it names selective rationalization; it retracts its own earlier slogan that capitalism cannot tolerate what it cannot monetise; and it states in terms that its Appendix B model "demonstrates logical possibility, not an empirical result." It computes nothing. This paper computes it. The contribution is the arithmetic and the mechanism that makes the arithmetic come out the way it does.
  - The mechanism is appropriability, which the seed does not name. Borrowing it from the economics of innovation [@teece1986] converts "socially productive slack" from a description into a quantity with a cut order, and supplies the paper's null: uniform appropriability makes the operator's ordering and the social ordering identical.
  - The seed's compressed slogan, that they kept the car and lost the place, comes out of the model as a derivation rather than an assertion: socially the first thing to shed is the parking the transaction requires, and privately it survives to sixth.

The documentary find:
  - The seed cites *Newman v. Piggie Park* for the proposition that Black customers were confined to takeaway at kitchen windows. That is verbatim from finding of fact 4 and is correct. Reading the whole opinion turned up something the seed missed and something better: the district court held the five drive-ins **outside** Title II of the Civil Rights Act of 1964 because they had no seating "sufficient to accommodate any appreciable number of patrons", served in disposable containers, and sold half their food for consumption off the premises. The statutory category was "principally engaged in selling food for consumption on the premises". The capacity to remain was the coverage trigger, and designing it away was a successful first-instance defence.
  - The Fourth Circuit reversed and the Supreme Court called the reasoning erroneous. Both were verified: the reversal only as the Supreme Court recounts it, because the Fourth Circuit opinion itself could not be obtained, and the manuscript attributes it that way rather than to a reading of that court's own words.
  - Retrieval was not straightforward and is recorded in `sources.md`: CourtListener's opinion endpoint requires authentication, Justia serves a bot challenge, and law.resource.org has no copy. The district court text was read from the Internet Archive's March 2025 capture of the Justia page, with citation, court, division, docket and date independently confirmed through CourtListener's search API. The Supreme Court per curiam was read from the Library of Congress facsimile of the official U.S. Reports volume.
  - An early phrase probe for "kitchen window" returned zero and briefly suggested the seed had invented the detail. The opinion says "kitchen windows". The probe was wrong, not the seed, and the lesson recorded here is that a null result from an exact-phrase search is evidence about the phrase and not about the claim.

Bibliography:
  - 30 entries, all 30 cited in the manuscript. Eleven carry DOIs resolved through Crossref against the recorded identifier. Nineteen are books, essays in journals that do not deposit DOIs, or primary legal sources; for each, what was actually checked is recorded in `sources.md`, and none carries a numeric or specific claim.
  - Four of the seed's sources were dropped rather than cited on its authority. Barefoot's drive-in cinema counts could not be retrieved at either candidate URL, so no count of drive-in cinemas or restaurants appears anywhere in the manuscript. The McDonald's, SONIC and Taco Bell corporate statements are first-party claims that could not be independently corroborated and that a stipulated model does not need. The IPCC urban chapter was dropped because citing an assessment report alongside invented emission factors would imply a calibration this paper does not have.

Model corrections during the work:
  - The brief asserted, before anything was computed, that the private and social cut orders were "close to reversed". They are not: the Kendall rank correlation is 0.556, positive. The brief was corrected and the manuscript states the narrower claim the arithmetic supports. Writing the number down is what caught it.
  - The results serializer keeps six significant digits rather than six decimal places, carried over from the previous paper in this workspace for the same reason: rounding to decimals destroys small magnitudes.
  - A claim bound the numeral 1.000 to the ensemble's maximum rank correlation and failed the local gate. The gate was right: that 1.000 was the uniform-appropriability reference, and the sentence now reports the actual maximum, 0.822.

Verification:
  - `papers run --id sites` records the execution; 26 invariants pass and a failed invariant fails the run. Two grids are enumerated exhaustively (2401 rent levels against ten functions; 1482 trip-length and emission-factor combinations, plus 49 duty thresholds) and the robustness test is a seeded ensemble of 800 draws with every footprint and appropriability perturbed by an independent uniform factor in [0.6, 1.4].
  - `claims.yaml` binds 52 claims at the reviewed manuscript hash: 35 computations bound to JSON pointers in the recorded run, 8 source claims each with a locator and a candid verification note, 4 assumptions, 2 definitions, 2 interpretations and 1 normative limit. Two numbers in the manuscript come from the court's findings of fact and are attributed to the court in the text.
  - `papers check --stage local` passes. All eleven PDF pages were inspected at full size and the record is in `visual-review.json`.

Known limits, all stated in the manuscript:
  - The ten functions are an itemisation of the paper's own devising, and the ensemble varies their numbers but not the list.
  - Appropriability is the stipulation everything rests on and no empirical estimate of it exists for any of these functions.
  - The burden parameters are invented, which is why they are swept across three orders of magnitude rather than defended; no external emissions assessment is used anywhere.
  - The model prices functions and is silent about the people who provide them, and it has no distributional content at all, which the Piggie Park record makes an uncomfortable silence rather than a neutral one.
  - The 1966 holding was repudiated. The paper claims the incentive is general, not that the exemption survives.

Editorial:
  - The first draft cited 8 of 30 bibliography entries and read as a formal model with critical theory applied as a coat. Two sections were added giving each tradition specific work, taking the count to 30 of 30 and adding roughly a thousand words.
  - Twelve voice diagnostics were triaged and all twelve rewritten; the manuscript now returns zero editorial candidates and corpus lint reports no outliers. Four sentences were shortened to break a run of thirty-one without a short one.
  - Both figures were revised after inspection in page context. Figure 1 panel (a) had an annotation pointing the wrong way, panel (b) had a legend covering an annotation, and panel (c) had row labels colliding with tick numbers and the axis label. Figure 2 panel (c) had an annotation first on a line and then under a legend. All were fixed and re-inspected.
  - Legal citations were reworked so the reporter sits in `container-title`, `volume` and `page` rather than inside the case title, which was rendering as "941 1966" at four inline sites.
