# задание 1 из hard
# решил облегчить задачу себе и проверяющего, добавив тестовые примеры и поочередно проходя их в цикле
# кроме функций за рамки не выходил

def medicine_anketa(name, age, weight):
    person_info = name + ', ' + str(age) + ' год, вес ' + str(weight) + ' - '
    out_of_normal_weight = weight < 50 or weight > 120

    if age < 30 and 50 <= weight < 120:
        print(person_info + 'хорошее состояние')
    elif 30 <= age <= 40 and out_of_normal_weight:
        print(person_info + 'следует заняться собой')
    elif age > 40 and out_of_normal_weight:
        print(person_info + 'следует обратится к врачу!')
    else:
        print('Что ты такое!?')


test_data = (('Вася Пупкин', 29, 90),
             ('Вася Пупкин', 31, 121),
             ('Вася Пупкин', 31, 49),
             ('Вася Пупкин', 41, 121),
             ('Вася Пупкин', 41, 49),
             )
i = 0
while i < 5:
    medicine_anketa(test_data[i][0], test_data[i][1], test_data[i][2])
    i += 1

# name = input('Введите Ваше имя: ')
# age = int(input('Введите возраст: '))
# weight = float(input('Введите вес: '))
#
# medicine_anketa(name, age, weight)
