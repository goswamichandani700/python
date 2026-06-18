# Create a candlestick chart showing the movement of the BSE Sensex over the last 30 days. Read the data from a CSV file and display a candle for each trading day.

import mplfinance as mpl 
import pandas as pd 
#load data 
sensex = pd.read_csv('sensex.csv').squeeze()
sensex["Date"] = pd.to_datetime(sensex["Date"])
sensex.set_index('Date', inplace=True)
mpl.plot(sensex,type='candle',title='sensex',style='yahoo')