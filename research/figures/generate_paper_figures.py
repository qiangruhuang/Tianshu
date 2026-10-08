#!/usr/bin/env python3
"""Generate Paper 1 Figures 1–5 from frozen/committed evidence.

Run from repository root:
    python research/figures/generate_paper_figures.py

Outputs are written to research/figures/generated/.
No experiment is run by this script; it only visualizes already frozen results.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "figures" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

# Figure 1: architecture
fig, ax = plt.subplots(figsize=(13, 4.3))
ax.set_axis_off()
labels = [
    ("Persistent\nsemantics", 0.03), ("Mission\nSnapshot", 0.20),
    ("Readiness", 0.37), ("GSC\nCompiler", 0.52),
    ("Planner", 0.68), ("Validator", 0.82),
]
w = 0.12
for label, x in labels:
    box = FancyBboxPatch((x, 0.42), w, 0.28,
                         boxstyle="round,pad=0.02,rounding_size=0.02",
                         transform=ax.transAxes)
    ax.add_patch(box)
    ax.text(x+w/2, 0.56, label, ha="center", va="center",
            transform=ax.transAxes, fontsize=12, fontweight="bold")
for (_, x1), (_, x2) in zip(labels[:-1], labels[1:]):
    ax.add_patch(FancyArrowPatch((x1+w, 0.56), (x2, 0.56),
                                transform=ax.transAxes, arrowstyle="->",
                                mutation_scale=16, linewidth=1.5))
ax.text(0.58, 0.25,
        "admitted Provider–Action set\n+ rejection provenance\n+ snapshot / revision / hash binding",
        ha="center", va="center", transform=ax.transAxes, fontsize=10)
ax.text(0.87, 0.22,
        "release only if current-state,\nauthorization, provider,\nmembership & freshness checks pass",
        ha="center", va="center", transform=ax.transAxes, fontsize=9)
fig.tight_layout()
fig.savefig(OUT / "Fig1_GSC_architecture.png", dpi=220, bbox_inches="tight")
fig.savefig(OUT / "Fig1_GSC_architecture.svg", bbox_inches="tight")
plt.close(fig)

# Figures 2–4 use the frozen compact data file.
summary = pd.read_csv(ROOT / "research" / "figures" / "Paper1_figure_data.csv")

# Figure 2: E1 same-cardinality mechanism test.
d = summary[summary.figure == "Fig2"]
fig, ax = plt.subplots(figsize=(8.6, 4.8))
bars = ax.barh(d.item, d.value_1)
ax.set_xlabel("Median generated nodes under A* (N=640, rho=0.05)")
ax.set_xscale("log")
for bar, val in zip(bars, d.value_1):
    ax.text(val*1.06, bar.get_y()+bar.get_height()/2, f"{val:g}", va="center", fontsize=10)
ax.text(0.02, -0.20,
        "Blind search solved: GSC 30/30; Random-core 20/30; State-aware 0/30; Full-domain 0/30.",
        transform=ax.transAxes, fontsize=9)
fig.tight_layout()
fig.savefig(OUT / "Fig2_E1_same_cardinality_mechanism.png", dpi=220, bbox_inches="tight")
fig.savefig(OUT / "Fig2_E1_same_cardinality_mechanism.svg", bbox_inches="tight")
plt.close(fig)

# Figure 3: E5 q=0 conditional reduction.
d = summary[summary.figure == "Fig3"]
fig, ax = plt.subplots(figsize=(8.2, 4.8))
bars = ax.bar(d.item, d.value_1)
ax.set_ylabel("Median generated-node reduction vs Full-domain (%)")
ax.set_ylim(0, 75)
for bar, val in zip(bars, d.value_1):
    ax.text(bar.get_x()+bar.get_width()/2, val+2, f"{val:.1f}%", ha="center", fontsize=10)
ax.text(0.02, -0.18, "At q=1, all methods converge.", transform=ax.transAxes, fontsize=9)
fig.tight_layout()
fig.savefig(OUT / "Fig3_E5_public_topology_reduction.png", dpi=220, bbox_inches="tight")
fig.savefig(OUT / "Fig3_E5_public_topology_reduction.svg", bbox_inches="tight")
plt.close(fig)

# Figure 4: E6b native admission/selectivity.
d = summary[summary.figure == "Fig4"]
adm = d.value_1.to_numpy(dtype=float)
tot = d.value_2.to_numpy(dtype=float)
fig, ax = plt.subplots(figsize=(8.4, 4.8))
ax.bar(d.item, adm, label="Admitted")
ax.bar(d.item, tot-adm, bottom=adm, label="Excluded")
ax.set_ylabel("Provider-related objects")
ax.legend()
for i, (a, t) in enumerate(zip(adm, tot)):
    ax.text(i, t+1, f"{int(a)}/{int(t)}", ha="center", fontsize=10)
ax.text(0.02, -0.18,
        "Overall: 165/181 admitted; 16/181 excluded (8.84%); 136/136 goals retain >=1 witness.",
        transform=ax.transAxes, fontsize=9)
fig.tight_layout()
fig.savefig(OUT / "Fig4_E6b_native_provider_admission.png", dpi=220, bbox_inches="tight")
fig.savefig(OUT / "Fig4_E6b_native_provider_admission.svg", bbox_inches="tight")
plt.close(fig)

# Figure 5: E6b mature-planner null from committed paired results.
pairs = pd.read_csv(ROOT / "e6b" / "results" / "run-37713826709" / "paired_results.csv")
pairs["generated_ratio"] = pairs.gsc_generated / pairs.full_generated
pairs["expansion_ratio"] = pairs.gsc_expansions / pairs.full_expansions
pairs["plan_ratio"] = pairs.gsc_plan_length / pairs.full_plan_length
x = np.arange(len(pairs))
fig, ax = plt.subplots(figsize=(10.5, 4.9))
ax.plot(x, pairs.generated_ratio, marker="o", label="Generated states")
ax.plot(x, pairs.expansion_ratio, marker="s", label="Expanded states")
ax.plot(x, pairs.plan_ratio, marker="^", label="Plan length")
ax.axhline(1.0, linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(pairs.instance.str.replace(".pddl", "", regex=False), rotation=45)
ax.set_ylabel("GSC / Full ratio")
ax.set_ylim(0.95, 1.05)
ax.legend(ncol=3)
ax.text(0.02, -0.28,
        "All 12 pairs also have identical translator variables/facts/operators and byte-identical final sas_plan.",
        transform=ax.transAxes, fontsize=9)
fig.tight_layout()
fig.savefig(OUT / "Fig5_E6b_mature_planner_null.png", dpi=220, bbox_inches="tight")
fig.savefig(OUT / "Fig5_E6b_mature_planner_null.svg", bbox_inches="tight")
plt.close(fig)

print(f"Generated figures in {OUT}")
