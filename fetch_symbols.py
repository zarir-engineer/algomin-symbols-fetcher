import requests
import pandas as pd
import json
from io import StringIO


def main():
    url = "https://api.kite.trade/instruments"
    response = requests.get(url)

    if response.status_code == 200:
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)

        # Filter NSE segment
        nse_stocks = df[(df['exchange'] == 'NSE') & (df['segment'] == 'NSE')]

        # Select and rename columns, convert token to string
        nse_symbols = nse_stocks[['tradingsymbol', 'instrument_token']].copy()
        nse_symbols.columns = ['symbol', 'token']
        nse_symbols['token'] = nse_symbols['token'].astype(str)

        # Convert to list of dicts
        symbols_list = nse_symbols.to_dict(orient='records')

        # Write to JSON file in public/
        with open("public/symbols.json", "w") as f:
            json.dump(symbols_list, f, indent=2)

        print("✅ symbols.json created successfully.")
    else:
        print("❌ Failed to download instrument list. Status code:", response.status_code)


main()
