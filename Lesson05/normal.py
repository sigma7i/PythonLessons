# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import Lesson05.easy as easy
import os

CONSOLE_TEXT = '''
1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку
5. Вернуть все как было
6. Выход
'''
print(os.getcwd())

# сохраняем возможность вернуть все на место
actions_list = []

while True:
    try:
        action = int(input(CONSOLE_TEXT))
    except ValueError:
        print('Необходимо выбрать пункт')

    if action == 1:
        easy.change_directory()
    elif action == 2:
        easy.show_dirs()
    elif action == 3:
        easy.directory_action(easy.delete_dir,
                              ok='Успешно удалено',
                              failure='Ошибка удаления',
                              log=actions_list.remove)
    elif action == 4:
        easy.directory_action(easy.create_dir,
                              ok='Успешно создано',
                              failure='Ошибка создания',
                              log=actions_list.append)
    elif action == 5:
        for d in actions_list: easy.delete_dir(d)
    elif action == 6:
        break
    else:
        print('Неизвестная команда')
