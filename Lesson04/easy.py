# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
original_list = [1, 2, 4, 0]

pow_list = [i*i for i in original_list]

print(pow_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit1 = ['Apple', 'Orange', 'grape', 'Banana', 'blackberry', 'Kiwi', 'waterMelon']
fruit2 = ['Apple', 'Orange', 'Grape', 'Banana', 'Orange', 'Strawberry','Cherry', 'Melon']

def tolower(*args):
    try:
        return [i.lower() for i in args]
    except AttributeError:
        print('В качестве аргумента была передана НЕ последовательность элементов')

union_list = [i for i in tolower(*fruit1) if i in tolower(*fruit2)]

print(union_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

rand_list = [random.randint(-5, 100) for _ in range(20)]

# def is_satisfies(el):
#     if el % 3 == 0 and el > 0 and el % 4 != 0:
#         return True
#     return False

# чтобы не нагромождать генератор
is_satisfies = lambda el: el % 3 == 0 and el > 0 and el % 4 != 0

satisf_elements = [el for el in rand_list if is_satisfies(el)]

print(satisf_elements)