# The Canary in the Parking Lot

Why the Capacity to Remain Is the First Thing a Site Sheds.

A drive-in restaurant can be criticised for its land and fuel use and regretted for the social uses lost when it closes. The two judgements concern different quantities: profitability, ecological cost and the uses a place supports. We model a site as a set of functions, each with a footprint, a social value and an appropriability, the share of its value the operator can charge for. Under rising ground rent an operator removes functions in order of private return per unit footprint. The five functions that let people remain on site are removed first, whereas an ordering by social value would first remove the parking the transaction requires. With uniform appropriability the two orders coincide. Seating disappears well before closure: the last way of staying is removed at a ground rent of 13.2 and the site closes at 81.9, and when the last seat goes the site still earns 0.588 of its peak profit while having lost 0.423 of its social value. Removing every way of staying reduces the ecological burden of a meal occasion by 0.0212, and by no more than 0.0377 across 1482 combinations of travel parameters, because most of the burden comes from travel the operator does not control. An obligation triggered by on-premises capacity can be avoided by removing that capacity: a duty worth 0.0704 of private return leads to the removal of 0.3226 of social value. A United States district court accepted an exemption on this basis in 1966, and it was reversed on appeal.

## Simulation

```bash
cd simulation
uv run run_all.py        # -> output/results.json + output/figures/*.png
```

Twenty-six invariant checks fail the run if broken, among them the identity of the two cut orders when appropriability is uniform, the equality of each function's loss ratio with the reciprocal of its appropriability, the requirement that profit and social value never rise with rent, the requirement that design never controls a tenth of a meal occasion's burden anywhere on the swept grid, and the exact agreement between the grid and the closed form for the duty that empties a site at zero rent. Two grids are enumerated exhaustively; the robustness test is a seeded ensemble of 800 draws. Execution is recorded in `verification/sites.json` and every number quoted in the manuscript is bound to a JSON pointer in `claims.yaml`, except two taken from a court's findings of fact and attributed to the court. Nothing here is calibrated to any business, and the model estimates no firm's returns.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build the-canary-in-the-parking-lot`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
