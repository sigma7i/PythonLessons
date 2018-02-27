# Задание 1

user_value = input('Введите любое значение ')
print(user_value)

# задание 2
input_value = input('Введите число: ')
if input_value.isnumeric():
    print(int(input_value) + 2)
else:
    print("Нужно ввести число")

# задание 3
age = int(input('Введите Ваш возраст'))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')



