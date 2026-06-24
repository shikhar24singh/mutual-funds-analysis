# Data Dictionary

## 1. Fund Master (`01_fund_master.csv`)

| Column        | Data Type | Description                                |
| ------------- | --------- | ------------------------------------------ |
| amfi_code     | Integer   | Unique scheme identifier assigned by AMFI  |
| fund_house    | Text      | Asset Management Company (AMC)             |
| scheme_name   | Text      | Name of the mutual fund scheme             |
| category      | Text      | Primary fund category                      |
| sub_category  | Text      | Detailed scheme classification             |
| benchmark     | Text      | Benchmark index used for comparison        |
| expense_ratio | Float     | Annual expense charged by the fund         |
| exit_load     | Float     | Exit load percentage charged on redemption |

---

## 2. NAV History (`02_nav_history.csv`)

| Column    | Data Type | Description              |
| --------- | --------- | ------------------------ |
| amfi_code | Integer   | Scheme identifier        |
| date      | Date      | NAV reporting date       |
| nav       | Float     | Net Asset Value per unit |

---

## 3. AUM by Fund House (`03_aum_by_fund_house.csv`)

| Column       | Data Type | Description                       |
| ------------ | --------- | --------------------------------- |
| date         | Date      | Reporting month                   |
| fund_house   | Text      | Asset Management Company          |
| aum_crore    | Float     | Assets Under Management (₹ Crore) |
| market_share | Float     | Market share percentage           |
| scheme_count | Integer   | Number of active schemes          |

---

## 4. Monthly SIP Inflows (`04_monthly_sip_inflows.csv`)

| Column              | Data Type | Description                          |
| ------------------- | --------- | ------------------------------------ |
| month               | Date      | Reporting month                      |
| sip_inflow_crore    | Float     | SIP inflow amount (₹ Crore)          |
| active_sip_accounts | Integer   | Number of active SIP accounts        |
| new_sip_accounts    | Integer   | Newly registered SIP accounts        |
| sip_aum_crore       | Float     | SIP Assets Under Management          |
| yoy_growth_percent  | Float     | Year-over-Year SIP growth percentage |

---

## 5. Category Inflows (`05_category_inflows.csv`)

| Column           | Data Type | Description                  |
| ---------------- | --------- | ---------------------------- |
| month            | Date      | Reporting month              |
| category         | Text      | Fund category                |
| net_inflow_crore | Float     | Net inflow amount in ₹ Crore |

---

## 6. Industry Folio Count (`06_industry_folio_count.csv`)

| Column        | Data Type | Description           |
| ------------- | --------- | --------------------- |
| month         | Date      | Reporting month       |
| total_folios  | Integer   | Total industry folios |
| equity_folios | Integer   | Equity scheme folios  |
| debt_folios   | Integer   | Debt scheme folios    |
| hybrid_folios | Integer   | Hybrid scheme folios  |
| other_folios  | Integer   | Other category folios |

---

## 7. Scheme Performance (`07_scheme_performance.csv`)

| Column           | Data Type | Description                      |
| ---------------- | --------- | -------------------------------- |
| amfi_code        | Integer   | Scheme identifier                |
| scheme_name      | Text      | Mutual fund scheme name          |
| return_1y        | Float     | One-year return (%)              |
| return_3y        | Float     | Three-year CAGR return (%)       |
| return_5y        | Float     | Five-year CAGR return (%)        |
| benchmark_return | Float     | Benchmark return (%)             |
| alpha            | Float     | Excess return over benchmark     |
| beta             | Float     | Volatility relative to benchmark |
| sharpe_ratio     | Float     | Risk-adjusted return metric      |
| expense_ratio    | Float     | Fund expense ratio (%)           |

---

## 8. Investor Transactions (`08_investor_transactions.csv`)

| Column           | Data Type | Description                      |
| ---------------- | --------- | -------------------------------- |
| transaction_id   | Integer   | Unique transaction identifier    |
| investor_id      | Integer   | Investor identifier              |
| amfi_code        | Integer   | Scheme identifier                |
| transaction_date | Date      | Transaction date                 |
| transaction_type | Text      | SIP, Lumpsum, or Redemption      |
| amount           | Float     | Transaction amount               |
| state            | Text      | Investor state                   |
| city             | Text      | Investor city                    |
| kyc_status       | Text      | Investor KYC verification status |
| age_group        | Text      | Investor age category            |
| gender           | Text      | Investor gender                  |

---

## 9. Portfolio Holdings (`09_portfolio_holdings.csv`)

| Column          | Data Type | Description                     |
| --------------- | --------- | ------------------------------- |
| amfi_code       | Integer   | Scheme identifier               |
| stock_symbol    | Text      | Stock ticker symbol             |
| company_name    | Text      | Company name                    |
| sector          | Text      | Industry sector                 |
| holding_percent | Float     | Portfolio allocation percentage |
| market_value    | Float     | Current market value of holding |

---

## 10. Benchmark Indices (`10_benchmark_indices.csv`)

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Index reporting date |
| index_name  | Text      | Benchmark index name |
| close_value | Float     | Closing index value  |

---

# Source Reference

| Dataset               | Source                       |
| --------------------- | ---------------------------- |
| Fund Master           | AMFI Mutual Fund Database    |
| NAV History           | MFAPI / AMFI NAV Records     |
| AUM by Fund House     | AMFI Industry Reports        |
| Monthly SIP Inflows   | AMFI Monthly SIP Reports     |
| Category Inflows      | AMFI Category Reports        |
| Industry Folio Count  | AMFI Industry Statistics     |
| Scheme Performance    | Fund Performance Dataset     |
| Investor Transactions | Simulated Investor Dataset   |
| Portfolio Holdings    | Portfolio Disclosure Reports |
| Benchmark Indices     | NSE/BSE Benchmark Data       |
