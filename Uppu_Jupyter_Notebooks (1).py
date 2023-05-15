#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = "darkgrid")


# In[11]:


df = pd.read_csv('/home/student/Desktop/classroom/myfiles/notebooks/fortune500.csv')


# In[12]:


df.head()


# In[13]:


df.tail()


# In[13]:


df.columns = ['year', 'rank', 'company', 'revenue', 'profit']


# In[14]:


df.head()


# In[15]:


len(df)


# In[16]:


df.dtypes


# In[17]:


non_numeric_profits = df.profit.str.contains('[^0-9.-]')
df.loc [non_numeric_profits].head()


# In[18]:


set(df.profit[non_numeric_profits])


# In[19]:


len(df.profit[non_numeric_profits])


# In[22]:


bin_sizes, _, _ = plt.hist(df.year[non_numeric_profits], bins= range(1955,2006))


# In[23]:


df = df.loc[~non_numeric_profits]
df.profit = df.profit.apply(pd.to_numeric)


# In[24]:


len(df)


# In[25]:


df.dtypes


# In[27]:


group_by_year = df.loc[:, ['year', 'revenue', 'profit']].groupby ('year')
avgs = group_by_year.mean()
x = avgs.index
y1= avgs.profit
def plot(x, y, ax, title, y_label):
    ax.set_title (title)
    ax.set_ylabel(y_label)
    ax.plot(x, y)
    ax.margins (x=0, y=0)


# In[29]:


fig, ax = plt.subplots()
plot (x, y1, ax,'Increase in mean Fortune 500 company profits from 1955 to 2005','profit (millions)')


# In[30]:


y2 = avgs.revenue
fig, ax = plt.subplots()
plot (x,y2,ax,'Increase in mean Fortune 500 company profits from 1955 to 2005', 'Revenue (millions)')


# In[1]:





# In[3]:


def plot_with_std(x, y, stds, ax, title, y_label):
    ax.fill_between(x, y - stds, y + stds, alpha = 0.2)
    plot (x, y, ax, title, y_label)
fig, (ax1, ax2) = plt.subplots(ncols= 2)
title = 'Increase in mean and std fortune 500 company %s from 1955 to 2005'
stds1 = group_by_year.std().profit.values
stds2 = group_by_year.std().revenue.values
plot_with_std (x, y1.values, stds1, ax1, title % 'profits', 'Profit (millions)') 
plot_with_std (x, y2.values, stds2, ax2, title % 'revenues', 'Revenue (millions)')
fig.set_size_inches(14,4)
fig.tight_layout()


# In[ ]:




