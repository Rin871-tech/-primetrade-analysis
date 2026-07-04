"""
Debug: Check date formats in both CSVs
"""

import pandas as pd

print("=" * 80)
print("DEBUGGING DATE FORMATS")
print("=" * 80)

# Load sentiment data
sentiment_df = pd.read_csv('bitcoin_sentiment.csv')
print("\n📍 SENTIMENT DATA:")
print(f"Shape: {sentiment_df.shape}")
print(f"Columns: {sentiment_df.columns.tolist()}")
print("\nFirst 5 rows:")
print(sentiment_df.head())
print(f"\nUnique dates in 'date' column: {sentiment_df['date'].nunique()}")
print("Sample dates:")
print(sentiment_df['date'].unique()[:5])

# Load trader data
trader_df = pd.read_csv('trader_data.csv')
print("\n📍 TRADER DATA:")
print(f"Shape: {trader_df.shape}")
print(f"Columns: {trader_df.columns.tolist()}")
print("\nFirst 5 rows:")
print(trader_df[['Account', 'Timestamp', 'Closed PnL']].head())

# Try to parse trader timestamps
print("\n📍 PARSING TRADER TIMESTAMPS:")
try:
    trader_df['Timestamp'] = pd.to_datetime(trader_df['Timestamp'], format='%d-%m-%Y %H:%M', errors='coerce')
    trader_df['date'] = trader_df['Timestamp'].dt.date
    print(f"✓ Parsed successfully")
    print(f"Unique dates in trader data: {trader_df['date'].nunique()}")
    print("Sample dates:")
    print(trader_df['date'].unique()[:5])
except Exception as e:
    print(f"✗ Error: {e}")

# Convert sentiment dates to datetime
print("\n📍 PARSING SENTIMENT DATES:")
print(f"Sample sentiment dates as-is:")
print(sentiment_df['date'].head(10))

# Try parsing sentiment dates
try:
    sentiment_df['date_parsed'] = pd.to_datetime(sentiment_df['date'], format='%Y-%m-%d', errors='coerce')
    sentiment_df['date_only'] = sentiment_df['date_parsed'].dt.date
    print(f"✓ Parsed with format '%Y-%m-%d'")
    print(f"Unique dates: {sentiment_df['date_only'].nunique()}")
    print("Sample:")
    print(sentiment_df[['date', 'date_only']].head(10))
except Exception as e:
    print(f"✗ Error: {e}")

# Check date overlap
print("\n📍 CHECKING DATE OVERLAP:")
trader_dates = set(trader_df['date'].dropna().unique())
sentiment_dates = set(sentiment_df['date_only'].dropna().unique())

overlap = trader_dates.intersection(sentiment_dates)
print(f"Trader dates: {len(trader_dates)}")
print(f"Sentiment dates: {len(sentiment_dates)}")
print(f"Overlapping dates: {len(overlap)}")
print(f"\nFirst 5 overlapping dates: {list(overlap)[:5]}")