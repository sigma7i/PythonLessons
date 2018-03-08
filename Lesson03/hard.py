# Задание - 1
# Задание - 2
def create_unit(name, health =100, damage = 50, armor = 1.2):
    return {'name': name, 'health': health, 'damage': damage, 'armor': armor}

def get_damage(person, attack_person):
    return attack_person['damage'] / person['armor']

def attack(person, attack_person):
    damage = get_damage(person, attack_person)
    person['health'] -= damage
    print('{} атакует {}'.format(attack_person['name'], person['name']))
    print(f'Получен урон: {damage}')

def save_to_file(persion):
    with open(persion['name']+'.txt', 'w', encoding='UTF-8') as fw:
        for kw, val in persion.items():
            fw.write(f'{kw} {val}\n')

def save_many_payers(*persons):
    for p in persons:
        save_to_file(p)

def read_from_file(person):
    persion_dic = {'name': person['name']}
    with open(person['name'] + '.txt', 'r', encoding='UTF-8') as fr:
        file_lines = fr.readlines()
        for line in file_lines:
            key, value = line.replace('\n', '').split(' ')
            if key != 'name':
                persion_dic[key] = float(value)

    return create_unit(**persion_dic)

def fight(player, enemy):
    i = 1
    while True:
        if i % 2 == 0:
            attack(player, enemy)
        else:
            attack(enemy, player)

        if player['health'] <= 0:
            print(player['name'] + ' проиграл')
            break
        if enemy['health'] <= 0:
            print(enemy['name'] + ' проиграл')
            break
        i+=1

# использование
player = create_unit('elf', armor=1.3)
enemy = create_unit('ork', 150, 40)

save_many_payers(player, enemy)

saved_player = read_from_file(player)
saved_enemy = read_from_file(enemy)

fight(saved_player, saved_enemy)