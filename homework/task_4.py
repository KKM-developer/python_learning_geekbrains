class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        return print('Машина едет')
    def stop(self):
        return print('Машина остановилась')
    def turn(self, direction):
        return print(f'Машина повернула на {direction}')
    def show_speed(self):
        return print(f'Машина едет со скоростью {self.speed}')


class TownCar(Car):
    __speed_limit = 60
    def speed_limit(self, speed):
        if speed > TownCar.__speed_limit:
            print("Превышение скорости")

class SportCar(Car):
    __speed_limit = 90
    def speed_limit(self, speed):
        if speed > SportCar.__speed_limit:
            print("Превышение скорости")



class WorkCar(Car):
    __speed_limit = 40
    def speed_limit(self, speed):
        if speed > WorkCar.__speed_limit:
            print("Превышение скорости")


class PoliceCar(Car):
    is_police = True

town = TownCar()
spotr = SportCar()
work = WorkCar()
police = PoliceCar()



town.color = 'Red'
town.name = 'Volvo'
town.speed_limit(80)

spotr.color = 'yellow'
spotr.name = 'Ferrari'
spotr.speed = 100
spotr.show_speed()
spotr.go()
spotr.turn('лево')

work.color = 'White'
work.name = 'Kamaz'
work.turn('право')
work.stop()