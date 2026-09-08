"""The canary in the parking lot, computed.

Every quantity below is a property of an explicitly stated model. Nothing here
is fitted to any site, estimates any real firm's returns, or describes any
particular business. The functional forms and the ten functions are stipulated;
what is computed is what they jointly imply.

1. The order of the cut. A site provides several functions at once. Each has a
   footprint in space and time, a social value, and an appropriability: the
   share of the value it creates that the operator can charge for. Private
   return is appropriability times social value, so the only independent
   stipulations are footprint, social value and appropriability. Under rising
   ground rent the operator keeps a function while its private return covers the
   rent on its footprint, which orders the cuts by private yield density. A
   public evaluation would order them by social yield density. The two orders
   coincide exactly when appropriability is uniform, so everything here is
   driven by its variation and nothing by the arithmetic.

2. The lead. Because the capacity to remain is cut early and closure comes last,
   the loss of somewhere to stay precedes the closure that gets noticed. The
   interval between the two is computed in rent and reported as a ratio, which
   is what the canary metaphor asserts without quantifying.

3. The burden. The operator optimises over what the operator pays for. The
   footprint of a car-reached site is dominated by the trips taken to reach it
   and the food served, neither of which a redesign touches. The share of total
   burden that any redesign can move is computed and swept across three orders
   of magnitude of travel assumptions, because the conclusion should not rest on
   one emission factor.

4. The obligation. Duties that attach to the capacity to remain lower the rent
   at which an operator removes it. Where the duty is triggered by a threshold
   rather than scaled to the capacity, it creates a notch, and a band of designs
   in which cutting the capacity is profitable at any rent whatsoever.

Seeded. A failed invariant fails the run.
"""
from __future__ import annotations

import numpy as np

SEED = 20260908


def _py(x):
    if isinstance(x, (bool, np.bool_)):
        return bool(x)
    if isinstance(x, dict):
        return {k: _py(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_py(v) for v in x]
    if isinstance(x, (np.floating,)):
        return float(f"{float(x):.6g}")
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, np.ndarray):
        return [_py(v) for v in x.tolist()]
    if isinstance(x, float):
        return float(f"{x:.6g}")
    return x


# ---------------------------------------------------------------------------
# The site
# ---------------------------------------------------------------------------
# footprint: capacity in space and time the function occupies, in stipulated
#            units; footprint_share below renormalises these to sum to one
# social:    value the function creates per year, in stipulated units
# appropr:   share of that value the operator can charge for
#
# Appropriability is the load-bearing stipulation. The transaction is almost
# perfectly appropriable, since the operator charges for it directly. Being able
# to stay after paying is barely appropriable at all: most of what it is worth
# accrues to the people staying, and to people they meet, not to the till.

FUNCTIONS = [
    # id                label                                  footprint social appropr
    ("transaction",     "ordering and payment",                    0.08,   9.0,   0.95),
    ("kitchen",         "preparing the food",                      0.14,   8.0,   0.92),
    ("collection",      "collecting an order without parking",     0.10,   5.0,   0.88),
    ("menu",            "a wider menu than the minimum",           0.06,   2.4,   0.85),
    ("parking",         "parking long enough to be served",        0.22,   4.2,   0.80),
    ("shelter",         "shelter from weather",                    0.05,   2.2,   0.30),
    ("seating",         "tables and chairs",                       0.16,   5.6,   0.22),
    ("restrooms",       "restrooms open to customers",             0.05,   2.8,   0.16),
    ("dwell",           "staying after the purchase is finished",  0.18,   6.4,   0.10),
    ("commons",         "meeting others without buying",           0.12,   4.0,   0.04),
]
IDS = [f[0] for f in FUNCTIONS]
PRESENCE = ("shelter", "seating", "restrooms", "dwell", "commons")
FIXED_COST = 2.0     # annual cost of being open at all, independent of design
RENT_GRID = np.round(np.linspace(0.0, 120.0, 2401), 4)


