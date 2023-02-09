#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import requests
import os
import matplotlib.pyplot as plt
import seaborn as sns
import gspread
get_ipython().run_line_magic('matplotlib', 'inline')
os.getcwd()


# In[2]:


df = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/step_1_lesson_7.csv')


# In[3]:


df


# In[4]:


# 1.Для начала, давайте посмотрим на распределение посещений сайта по дням. 
# Постройте график с распределением количества посещений от ботов и обычных пользователей сайта Яндекс.Метрика.


# In[5]:


df.value_counts()


# In[6]:


f, ax = plt.subplots(figsize=(10, 10))
sns.barplot(x='visits', y='date', data=df, hue='user_type')


# In[7]:


# 2.Определите процент посещений сайта Яндекс.Метрики с бразузера Google Chrome
df_step_2 = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/step_2_lesson_7.csv')


# In[8]:


df_step_2.info()


# In[14]:


df_step_2


# In[22]:


count = (df_step_2.visits / df_step_2.visits.sum()) * 100
count.round()


# In[ ]:


# 3.Давайте выясним, с какого браузера приходит больше всего ботов. Посмотрите на данные и определите, 
# у какого браузера самая большая доля посещений сайта ботами от общего числа посещений в этом браузере?

# у браузера UCWEB


# In[44]:


df_step_3 = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/step_3_lesson_7.csv')


# In[145]:


de_sum = df_step_3.groupby('browser', as_index=False).agg({'visits' : 'sum'})
de_sum = de_sum.rename(columns={'visits' : 'sum_vis'})


# In[159]:


df_step_3 = df_step_3.merge(de_sum, on='browser', how='inner')
df_step_3.head()


# In[151]:


df_robots = df_step_3.query('user_type == "Robots"')


# In[157]:


df_robots['precen'] = (df_robots.visits / df_robots.sum_vis) * 100


# In[158]:


df_robots


# In[2]:


# 4.Выгрузите данные, содержащие информацию о дне, типе пользователя, браузере. 
# Создайте колонку с метрикой доли заходов на сайт для каждого из этих разрезов.

# В ответе укажите процент открытий сайта настоящими пользователями Safari 
# (не ботами) с точностью до 1 знака после точки.


# In[7]:


df_step_3.head(3)


# In[8]:


df_step_3['sum_count'] = df_step_3.visits.sum()


# In[10]:


df_step_3.head(2)


# In[17]:


safari_pip = df_step_3.query('user_type == "People" & browser == "Safari"')
safari_pip


# In[16]:


((safari_pip.visits / safari_pip.sum_count) * 100).round(1)


# In[20]:


# 5.При помощи библиотеки gspread отправьте данные из предыдущего шага в Google SpreadSheet.


# In[22]:


from oauth2client.service_account import ServiceAccountCredentials


# Specify path to your file with credentials
path_to_credential = '/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/snappy-cosine-377017-fda1637920fb.json' 

# Specify name of table in google sheets
table_name = 'step_4_lesson_7'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(path_to_credential, scope)

gs = gspread.authorize(credentials)
work_sheet = gs.open(table_name)

# Select 1st sheet
sheet1 = work_sheet.sheet1

# Get data in python lists format
data = sheet1.get_all_values()

# Get header from data
headers = data.pop(0)

# Create df
df = pd.DataFrame(data, columns=headers)
df.head()


# In[ ]:


# 6.Прочитайте дополнительные данные из Google SpreadSheet, объедините вашу таблицу из предыдущего шага с 
# таблицей аналитика и посчитайте количество визитов на человека 
# (отношение visits к users) в разрезе по браузеру и значениям Robots/People
# В ответе укажите, 
# сколько визитов на уникального пользователя совершается ботами с браузера Google Chrome (округлите до целого)


# In[50]:


from io import BytesIO
import requests

r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQWMsvBTVio9C7IOOxfFO9C15BRHyME-_ENHqBodDOjuiHwk9fCuF5hUVmDs497PZOqPYK3exdSikOK/pub?gid=1006633900&single=true&output=csv')
data = r.content

df = pd.read_csv(BytesIO(data))


# In[51]:


df = df.merge(df_step_3, on=('browser', 'user_type', 'date'))


# In[53]:


df.head()


# In[58]:


df['visits_users'] = df.visits / df.users


# In[60]:


df.loc[(df.browser == 'Google Chrome') & (df.user_type == 'People')].visits_users.round()

