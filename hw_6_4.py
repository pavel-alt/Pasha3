"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

from time import sleep


class Car:

    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"The car moving about {self.speed} km/h")

    def go(self):
        if self.speed == 0:
            self.speed = 100
        print("Headway")
        self.show_speed()

    def stop(self):
        if self.speed > 0:
            self.speed = 0
        print("Standing")

    def turn(self, direction=None):
        var_direction = ["right", "left", "around"]
        if direction in var_direction:
            print(f"The car moving {direction} about {self.speed / 2} km/h")
        else:
            print("Headway")
            print(f"The car moving about {self.speed} km/h")


class TownCar(Car):

    def show_speed(self):
        print(f"The car moving about {self.speed} km/h")
        if self.speed > 60:
            print("Warning!! Over speed!!")
            sleep(2)
            self.speed = 60
            print(f"The car moving about {self.speed} km/h")


class SportCar(Car):

    def hello(self):
        print("It's time for scare speed!!")


class WorkCar(Car):

    def show_speed(self):
        print(f"The car moving about {self.speed} km/h")
        if self.speed > 40:
            print("Warning!! Over speed!!")
            sleep(2)
            self.speed = 40
            print(f"The car moving about {self.speed} km/h")


class PoliceCar(Car):

    def hello(self):
        print("I'll catch you!")


tractor = WorkCar(70, "yellow", "tractor", False)
tractor.show_speed()
tractor.stop()
tractor.go()
tractor.turn("left")

bus = TownCar(70, "yellow", "bus", False)
bus.show_speed()
bus.stop()
bus.go()
bus.turn("right")

lamba = SportCar(100, "yellow", "lamba", False)
lamba.hello()
lamba.show_speed()
lamba.stop()
lamba.go()
lamba.turn("right")

mahony = PoliceCar(100, "yellow", "Mahony", True)
mahony.hello()
mahony.show_speed()
mahony.stop()
mahony.go()
mahony.turn("right")