def _table(footprints=None, appropr=None) -> list:
    rows = []
    for i, (fid, label, c, v, a) in enumerate(FUNCTIONS):
        c = footprints[i] if footprints is not None else c
        a = appropr[i] if appropr is not None else a
        rows.append({"id": fid, "label": label, "footprint": c, "social": v,
                     "footprint_share": None,
                     "appropriability": a, "private": a * v,
                     "private_density": a * v / c, "social_density": v / c,
                     "loss_ratio": 1.0 / a})
    total = sum(r["footprint"] for r in rows)
    for r in rows:
        r["footprint_share"] = r["footprint"] / total
    return rows


def _order(rows: list, key: str) -> list:
    """Ids in the order they would be cut: least yield per unit footprint first."""
    return [r["id"] for r in sorted(rows, key=lambda r: r[key])]


def _kendall_tau(a: list, b: list) -> float:
    """Rank correlation between two orderings of the same items, no ties."""
    ra = {x: i for i, x in enumerate(a)}
    rb = {x: i for i, x in enumerate(b)}
    items = list(a)
    n, conc, disc = len(items), 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            x, y = items[i], items[j]
            s = (ra[x] - ra[y]) * (rb[x] - rb[y])
            if s > 0:
                conc += 1
            elif s < 0:
                disc += 1
    return (conc - disc) / (n * (n - 1) / 2)


def _cut_rent(row: dict) -> float:
    """Ground rent at which this function stops covering its own footprint."""
    return row["private_density"]


def _profit(rows: list, rent: float) -> float:
    kept = [r for r in rows if r["private_density"] >= rent]
    return sum(r["private"] - rent * r["footprint"] for r in kept) - FIXED_COST


