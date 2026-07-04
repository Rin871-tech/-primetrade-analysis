# Primetrade.ai Data Science Intern - Assignment Solution

**Objective**: Analyze trader performance vs market sentiment on Hyperliquid  
**Expected Runtime**: ~15-20 minutes (after data is ready)  
**Status**: Ready to execute

---

## ⚡ QUICK START (You are here!)

### Step 1: Download the Data (5 minutes)
1. Visit the Google Drive links provided:
   - **Sentiment Data**: https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing
   - **Trader Data**: https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing
2. Click the download icon (↓) in the top right of each Drive folder
3. Save both files to your working directory:
   - Rename to `bitcoin_sentiment.csv`
   - Rename to `trader_data.csv`

### Step 2: Set Up Environment (2 minutes)
```bash
pip install pandas numpy matplotlib seaborn
```

### Step 3: Run Analysis (5 minutes)
```bash
python primetrade_solution.py
```

This will:
- Load and validate both datasets
- Create key metrics (PnL, win rate, leverage, etc.)
- Generate 3 publication-ready charts
- Export summary statistics
- Print all key findings to console

### Step 4: Customize Write-up (10 minutes)
1. Open `WRITEUP.md`
2. Replace all `[VALUE]` and `[X]` placeholders with actual numbers from your analysis output
3. Review the strategy recommendations and adjust to match your findings
4. Keep it to ~1 page

### Step 5: Prepare Submission (5 minutes)
Create a GitHub repo or Google Drive folder with:
```
/primetrade_submission
├── primetrade_solution.py          (main analysis script)
├── WRITEUP.md                      (1-page summary)
├── README.md                       (this file)
├── insight_1_performance_by_sentiment.png
├── insight_2_behavior_by_sentiment.png
├── insight_3_segmentation_analysis.png
└── summary_statistics.csv
```

**Submit via the Google Form provided by Primetrade.ai**

---

## 📊 What Each Output Means

### insight_1_performance_by_sentiment.png
- **Left**: PnL distribution (Fear vs Greed days)
- **Right**: Win rate comparison
- **Key Question Answered**: Q1 - Does performance differ by sentiment?

### insight_2_behavior_by_sentiment.png
- **Left**: Trade frequency changes
- **Middle**: Leverage usage changes  
- **Right**: Position size changes
- **Key Question Answered**: Q2 - Do traders change behavior?

### insight_3_segmentation_analysis.png
- **Left**: High vs Low leverage traders
- **Middle**: Frequent vs Infrequent traders
- **Right**: Winners vs Inconsistent traders
- **Key Question Answered**: Q3 - What segments exist and how do they perform?

### summary_statistics.csv
- Complete summary table with all metrics
- Use these numbers to fill the WRITEUP.md placeholders

---

## 🎯 Evaluation Criteria Checklist

Before submitting, verify:

- [ ] **Data Cleaning** (Part A)
  - Loaded both datasets without errors
  - Documented rows, columns, missing values, duplicates
  - Successfully aligned datasets by date
  - Created all required metrics (PnL, win rate, leverage, etc.)

- [ ] **Analysis** (Part B)
  - Question 1: Performance comparison with evidence
  - Question 2: Behavioral changes with evidence
  - Question 3: 2-3 trader segments identified
  - At least 3 charts/visualizations provided

- [ ] **Actionable Output** (Part C)
  - 2+ strategy recommendations provided
  - Each includes "rule of thumb" phrasing
  - Backed by data and segments
  - Realistic and implementable

- [ ] **Communication**
  - Write-up is clear and structured
  - No generic insights (specific to YOUR data)
  - Charts are labeled and readable
  - Code is commented and reproducible

- [ ] **Reproducibility**
  - Code runs without modifications (update file paths)
  - README clearly explains setup
  - All dependencies listed
  - All outputs saved with correct filenames

---

## 🔧 Troubleshooting

### "Module not found" error
```bash
pip install pandas numpy matplotlib seaborn
```

### "File not found: bitcoin_sentiment.csv"
- Check file names match exactly: `bitcoin_sentiment.csv` and `trader_data.csv`
- Check files are in same directory as script
- Or modify the file paths in the script:
  ```python
  sentiment_df = pd.read_csv('/path/to/your/file.csv')
  ```

### "No columns found for [metric]"
- Check your CSV column names match the code
- You may need to adjust column references in the script
- Print `trader_df.columns` to see available columns

### "Sentiment data won't merge"
- Ensure date columns are converted to datetime format
- Both datasets should have a date/timestamp column
- Verify date ranges overlap between datasets

---

## 💡 Pro Tips

1. **Skip the bonus**: Focus on A, B, C - this is enough for shortlisting
2. **Use actual numbers**: Don't round for the write-up—use raw values from `summary_statistics.csv`
3. **Make insights specific**: "Traders use 2.3x more leverage during Fear" beats "Traders change leverage"
4. **Link strategies to segments**: "For high-leverage traders, reduce leverage 20% during Fear" is actionable
5. **Charts speak louder**: Clean, labeled visualizations are key to credibility

---

## ⏱️ Timeline

If running NOW and submitting by 11:50 PM:
- **11:00 - 11:15**: Download data + setup
- **11:15 - 11:25**: Run script + collect outputs
- **11:25 - 11:45**: Fill in write-up with actual numbers
- **11:45 - 11:50**: Final check + submit

**You've got this!** 🚀

---

## Questions?

If the script fails:
1. Check that CSV file names match exactly
2. Print the first few rows: `print(sentiment_df.head())`
3. Check column names: `print(trader_df.columns)`
4. Adjust the script to match your data structure

Good luck! 💪