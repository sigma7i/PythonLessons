# Задание - 1

def person_info(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'

print(person_info('Василий', 21, 'Москва'))

# Задание - 2
def get_max(first, second, third):
    return max(first, second, third)

print(get_max(2,-9, 7))

# Задание - 3
def get_max_str_len(*args):
    return max(args, key=len)

print(get_max_str_len('one', 'first', 'remind', 'competition', 'python lessons'))