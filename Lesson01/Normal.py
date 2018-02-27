# Задание 1 из Normal

input_integer = 0

while input_integer <= 0 or input_integer >= 10:
    input_value = input('Введите число больше 0, но меньше 10: ')
    if not input_value.isnumeric():
        print('Необходимо ввести число')
        continue

    input_integer = int(input_value)
    if 0 < input_integer < 10:
        print(input_integer ** 2)
    else:
        print('Необходимо ввести число в диапазоне 0 и 10')

# Задание 2 из Normal
print('Переходим на задание 2')

a = int(input('Введите число а = '))
b = int(input('Введите число b = '))

print('Изначально: a = ' + str(a) + ' b = ' + str(b)) # возможно можно без приведение к str

a += b
b -= a - b
a -= b

print('Результат: a = ' + str(a) + ' b = ' + str(b)) # возможно можно без приведение к str


