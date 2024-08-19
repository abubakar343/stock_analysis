#!/usr/bin/env python
# coding: utf-8

#importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data as wb

#insert the ticker, set the duration and fetch prices
stock_tickers = ["F","TSLA"]
stock_prices = wb.get_data_yahoo(stock_tickers,start = "2021-05-01",end = "2022-05-07")
print(stock_prices.head())

#visualize stock returns
stock_monthly_returns = stock_prices['Adj Close'].resample('M').ffill().fillna().pct_change()
fig = plt.figure()
(stock_monthly_returns + 1).cumprod().plot()
plt.show()

#monthly returns
stock_monthly_returns = stock_prices['Adj Close'].resample('M').ffill().fillna(0).pct_change()
print(stock_monthly_returns)

#mean, standard deviation and variance of monthly returns
print(stock_monthly_returns.mean())
print(stock_monthly_returns.std())
print(stock_monthly_returns.var())

#correlation and co-variance
print(stock_monthly_returns.corr())
print(stock_monthly_returns.cov())

#end of code
