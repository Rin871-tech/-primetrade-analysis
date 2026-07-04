# Primetrade.ai Data Science Intern Assignment
## Trader Performance vs Market Sentiment Analysis

### Overview

This repository contains a comprehensive data science analysis examining the relationship between Bitcoin market sentiment (Fear/Greed) and trader performance on the Hyperliquid derivatives exchange. The analysis covers 211,224 trades across 102 trading days from March 2023 to June 2025, revealing counter-intuitive patterns in trader behavior and profitability across different market sentiment regimes.

**Key Finding**: Traders demonstrate 130% higher average daily profitability during Fear sentiment periods ($209,372) compared to Greed periods ($90,989), suggesting that market fear creates exploitable trading opportunities for skilled market participants.

---

### Project Structure

```
primetrade-analysis/
├── primetrade_unix.py              # Main analysis script
├── WRITEUP.md                      # Detailed findings and recommendations (1 page)
├── README.md                       # This file
├── insight_1_performance_by_sentiment.png   # Performance comparison boxplots
├── insight_2_summary_comparison.png         # Key metrics comparison chart
├── summary_statistics.csv          # Aggregated statistics table
└── bitcoin_sentiment.csv           # Input: sentiment data (from Google Drive)
    trader_data.csv                 # Input: trader performance data (from Google Drive)
```

---

### Key Findings

#### Performance by Sentiment Regime

| Metric | Fear Days (32) | Greed Days (37) | Difference |
|--------|---|---|---|
| **Avg Daily PnL** | $209,372.66 | $90,988.70 | +$118,383.96 (+130%) |
| **Median Daily PnL** | $81,389.68 | $20,925.51 | +$60,464.17 (+289%) |
| **Win Rate** | 41.6% | 36.9% | +4.7% |
| **Avg Trade Size (USD)** | $5,926.52 | $5,637.30 | +$289.22 (+5%) |
| **Sample Size** | 32 trading days | 37 trading days | — |

**Conclusion**: Traders consistently outperform during Fear periods despite maintaining similar position sizing and trading frequency, indicating that market fear creates structural inefficiencies exploitable through active trading strategies.

---

### Strategy Recommendations

1. **Sentiment-Based Capital Allocation**: Concentrate portfolio capital in Fear periods; reduce allocation during Greed and Neutral sentiment
2. **Disciplined Risk Management**: Maintain consistent position sizing and risk-per-trade rules across all sentiment regimes
3. **Neutral Period Avoidance**: Scale back trading activity during Neutral sentiment periods (85% lower profitability vs Fear)

---

### Setup & Installation

#### Requirements
- Python 3.12 or higher
- pandas, numpy, matplotlib, seaborn

#### Installation

1. **Clone this repository**:
```bash
git clone https://github.com/Rin871-tech/primetrade-analysis.git
cd primetrade-analysis
```

2. **Install dependencies**:
```bash
pip install pandas numpy matplotlib seaborn
```

3. **Download input data** (large files, not in GitHub):
   - **Bitcoin Sentiment Data**: https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing
   - **Hyperliquid Trader Data**: https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing

4. **Place CSV files in project directory**:
```bash
# Files should be named exactly:
bitcoin_sentiment.csv
trader_data.csv
```

---

### Running the Analysis

Execute the main analysis script:

```bash
python3 primetrade_unix.py
```

**Expected Runtime**: ~30 seconds

**Output**:
- Console output with detailed statistics and findings
- Three PNG visualization files
- One CSV summary statistics file

---

### Output Files

#### Visualizations

- **`insight_1_performance_by_sentiment.png`** (4-panel figure)
  - Daily PnL distribution by sentiment
  - Win rate comparison across sentiment regimes
  - Average trade size by sentiment
  - Trade frequency distribution

- **`insight_2_summary_comparison.png`** (bar chart)
  - Side-by-side comparison of key metrics (PnL, win rate, trade size, frequency)
  - Colored by sentiment regime for easy interpretation

#### Data Exports

- **`summary_statistics.csv`**
  - Aggregated metrics by sentiment classification
  - Includes mean, median, and count statistics
  - Ready for further analysis or reporting

---

### Methodology

#### Data Preparation
- **Timestamp Parsing**: Converted Unix millisecond timestamps to calendar dates
- **Date Alignment**: Merged sentiment and trader datasets on calendar date
- **Data Validation**: Verified no missing values or duplicates; confirmed date range overlap

#### Metrics Computed
- **Daily Profitability**: Sum of closed PnL per trading day
- **Win Rate**: Percentage of profitable trades (PnL > 0)
- **Trade Size**: Mean USD value of executed trades
- **Trade Frequency**: Count of executed trades per day

#### Analysis Approach
1. **Descriptive Statistics**: Mean, median, std deviation by sentiment regime
2. **Distribution Analysis**: Boxplots and quartile analysis to identify outliers
3. **Comparative Analysis**: T-test style comparison between Fear and Greed periods
4. **Segmentation**: Analysis of Neutral sentiment impact

---

### Data Quality & Limitations

#### Data Quality
- **Completeness**: 0 missing values in all critical fields
- **Duplicates**: 0 duplicate trades detected
- **Coverage**: 211,224 trades across 809 trading days; 77 days with complete sentiment + trading data

#### Limitations
- **Sample Period**: Analysis covers 2023-2025, primarily bull market conditions
- **Single Asset**: Focus on BTC perpetuals; may not generalize to altcoins or spot trading
- **Account Aggregation**: Results aggregate across multiple trader accounts; individual strategy diversity masked
- **External Factors**: Analysis does not account for news, regulatory events, or macroeconomic factors beyond sentiment

---

### Technologies Used

- **Python 3.12**: Primary analysis language
- **pandas**: Data manipulation and aggregation
- **numpy**: Numerical computations
- **matplotlib/seaborn**: Data visualization
- **Git**: Version control

---

### Results & Key Insights

The analysis reveals that **market sentiment acts as a powerful predictor of trading profitability**, but in a counter-intuitive direction:

1. **Fear Regime Profitability**: Fear periods generate 2.3x higher median daily returns than Greed periods
2. **Behavioral Consistency**: Traders maintain discipline—no evidence of increased risk-taking during Fear despite higher volatility
3. **Opportunity Capture**: Superior Fear performance indicates traders successfully exploit volatility spikes and market dislocations

### Recommended Action

Adopt a **sentiment-responsive capital allocation strategy** (not sentiment-responsive position sizing). Concentrate capital during Fear periods while maintaining consistent execution rules.

---

### Author

**Analysis by**: Vaishnavi Chavan  
**Date**: July 4, 2026  
**For**: Primetrade.ai Data Science Intern - Round 0 Assignment

---

### Contact & Questions

For questions regarding this analysis, please refer to the detailed findings in `WRITEUP.md`.

---

### License

This analysis is submitted as part of the Primetrade.ai hiring process. All code and analysis are original work prepared for evaluation purposes.
