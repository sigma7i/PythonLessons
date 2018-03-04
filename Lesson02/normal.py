import random

# задача 1
integer_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []

for item in integer_list:
    if item > 0:
        qr = item ** 0.5
        if qr % 1 == 0:
            new_list.append(int(qr))

print(new_list)

# задача 2
date = '02.11.2013'
days = [
    'первое',
    'второе',
    'третье',
    'четвертое',
    'пятое',
    'шестое',
    'седьмое',
    'восьмое',
    'девятое',
    'десятое',
    'одиннадцатое',
    'двенадцатое',
    'тринадцатое',
    'четырнадцатое',
    'пятнадцатое',
    'шестнадцатое',
    'семнадцатое',
    'восемнадцатое',
    'девятнадцотое',
    'двадцатое',
    'двадцать первое',
    'двадцать второе',
    'двадцать третье',
    'двадцать четвертое',
    'двадцать пятое',
    'двадцать шестое',
    'двадцать седьмое',
    'двадцать восьмое',
    'двадцать девятое',
    'тридцатое',
    'тридцать первое'
]
months = [
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря'
]

dates = date.split('.')
current_day = int(dates[0])
current_mounth = int(dates[1])

print(f'{days[current_day - 1]} {months[current_mounth - 1]} {dates[2]} года')

# задача 3

random_list = []

for i in range(-100, 100):
    random_list.append(random.randint(-100, 100))

print(random_list)

# задача 4
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = set(lst)

print(lst2)

unique = []
for uq in lst:
    if lst.count(uq) == 1:
        unique.append(uq)

print(unique)
