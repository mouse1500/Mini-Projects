#
import pandas as pd
import os # импортируем библиотеку os
os.getcwd()

bookings = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/bookings.csv', encoding='windows-1251', sep=';')


bookings.info() # Смотрим какие данные хроняться в таблице и их количество

bookings.head()

bookings.columns


bookings = bookings.rename(str.lower, axis='columns') # Првиедение колонок к одному виду. Сначала все наименования приводим к нижнему регистру

def replace_space_with_star(name):     # Затем меняем пробел между словами на знак"_"
    new_name = name.replace(' ', '_')
    return new_name

bookings = bookings.rename(columns=replace_space_with_star)
bookings

bookings.groupby(['is_canceled', 'country'],as_index=False) .agg({'is_canceled' : 'count'}) .sort_values('is_canceled', ascending=False)

filter = bookings['is_canceled'] == 1
filter_book = bookings[filter]
filter_book['country'].value_counts()[:10]

bookings['hotel'].value_counts()

hotel_value_1 = ['City Hotel']
filter = bookings['hotel'].isin(hotel_value_1)
filter_book_1 = bookings[filter]
f1 = filter_book_1['stays_total_nights'].mean().round(2)


hotel_value_2 = ['Resort Hotel']
filter = bookings['hotel'].isin(hotel_value_2)
filter_book_2 = bookings[filter]
f2 = filter_book_2['stays_total_nights'].mean().round(2)

print(f1, f2)

bookings['assigned_room_type'] # тип полученного номера (может отличаться от забронированного)

bookings['reserved_room_type'] # тип зарезервированного номера

bookings.query('reserved_room_type != assigned_room_type').shape

filter = bookings['arrival_date_year'] == 2016
bookings_filter = bookings[filter]
bookings_filter['arrival_date_month'].value_counts()

filter = bookings['arrival_date_year'] == 2017
bookings_filter = bookings[filter]
bookings_filter['arrival_date_month'].value_counts()


hotel_value = ['City Hotel']
filter = (bookings['hotel'].isin(hotel_value)) & (bookings['is_canceled'] == 1)
filter_book_1 = bookings[filter]

filter_book_1.groupby('arrival_date_year')['arrival_date_month'].value_counts()

filter_book_1

bookings[['adults','children','babies']].mean()

bookings['total_kids'] = bookings['children'] + bookings['babies'] # Шаг 12

bookings['total_kids']

bookings.groupby('hotel', as_index=False) .agg({'total_kids' : 'mean'}) .round(2) .max()

