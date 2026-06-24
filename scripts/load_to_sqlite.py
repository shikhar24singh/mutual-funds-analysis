import pandas as pd
from sqlalchemy import create_engine

fund_master = pd.read_csv("data/processed/01_fund_master_clean.csv")
nav_history = pd.read_csv("data/processed/02_nav_history_clean.csv")
aum_by_fund_house = pd.read_csv("data/processed/03_aum_by_fund_house_clean.csv")
monthly_sip_inflows = pd.read_csv("data/processed/04_monthly_sip_inflows_clean.csv")
category_inflows = pd.read_csv("data/processed/05_category_inflows_clean.csv")
industry_folio_count = pd.read_csv("data/processed/06_industry_folio_count_clean.csv")
scheme_performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
investor_transactions = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
portfolio_holdings = pd.read_csv("data/processed/09_portfolio_holdings_clean.csv")
benchmark_indices = pd.read_csv("data/processed/10_benchmark_indices_clean.csv")

engine = create_engine("sqlite:///database/bluestock_mf.db")

fund_master.to_sql(
    "fund_master",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

aum_by_fund_house.to_sql(
    "aum_by_fund_house",
    engine,
    if_exists="replace",
    index=False
)

monthly_sip_inflows.to_sql(
    "monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

category_inflows.to_sql(
    "category_inflows",
    engine,
    if_exists="replace",
    index=False
)

industry_folio_count.to_sql(
    "industry_folio_count",
    engine,
    if_exists="replace",
    index=False
)

scheme_performance.to_sql(
    "scheme_performance",
    engine,
    if_exists="replace",
    index=False
)

investor_transactions.to_sql(
    "investor_transactions",
    engine,
    if_exists="replace",
    index=False
)

portfolio_holdings.to_sql(
    "portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)

benchmark_indices.to_sql(
    "benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)

print("All datasets loaded into SQLite successfully.")