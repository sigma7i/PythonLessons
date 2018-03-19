# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный класс, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, name, color, type = 'плюшевая игрушка'):
        self.name = name
        self.color = color
        self.type = type

    def purchase_materials(self):
        print(f'закупаем материалы для {self.name}')

    def make_toy(self):
        print(f'создаю игрушку {self.name} типа {self.type}')

    def colorize_toy(self):
        print(f'идет окрашивание игрушки {self.name} в цвет {self.color}')

class TeddyBear(Toy):
     def __init__(self, color):
         super().__init__('плюшевый мишка', color)

class DogToy(Toy):
    def __init__(self, color):
        super().__init__('игрушечная собака', color, 'игрушка')

    def make_toy(self):
        super().make_toy()
        print('вставляю батарейки')

class PlasticineCheburashka(Toy):
    def __init__(self, color):
        super().__init__('пластелиновый чебурашка', color, 'пластелиновая игрушка')

    def purchase_materials(self):
        print(f'закупаем пластелин цвет: {self.color} для {self.name}')

    def colorize_toy(self):
        pass # пластелин и так имеет цвет


class Factory:
    def __init__(self):
        print('запуск фабрики...')

    def make_toy(self, toy):
        toy.purchase_materials()
        toy.make_toy()
        toy.colorize_toy()
        print(f'Производство {toy.name} закончено\n')

bear = TeddyBear('коричневый')
dog = DogToy('черный')
cheburashka = PlasticineCheburashka('зеленый')

factory = Factory()
factory.make_toy(bear)
factory.make_toy(dog)
factory.make_toy(cheburashka)


