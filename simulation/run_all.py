"""Reproduce every number and both figures.

    cd simulation && uv run run_all.py
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))

    from figures import plot_order, plot_burden
    plot_order(results, str(OUT / "figures" / "order.png"))
    plot_burden(results, str(OUT / "figures" / "burden.png"))

    O, L, B, Q, E = (results["order"], results["lead"], results["burden"],
                     results["obligation"], results["ensemble"])
    print("the order of the cut:")
    print("  private:", " < ".join(O["private_order"]))
    print("  social: ", " < ".join(O["social_order"]))
    print(f"  tau {O['kendall_tau']:.3f}; with equal appropriability everywhere "
          f"{O['uniform_appropriability_tau']:.3f}")
    print(f"  the first cut destroys {O['first_cut_loss_ratio']:.1f} of social value "
          f"per unit of private return, the last {O['last_cut_loss_ratio']:.3f}")
    print("the lead:")
    print(f"  nowhere left to stay at rent {L['all_presence_gone_rent']:.2f}; "
          f"the doors close at {L['closure_rent']:.2f}, a factor of "
          f"{L['lead_over_closure']:.2f}")
    print(f"  at that moment the site keeps {L['profit_retained_when_presence_gone']:.3f} "
          f"of its peak profit and has lost {L['social_lost_when_presence_gone']:.3f} "
          f"of its social value")
    print(f"  it stays open across {L['share_of_rent_range_open_but_empty']:.3f} of the "
          f"rent range with nowhere to stay")
    print("the burden:")
    print(f"  the site is {B['base']['design_controlled_share']:.3f} of a meal "
          f"occasion; removing every way of staying saves "
          f"{B['base_reduction_from_removing_all_presence']:.4f}")
    print(f"  across {B['grid_cells']} cells the saving never exceeds "
          f"{B['max_reduction']:.4f}")
    print(f"  the site would have to be {B['site_kg_multiple_needed']:.1f} times "
          f"heavier for design to control half the burden")
    print("the obligation:")
    print(f"  a duty worth {Q['focal_duty_share']:.4f} of private return removes "
          f"{', '.join(Q['focal_dropped'])} at any rent, destroying "
          f"{Q['focal_social_destroyed_share']:.4f} of social value")
    print(f"  leverage {Q['focal_leverage']:.3f}; a duty scaled instead of triggered "
          f"would need a rate of "
          f"{Q['duty_rate_removing_presence_at_zero_rent_analytic']:.2f}")
    print("robustness:")
    print(f"  over {E['draws']} draws the first cut is a way of staying in "
          f"{E['first_cut_is_presence_share']:.3f}; all five sit within the first six "
          f"in {E['presence_within_first_six_share']:.3f}")
    print(f"  worst draw still averages rank {E['presence_mean_rank_worst_draw']:.1f} "
          f"of ten for the five ways of staying")
    print("checks:", f"{sum(results['checks'].values())}/{len(results['checks'])}")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
