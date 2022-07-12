import requests
import pandas as pd
import json
import sys

#api key
api_key = ""

url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey="
url = url + api_key
html_data = requests.get(url)

if html_data.ok == False:
    sys.exit("Request was not successful. Check for connection or API credentials validity.")

html_data = html_data.text

# creates dataframe
currencies_df = pd.DataFrame(columns = ["Rate"])

# loads json object to dict
jsonobj = json.loads(html_data)

# loops through dictionary of interest
for key, value in jsonobj['rates'].items():
    # appends to dataframe
    df_newrow = pd.DataFrame({"Currency": key, "Rate": value}, index=[0])
    currencies_df = pd.concat([currencies_df, df_newrow], ignore_index=True)

# manipulates types
currencies_df["Rate"] = currencies_df["Rate"].astype("float")
currencies_df.set_index("Currency", inplace=True)

# removes index name
currencies_df.rename_axis(index = None, inplace = True)

# saves csv
currencies_df.to_csv("./data/exchange_rates_1.csv")
