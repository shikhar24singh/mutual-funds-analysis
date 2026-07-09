# Bluestock Mutual Fund Analytics Capstone

A comprehensive end-to-end Data Analytics project that analyzes the Indian Mutual Fund industry using Python, SQLite, SQL, Power BI, and statistical analysis. The project covers data ingestion, cleaning, exploratory data analysis, financial performance evaluation, advanced risk metrics, and an interactive Power BI dashboard.

---

## Project Overview

The objective of this project is to build a complete Mutual Fund Analytics pipeline capable of:

- Cleaning and integrating multiple mutual fund datasets
- Storing processed data in SQLite
- Performing SQL-based business analysis
- Conducting Exploratory Data Analysis (EDA)
- Computing financial performance and risk metrics
- Building an interactive Power BI dashboard
- Creating a simple mutual fund recommendation system

---

## Project Structure

```
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│       └── bluestock_mf.db
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Dataset Description

The project uses ten datasets representing different aspects of the Indian Mutual Fund ecosystem.

| Dataset | Description |
|----------|-------------|
| Fund Master | Scheme information, fund house, category, expense ratio |
| NAV History | Historical daily NAV values |
| AUM by Fund House | Assets Under Management trends |
| Monthly SIP Inflows | SIP investment statistics |
| Category Inflows | Net inflows by mutual fund category |
| Industry Folio Count | Investor folio statistics |
| Scheme Performance | Returns, Sharpe Ratio inputs, risk metrics |
| Investor Transactions | SIP, Lump Sum and Redemption transactions |
| Portfolio Holdings | Stock and sector allocations |
| Benchmark Indices | Market benchmark data (NIFTY50, etc.) |

---

# Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- SQLite
- SQL
- Power BI
- Jupyter Notebook
- VS Code

---

# ETL Pipeline

The ETL process includes:

- Reading raw CSV files
- Cleaning missing values
- Standardizing column names
- Removing duplicates
- Data type conversion
- Exporting cleaned datasets
- Loading into SQLite database

---

# Database Design

The project uses SQLite as its analytical database.

Main tables include:

- fund_master
- nav_history
- aum_by_fund_house
- monthly_sip_inflows
- category_inflows
- industry_folio_count
- scheme_performance
- investor_transactions
- portfolio_holdings
- benchmark_indices

---

# SQL Analysis

SQL queries were written to answer common business questions including:

- Top fund houses by AUM
- NAV trends
- Monthly SIP growth
- Category-wise inflows
- Investor transaction summaries
- Portfolio allocation analysis
- Benchmark comparison

---

# Exploratory Data Analysis

The EDA notebook includes:

- NAV Trend Analysis
- AUM Growth Analysis
- Monthly SIP Trends
- Category Inflow Heatmaps
- Investor Demographics
- Geographic Distribution
- Folio Growth
- NAV Correlation Heatmap
- Sector Allocation Analysis
- Key EDA Insights

---

# Performance Analytics

Financial performance metrics computed include:

- Daily Returns
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Fund Scorecard
- Benchmark Comparison

Generated reports include:

- sharpe_ratio_report.csv
- sortino_ratio_report.csv
- alpha_beta.csv
- drawdown_report.csv
- fund_scorecard.csv

---

# Advanced Analytics

Advanced analysis includes:

- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Mutual Fund Recommendation System
- Sector HHI Concentration
- Advanced Business Insights

Generated reports include:

- var_cvar_report.csv
- rolling_sharpe_chart.png
- sip_continuity_report.csv
- sector_hhi_report.csv

---

# Power BI Dashboard

The Power BI dashboard consists of four pages.

## Page 1 — Industry Overview

- KPI Cards
- Industry AUM Trend
- AUM by AMC
- SIP Growth
- Industry Summary

---

## Page 2 — Fund Performance

- Risk vs Return Scatter Plot
- NAV Trend
- Fund Performance Table
- Fund Filters

---

## Page 3 — Investor Analytics

- State-wise Investments
- Gender Distribution
- Age Group Analysis
- Transaction Type Analysis

---

## Page 4 — SIP & Market Trends

- SIP vs NIFTY50 Trend
- Category Inflow Heatmap
- Top Categories
- Market Trend Analysis

---

# Recommendation System

The recommendation engine ranks funds using:

- Risk Grade
- Sharpe Ratio
- Three-Year Return
- Expense Ratio

Users can select:

- Low Risk
- Moderate Risk
- High Risk

The script returns the top three matching mutual funds.

---

# Key Features

- Complete ETL Pipeline
- SQLite Database
- SQL Analytics
- Exploratory Data Analysis
- Financial Performance Analysis
- Risk Analytics
- Power BI Dashboard
- Recommendation Engine

---

# How to Run

## Clone Repository

```bash
git clone <repository-url>
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

---

## Compute Financial Metrics

```bash
python scripts/compute_metrics.py
```

---

## Run Recommendation Engine

```bash
python scripts/recommender.py
```

---

## Open Dashboard

Open:

```
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

# Results

The project successfully demonstrates:

- End-to-end Data Analytics workflow
- Financial performance evaluation
- Risk-adjusted investment analysis
- Portfolio concentration analysis
- Interactive business intelligence dashboard
- Automated mutual fund recommendations

---

# Future Improvements

- Live AMFI API integration
- Real-time NAV updates
- Machine Learning-based recommendation engine
- Portfolio optimization using Modern Portfolio Theory
- Streamlit web application deployment
- Cloud database integration

---

# Author

**Shikhar Singh**

B.Tech CSE (Data Science)

Ajay Kumar Garg Engineering College

---

# License

This project is intended for educational and portfolio purposes.