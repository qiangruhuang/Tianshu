#!/usr/bin/env python3
"""Reproduce Paper 1 Figures 1–5 in submission-safe formats.

Run from repository root:
    python research/figures/generate_paper_figures_v1_2.py

Outputs:
    research/figures/rendered/*.png   (preview, 300 dpi)
    research/figures/rendered/*.pdf   (vector submission source)
    research/figures/rendered/*.eps   (vector submission source)

No experiment is rerun. The script visualizes frozen reported evidence only.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "rendered"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.size": 10,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

def save_all(fig, stem):
    fig.savefig(OUT / f"{stem}.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.eps", bbox_inches="tight")
    plt.close(fig)

fig, ax = plt.subplots(figsize=(7.5, 2.7))
ax.set_axis_off()
labels = [("Persistent\nsemantics",0.01),("Mission\nSnapshot",0.19),("Readiness",0.37),("GSC\nCompiler",0.52),("Planner",0.68),("Validator",0.83)]
w = 0.13
for label, x in labels:
    ax.add_patch(FancyBboxPatch((x,0.48),w,0.25,boxstyle="round,pad=0.015,rounding_size=0.02",transform=ax.transAxes,fill=False,linewidth=1.2))
    ax.text(x+w/2,0.605,label,ha="center",va="center",transform=ax.transAxes,fontsize=9,fontweight="bold")
for (_,x1),(_,x2) in zip(labels[:-1],labels[1:]):
    ax.add_patch(FancyArrowPatch((x1+w,0.605),(x2,0.605),transform=ax.transAxes,arrowstyle="->",mutation_scale=12,linewidth=1.0))
ax.text(0.585,0.29,"admitted Provider–Action set\n+ rejection provenance\n+ snapshot / revision / hash binding",ha="center",va="center",transform=ax.transAxes,fontsize=8)
ax.text(0.895,0.25,"current-state + authorization\n+ provider + freshness checks",ha="center",va="center",transform=ax.transAxes,fontsize=8)
fig.tight_layout(); save_all(fig,"Fig1_GSC_architecture")

methods=["GSC","Random-core","State-aware","Full-domain"]; generated=[4,31,308,612]
fig,ax=plt.subplots(figsize=(6.2,3.8)); bars=ax.barh(methods,generated); ax.set_xlabel("Median generated nodes under A* (N=640, ρ=0.05)"); ax.set_xscale("log"); ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
for bar,val in zip(bars,generated): ax.text(val*1.07,bar.get_y()+bar.get_height()/2,str(val),va="center",fontsize=9)
ax.text(0.0,-0.22,"Blind search solved: 30/30, 20/30, 0/30, and 0/30, respectively.",transform=ax.transAxes,fontsize=8)
fig.tight_layout(); save_all(fig,"Fig2_E1_same_cardinality_mechanism")

tasks=["Rovers 03","Rovers 05","Rovers 07"]; reductions=[38.5,45.5,66.7]
fig,ax=plt.subplots(figsize=(5.8,3.6)); bars=ax.bar(tasks,reductions); ax.set_ylabel("Generated-node reduction vs Full-domain (%)"); ax.set_ylim(0,75); ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
for bar,val in zip(bars,reductions): ax.text(bar.get_x()+bar.get_width()/2,val+1.8,f"{val:.1f}%",ha="center",fontsize=9)
ax.text(0.0,-0.21,"At q=1, all methods converge.",transform=ax.transAxes,fontsize=8)
fig.tight_layout(); save_all(fig,"Fig3_E5_public_topology_reduction")

cats=["Rovers","Cameras","Stores"]; adm=np.array([58,60,47]); tot=np.array([58,65,58]); exc=tot-adm
fig,ax=plt.subplots(figsize=(5.8,3.6)); ax.bar(cats,adm,label="Admitted"); ax.bar(cats,exc,bottom=adm,label="Excluded"); ax.set_ylabel("Provider-related objects"); ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False); ax.legend(frameon=False)
for i,(a,t) in enumerate(zip(adm,tot)): ax.text(i,t+1.0,f"{a}/{t}",ha="center",fontsize=9)
ax.text(0.0,-0.21,"165/181 admitted; 16/181 excluded (8.84%); 136/136 goals retain ≥1 witness.",transform=ax.transAxes,fontsize=8)
fig.tight_layout(); save_all(fig,"Fig4_E6b_native_provider_admission")

paired=ROOT/"e6b"/"results"/"run-37713826709"/"paired_results.csv"; df=pd.read_csv(paired); assert len(df)==12; assert (df["full_generated"]==df["gsc_generated"]).all(); assert (df["full_expansions"]==df["gsc_expansions"]).all(); assert (df["full_plan_length"]==df["gsc_plan_length"]).all()
metrics=["Generated states","Expanded states","Plan length","Translator task","Final plan bytes"]; identical=[12]*5
fig,ax=plt.subplots(figsize=(6.2,3.8)); bars=ax.barh(metrics,identical); ax.set_xlim(0,12.8); ax.set_xlabel("Identical Full–GSC pairs (out of 12)"); ax.set_xticks([0,3,6,9,12]); ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
for bar in bars: ax.text(12.08,bar.get_y()+bar.get_height()/2,"12/12",va="center",fontsize=9)
ax.text(0.0,-0.19,"Fast Downward 26.6; final plans are byte-identical for all holdout tasks.",transform=ax.transAxes,fontsize=8)
fig.tight_layout(); save_all(fig,"Fig5_E6b_mature_planner_null")
print(f"Figures written to {OUT}")
