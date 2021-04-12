# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        color_list = [["red", 7], ["yellow", 2], ["green", 5]]
        color_print = [el[0] for el in color_list]
        color_print = color_print[color_print.index(self.__color):] + color_print[:color_print.index(self.__color)]
        color = cycle(color_print)
        var_sleep = cycle([el[1] for el in color_list])
        while True:
            var_color = next(color)
            print(var_color)
            sleep(next(var_sleep))


traffic_light = TrafficLight("yellow")
traffic_light.running()

