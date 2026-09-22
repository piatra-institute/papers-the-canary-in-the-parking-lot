"""Figures for *The Canary in the Parking Lot*."""
from __future__ import annotations

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

INK, GRID = "#1a1a1a", "#d9d9d9"
AMBER, GREEN, BLUE, GRAY, RED = "#b45309", "#15803d", "#2563eb", "#57534e", "#b3202c"
PRESENCE = ("shelter", "seating", "restrooms", "dwell", "commons")


def _style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK)
    ax.tick_params(colors=INK, labelsize=8.5)
    ax.set_axisbelow(True)
    ax.grid(True, color=GRID, lw=0.6)


def plot_order(res, path):
    O, L = res["order"], res["lead"]
    fig, axes = plt.subplots(1, 3, figsize=(12.6, 3.9))

    # a. the order of the cut
    ax = axes[0]
    _style(ax)
    ranks = {r["id"]: r for r in O["ranks"]}
    ids = O["private_order"]
    y = np.arange(len(ids))
    vals = [ranks[i]["cut_rent"] for i in ids]
    cols = [AMBER if i in PRESENCE else BLUE for i in ids]
    ax.barh(y, vals, color=cols, height=0.66)
    ax.set_yticks(y)
    ax.set_yticklabels([ranks[i]["label"] for i in ids], fontsize=7.6)
    ax.set_xscale("log")
    ax.set_xlabel("ground rent at which the function is removed",
                  fontsize=8.5)
    ax.axhline(4.5, color=INK, lw=0.9, ls="--")
    ax.text(0.97, 0.47, "ways of staying\n(below the line)",
            transform=ax.transAxes, ha="right", va="top", fontsize=7.6, color=INK,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.9, pad=2.2))
    ax.set_title("a. order of removal",
                 fontsize=9.5, color=INK, loc="left")
    ax.legend(handles=[Patch(facecolor=AMBER, label="a way of staying"),
                       Patch(facecolor=BLUE, label="transactional function")],
              loc="lower right", fontsize=7.6, frameon=True, framealpha=0.92,
              facecolor="white", edgecolor="none")

    # b. what is lost, and when
    ax = axes[1]
    _style(ax)
    t = O["trajectory"]
    rent = [x["rent"] for x in t]
    peak = t[0]["profit"]
    ax.plot(rent, [x["social_kept"] for x in t], color=GREEN, lw=1.8,
            label="social value")
    ax.plot(rent, [max(x["profit"], 0) / peak for x in t], color=BLUE, lw=1.8,
            label="profit vs peak")
    ax.plot(rent, [x["presence_kept"] for x in t], color=AMBER, lw=1.8,
            label="ways of staying")
    ax.axvline(L["all_presence_gone_rent"], color=AMBER, lw=0.9, ls="--")
    ax.axvline(L["closure_rent"], color=RED, lw=0.9, ls="--")
    ax.axvspan(L["all_presence_gone_rent"], L["closure_rent"], color=GRID, alpha=0.5)
    ax.text(L["all_presence_gone_rent"] * 1.30, 0.90,
            f"last way of staying\nremoved at {L['all_presence_gone_rent']:.1f}",
            fontsize=7.6, color=AMBER, va="top")
    ax.text(L["closure_rent"] * 0.97, 0.60, f"closure at\nrent "
            f"{L['closure_rent']:.1f}", fontsize=7.6, color=RED, ha="right")
    ax.set_xlabel("ground rent", fontsize=8.5)
    ax.set_ylabel("share remaining", fontsize=8.5)
    ax.set_ylim(-0.03, 1.06)
    ax.set_title("b. value and profit under rising rent", fontsize=9.5,
                 color=INK, loc="left")
    ax.legend(fontsize=7.6, frameon=True, framealpha=0.92, facecolor="white",
              edgecolor="none", loc="upper right")

    # c. private against social ordering
    ax = axes[2]
    _style(ax)
    for r in O["ranks"]:
        c = AMBER if r["id"] in PRESENCE else BLUE
        ax.plot([0, 1.6], [r["private_rank"], r["social_rank"]], color=c, lw=1.4,
                marker="o", ms=3.4)
        ax.text(-0.06, r["private_rank"], r["label"], fontsize=6.8, color=INK,
                ha="right", va="center")
    ax.set_xlim(-2.6, 3.05)
    ax.set_xticks([0, 1.6])
    ax.set_xticklabels(["operator\norder", "social\norder"], fontsize=7.6)
    ax.set_yticks([])
    ax.grid(False)
    ax.text(1.74, 3.4, f"τ = {O['kendall_tau']:.3f}\n(1.000 with uniform\nappropriability)", fontsize=7.4, color=INK, va="top")
    ax.set_title("c. private and social order, first removed at bottom", fontsize=9.5,
                 color=INK, loc="left")

    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_burden(res, path):
    B, Q = res["burden"], res["obligation"]
    fig, axes = plt.subplots(1, 3, figsize=(12.6, 3.9))

    # a. what a meal occasion actually costs
    ax = axes[0]
    _style(ax)
    base = B["base"]
    parts = [("travel", base["travel"], GRAY),
             ("food", base["food"], GREEN),
             ("site", base["site"], AMBER)]
    left = 0.0
    for label, val, col in parts:
        ax.barh([0], [val], left=left, color=col, height=0.5)
        if val / base["total"] > 0.08:
            ax.text(left + val / 2, 0, f"{label}\n{val:.2f}", ha="center",
                    va="center", fontsize=8, color="white")
        left += val
    ax.annotate(f"site: {base['design_controlled_share']:.3f} of total",
                xy=(base["travel"] + base["food"] + base["site"] / 2, 0.28),
                xytext=(1.5, 0.68), fontsize=7.8, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.9))
    ax.set_ylim(-0.6, 0.95)
    ax.set_yticks([])
    ax.set_xlabel("kg CO$_2$e per meal occasion, stipulated", fontsize=8.5)
    ax.set_title("a. burden of one meal occasion", fontsize=9.5,
                 color=INK, loc="left")

    # b. the sweep
    ax = axes[1]
    _style(ax)
    g = B["grid"]
    trips = sorted({x["trip_km"] for x in g})
    facs = sorted({x["factor"] for x in g})
    M = np.zeros((len(facs), len(trips)))
    for x in g:
        M[facs.index(x["factor"]), trips.index(x["trip_km"])] = \
            x["reduction_from_removing_all_presence"] * 100
    im = ax.imshow(M, origin="lower", aspect="auto", cmap="YlOrBr",
                   extent=[trips[0], trips[-1], facs[0], facs[-1]])
    cb = fig.colorbar(im, ax=ax)
    cb.ax.tick_params(labelsize=7.5)
    cb.set_label("per cent", fontsize=8)
    ax.set_xlabel("round trip to reach the site, km", fontsize=8.5)
    ax.set_ylabel("kg CO$_2$e per km", fontsize=8.5)
    ax.set_title("b. burden reduction from removing ways of staying (%)",
                 fontsize=9.5, color=INK, loc="left")
    ax.text(0.97, 0.06, f"maximum {B['max_reduction']*100:.2f}% over "
            f"{B['grid_cells']} cells", transform=ax.transAxes, ha="right",
            fontsize=7.6, color=INK,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.88, pad=2.4))

    # c. the notch
    ax = axes[2]
    _style(ax)
    n = Q["notch"]
    th = [x["threshold"] for x in n]
    ax.plot(th, [x["duty_as_share_of_private_return"] for x in n], color=BLUE,
            lw=1.8, label="private return given up")
    ax.plot(th, [x["social_destroyed_share"] for x in n], color=GREEN, lw=1.8,
            label="social value lost")
    ax.axvline(Q["focal_threshold"], color=INK, lw=0.9, ls=":")
    ax.set_xlabel("threshold share of the site given to staying", fontsize=8.5)
    ax.set_ylabel("share", fontsize=8.5)
    ax.set_title("c. cost of avoiding a threshold duty", fontsize=9.5,
                 color=INK, loc="left")
    ax.legend(fontsize=7.6, frameon=True, framealpha=0.92, facecolor="white",
              edgecolor="none", loc="center left")
    ax.annotate(f"threshold 0.10: private return {Q['focal_duty_share']:.3f},\n"
                f"social value "
                f"{Q['focal_social_destroyed_share']:.3f}",
                xy=(Q["focal_threshold"], Q["focal_duty_share"]),
                xytext=(0.515, 0.435), ha="right", va="top", fontsize=7.4, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.9),
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.9, pad=2.2))

    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
