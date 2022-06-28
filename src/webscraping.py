from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
html_data = requests.get(url).text

# create BeautifulSoup obj
soup = BeautifulSoup(html_data, 'html.parser')

# creates dataframe
marketCapitalization_df = pd.DataFrame(columns=["Bank Name", "Market Cap (US$ Billion)"])

# slices for table body of interest (3)
table = soup.find_all("tbody")[3]

# slices for tag tr
marketCapitalization_table = table.find_all("tr")

# loops through marketCapitalization_table
for row in marketCapitalization_table:
    col = row.find_all("td")
    if(col != []):
        # gets name
        bank_name = str(col[1].text).replace("\n", "")
        # gets market cap
        bank_mcap = str(col[2].text).replace("\n", "")
        # appends to dataframe
        df_newrow = pd.DataFrame({"Bank Name": bank_name, "Market Cap (US$ Billion)": bank_mcap}, index=[0])
        marketCapitalization_df = pd.concat([marketCapitalization_df, df_newrow], ignore_index=True)

# cleans data
marketCapitalization_df["Market Cap (US$ Billion)"] = marketCapitalization_df["Market Cap (US$ Billion)"].apply(lambda x: x.split("[")[0])

# manipulates types 
marketCapitalization_df["Market Cap (US$ Billion)"] = marketCapitalization_df["Market Cap (US$ Billion)"].astype("float")
marketCapitalization_df["Bank Name"] = marketCapitalization_df["Bank Name"].astype("string")

marketCapitalization_df.to_json('./data/bank_market_cap.json')
