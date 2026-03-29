"""
Louis Vuitton Brand Data Analysis
Author: Bhagath Sadhana
GitHub: https://github.com/Sadhanabhagath
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")

plt.rcParams.update({
    "figure.facecolor": "#FAFAFA",
    "axes.facecolor": "#FAFAFA",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "font.family": "sans-serif",
    "font.size": 11,
})

PURPLE = "#7F77DD"
TEAL   = "#1D9E75"
AMBER  = "#EF9F27"
CORAL  = "#D85A30"
GRAY   = "#888780"

# ── 1. DATASETS ─────────────────────────────────────────────────────────────

revenue_df = pd.DataFrame({
    "year":    [2019, 2020, 2021, 2022, 2023, 2024],
    "revenue": [22.2, 21.2, 30.9, 38.6, 42.2, 40.8],   # €B LVMH F&L
    "margin":  [33,   28,   39,   41,   42,   40],        # operating margin %
})
revenue_df["growth"] = revenue_df["revenue"].pct_change() * 100

region_df = pd.DataFrame({
    "region":  ["Asia Pacific", "Europe", "United States", "Japan", "Other"],
    "share":   [35, 26, 24, 9, 6],
})

product_df = pd.DataFrame({
    "category": ["Leather goods", "Ready-to-wear", "Shoes", "Watches & jewellery", "Other"],
    "share":    [52, 20, 14, 8, 6],
})

competitor_df = pd.DataFrame({
    "brand":       ["Louis Vuitton", "Chanel", "Hermès", "Gucci", "Prada", "Dior"],
    "brand_value": [40.7, 22.1, 19.3, 15.6, 9.8, 8.4],  # $B
})

scorecard_df = pd.DataFrame({
    "dimension": ["Brand recognition", "Price premium", "Heritage & story",
                  "Innovation index", "Digital presence", "Sustainability"],
    "score":     [98, 95, 92, 80, 74, 61],
})


# ── 2. EDA — SUMMARY STATISTICS ─────────────────────────────────────────────

print("=" * 55)
print("  LOUIS VUITTON — BRAND DATA ANALYSIS")
print("=" * 55)

print("\n── Revenue Summary (LVMH Fashion & Leather Goods, €B) ──")
print(revenue_df[["year","revenue","growth","margin"]].to_string(index=False))

print(f"\n  CAGR 2019–2023 : {((42.2/22.2)**0.25 - 1)*100:.1f}%")
print(f"  Peak revenue   : €{revenue_df['revenue'].max()}B ({int(revenue_df.loc[revenue_df['revenue'].idxmax(),'year'])})")
print(f"  Peak margin    : {revenue_df['margin'].max()}% ({int(revenue_df.loc[revenue_df['margin'].idxmax(),'year'])})")
print(f"  Avg margin     : {revenue_df['margin'].mean():.1f}%")

print("\n── Regional Revenue Share ──")
print(region_df.to_string(index=False))
print(f"\n  Top region     : {region_df.loc[region_df['share'].idxmax(),'region']} ({region_df['share'].max()}%)")

print("\n── Product Category Mix ──")
print(product_df.to_string(index=False))
print(f"\n  Core category  : {product_df.loc[product_df['share'].idxmax(),'category']} ({product_df['share'].max()}%)")

print("\n── Competitive Benchmark ($B brand value) ──")
print(competitor_df.to_string(index=False))
lv_val = competitor_df.loc[competitor_df["brand"] == "Louis Vuitton", "brand_value"].values[0]
chanel_val = competitor_df.loc[competitor_df["brand"] == "Chanel", "brand_value"].values[0]
print(f"\n  LV vs Chanel premium : {lv_val/chanel_val:.1f}x")
print(f"  LV vs avg of others  : {lv_val / competitor_df[competitor_df['brand'] != 'Louis Vuitton']['brand_value'].mean():.1f}x")

print("\n── Brand Strength Scorecard ──")
print(scorecard_df.to_string(index=False))
print(f"\n  Overall avg score : {scorecard_df['score'].mean():.1f}/100")
print(f"  Strongest dim     : {scorecard_df.loc[scorecard_df['score'].idxmax(),'dimension']}")
print(f"  Weakest dim       : {scorecard_df.loc[scorecard_df['score'].idxmin(),'dimension']}")
print("=" * 55)


# ── 3. VISUALISATIONS ────────────────────────────────────────────────────────

fig = plt.figure(figsize=(16, 14))
fig.suptitle("Louis Vuitton — Brand Data Analysis Dashboard",
             fontsize=16, fontweight="bold", y=0.98, color="#2C2C2A")

# ── 3a. Revenue trend ────────────────────────────────────────────────────────
ax1 = fig.add_subplot(3, 3, (1, 2))
bars = ax1.bar(revenue_df["year"], revenue_df["revenue"],
               color=PURPLE, alpha=0.85, width=0.6, zorder=2, label="Revenue (€B)")
ax1.plot(revenue_df["year"], revenue_df["revenue"],
         color=PURPLE, marker="o", markersize=5, linewidth=1.5, zorder=3)
for bar, val in zip(bars, revenue_df["revenue"]):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             f"€{val}B", ha="center", va="bottom", fontsize=9, color="#3C3489")
ax1.set_title("Revenue Trend — LVMH Fashion & Leather Goods", fontsize=11, fontweight="500")
ax1.set_ylabel("Revenue (€B)")
ax1.set_ylim(0, 50)
ax1.set_xticks(revenue_df["year"])

# ── 3b. YoY growth ──────────────────────────────────────────────────────────
ax2 = fig.add_subplot(3, 3, 3)
growth_data = revenue_df.dropna(subset=["growth"])
colors_g = [TEAL if g >= 0 else CORAL for g in growth_data["growth"]]
ax2.bar(growth_data["year"], growth_data["growth"].round(1),
        color=colors_g, alpha=0.85, width=0.6, zorder=2)
ax2.axhline(0, color=GRAY, linewidth=0.8, linestyle="--")
for x, g in zip(growth_data["year"], growth_data["growth"]):
    ax2.text(x, g + (1.5 if g >= 0 else -3), f"{g:.1f}%",
             ha="center", fontsize=8.5, color="#2C2C2A")
ax2.set_title("YoY Revenue Growth (%)", fontsize=11, fontweight="500")
ax2.set_ylabel("Growth (%)")
ax2.set_xticks(growth_data["year"])

# ── 3c. Operating margin ─────────────────────────────────────────────────────
ax3 = fig.add_subplot(3, 3, 4)
ax3.fill_between(revenue_df["year"], revenue_df["margin"],
                 alpha=0.2, color=AMBER)
ax3.plot(revenue_df["year"], revenue_df["margin"],
         color=AMBER, marker="o", markersize=6, linewidth=2)
for x, m in zip(revenue_df["year"], revenue_df["margin"]):
    ax3.text(x, m + 0.8, f"{m}%", ha="center", fontsize=9, color="#633806")
ax3.set_title("Operating Margin (%)", fontsize=11, fontweight="500")
ax3.set_ylabel("Margin (%)")
ax3.set_ylim(20, 50)
ax3.set_xticks(revenue_df["year"])

# ── 3d. Regional breakdown ───────────────────────────────────────────────────
ax4 = fig.add_subplot(3, 3, 5)
region_colors = [PURPLE, "#AFA9EC", "#CECBF6", "#7F77DD", GRAY]
wedges, texts, autotexts = ax4.pie(
    region_df["share"], labels=region_df["region"],
    autopct="%1.0f%%", colors=region_colors,
    startangle=140, pctdistance=0.75,
    textprops={"fontsize": 8.5}
)
for at in autotexts:
    at.set_fontsize(8)
    at.set_color("white")
ax4.set_title("Revenue by Region", fontsize=11, fontweight="500")

# ── 3e. Product mix donut ────────────────────────────────────────────────────
ax5 = fig.add_subplot(3, 3, 6)
prod_colors = [PURPLE, TEAL, AMBER, "#D4537E", GRAY]
wedges2, texts2, autotexts2 = ax5.pie(
    product_df["share"], labels=product_df["category"],
    autopct="%1.0f%%", colors=prod_colors,
    startangle=90, pctdistance=0.78,
    wedgeprops=dict(width=0.55),
    textprops={"fontsize": 8}
)
for at in autotexts2:
    at.set_fontsize(8)
    at.set_color("white")
ax5.set_title("Product Category Mix", fontsize=11, fontweight="500")

# ── 3f. Competitor benchmark ─────────────────────────────────────────────────
ax6 = fig.add_subplot(3, 3, (7, 8))
bar_colors = [PURPLE] + [GRAY] * (len(competitor_df) - 1)
hbars = ax6.barh(competitor_df["brand"], competitor_df["brand_value"],
                 color=bar_colors, alpha=0.85, height=0.6, zorder=2)
for bar, val in zip(hbars, competitor_df["brand_value"]):
    ax6.text(val + 0.3, bar.get_y() + bar.get_height()/2,
             f"${val}B", va="center", fontsize=9, color="#2C2C2A")
ax6.set_title("Luxury Brand Benchmark — Brand Value ($B)", fontsize=11, fontweight="500")
ax6.set_xlabel("Brand Value ($B)")
ax6.invert_yaxis()
ax6.set_xlim(0, 50)

# ── 3g. Brand strength radar-style bar ───────────────────────────────────────
ax7 = fig.add_subplot(3, 3, 9)
sc_colors = [TEAL if s >= 85 else AMBER if s >= 70 else CORAL
             for s in scorecard_df["score"]]
hbars2 = ax7.barh(scorecard_df["dimension"], scorecard_df["score"],
                  color=sc_colors, alpha=0.85, height=0.6, zorder=2)
for bar, val in zip(hbars2, scorecard_df["score"]):
    ax7.text(val + 0.5, bar.get_y() + bar.get_height()/2,
             str(val), va="center", fontsize=9, color="#2C2C2A")
ax7.set_title("Brand Strength Scorecard", fontsize=11, fontweight="500")
ax7.set_xlabel("Score / 100")
ax7.invert_yaxis()
ax7.set_xlim(0, 112)
legend_patches = [
    mpatches.Patch(color=TEAL,  label="Strong (≥85)"),
    mpatches.Patch(color=AMBER, label="Good (70–84)"),
    mpatches.Patch(color=CORAL, label="Gap (<70)"),
]
ax7.legend(handles=legend_patches, fontsize=8, loc="lower right",
           framealpha=0.6, edgecolor="none")

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig("lv_analysis_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nDashboard saved as lv_analysis_dashboard.png")
