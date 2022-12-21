#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
os.getcwd()


# In[50]:


df_1 = pd.DataFrame()

a = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/4/data/')


# In[51]:


for i in a:
    path_to_folder = '/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/4/data/' + i
    date = path_to_folder.split('/')[-1]
    b = os.listdir(path_to_folder)
    
    for j in b:
        path_to_name = path_to_folder + '/' + j
        name = path_to_name.split('/')[-1]
        c = os.listdir(path_to_name)
        
        for k in c:
            path_to_file = path_to_name + '/' + k
            file = pd.read_csv(path_to_file)
            file['name'] = name
            file['date'] = date
            df_1 = df_1.append(file)


# In[52]:


df_1 = df_1.drop(columns=['Unnamed: 0'])


# In[53]:


df_1 = df_1.reset_index(drop=True)
df_1


# In[54]:


df_1['quantity'].sum()


# In[55]:


df_1.groupby('name', as_index=False).agg({'quantity':'sum'}).sort_values('quantity', ascending=False)


# In[56]:


df_prod = df_1.groupby('product_id', as_index=False).agg({'quantity':'sum'}).sort_values('quantity', ascending=False)
df_prod.head(10)


# In[57]:


plt.subplots(figsize=(10, 10))
sns.barplot(data=df_prod.head(10), x='product_id', y='quantity')
plt.xticks(fontsize = 12, rotation = 70)


# In[58]:


df_1.head()


# In[59]:


df_day = df_1.groupby('date', as_index=False).agg({'quantity':'sum'}).sort_values('quantity', ascending=False)
df_day.head(10)


# In[60]:


plt.subplots(figsize=(10, 10))
sns.color_palette("flare", as_cmap=True)
sns.barplot(data=df_day, x='date', y='quantity', palette="rocket")
plt.xticks(fontsize = 12, rotation = 70)


# In[62]:


df_1.drop_duplicates(subset=['name', 'product_id', 'date'])     .groupby(['name','product_id'], as_index=False).agg({'date' : 'nunique'}).query('date> 1')


# In[63]:


df_exel = pd.read_excel('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/4_inn.xls')


# In[64]:


df_txt = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/4_necessary_inn.txt', header = None)


# In[72]:


df_exel['head_inn']


# In[87]:


df_exel.info()


# In[84]:


alfa = df_txt[0].tolist()


# In[88]:


new_df_exel = df_exel.query('head_inn in @alfa')


# In[90]:


new_df_exel['income,RUB'].sum()


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




