class Car:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color
        self._engine()

    def go(self):
        print(self.name, 'is starting to move')

    def stop(self):
        print(self.name, 'is stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def _engine(self):
        print(self.name, 'is starting')


class TownCar(Car):
    def max_speed(self):
        if self.speed > 60:
            print(self.name, 'is going too fast')


class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        print(self.name, 'starting from 0 to 100 real quick')


class WorkCar(TownCar):
    pass


class PoliceCar(SportCar):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color)
        self.is_police = is_police

    def police_siren(self, is_police):
        if is_police == True:
            print('WiuWiuWiu')

jeep = Car('wrangler', 120, 'green')

jeep.go()
jeep.turn('back')

honda = TownCar('civic', 155, 'black')

honda.max_speed()

nissan = WorkCar('premiera', 120, 'white')

nissan.max_speed()


skyline = SportCar('gtr', 280, 'blue')

opel = PoliceCar('vectra', 250, 'black',True)

opel.police_siren(True)