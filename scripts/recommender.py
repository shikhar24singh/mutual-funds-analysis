from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

scheme = pd.read_csv(
    BASE_DIR / "data" / "processed" / "07_scheme_performance_clean.csv"
)

sharpe = pd.read_csv(
    BASE_DIR / "reports" / "sharpe_ratio_report.csv"
)



if "sharpe_ratio" not in sharpe.columns:

    # Find the numeric column other than amfi_code
    cols = [c for c in sharpe.columns if c != "amfi_code"]

    if len(cols) == 1:
        sharpe = sharpe.rename(columns={cols[0]: "sharpe_ratio"})
    else:
        raise Exception(
            f"Could not find 'sharpe_ratio' column.\nColumns found: {list(sharpe.columns)}"
        )


print("Scheme Columns:")
print(scheme.columns.tolist())

print("\nSharpe Columns:")
print(sharpe.columns.tolist())

funds = scheme.merge(
    sharpe,
    on="amfi_code",
    how="left"
)

print("\nMerged Columns:")
print(funds.columns.tolist())


def recommend_funds(risk_level):

    risk_level = risk_level.strip().lower()

    risk_column = "risk_grade"

    if risk_column not in funds.columns:
        risk_column = "risk_category"

    if risk_level == "low":
        risk = ["Low"]

    elif risk_level == "moderate":
        risk = ["Moderate"]

    elif risk_level == "high":
        risk = ["High", "Very High"]

    else:
        print("\nInvalid Risk Level.")
        return None

    result = (
        funds[
            funds[risk_column].isin(risk)
        ]
        .sort_values(
            by=["sharpe_ratio", "return_3yr_pct"],
            ascending=False
        )
        .head(3)
    )

    return result[
        [
            "scheme_name",
            "fund_house",
            "category",
            risk_column,
            "return_3yr_pct",
            "expense_ratio_pct",
            "sharpe_ratio"
        ]
    ]



if __name__ == "__main__":

    print("=" * 60)
    print("Mutual Fund Recommendation System")
    print("=" * 60)

    while True:

        risk = input(
            "\nEnter Risk Appetite (Low / Moderate / High): "
        )

        recommendation = recommend_funds(risk)

        if recommendation is not None:

            print("\nTop 3 Recommended Funds\n")

            print(
                recommendation.to_string(index=False)
            )

        again = input("\nTry Again? (y/n): ")

        if again.lower() != "y":
            break

    print("\nThank you!")