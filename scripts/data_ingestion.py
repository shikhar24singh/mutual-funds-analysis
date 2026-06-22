import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
aum_by_fund_house = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
monthly_sip_inflows = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category_inflows = pd.read_csv("data/raw/05_category_inflows.csv")
industry_folio_count = pd.read_csv("data/raw/06_industry_folio_count.csv")
scheme_performance = pd.read_csv("data/raw/07_scheme_performance.csv")
investor_transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
portfolio_holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
benchmark_indices = pd.read_csv("data/raw/10_benchmark_indices.csv")

datasets = {
    "Fund Master": fund_master,
    "NAV History": nav_history,
    "AUM by Fund House": aum_by_fund_house,
    "Monthly SIP Inflows": monthly_sip_inflows,
    "Category Inflows": category_inflows,
    "Industry Folio Count": industry_folio_count,
    "Scheme Performance": scheme_performance,
    "Investor Transactions": investor_transactions,
    "Portfolio Holdings": portfolio_holdings,
    "Benchmark Indices": benchmark_indices
}

for name, df in datasets.items():

    print("\n" + "=" * 60)
    print(f"DATASET: {name}")
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

print("\n" + "=" * 60)
print("DATA INGESTION COMPLETED SUCCESSFULLY")
print("=" * 60)
