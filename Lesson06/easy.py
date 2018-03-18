# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class BaseCar:
    def __init__(self, speed, name, is_police = False):
        self.speed = speed
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} машина поехала со скоростью {self.speed}')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')


class TownCar(BaseCar):
    def __init__(self, speed):
        super().__init__(speed, 'городская машина')

class SportCar(BaseCar):
    def __init__(self, speed):
        super().__init__(speed, 'спортивная машина')

class WorkCar(BaseCar):
    def __init__(self, speed):
        super().__init__(speed, 'рабочая машина')

class PoliceCar(BaseCar):
    def __init__(self, speed):
        super().__init__(speed, 'полицейская машина', is_police= True)

town_car = TownCar(60)
sport_car = SportCar(100)
work_car = WorkCar(70)
police_car = PoliceCar(95)

for car in (town_car,sport_car, work_car, police_car):
    car.go()
    car.turn('лево')
    car.turn('право')
    if car.is_police:
        car.turn('развилку')

    car.stop()








