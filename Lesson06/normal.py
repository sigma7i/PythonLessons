# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    # def save_to_file(self):
    #     with open(self.name + '.txt', 'w', encoding='UTF-8') as fw:
    #         for key, value in vars(self).items():
    #             fw.write(f'{key} {value}\n')
    #
    # def read_from_file(self):
    #     with open(self.name + '.txt', 'r', encoding='UTF-8') as fr:
    #         file_lines = fr.readlines()
    #         for line in file_lines:
    #             key, value = line.replace('\n', '').split(' ')
    #             if key == 'name':
    #                 name =

    def _get_damage(self, attack_person):
        return self.damage / attack_person.armor

    def attack(self, attack_person):
        damage = self._get_damage(attack_person)
        attack_person.health -= damage
        print(f'{self.name} атакует {attack_person.name}')
        print(f'Получен урон: {damage}')






# def fight(player, enemy):
#     i = 1
#     while True:
#         if i % 2 == 0:
#             attack(player, enemy)
#         else:
#             attack(enemy, player)
#
#         if player['health'] <= 0:
#             print(player['name'] + ' проиграл')
#             break
#         if enemy['health'] <= 0:
#             print(enemy['name'] + ' проиграл')
#             break
#         i+=1
#
# # использование
# player = create_unit('elf', armor=1.3)
# enemy = create_unit('ork', 150, 40)
#
# save_many_payers(player, enemy)
#
# saved_player = read_from_file(player)
# saved_enemy = read_from_file(enemy)
#
# fight(saved_player, saved_enemy)