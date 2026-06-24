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


nav_history["date"] = pd.to_datetime(nav_history["date"])

nav_history = nav_history.sort_values(
    ["amfi_code", "date"]
)

nav_history["nav"] = (
    nav_history
    .groupby("amfi_code")["nav"]
    .ffill()
)

nav_history = nav_history.drop_duplicates()

nav_history = nav_history[
    nav_history["nav"] > 0
]



investor_transactions["transaction_type"] = (
    investor_transactions["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

investor_transactions = (
    investor_transactions[
        investor_transactions["transaction_type"]
        .isin(valid_types)
    ]
)

investor_transactions = (
    investor_transactions[
        investor_transactions["amount_inr"] > 0
    ]
)

investor_transactions["transaction_date"] = (
    pd.to_datetime(
        investor_transactions["transaction_date"]
    )
)


return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    scheme_performance[col] = (
        pd.to_numeric(
            scheme_performance[col],
            errors="coerce"
        )
    )

scheme_performance = (
    scheme_performance.dropna(
        subset=return_cols
    )
)

scheme_performance = (
    scheme_performance[
        scheme_performance["expense_ratio_pct"]
        .between(0.1, 2.5)
    ]
)


from pathlib import Path

Path("data/processed").mkdir(parents=True, exist_ok=True)

fund_master.to_csv(
    "data/processed/01_fund_master_clean.csv",
    index=False
)

nav_history.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

aum_by_fund_house.to_csv(
    "data/processed/03_aum_by_fund_house_clean.csv",
    index=False
)

monthly_sip_inflows.to_csv(
    "data/processed/04_monthly_sip_inflows_clean.csv",
    index=False
)

category_inflows.to_csv(
    "data/processed/05_category_inflows_clean.csv",
    index=False
)

industry_folio_count.to_csv(
    "data/processed/06_industry_folio_count_clean.csv",
    index=False
)

scheme_performance.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

investor_transactions.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

portfolio_holdings.to_csv(
    "data/processed/09_portfolio_holdings_clean.csv",
    index=False
)

benchmark_indices.to_csv(
    "data/processed/10_benchmark_indices_clean.csv",
    index=False
)

print("All cleaned datasets saved successfully.")