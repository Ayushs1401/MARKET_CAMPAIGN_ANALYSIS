#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[4]:


df=pd.read_csv("WA_Marketing-Campaign.csv")
df.head()


# In[5]:


df.head()


# In[6]:


df['LocationID'].unique()


# In[7]:


df.drop(columns='LocationID',inplace=True,axis='column')


# In[8]:


df.head()


# In[9]:


df.rename(columns = {'week':'Week'}, inplace = True)


# In[10]:


df.head()


# In[11]:


df.isnull().sum()


# In[12]:


df['MarketID'].value_counts()


# In[13]:


df['MarketSize'].value_counts()


# # CORRELATION ANALYSIS
# 

# In[14]:


df.corr()


# In[15]:


sns.heatmap(df.corr(),annot=True)


# So it is evident from the heatmap above that 
# sales is negatively correlated with age  of store and promotion
# Meaning that sales is inversely proportional to ageof store and Promotion technique

# In[16]:


df['Promotion'].value_counts()


# In[17]:


sns.barplot(x='MarketSize',y='SalesInThousands',data=df)
plt.ylabel("Total sales in Thousands")


# so it is quite interesting to see that the small markets are making more revenue in comparison of medium markets

# In[18]:


sns.barplot(x='AgeOfStore',y='SalesInThousands',data=df)
plt.ylabel("Total sales in Thousands")


# In[19]:


sns.barplot(x='Week',y='SalesInThousands',data=df)
plt.ylabel("Total sales in Thousands")


# In[20]:


sns.countplot(x='Promotion',hue='Week',data=df)


# In[21]:


sns.pairplot(data=df)


# In[22]:


sns.countplot(x='AgeOfStore',hue='MarketSize',data=df)

plt.ylabel("Count of markets by size")
plt.legend(loc='upper right')


# the graph indicate that the as the age of the store increases medium markets are able to produce more sustainable buisness

# In[23]:


sns.countplot(x='Promotion',hue='MarketSize',data=df)
plt.legend(fontsize=8,loc='upper right')


# # A/B Testing

# In[27]:


sns.barplot(x='Promotion',y='SalesInThousands',hue='MarketSize',data=df)
plt.ylabel("Total sales in Thousands")
plt.legend(fontsize=8,loc="upper left")


# Inspite of having highest promotion strategy in medium markets they are not producing that amount of profthe markit in comparison of small markets and large markets.In fact,small markets tend to perform better than medium under less promotion in each technique.
# It is better to perform more promotion in small markets rather than in medium markets for more profits.
# 
# 
# Small markets have best sales to promotion count ratio,followed by large market and then finally medium markets

# In[28]:


groupA = df[df['Promotion'] == 1]['SalesInThousands']
groupB = df[df['Promotion'] == 2]['SalesInThousands']
groupC = df[df['Promotion'] == 3]['SalesInThousands']


# In[29]:


from scipy import stats
ttest1 = stats.ttest_ind(groupA,groupB, equal_var = True)
ttest1


# In[30]:


tttest2 = stats.ttest_ind(groupA,groupC, equal_var = True)
ttest2


# In[34]:


ttest3 = stats.ttest_ind(groupB,groupC, equal_var = True)
ttest3


# # CONCLUSION

# Based on the hypothesis testing results, there is a significant difference between promotions 1 and 2, indicating different approaches to the target market and resulting sales. Meanwhile, promotions 1 and 3 did not show a significant difference, suggesting that either promotion 1 or 3 could be maintained, alongside promotion 2, to achieve maximum sales with different target markets.
# 
# This statement summarizes the findings from A/B testing, highlighting the significant performance disparity between promotions 1 and 2, while promotions 1 and 3 perform similarly. Therefore, maintaining either promotion 1 or 3, alongside promotion 2, is recommended to cater to varying target markets effectively.
