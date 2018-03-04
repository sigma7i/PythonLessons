# Задание-1:
equation = 'y = -12x + 11111140.2121'
x = 2.5

# не универсальное решение
eval = equation.split(' ')[2:]
argument = int(eval[0].replace('x', ''))

print(f'Result {argument * x + float(eval[2])}')

# Задание-2:
data = input('Введите дату: ')

day_in_mounth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if len(data) != 10:
    print('Некорретный формат даты')
else:
    data_to_list = data.split('.')
    day = int(data_to_list[0])
    mounth = int(data_to_list[1])
    year = int(data_to_list[2])
    if not 1 <= day <= 31:
        print('дни выходят из задоного диапазона')
    elif not 1 <= mounth <= 12:
        print('месяца выходят из задоного диапазона')
    elif not 1 <= year <= 9999:
        print('года выходят из задоного диапазона')

    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    day_in_mounth[1] = 29

    if day > day_in_mounth[mounth - 1]:
        print('максимальный день не соотвествует месяцу')