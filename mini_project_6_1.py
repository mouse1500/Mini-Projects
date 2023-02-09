#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?q=sunflowers')
res = r.json()


# In[3]:


# 1.Предположим, ваша задача – найти все произведения, связанные с подсолнухами.
# Выполните поиск по слову "sunflowers". Внимательно посмотрите на формат ответа и 
# сохраните id полученных объектов в список sunflower_ids.
# В качестве ответа выберите id объектов из списка numbers, которые присутствуют в полученном списке sunflower_ids.


# In[4]:


sunflower_ids = res['objectIDs']


# In[5]:


numbers = [437329, 436524, 16822570, 20149, 2032]


# In[6]:


result = list(set(sunflower_ids) & set(numbers))
result


# In[31]:


# 2.собрать информацию об этих объектах. Сколько объектов относятся к японской культуре?


# In[8]:


r_test = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/437980')
obj_test = r_test.json()


# In[ ]:


# 3.Теперь напишите цикл, с помощью которого будет собрана информация об объектах, которые были получены в sunflower_ids. 
# Результаты запишите в датафрейм, а именно – следующие параметры:
# objectID, title, artistDisplayName, department, objectBeginDate, objectEndDate, period, objectName, culture


# In[25]:


df = pd.DataFrame()


# In[29]:


for i in sunflower_ids: 
    a  = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}')
    obj = a.json()
    df_it = pd.DataFrame({'objectID' : obj.get('objectID'),
                      'title' : obj.get('title'), 
                      'artistDisplayName' : obj.get('artistDisplayName'), 
                      'department' : obj.get('department'), 
                      'objectBeginDate' : obj.get('objectBeginDate'), 
                      'objectEndDate' : obj.get('objectEndDate'), 
                      'period' : obj.get('period'), 
                      'objectName' : obj.get('objectName'), 
                      'culture' : obj.get('culture')}, index=[0])
    df = pd.concat([df_it, df])


# In[30]:


df.culture.value_counts()


# In[22]:


# 4.Найди большее число работ по периоду.


# In[32]:


r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=6&q=cat')
cats = r.json()


# In[37]:


asia = cats['objectIDs']


# In[38]:


for i in asia: 
    a  = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=6&q=cat')
    obj = a.json()
    df_it = pd.DataFrame({'objectID' : obj.get('objectID'),
                      'title' : obj.get('title'), 
                      'artistDisplayName' : obj.get('artistDisplayName'), 
                      'department' : obj.get('department'), 
                      'objectBeginDate' : obj.get('objectBeginDate'), 
                      'objectEndDate' : obj.get('objectEndDate'), 
                      'period' : obj.get('period'), 
                      'objectName' : obj.get('objectName'), 
                      'culture' : obj.get('culture')}, index=[0])
    df = pd.concat([df_it, df])


# In[45]:


df.period.value_counts()

