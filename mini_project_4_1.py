#!/usr/bin/env python
# coding: utf-8

# In[94]:


import pandas as pd
import os

os.getcwd()


# In[95]:


prod_activations_logs = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/5_subsid/subsid/prod_activations_logs.csv', sep=';')
tm_sales_1 = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/5_subsid/subsid/tm_sales_1.csv', sep=';')
tm_sales_2 = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/5_subsid/subsid/tm_sales_2.csv', sep=';')
tm_sales_3 = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/5_subsid/subsid/tm_sales_3.csv', sep=';')


# In[67]:


prod_activations_logs['END_DTTM'] = pd.to_datetime(prod_activations_logs['END_DTTM'])
prod_activations_logs['START_DTTM'] = pd.to_datetime(prod_activations_logs['START_DTTM'])
prod_activations_logs.head(10)


# In[47]:


tm_sales_1.head()


# In[48]:


tm_sales_2.head()


# In[49]:


tm_sales_3.head()


# In[50]:


# Соеденим tm_sales_1, tm_sales_2, tm_sales_3 в один датафрейм и уберен пустые значения.


# In[96]:


tm_sales = pd.concat([tm_sales_1, tm_sales_2, tm_sales_3]).dropna().reset_index()


# In[97]:


tm_sales = tm_sales.drop(columns=['index'])


# In[98]:


tm_sales['ACT_DTTM'] = pd.to_datetime(tm_sales['ACT_DTTM'])
tm_sales


# In[99]:


def id_concat(data):
    if not data.startswith('id'):
        id_sub = 'id' + data
        return id_sub
    else:
        return data


# In[100]:


tm_sales['SUBS_ID'] = tm_sales.SUBS_ID.apply(id_concat)


# In[101]:


full_data = prod_activations_logs.merge(tm_sales, how='inner', on=['SUBS_ID', 'PROD_ID'])


# In[102]:


full_data['START_DTTM'] = pd.to_datetime(full_data['START_DTTM'], format='%d-%m-%Y %H:%M')


# In[103]:


full_data['END_DTTM'] = pd.to_datetime(full_data['END_DTTM'], format='%d-%m-%Y %H:%M')


# In[104]:


full_data


# In[107]:


full_data['delta'] = full_data.END_DTTM - full_data.START_DTTM


# In[115]:


full_data.query('delta > "5m"').sort_values('SUBS_ID', ascending=True)

