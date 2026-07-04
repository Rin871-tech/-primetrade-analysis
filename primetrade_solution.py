"""
Primetrade.ai Data Science Intern - Final Analysis
Fixed for Unix timestamps in trader data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 6)

print("=" * 80)
print("PRIMETRADE.AI - TRADER PERFORMANCE VS SENTIMENT ANALYSIS")
print("=" * 80)

# ============================================================================
# PART A: DATA LOADING
# ============================================================================

print("\n[PART A] Loading and preparing datasets...")

# Load sentiment data
sentiment_df = pd.read_csv('bitcoin_sentiment.csv')
print(f"✓ Sentiment data: {sentiment_df.shape}")

# Load trader data
trader_df = pd.read_csv('trader_data.csv')
print(f"✓ Trader data: {trader_df.shape}")

# ============================================================================
# PART B: DATA PREPARATION
# ============================================================================

print("\n[PART B] Data preparation...")

# Convert sentiment date string to date object
sentiment_df['date'] = pd.to_datetime(sentiment_df['date'], format='%Y-%m-%d').dt.date

# Convert trader Unix timestamp to date
# Timestamp column is in MILLISECONDS (Unix epoch), so divide by 1000
trader_df['Timestamp'] = pd.to_datetime(trader_df['Timestamp'], unit='ms')
trader_df['date'] = trader_df['Timestamp'].dt.date

print(f"✓ Timestamp conversion complete")
print(f"✓ Sentiment date range: {min(sentiment_df['date'])} to {max(sentiment_df['date'])}")
print(f"✓ Trader date range: {min(trader_df['date'])} to {max(trader_df['date'])}")

# Create daily sentiment mapping
daily_sentiment = sentiment_df.groupby('date')['classification'].first().reset_index()
daily_sentiment.columns = ['date', 'sentiment']
print(f"✓ Sentiment days: {len(daily_sentiment)}")

# ============================================================================
# PART C: CREATE METRICS
# ============================================================================

print("\n[PART C] Creating trading metrics...")

# Daily PnL by account
daily_pnl = trader_df.groupby(['date', 'Account']).agg({
    'Closed PnL': ['sum', 'mean', 'std'],
    'Account': 'count'
}).reset_index()
daily_pnl.columns = ['date', 'account', 'total_pnl', 'avg_pnl_per_trade', 'pnl_std', 'num_trades']

# Win rate by account
trader_df['is_win'] = trader_df['Closed PnL'] > 0
daily_win_rate = trader_df.groupby(['date', 'Account']).agg({
    'is_win': 'mean'
}).reset_index()
daily_win_rate.columns = ['date', 'account', 'win_rate']

# Average trade size
daily_size = trader_df.groupby(['date', 'Account']).agg({
    'Size USD': 'mean'
}).reset_index()
daily_size.columns = ['date', 'account', 'avg_trade_size_usd']

print("✓ Metrics created:")
print(f"  - Daily PnL: {len(daily_pnl)} records")
print(f"  - Win rates: {len(daily_win_rate)} records")
print(f"  - Trade sizes: {len(daily_size)} records")

# ============================================================================
# MERGE ALL METRICS WITH SENTIMENT
# ============================================================================

print("\n[PART D] Merging with sentiment data...")

# Merge all metrics
analysis_df = daily_pnl.copy()
analysis_df = analysis_df.merge(daily_win_rate, on=['date', 'account'], how='left')
analysis_df = analysis_df.merge(daily_size, on=['date', 'account'], how='left')

# Merge with sentiment
analysis_df = analysis_df.merge(daily_sentiment, on='date', how='left')

# Remove rows without sentiment data
analysis_df = analysis_df.dropna(subset=['sentiment'])

print(f"✓ Final analysis dataset: {analysis_df.shape}")
print(f"✓ Date range for analysis: {analysis_df['date'].min()} to {analysis_df['date'].max()}")

if len(analysis_df) == 0:
    print("\n⚠️  WARNING: No overlapping dates between sentiment and trader data!")
    print("Sentiment data is from 2018, but trader data is from 2024.")
    print("Using ALL trader data with sentiment mapping for same dates...")
    
    # Use all trader metrics regardless of sentiment overlap
    analysis_df = daily_pnl.copy()
    analysis_df = analysis_df.merge(daily_win_rate, on=['date', 'account'], how='left')
    analysis_df = analysis_df.merge(daily_size, on=['date', 'account'], how='left')
    analysis_df = analysis_df.merge(daily_sentiment, on='date', how='left')
    analysis_df['sentiment'] = analysis_df['sentiment'].fillna('Current Period')

# ============================================================================
# PART E: ANALYSIS & INSIGHTS
# ============================================================================

print("\n" + "=" * 80)
print("ANALYSIS RESULTS")
print("=" * 80)

print("\n1. PERFORMANCE BY SENTIMENT REGIME\n")

fear_data = analysis_df[analysis_df['sentiment'].str.contains('Fear', case=False, na=False)]
greed_data = analysis_df[analysis_df['sentiment'].str.contains('Greed', case=False, na=False)]
neutral_data = analysis_df[~analysis_df['sentiment'].str.contains('Fear|Greed', case=False, na=False)]

print(f"FEAR Days ({len(fear_data)} records):")
if len(fear_data) > 0:
    print(f"  - Avg Daily PnL: ${fear_data['total_pnl'].mean():,.2f}")
    print(f"  - Median Daily PnL: ${fear_data['total_pnl'].median():,.2f}")
    print(f"  - Avg Win Rate: {fear_data['win_rate'].mean()*100:.1f}%")
    print(f"  - Avg Trade Size (USD): ${fear_data['avg_trade_size_usd'].mean():,.2f}")
else:
    print("  (No Fear data)")

print(f"\nGREED Days ({len(greed_data)} records):")
if len(greed_data) > 0:
    print(f"  - Avg Daily PnL: ${greed_data['total_pnl'].mean():,.2f}")
    print(f"  - Median Daily PnL: ${greed_data['total_pnl'].median():,.2f}")
    print(f"  - Avg Win Rate: {greed_data['win_rate'].mean()*100:.1f}%")
    print(f"  - Avg Trade Size (USD): ${greed_data['avg_trade_size_usd'].mean():,.2f}")
else:
    print("  (No Greed data)")

if len(neutral_data) > 0:
    print(f"\nOTHER SENTIMENT ({len(neutral_data)} records):")
    print(f"  - Avg Daily PnL: ${neutral_data['total_pnl'].mean():,.2f}")
    print(f"  - Avg Win Rate: {neutral_data['win_rate'].mean()*100:.1f}%")

# Use whichever group has data
if len(fear_data) > 0 and len(greed_data) > 0:
    pnl_diff = greed_data['total_pnl'].mean() - fear_data['total_pnl'].mean()
    wr_diff = (greed_data['win_rate'].mean() - fear_data['win_rate'].mean()) * 100
    print(f"\n📊 KEY DIFFERENCE (Greed - Fear):")
    print(f"  - PnL: ${pnl_diff:+,.2f}")
    print(f"  - Win Rate: {wr_diff:+.1f}%")

# ============================================================================
# VISUALIZATIONS
# ============================================================================

print("\n[GENERATING CHARTS]...")

fig = plt.figure(figsize=(15, 12))

# Chart 1: PnL by sentiment
ax1 = plt.subplot(2, 2, 1)
sentiment_groups = list(analysis_df['sentiment'].unique())
pnl_by_sentiment = [analysis_df[analysis_df['sentiment'] == s]['total_pnl'].dropna().values for s in sentiment_groups if s]
if pnl_by_sentiment:
    bp1 = ax1.boxplot(pnl_by_sentiment)
    ax1.set_xticklabels(sentiment_groups)
    ax1.set_title('Daily PnL Distribution by Sentiment', fontweight='bold')
    ax1.set_ylabel('Daily PnL ($)')
    ax1.grid(alpha=0.3)

# Chart 2: Win rate by sentiment
ax2 = plt.subplot(2, 2, 2)
wr_by_sentiment = [analysis_df[analysis_df['sentiment'] == s]['win_rate'].dropna().values for s in sentiment_groups if s]
if wr_by_sentiment:
    bp2 = ax2.boxplot(wr_by_sentiment)
    ax2.set_xticklabels(sentiment_groups)
    ax2.set_title('Win Rate by Sentiment', fontweight='bold')
    ax2.set_ylabel('Win Rate')
    ax2.grid(alpha=0.3)

# Chart 3: Trade size by sentiment
ax3 = plt.subplot(2, 2, 3)
size_by_sentiment = [analysis_df[analysis_df['sentiment'] == s]['avg_trade_size_usd'].dropna().values for s in sentiment_groups if s]
if size_by_sentiment:
    bp3 = ax3.boxplot(size_by_sentiment)
    ax3.set_xticklabels(sentiment_groups)
    ax3.set_title('Average Trade Size (USD) by Sentiment', fontweight='bold')
    ax3.set_ylabel('Trade Size (USD)')
    ax3.grid(alpha=0.3)

# Chart 4: Number of trades
ax4 = plt.subplot(2, 2, 4)
trades_by_sentiment = [analysis_df[analysis_df['sentiment'] == s]['num_trades'].dropna().values for s in sentiment_groups if s]
if trades_by_sentiment:
    bp4 = ax4.boxplot(trades_by_sentiment)
    ax4.set_xticklabels(sentiment_groups)
    ax4.set_title('Number of Trades per Day by Sentiment', fontweight='bold')
    ax4.set_ylabel('Number of Trades')
    ax4.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('insight_1_performance_by_sentiment.png', dpi=300, bbox_inches='tight')
print("✓ Saved: insight_1_performance_by_sentiment.png")
plt.close()

# Summary comparison
fig, ax = plt.subplots(figsize=(12, 6))

summary_data = []
summary_labels = []
for sentiment in sentiment_groups:
    s_data = analysis_df[analysis_df['sentiment'] == sentiment]
    if len(s_data) > 0:
        summary_data.append([
            s_data['total_pnl'].mean(),
            s_data['win_rate'].mean() * 100,
            s_data['avg_trade_size_usd'].mean() / 1000,
            s_data['num_trades'].mean()
        ])
        summary_labels.append(sentiment)

if summary_data:
    summary_data = np.array(summary_data)
    x = np.arange(len(summary_labels))
    width = 0.2
    
    metrics = ['Avg PnL', 'Win Rate (%)', 'Avg Size (K)', 'Num Trades']
    
    for i, metric in enumerate(metrics):
        ax.bar(x + i*width, summary_data[:, i], width, label=metric, alpha=0.8)
    
    ax.set_ylabel('Value', fontsize=11)
    ax.set_title('Key Metrics by Sentiment', fontsize=13, fontweight='bold')
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(summary_labels)
    ax.legend()
    ax.grid(alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('insight_2_summary_comparison.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: insight_2_summary_comparison.png")
    plt.close()

# ============================================================================
# SAVE SUMMARY STATISTICS
# ============================================================================

summary_rows = []
for sentiment in sentiment_groups:
    s_data = analysis_df[analysis_df['sentiment'] == sentiment]
    if len(s_data) > 0:
        summary_rows.append({
            'Sentiment': sentiment,
            'Avg Daily PnL': s_data['total_pnl'].mean(),
            'Median Daily PnL': s_data['total_pnl'].median(),
            'Avg Win Rate': f"{s_data['win_rate'].mean()*100:.1f}%",
            'Avg Trade Size (USD)': s_data['avg_trade_size_usd'].mean(),
            'Avg Num Trades': s_data['num_trades'].mean(),
            'Records': len(s_data)
        })

summary_stats = pd.DataFrame(summary_rows)
summary_stats.to_csv('summary_statistics.csv', index=False)
print("✓ Saved: summary_statistics.csv")

# ============================================================================
# STRATEGIES
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY RECOMMENDATIONS")
print("=" * 80)

overall_avg_size = analysis_df['avg_trade_size_usd'].mean()
overall_avg_pnl = analysis_df['total_pnl'].mean()
overall_win_rate = analysis_df['win_rate'].mean()

print(f"""
OVERALL PERFORMANCE:
- Average Daily PnL: ${overall_avg_pnl:,.2f}
- Average Win Rate: {overall_win_rate*100:.1f}%
- Average Trade Size: ${overall_avg_size:,.2f}

STRATEGY 1: Adaptive Position Sizing
→ Increase position sizes during high-performance periods
→ Reduce sizes during periods with negative average PnL
→ Dynamic sizing based on daily sentiment and past performance

STRATEGY 2: Risk Management by Sentiment
→ Tighten stop losses when win rate < {overall_win_rate*100:.1f}%
→ Expand profit targets when win rate > {overall_win_rate*100:.1f}%
→ Adjust leverage inversely with sentiment volatility

STRATEGY 3: Trading Frequency Optimization
→ Increase trade frequency during high-PnL periods
→ Reduce frequency during drawdown periods
→ Monitor P&L trend and adjust execution speed accordingly
""")

print("\n" + "=" * 80)
print("✅ ANALYSIS COMPLETE!")
print("=" * 80)
print("\nOutputs generated:")
print("  1. insight_1_performance_by_sentiment.png")
print("  2. insight_2_summary_comparison.png")
print("  3. summary_statistics.csv")
print("\nNext: Fill WRITEUP.md with these values and submit!")