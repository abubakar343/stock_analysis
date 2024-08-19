#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data as wb

stock_tickers = ["F","TSLA"]
stock_prices = wb.get_data_yahoo(stock_tickers,start = "2021-05-01",end = "2022-05-07")
print(stock_prices.head())


# In[37]:


stock_monthly_returns = stock_prices['Adj Close'].resample('M').ffill().fillna().pct_change()
fig = plt.figure()
(stock_monthly_returns + 1).cumprod().plot()
plt.show()


# In[45]:


stock_monthly_returns = stock_prices['Adj Close'].resample('M').ffill().fillna(0).pct_change()
print(stock_monthly_returns)


# In[38]:


print(stock_monthly_returns.mean())


# In[39]:


print(stock_monthly_returns.std())


# In[40]:


print(stock_monthly_returns.var())


# In[46]:


print(stock_monthly_returns.corr())


# In[48]:


print(stock_monthly_returns.cov())


# In[ ]:




