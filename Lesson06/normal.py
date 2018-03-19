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
import pickle


class Person:
    def __init__(self, name, health, damage, armor=1):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def save_to_file(self):
        with open(self.name + '.txt', 'wb') as wb:
            pickle.dump(self, wb)

    def read_from_file(self):
        with open(self.name + '.txt', 'rb') as rb:
            return pickle.load(rb)

    def _get_damage(self, attack_person):
        return self.damage / attack_person.armor

    def attack(self, attack_person):
        damage = round(self._get_damage(attack_person), 2)
        attack_person.health -= damage
        print(f'{self.name} атакует {attack_person.name}')
        print(f'Получен урон: {damage}')


class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        i = 1
        while True:
            if i % 2 == 0:
                self.player.attack(self.enemy)
            else:
                self.enemy.attack(self.player)

            if self.player.health <= 0:
                print(self.player.name + ' проиграл')
                break
            if self.enemy.health <= 0:
                print(self.enemy.name + ' проиграл')
                break
            i += 1


player = Person('elf', 100, 80, 1.3)
enemy = Person('ork', 150, 40, 1.4)

player.save_to_file()

saved_player = player.read_from_file()

fight_arena = Fight(saved_player, enemy)

fight_arena.fight()
