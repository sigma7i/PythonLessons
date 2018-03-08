# Задание - 1

emploees = ('Иванов', 'Петров', 'Сидоров', 'Яковлев', 'Николаев')
salarys = (10000, 50000, 9500, 27000, 67000)

with open('salary.txt', 'w+', encoding='UTF-8') as f:
    f.writelines([a + ' - ' + str(b) + '\n' for a,b in zip(emploees, salarys)])
    f.seek(0)
    file_lines = f.readlines()

dic = {}
for line in file_lines:
    key, value = line.replace('\n', '').split(' - ')
    dic[key] = float(value)

for kw, val in dic.items():
    if val <= 50000:
        print('{} - {}'.format(kw.upper(), val - (val * 0.13) ))

