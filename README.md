# The Canary in the Parking Lot

Why the Capacity to Remain Is the First Thing a Site Sheds.
A drive-in can be criticised for what it consumes and mourned for what closes
with it; the judgements differ because profitability, ecological cost and lived
use are different measures. This paper computes what that separation implies.
Each function of a site has a footprint, a social value, and an appropriability,
the share of the value it creates that the operator can charge for. Under rising
ground rent functions are dropped in order of private yield per unit footprint,
and the five constituting the capacity to remain are the first five dropped,
while the thing a public evaluation would drop first is the parking the
transaction itself requires. Set appropriability uniform and the two orders
become identical, which places the whole result in that one variable. Because
the capacity to remain goes early and closure comes last, the canary metaphor
acquires a number: nowhere is left to sit at a ground rent of 13.2 and the doors
close at 81.9, and when the last seat goes the site still earns 0.588 of its peak
profit while having lost 0.423 of its social value. Removing every way of staying
reduces the site's ecological burden by 0.0212, never by more than 0.0377 across
1482 combinations of trip length and emission factor, because the burden belongs
to journeys the operator neither pays for nor controls. A duty attaching to the
capacity to remain is cheap to escape by removing it: one worth 0.0704 of private
return buys the removal of 0.3226 of social value. That argument was made and
accepted in a United States district court in 1966, then reversed.

## Simulation

```bash
cd simulation
uv run run_all.py        # -> output/results.json + output/figures/*.png
```

Twenty-six invariant checks fail the run if broken, among them the identity of
the two cut orders when appropriability is uniform, the equality of each
function's loss ratio with the reciprocal of its appropriability, the requirement
that profit and social value never rise with rent, the requirement that design
never controls a tenth of a meal occasion's burden anywhere on the swept grid,
and the exact agreement between the grid and the closed form for the duty that
empties a site at zero rent. Two grids are enumerated exhaustively; the
robustness test is a seeded ensemble of 800 draws. Execution is recorded in
`verification/sites.json` and every number quoted in the manuscript is bound to a
JSON pointer in `claims.yaml`, except two taken from a court's findings of fact
and attributed to the court. Nothing here is calibrated to any business, and the
model estimates no firm's returns.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build the-canary-in-the-parking-lot`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
