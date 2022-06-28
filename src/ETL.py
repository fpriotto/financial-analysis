import glob
import pandas as pd
from datetime import datetime

def extract_from_json(file_to_process):

    """
    Extracts data from json-type files. Returns a dataframe

    param p1: file to be converted
    """

    dataframe = pd.read_json(file_to_process)
    return dataframe

def extract():

    """
    Extracts data from specific file types. Returns the extracted data.
    """

    columns=["Bank Name", "Market Cap (US$ Billion)"]
    extracted_data = pd.DataFrame(columns = columns)
    
    for jsonfile in glob.glob('./data/*.json'):
        if jsonfile[7:] == 'bank_market_cap.json':
            extracted_data = pd.concat([extracted_data, extract_from_json(jsonfile)], ignore_index=True)
    # more file types could be added here
    
    return extracted_data

def get_exchange_rate(currency):

    """
    Gets the exchange rate given the desired currency based in USD. Returns the exchange rate.

    param p1: currency for convertion
    """

    exchange_df = pd.read_csv('./data/exchange_rates_1.csv', index_col=0)
    base_rate = exchange_df.loc[['USD'],:].Rate[0]

    # changes base
    exchange_df["Rate"] = exchange_df["Rate"].apply(lambda x: x/base_rate)

    # gets exchange rate
    exchange_rate = exchange_df.loc[[currency],:].Rate[0]
    return exchange_rate

def transform(df, exchange_rate, currency):

    """
    Transforms dataframe given project parameters. Returns the transformed dataframe.

    param p1: dataframe to transform
    param p2: exchange rate of convertion
    param p3: currency for convertion
    """

    # converts dataframe
    df['Market Cap (US$ Billion)'] = df['Market Cap (US$ Billion)'].apply(lambda x: x*exchange_rate)
    df['Market Cap (US$ Billion)'] = round(df['Market Cap (US$ Billion)'], 3)

    text = 'Market Cap (' + currency + '$ Billion)'

    # changes the name of the column
    df.rename(columns={'Market Cap (US$ Billion)':text}, inplace=True)
    return df

def load(df, filename):

    """
    Loads the dataframe in csv format given the name of the file. The file is stored in "data" folder.

    param p1: dataframe to be saved.
    param p2: file name to be saved as.
    """

    if(filename[-4:] != '.csv'):
        filename = filename + '.csv'

    df.to_csv(('./data/' + filename), index=False)

def log(msg, logfile):

    """
    logs message into financial_logfile.txt stored in "data" folder.

    param p1: message to log.
    param p2: file name to be saved as.
    """

    # gets timestamp of current moment
    timestamp_format = '%H:%M:%S-%h-%d-%Y'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    
    # logs msg into logfile
    if(logfile[-4:] != '.txt'):
        logfile = logfile + '.txt'
    with open("./data/" + logfile, "a") as file:
        file.write(timestamp + ': ' + msg + '\n')