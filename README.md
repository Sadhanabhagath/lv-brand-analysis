# Louis Vuitton Brand Data Analysis

> A comprehensive data analysis project on Louis Vuitton — the world's largest luxury fashion house, valued at approximately **$40.7 billion**.

---

## Project Overview

This project explores the financial performance, market positioning, regional distribution, and brand strength of Louis Vuitton through data analysis and interactive visualisation. Louis Vuitton, founded in Paris in 1854, is the flagship brand of LVMH and is globally renowned for its iconic monogrammed leather goods and high-end ready-to-wear collections.

---

## Objectives

- Analyse Louis Vuitton's revenue growth trend from 2019 to 2024
- Break down revenue by region and product category
- Benchmark LV against key luxury competitors (Chanel, Hermès, Gucci, Prada, Dior)
- Assess brand strength across six strategic dimensions
- Identify key growth drivers and risk factors

---

## Key Findings

### Revenue Growth
- LVMH Fashion & Leather Goods (LV's core segment) grew from **€21.2B in 2020** to **€42.2B in 2023** — nearly doubling in three years
- 2021 saw explosive **+46% YoY growth** driven by post-COVID revenge spending
- Growth moderated in 2024 (~€40.8B estimated) amid macroeconomic headwinds in Asia Pacific

### Operating Margin
- Operating margins expanded from **28% (2020)** to **~42% (2023)**, reflecting LV's pricing power and cost discipline
- Luxury's inelastic demand model shields margins even during broader economic downturns

### Regional Breakdown (2023 estimates)
| Region         | Revenue Share |
|----------------|--------------|
| Asia Pacific   | 35%          |
| Europe         | 26%          |
| United States  | 24%          |
| Japan          | 9%           |
| Other markets  | 6%           |

> Asia Pacific is LV's largest market — sensitivity to Chinese consumer confidence is a key risk factor

### Product Category Mix
| Category              | Share |
|-----------------------|-------|
| Leather goods         | 52%   |
| Ready-to-wear         | 20%   |
| Shoes                 | 14%   |
| Watches & jewellery   | 8%    |
| Other                 | 6%    |

### Competitive Positioning (Brand Value, $B)
| Brand          | Brand Value |
|----------------|------------|
| Louis Vuitton  | $40.7B     |
| Chanel         | $22.1B     |
| Hermès         | $19.3B     |
| Gucci          | $15.6B     |
| Prada          | $9.8B      |
| Dior           | $8.4B      |

LV leads the luxury sector by a significant margin — nearly **2x the brand value of Chanel**, its closest competitor.

### Brand Strength Scorecard
| Dimension         | Score  |
|-------------------|--------|
| Brand recognition | 98/100 |
| Price premium     | 95/100 |
| Heritage & story  | 92/100 |
| Innovation index  | 80/100 |
| Digital presence  | 74/100 |
| Sustainability    | 61/100 |

> LV scores near-perfect on heritage and pricing power. Sustainability remains a structural gap as Gen Z scrutiny on luxury ESG practices intensifies.

---

## Growth Drivers & Risks

### Growth Drivers
- Digital expansion and e-commerce investment
- High-profile collaborations (Supreme, Tyler the Creator, Pharrell Williams)
- Experiential retail and flagship store investments
- China market recovery potential
- Men's fashion and streetwear crossover
- Travel retail rebound post-COVID

### Key Risks
- China slowdown and geopolitical sensitivity
- Global counterfeit market (~$500B annually industry-wide)
- Brand dilution risk from over-expansion
- FX volatility affecting reported EUR revenues
- Gen Z preference shifts toward understated luxury
- Increasing ESG and sustainability scrutiny

---

## Tools & Technologies

- **Python** — data processing and analysis (Pandas, NumPy)
- **Chart.js** — interactive data visualisation
- **HTML/CSS/JavaScript** — interactive dashboard
- **Data sources** — LVMH Annual Reports, Kantar BrandZ, Interbrand, industry estimates

---

## Repository Structure

```
lv-brand-analysis/
│
├── README.md               # Project overview and findings (this file)
├── analysis.py             # Python EDA script
├── data/
│   └── lv_data.csv         # Dataset (revenue, regions, categories, competitors)
├── dashboard/
│   └── dashboard.html      # Interactive visualisation dashboard
└── requirements.txt        # Python dependencies
```

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/Sadhanabhagath/lv-brand-analysis.git
cd lv-brand-analysis

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python analysis.py

# Open the dashboard
open dashboard/dashboard.html
```

---

## About

**Bhagath Sadhana**
B.Tech — Computer Science and Engineering, Vel Tech University
- Email: bhagathsadhana28@gmail.com
- GitHub: [github.com/Sadhanabhagath](https://github.com/Sadhanabhagath)

---

*Data sourced from LVMH Annual Reports, Kantar BrandZ Global 2024, Interbrand Best Global Brands, and publicly available industry estimates. All figures are approximate and for analytical purposes.*
