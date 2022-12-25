#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
os.getcwd()

df = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/5/transaction_data.csv')

#Проверьте размер таблицы, типы переменных, число пропущенных значений и описательную статистику.
#Вопрос: сколько в датасете пропущенных значений?
df.info()
df.isna().sum()

#Проверьте, какие значения принимает колонка transaction. 
#Сколько наблюдений относятся к тому или иному уровню? 
#Визуализируйте результат с помощью барплота.
df['transaction'].value_counts()
new_tr = df.transaction.value_counts().reset_index()
sns.barplot(x='index', y='transaction', data=new_tr)

#Сколько транзакций осуществил каждый из пользователей? Осуществлёнными считаются транзакции со значением successfull
#Посмотрите на характеристики распределения, а затем постройте гистограмму числа успешных транзакций, 
#совершённых каждым пользователем, где:
#по оси x – число транзакций
#по оси y – доля пользователей с таким числом транзакций
new_pipl = df.query('transaction == "successfull"').groupby('name', as_index=False).agg({'transaction' : 'count'})     .sort_values('transaction', ascending=False).reset_index().drop(columns='index')
sns.distplot(new_pipl.transaction)
new_pipl.describe()

#Постройте сводную таблицу c новыми данными user_vs_minute_pivot, где:
#столбцы – имена пользователей
#строки – минута времени осуществления операции (minute)
#значения – число совершённых операций
#Пропущенные значения заполните нулями.
transaction_data = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/transaction_data_updated.csv')
transaction_data.head()
df_tr = transaction_data.groupby(['name', 'minute'], as_index=False).agg({'transaction' : 'count'})
user_vs_minute_pivot = df_tr.pivot(index='minute', columns='name', values='transaction').fillna(0)
user_vs_minute_pivot

#Посчитайте число минут, прошедших с начала дня. Результат сохраните в колонку true_minute. 
#Постройте график.
transaction_data.info()
transaction_data['date'] = pd.to_datetime(transaction_data['date'])
transaction_data['true_minute'] = transaction_data.date.dt.minute + (transaction_data.date.dt.hour * 60)
new_df = transaction_data.groupby('true_minute', as_index=False).agg({'name' : 'count'})
plt.subplots(figsize=(15, 15))
sns.barplot(x = 'true_minute', y= 'name', data=new_df)
plt.xticks(fontsize = 10, rotation = 90)