def _closure_rent(rows: list) -> float:
    lo, hi = 0.0, max(r["private_density"] for r in rows) + 1.0
    if _profit(rows, lo) <= 0:
        return 0.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if _profit(rows, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def run_order() -> dict:
    rows = _table()
    private_order = _order(rows, "private_density")
    social_order = _order(rows, "social_density")
    tau = _kendall_tau(private_order, social_order)

    by_id = {r["id"]: r for r in rows}
    ranks = []
    for fid in IDS:
        ranks.append({
            "id": fid, "label": by_id[fid]["label"],
            "private_rank": private_order.index(fid) + 1,
            "social_rank": social_order.index(fid) + 1,
            "rank_shift": social_order.index(fid) - private_order.index(fid),
            "cut_rent": _cut_rent(by_id[fid]),
            "loss_ratio": by_id[fid]["loss_ratio"],
            "appropriability": by_id[fid]["appropriability"],
        })

    # the null: identical appropriability everywhere
    uniform = _table(appropr=[0.5] * len(FUNCTIONS))
    uniform_tau = _kendall_tau(_order(uniform, "private_density"),
                               _order(uniform, "social_density"))

    # what the first cut destroys against what the last cut destroys
    first, last = by_id[private_order[0]], by_id[private_order[-1]]

    # cumulative social value lost as rent rises
    trajectory = []
    total_social = sum(r["social"] for r in rows)
    for rent in RENT_GRID:
        kept = [r for r in rows if r["private_density"] >= rent]
        trajectory.append({
            "rent": float(rent),
            "functions_kept": len(kept),
            "social_kept": sum(r["social"] for r in kept) / total_social,
            "presence_kept": sum(r["social"] for r in kept if r["id"] in PRESENCE)
                             / sum(r["social"] for r in rows if r["id"] in PRESENCE),
            "profit": _profit(rows, float(rent)),
        })

    return {
        "rows": rows, "ranks": ranks,
        "private_order": private_order, "social_order": social_order,
        "kendall_tau": tau, "uniform_appropriability_tau": uniform_tau,
        "first_cut": private_order[0], "first_cut_loss_ratio": first["loss_ratio"],
        "last_cut": private_order[-1], "last_cut_loss_ratio": last["loss_ratio"],
        "loss_ratio_spread": first["loss_ratio"] / last["loss_ratio"],
        "presence_private_ranks": sorted(private_order.index(p) + 1 for p in PRESENCE),
        "presence_social_ranks": sorted(social_order.index(p) + 1 for p in PRESENCE),
        "total_social": total_social,
        "trajectory": trajectory,
    }


# ---------------------------------------------------------------------------
# 2. The lead
# ---------------------------------------------------------------------------
def run_lead() -> dict:
    rows = _table()
    by_id = {r["id"]: r for r in rows}
    closure = _closure_rent(rows)

    presence_rents = {p: _cut_rent(by_id[p]) for p in PRESENCE}
    first_loss = min(presence_rents.values())
    last_presence = max(presence_rents.values())

    total_social = sum(r["social"] for r in rows)
    presence_social = sum(by_id[p]["social"] for p in PRESENCE)

    def at(rent):
        kept = [r for r in rows if r["private_density"] >= rent]
        return {
            "rent": rent,
            "functions_kept": len(kept),
            "social_share_kept": sum(r["social"] for r in kept) / total_social,
            "presence_share_kept": sum(r["social"] for r in kept if r["id"] in PRESENCE)
                                   / presence_social,
            "profit": _profit(rows, rent),
            "profit_share_of_peak": _profit(rows, rent) / _profit(rows, 0.0),
        }

    gone = at(last_presence + 1e-9)
    return {
        "presence_cut_rents": presence_rents,
        "first_presence_loss_rent": first_loss,
        "all_presence_gone_rent": last_presence,
        "closure_rent": closure,
        "lead_over_closure": closure / last_presence,
        "lead_from_first_loss": closure / first_loss,
        "rent_span_still_open_without_presence": closure - last_presence,
        "share_of_rent_range_open_but_empty":
            (closure - last_presence) / closure,
        "at_presence_gone": gone,
        "social_lost_when_presence_gone": 1.0 - gone["social_share_kept"],
        "profit_retained_when_presence_gone": gone["profit_share_of_peak"],
        "presence_social_share": presence_social / total_social,
    }


# ---------------------------------------------------------------------------
# 3. The burden
# ---------------------------------------------------------------------------
# Per meal occasion. The operator pays for the site and charges for the food;
# nobody bills the operator for the journey, and no redesign of the site changes
# how far anyone drove to reach it.

TRIP_KM = 12.0            # round trip to reach the site
EMISSION_KG_PER_KM = 0.19
SITE_KG = 0.22            # construction amortised plus operating energy
FOOD_KG = 2.50            # producing the meal itself
TRIP_GRID = np.round(np.linspace(2.0, 30.0, 57), 4)
FACTOR_GRID = np.round(np.linspace(0.05, 0.30, 26), 4)


def _burden(trip_km, factor, site_kg=SITE_KG, food_kg=FOOD_KG) -> dict:
    travel = trip_km * factor
    total = travel + site_kg + food_kg
    return {"travel": travel, "site": site_kg, "food": food_kg, "total": total,
            "design_controlled_share": site_kg / total}


def run_burden() -> dict:
    rows = _table()
    presence_footprint = sum(r["footprint_share"] for r in rows if r["id"] in PRESENCE)

    base = _burden(TRIP_KM, EMISSION_KG_PER_KM)
    removable = presence_footprint * base["site"]
    base_reduction = removable / base["total"]

    grid = []
    for t in TRIP_GRID:
        for f in FACTOR_GRID:
            b = _burden(float(t), float(f))
            grid.append({"trip_km": float(t), "factor": float(f),
                         "design_controlled_share": b["design_controlled_share"],
                         "reduction_from_removing_all_presence":
                             presence_footprint * b["site"] / b["total"]})
    reductions = [g["reduction_from_removing_all_presence"] for g in grid]

    # what it would take for the design to control half the burden
    solve_food = None
    for site_kg in np.round(np.linspace(SITE_KG, 40.0, 4000), 4):
        if _burden(TRIP_KM, EMISSION_KG_PER_KM, site_kg)["design_controlled_share"] >= 0.5:
            solve_food = float(site_kg)
            break

    return {
        "trip_km": TRIP_KM, "emission_kg_per_km": EMISSION_KG_PER_KM,
        "site_kg": SITE_KG, "food_kg": FOOD_KG,
        "presence_footprint_share": presence_footprint,
        "base": base,
        "base_reduction_from_removing_all_presence": base_reduction,
        "grid_cells": len(grid),
        "min_reduction": float(np.min(reductions)),
        "max_reduction": float(np.max(reductions)),
        "median_reduction": float(np.median(reductions)),
        "reduction_never_exceeds": float(np.max(reductions)),
        "site_kg_needed_for_half_the_burden": solve_food,
        "site_kg_multiple_needed": solve_food / SITE_KG if solve_food else None,
        "grid": grid,
    }


# ---------------------------------------------------------------------------
# 4. The obligation
# ---------------------------------------------------------------------------
# A duty attached to the capacity to remain. Scaled to that capacity it simply
# lowers the rent at which the capacity is cut. Triggered by a threshold, it
# creates a notch: below the threshold the duty vanishes, so cutting capacity
# pays at any rent at all, including none.

COVERAGE_THRESHOLDS = np.round(np.linspace(0.02, 0.50, 49), 4)


def run_obligation() -> dict:
    rows = _table()
    by_id = {r["id"]: r for r in rows}
    total_private = sum(r["private"] for r in rows)
    total_social = sum(r["social"] for r in rows)
    presence_footprint = sum(r["footprint_share"] for r in rows if r["id"] in PRESENCE)

    # (a) a duty scaled to the capacity provided: the cut rent falls by exactly
    #     the duty's rate, so the capacity goes at a lower rent than it would
    scaled = []
    for rate in np.round(np.linspace(0.0, 16.0, 161), 4):
        rents = {p: _cut_rent(by_id[p]) - float(rate) for p in PRESENCE}
        scaled.append({"rate": float(rate),
                       "all_presence_gone_rent": max(rents.values()),
                       "gone_at_zero_rent": max(rents.values()) <= 0.0})
    zero_rent_rate = next((s["rate"] for s in scaled if s["gone_at_zero_rent"]), None)
    # the same quantity in closed form: the duty rate has to cover the most
    # appropriable of the presence functions
    zero_rent_rate_analytic = max(_cut_rent(by_id[p]) for p in PRESENCE)

    # (b) a duty triggered by a threshold on the capacity provided
    order = sorted((by_id[p] for p in PRESENCE), key=lambda r: r["private_density"])
    notch = []
    for theta in COVERAGE_THRESHOLDS:
        shed, sacrificed_private, sacrificed_social, dropped = 0.0, 0.0, 0.0, []
        remaining = presence_footprint
        for r in order:
            if remaining <= float(theta):
                break
            remaining -= r["footprint_share"]
            shed += r["footprint_share"]
            sacrificed_private += r["private"]
            sacrificed_social += r["social"]
            dropped.append(r["id"])
        reachable = remaining <= float(theta)
        notch.append({
            "threshold": float(theta), "reachable": reachable,
            "dropped": dropped, "n_dropped": len(dropped),
            "presence_footprint_after": remaining,
            "duty_that_triggers_the_cut": sacrificed_private,
            "duty_as_share_of_private_return": sacrificed_private / total_private,
            "social_destroyed": sacrificed_social,
            "social_destroyed_share": sacrificed_social / total_social,
            "social_destroyed_per_unit_duty":
                sacrificed_social / sacrificed_private if sacrificed_private else None,
        })

    focal = next(n for n in notch if abs(n["threshold"] - 0.10) < 1e-9)
    worst = max((n for n in notch if n["n_dropped"] > 0),
                key=lambda n: n["social_destroyed_per_unit_duty"])

    return {
        "total_private": total_private, "total_social": total_social,
        "presence_footprint_share": presence_footprint,
        "scaled": scaled,
        "duty_rate_removing_presence_at_zero_rent": zero_rent_rate,
        "duty_rate_removing_presence_at_zero_rent_analytic": zero_rent_rate_analytic,
        "notch": notch, "focal": focal, "worst": worst,
        "focal_threshold": focal["threshold"],
        "focal_duty_share": focal["duty_as_share_of_private_return"],
        "focal_social_destroyed_share": focal["social_destroyed_share"],
        "focal_dropped": focal["dropped"],
        "focal_leverage": focal["social_destroyed_share"] / focal["duty_as_share_of_private_return"],
    }


# ---------------------------------------------------------------------------
# Robustness
# ---------------------------------------------------------------------------
def run_ensemble(draws: int = 800) -> dict:
    """Does the ordering result survive other footprints and appropriabilities?"""
    rng = np.random.default_rng(SEED)
    base_c = np.array([f[2] for f in FUNCTIONS])
    base_a = np.array([f[4] for f in FUNCTIONS])
    presence_idx = [IDS.index(p) for p in PRESENCE]

    all_five, taus, first_is_presence = 0, [], 0
    within_six, worst_ranks, presence_mean_ranks = 0, [], []
    for _ in range(draws):
        c = base_c * rng.uniform(0.6, 1.4, size=base_c.shape)
        a = np.clip(base_a * rng.uniform(0.6, 1.4, size=base_a.shape), 0.01, 1.0)
        rows = _table(footprints=c.tolist(), appropr=a.tolist())
        priv = _order(rows, "private_density")
        soc = _order(rows, "social_density")
        taus.append(_kendall_tau(priv, soc))
        if set(priv[:5]) == set(PRESENCE):
            all_five += 1
        if priv[0] in PRESENCE:
            first_is_presence += 1
        pr = [priv.index(p) + 1 for p in PRESENCE]
        worst_ranks.append(max(pr))
        presence_mean_ranks.append(float(np.mean(pr)))
        if max(pr) <= 6:
            within_six += 1

    return {
        "draws": draws,
        "presence_is_the_first_five_share": all_five / draws,
        "first_cut_is_presence_share": first_is_presence / draws,
        "tau_median": float(np.median(taus)),
        "tau_min": float(np.min(taus)),
        "tau_max": float(np.max(taus)),
        "tau_never_reaches_one": bool(np.max(taus) < 1.0),
        "presence_within_first_six_share": within_six / draws,
        "worst_placed_way_of_staying_median_rank": float(np.median(worst_ranks)),
        "presence_mean_rank_median": float(np.median(presence_mean_ranks)),
        "presence_mean_rank_worst_draw": float(np.max(presence_mean_ranks)),
    }


# ---------------------------------------------------------------------------
# Invariants
# ---------------------------------------------------------------------------
def run() -> dict:
    order = run_order()
    lead = run_lead()
    burden = run_burden()
    obligation = run_obligation()
    ensemble = run_ensemble()

    rows = order["rows"]
    by_id = {r["id"]: r for r in rows}
    traj = order["trajectory"]
    single = [n for n in obligation["notch"] if n["n_dropped"] == 1]

    checks = {
        # the site
        "footprint_shares_sum_to_one":
            abs(sum(r["footprint_share"] for r in rows) - 1.0) < 1e-12,
        "private_return_is_appropriability_times_social_value": all(
            abs(r["private"] - r["appropriability"] * r["social"]) < 1e-12
            for r in rows),
        "the_loss_ratio_is_the_inverse_of_appropriability": all(
            abs(r["loss_ratio"] - 1.0 / r["appropriability"]) < 1e-12 for r in rows),

        # 1. the order of the cut
        "uniform_appropriability_makes_the_two_orders_identical":
            abs(order["uniform_appropriability_tau"] - 1.0) < 1e-12,
        "the_five_ways_of_staying_are_the_first_five_cut":
            set(order["private_order"][:5]) == set(PRESENCE),
        "the_orders_differ_without_being_reversed":
            0.0 < order["kendall_tau"] < 1.0,
        "what_a_public_evaluation_would_cut_first_is_parking_for_the_transaction":
            order["social_order"][0] == "parking",
        "the_cut_order_is_increasing_in_private_yield_density": all(
            by_id[order["private_order"][i]]["private_density"]
            < by_id[order["private_order"][i + 1]]["private_density"]
            for i in range(len(order["private_order"]) - 1)),

        # 2. the lead
        "profit_never_rises_with_rent": all(
            traj[i + 1]["profit"] <= traj[i]["profit"] + 1e-9
            for i in range(len(traj) - 1)),
        "social_value_never_rises_with_rent": all(
            traj[i + 1]["social_kept"] <= traj[i]["social_kept"] + 1e-12
            for i in range(len(traj) - 1)),
        "the_place_to_stay_goes_before_the_business_does":
            lead["all_presence_gone_rent"] < lead["closure_rent"],
        "the_site_is_still_profitable_when_the_last_seat_goes":
            lead["at_presence_gone"]["profit"] > 0,
        "only_the_transaction_survives_to_closure":
            abs(_profit(rows, lead["closure_rent"])) < 1e-6
            and sum(1 for r in rows
                    if r["private_density"] >= lead["closure_rent"]) == 1,

        # 3. the burden
        "the_three_burdens_sum_to_the_total":
            abs(burden["base"]["travel"] + burden["base"]["site"]
                + burden["base"]["food"] - burden["base"]["total"]) < 1e-12,
        "design_never_controls_a_tenth_of_the_burden": all(
            g["design_controlled_share"] < 0.10 for g in burden["grid"]),
        "removing_every_way_of_staying_never_cuts_the_burden_by_a_twentieth":
            burden["max_reduction"] < 0.05,
        "the_burden_reduction_falls_as_the_journey_grows": all(
            burden["grid"][i]["reduction_from_removing_all_presence"] > 0
            for i in range(len(burden["grid"]))),

        # 4. the obligation
        "a_scaled_duty_lowers_the_cut_rent_by_exactly_its_rate":
            abs(obligation["scaled"][10]["all_presence_gone_rent"]
                - (obligation["scaled"][0]["all_presence_gone_rent"]
                   - obligation["scaled"][10]["rate"])) < 1e-9,
        "the_grid_and_the_closed_form_agree_on_the_duty_that_empties_a_site":
            abs(obligation["duty_rate_removing_presence_at_zero_rent"]
                - obligation["duty_rate_removing_presence_at_zero_rent_analytic"]) < 0.11,
        "a_notch_that_costs_one_function_destroys_its_loss_ratio_in_value": all(
            abs(n["social_destroyed_per_unit_duty"]
                - by_id[n["dropped"][0]]["loss_ratio"]) < 1e-9 for n in single),
        "the_duty_is_cheaper_to_dodge_than_the_dodging_costs_society":
            obligation["focal_leverage"] > 1.0,
        "a_lower_threshold_never_costs_the_operator_less": all(
            obligation["notch"][i]["duty_as_share_of_private_return"]
            >= obligation["notch"][i + 1]["duty_as_share_of_private_return"] - 1e-12
            for i in range(len(obligation["notch"]) - 1)),
        "every_swept_threshold_is_reachable_by_cutting":
            all(n["reachable"] for n in obligation["notch"]),

        # robustness
        "the_ordering_result_is_not_an_artifact_of_the_chosen_numbers":
            ensemble["presence_is_the_first_five_share"] > 0.5,
        "no_draw_ever_aligns_the_private_and_social_orders":
            ensemble["tau_never_reaches_one"],

        # housekeeping
        "shares_stay_in_the_unit_interval": all(
            0.0 <= t[k] <= 1.0 for t in traj
            for k in ("social_kept", "presence_kept")),
    }

    failed = [k for k, v in checks.items() if not v]
    if failed:
        raise AssertionError("invariants failed: " + ", ".join(failed))

    return _py({"seed": SEED, "order": order, "lead": lead, "burden": burden,
                "obligation": obligation, "ensemble": ensemble, "checks": checks})
