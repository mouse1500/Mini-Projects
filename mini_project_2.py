#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import os
os.getcwd()


# In[2]:


user_data_df = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/3_user_data.csv')
logs_df = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/3_logs.csv')


# In[3]:


user_data_df.info()


# In[4]:


user_data_df.describe()


# In[5]:


user_data_df.head()


# In[6]:


logs_df.info()


# In[7]:


logs_df.describe()


# In[8]:


logs_df.head()


# In[9]:


logs_df['platform'].nunique()


# In[10]:


successful_operations = logs_df.query('success == True')


# In[11]:


b = successful_operations.groupby('client', as_index=False)     .agg({'success' : 'count'})     .sort_values('success', ascending=False)


# In[12]:


b.head(11)


# In[13]:


s = b['client'].to_list()[:9]


# In[14]:


s.sort()
print(s)


# In[15]:


logs_df['platform'].value_counts()


# In[16]:


logs_user = logs_df.merge(user_data_df, how='inner', on='client')


# In[17]:


logs_user.head()


# In[18]:


logs_user.query('premium == True')     .agg({'platform' : 'value_counts'})


# In[19]:


prem_df = logs_user.query('premium == True')
prem_df


# In[20]:


norm_df = logs_user.query('premium == False')
norm_df


# In[21]:


sns.distplot(norm_df.age)
sns.distplot(prem_df.age)


# In[22]:


logs_user.head()


# In[23]:


logs_user['success'].value_counts()


# In[24]:


cms = logs_user.query('success == True').groupby('client', as_index=False).agg({'success' : 'count'})


# In[25]:


cms['success'].value_counts()


# In[26]:


sns.distplot(cms.success)


# In[27]:


plt.subplots(figsize=(10, 10))
sns.countplot(data=logs_user.query('platform = computer' and 'success == True'), x='age')
plt.xticks(fontsize = 10, rotation = 90)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




