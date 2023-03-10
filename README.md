# В данном каталоге будут размещаться мини проекты, в кторых я буду отрабатывать свои навыки. 

## Мини-проект 1.
Задачи:
 - Импортируйте библиотеку pandas как pd. Загрузите датасет bookings.csv с разделителем ;. Проверьте размер таблицы, типы переменных, а затем выведите первые 7 строк, чтобы посмотреть на данные. 
 - Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания.
 - Пользователи из каких стран совершили наибольшее число успешных бронирований? Укажите топ-5.
 - На сколько ночей в среднем бронируют отели разных типов?
 - Иногда тип номера, полученного клиентом (assigned_room_type), отличается от изначально забронированного (reserved_room_type). Такое может произойти, например, по причине овербукинга. Сколько подобных наблюдений встретилось в датасете?
 - Проанализируйте даты запланированного прибытия. – На какой месяц чаще всего успешно оформляли бронь в 2016? Изменился ли самый популярный месяц в 2017?– Сгруппируйте данные по годам и проверьте, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждый из периодов
 - Посмотрите на числовые характеристики трёх переменных: adults, children и babies. Какая из них имеет наибольшее среднее значение?
 - Создайте колонку total_kids, объединив children и babies. Для отелей какого типа среднее значение переменной оказалось наибольшим?
 - Создайте переменную has_kids, которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка (total_kids), в противном случае – False.
 - Посчитайте отношение количества ушедших пользователей к общему количеству клиентов, выраженное в процентах (churn rate). Укажите, среди какой группы показатель выше.
 
 
 ## Мини-проект 2.
 Задачи:
  - Импортируйте библиотеку pandas как pd. Загрузите два датасета user_data и logs. Проверьте размер таблицы, типы переменных, наличие пропущенных значений, описательную статистику.
 - Какой клиент совершил больше всего успешных операций? (success == True)
 - С какой платформы осуществляется наибольшее количество успешных операций?
 - Какую платформу предпочитают премиумные клиенты?
 - Визуализируйте распределение возраста клиентов в зависимости от типа клиента (премиум или нет)
 - Постройте график распределения числа успешных операций
 - Визуализируйте число успешных операций, сделанных на платформе computer, в зависимости от возраста, используя sns.countplot (x – возраст, y – число успешных операций). 
 - Клиенты какого возраста совершили наибольшее количество успешных действий?
 
 
 ## Мини-проект 3.
 Задачи:
 - Соберите все данные из папки data в один датафрэйм, имеющий следующие столбцы: колонки из самих файлов (product_id, quantity), а также имя пользователя (name), и дата этих покупок (date), соответствует названию папки, где лежит папка с пользователем)
 - Выясните, какой пользователь купил больше всего товаров. Если их несколько, то перечислите имена через запятую с пробелом и в алфавитном порядке.
 - Найдите топ-10 товаров по числу проданных единиц за всё время и постройте барплот. Сколько было продано единиц товара с product_id==56?
 - Визуализируйте продажи по дням.
 - Сколько пользователей приобрели какой-либо товар повторно (более 1 раза)? Повтором будем считать покупку товара с одинаковым product_id, совершенную в разные дни. 
 
 ## Мини-проект 3.1.
 Имеется таблица с записями о компаниях, включая их ИНН, и отдельный текстовый файл с набором ИНН (колонка head_inn), которые хранятся в папке 4_inn.
 Задачи:
 - Извлечь из таблицы записи с ИНН, указанными в текстовом файле
 - Записать результат в файл selected_inn.csv
 
 
## Мини-проект 4.
Задачи:
 - Загрузите датасет transaction_data.csv. Проверьте размер таблицы, типы переменных, число пропущенных значений и описательную статистику.
 - Какие значения находятся в колонке transaction? Сколько наблюдений относятся к тому или иному уровню? Визуализируйте результат с помощью барплота. 
 - Сколько транзакций завершились ошибкой?
 - Сколько успешных транзакций осуществил каждый из пользователей? Постройте гистограмму распределения числа успешных транзакций.
 - Коллега прислал Вам обновленные данные. Постройте сводную таблицу user_vs_minute_pivot, где в качестве столбцов будут использованы имена пользователей, строк – минуты, значений – число совершенных операций в указанную минуту. Пропущенные значения заполните нулями.
 - Сохраните правильное число минут, прошедших с начала дня, в колонку true_minute.


## Мини-проект 4.1
Задача: 
- Для проверки результатов введите SUBS_ID из полученного датасета в порядке возрастания, через запятую с пробелом.
Особенности данных:
- Сотрудники телемаркетинга не всегда указывают полный id, если 'id' нет в начале SUBS_ID, то нужно его добавить
- Поля в файлах могут быть расположены абсолютно случайным образом, но названия полей статичны
- Продажа не засчитывается, если отключение (END_DTTM) произошло меньше чем через 5 минут после подключения (START_DTTM)
- Если в файле с продажами встречается строка без указанного SUBS_ID, она пропускается


## Мини-проект 5
Задача:
- Разберемся с распределением количества показов и кликов. Посчитайте среднее количество показов и среднее количество кликов на объявления за весь период (округлите до целых).
- Нарисуйте график распределения показов на объявление за весь период.
- Давайте посчитаем скользящее среднее показов с окном 2. Какое значение скользящего среднего получим за 6 апреля 2019 года (ответ округлите до целых)?
- Скользящее среднее часто используется для поиска аномалий в данных. Давайте попробуем нанести на один график значения арифметического среднего по дням и скользящего среднего количества показов. В какой день наблюдается наибольшая разница по модулю между арифметическим средним и скользящим средним? Дни, в которых скользящее среднее равно NaN, не учитываем. 
- Напишите функцию, которая найдет проблемное объявление (с наибольшим/наименьшим количеством показов) в день, в который была замечена самая большая по модулю аномалия. 
- Теперь подгрузим данные по рекламным клиентам и найдем среднее количество дней от даты создания рекламного клиента и первым запуском рекламного объявления этим клиентом.
- Вычислите конверсию из создания рекламного клиента в запуск первой рекламы в течение не более 365 дней. Ответ дайте в процентах и округлите до сотых. (Фильтровать нужно по значению в формате pd.Timedelta(365, unit='d'))
- Давайте разобъем наших клиентов по промежуткам от создания до запуска рекламного объявления, равным 30. Определите, сколько уникальных клиентов запустили свое первое объявление в первый месяц своего существования (от 0 до 30 дней). Список промежутков для метода pd.cut – [0, 30, 90, 180, 365]
- А теперь – выведем на интерактивный график эти категории с количеством уникальных клиентов в них.


## Мини-проект 5.1
Задача:
- Выделите из колонки attributes значение атрибута Parent. Т.е. если там записано Parent=x, то нам нужен x
- Выясните, какое из этих значений является самым частым
- Постройте распределение встречаемости значений в столбце type


## Мини-проект 6
Задача:
- Отражены в самих проектах.
