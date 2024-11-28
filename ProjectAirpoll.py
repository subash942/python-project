#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


import pandas as pd


# In[5]:


import plotly.express as px


# In[7]:


import matplotlib.pyplot 


# In[9]:


import seaborn as sns


# In[11]:


dataset = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\project\Air_Quality.csv")


# In[13]:


dataset.head()


# In[15]:


fig = px.scatter(dataset,x="city",y="pollutant_avg")
fig.show()


# In[17]:


dataset.info()


# In[19]:


dataset.isnull().sum()


# In[21]:


dataset.columns


# In[23]:


fig = px.scatter(dataset,x="city",y="pollutant_id")
fig.show()


# In[27]:


fig = px.scatter(dataset,x="pollutant_id",y="pollutant_max")
fig.show()


# In[29]:


dataset1 = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\project\AIR.csv")


# In[31]:


dataset1.info()


# In[33]:


dataset1.columns


# In[37]:


import matplotlib.pyplot as plt
top_cities = dataset1.nsmallest(10, '2021')

plt.figure(figsize=(12, 8))
plt.bar(top_cities['City'], top_cities['2021'], color='skyblue')
plt.title('Top 10 City Rankings in 2021', fontsize=16)
plt.xlabel('City', fontsize=12)
plt.ylabel('Rank', fontsize=12)
plt.xticks(rotation=45, fontsize=10)  
plt.tight_layout()
plt.show()


# In[39]:


dataset2 = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\project\world.csv")


# In[41]:


dataset2.info()


# In[43]:


dataset2.head()


# In[57]:


countries_of_interest = [
    'United States', 'Russia', 'China', 'India', 'Egypt',
    'Japan', 'Brazil', 'South Korea', 'Greece', 'Mexico'
]
filtered_data = dataset2[dataset2['Country'].isin(countries_of_interest)]

plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='AQI Value', data=filtered_data, palette='coolwarm')
plt.title('Air Quality Index (AQI) for Selected Countries with Different Alphabets', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('AQI Value', fontsize=12)

plt.xticks(rotation=45)
plt.show()


# In[55]:


countries_of_interest = ['India', 'Pakistan', 'Sri Lanka', 'United States', 'Russia', 'China']
filtered_data = dataset2[dataset2['Country'].isin(countries_of_interest)]
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='AQI Value', data=filtered_data, palette='coolwarm')
plt.title('Air Quality Index (AQI) for Selected Countries', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('AQI Value', fontsize=12)
plt.xticks(rotation=45)  
plt.show()


# In[ ]:




