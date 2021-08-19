
# import required packages
import json
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import statsmodels.api as sm




##### - Print price chart for specified asset in linear, or log - #####
def priceChart(symbol, linOrLog):

    # insert API key and asset symbol here
    API_KEY = ''

    # make API requests and print status codes
    res = requests.get('https://api.glassnode.com/v1/metrics/market/price_usd_close', params={'a': symbol, 'api_key': API_KEY})
    print(res.status_code)

    # convert json to a pandas dataframe
    df = pd.read_json(res.text, convert_dates=['t'])
    df.rename(columns={'t':'date'}, inplace=True)
    df.rename(columns={'v':'price'}, inplace=True)
    df['log10_price'] = np.log10(df['price'])
    #print(df)

    # print either linear or log chart based on user input
    if linOrLog == 'linear':
        x = df.date
        y = df.price
        plt.plot(x, y)
        plt.ylabel('Price')
        plt.title(symbol)
        plt.savefig(symbol + '_priceChart_linear.png')
        plt.show()
    elif linOrLog == 'log':
        x = df.date
        y = df.log10_price
        plt.plot(x, y)
        plt.ylabel('Price (log10)')
        plt.title(symbol)
        plt.savefig(symbol + '_priceChart_log10.png')
        plt.show()
    else:
        print('2nd argument in chart() function must be either "linear", or "log"')




##### - Export Glassnode Data to CSV file for processing in gretl - #####
def toGretl(symbol):

    # insert API key and asset symbol here
    API_KEY = ''

    # make API requests and print status codes
    res = requests.get('https://api.glassnode.com/v1/metrics/market/price_usd_close', params={'a': symbol, 'api_key': API_KEY})
    #print(res.status_code)

    # convert json to a pandas dataframe
    df = pd.read_json(res.text, convert_dates=['t'])
    df.rename(columns={'t':'date'}, inplace=True)
    df.rename(columns={'v':'price'}, inplace=True)
    df['log10_price'] = np.log10(df['price'])
    #print(df)

    # Export to CSV for gretl
    df.to_csv(symbol + ".csv")
    print("done")



priceChart("BTC", "log")