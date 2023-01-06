#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import seaborn as sns
import plotly.express as px
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
os.getcwd()


# In[2]:


ads_clients_data = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/6/ads_clients_data.csv', parse_dates=['create_date'])
ads_data = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/6/ads_data.csv', parse_dates=['date', 'time'])


# In[3]:


ads_clients_data.head()


# In[4]:


ads_data.head()


# In[5]:


# Посчитаем среднее количество разных рекламных событий (показы и клики) по объявлениям.


# In[6]:


value_event = ads_data.groupby(['event', 'ad_id'], as_index=False).agg({'platform' : 'count'})                 .pivot(index='ad_id', columns='event', values='platform').fillna(0)                 .mean()                 .round(0)
value_event


# In[7]:


#Давайте посмотрим на распределение показов объявлений
#По оси x – число показов
#По оси y – доля объявлений с такими показами
#Прологарифмируйте число показов, а затем постройте график, чтобы можно было понять форму распределения


# In[8]:


# Задаем параметр графика
sns.set(
    font_scale=2,
    style="whitegrid",
    rc={'figure.figsize':(20,7)}
        )


# In[9]:


# Отбираем нужный нам параметр, по колнке просмотры, убираем нули и логарифмируем его.
view_log = ads_data.groupby(['event', 'ad_id'], as_index=False).agg({'platform' : 'count'})                 .pivot(index='ad_id', columns='event', values='platform').query('view > 0')

view_log['view'] = np.log(view_log.view)


# In[10]:


# Строим график, что бы понять как происходит распределение
sns.distplot(view_log['view'])


# In[11]:


#Hужно найти среднее количество показов на 1 объявление (ad_id) по дням, 
#не учитывая объявления, у которых не было показов (обычное среднее). 
#После этого посчитайте скользящее среднее по полученному результату с окном в 2 элемента.
#Какое значение скользящего среднего получим за 6 апреля 2019 года? 
#Округлите ответ до целого числа.


# In[12]:


ads_data.head()


# In[13]:


# среднее количество показов
value = ads_data.query('event == "view"')         .pivot_table(index='ad_id', columns='date', values='platform', aggfunc='count')
value.head()


# In[14]:


mean_value = value.mean().round(0)
mean_value


# In[15]:


mean_roll = value.mean().rolling(window=2).mean().round(0)
mean_roll


# In[16]:


#В какой день наблюдается наибольшая разница по модулю между арифметическим средним и скользящим средним? 
#Дни, в которых скользящее среднее равно NaN, не учитываем.


# In[17]:


fig, ax = plt.subplots()
sns.lineplot(data=mean_value, ax=ax, label='mean')
sns.lineplot(data=mean_roll, ax=ax, label='rolling')
ax.tick_params(axis='x', rotation=45)
plt.legend()


# In[18]:


#Объедините данные рекламы с данными о рекламных клиентах. 
#Hайдите среднее количество дней от даты создания рекламного клиента (create_date) 
#и первым запуском рекламного объявления этим клиентом (date).
#В качестве ответа укажите среднее число дней.


# In[19]:


#Объедините данные
client_data = ads_clients_data.merge(ads_data, on=['client_union_id'], suffixes=('_clients_data', '_ads_data'))
client_data.head()


# In[20]:


#Hайдите среднее количество дней от даты создания рекламного клиента (create_date) 
#и первым запуском рекламного объявления этим клиентом (date).
client_data['dif'] = client_data.date_ads_data - client_data.create_date
client_data.head()


# In[42]:


#В качестве ответа укажите среднее число дней.
first_ad = client_data.groupby('client_union_id').dif.min()
first_ad.mean().days
first_ad


# In[22]:


# Bычислим конверсию из создания рекламного кабинета в запуск первой рекламы в течение не более 365 дней.


# In[43]:


d_day = pd.Timedelta(365, unit='day')
it_365 = first_ad.loc[first_ad < d_day]
np.round(len(it_365) / ads_clients_data.client_union_id.nunique() * 100, 2)


# In[24]:


#Разобъем наших клиентов по промежуткам от создания рекламного кабинета до запуска первого рекламного объявления.
#Определите, сколько уникальных клиентов запустили свое первое объявление в первый месяц своего существования (от 0 до 30 дней)


# In[25]:


client_data.head()


# In[37]:


bins = [0, 30, 90, 180, 365]

bins = [pd.Timedelta(x, 'd') for x in bins]

labels = ['0-30', '30-90', '90-180', '180-365']
bins


# In[ ]:





# In[47]:


day_delay = pd.cut(first_ad, bins, labels=labels)
day_delay = day_delay.value_counts()
day_delay


# In[ ]:


#постройте интерактивный барплот, на котором будут показаны категории с количеством уникальных клиентов в них 


# In[48]:


px.bar(day_delay)


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




