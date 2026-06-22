from pathlib import Path
import requests
import pandas as pd

project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "data" / "raw"

scheme_codes = [119551, 120503, 118632, 119092, 120841]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(output_dir / f"{code}_nav.csv", index=False)