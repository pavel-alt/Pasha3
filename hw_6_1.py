"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""

from time import sleep
from itertools import cycle

"""Мой вариант"""


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


"""Вариант препода"""


class TrafficLight:
    __colors = {"Красный": 7,"Желтый": 2, "Зеленый": 7}
    prev_colors = {"Красный": "Зеленый", "Желтый": "Красный", "Зеленый": "Желтый"}

    def running(self, run_count):
        colors_iteration = cycle(self.__colors)
        prev_color = "Зеленый"
        while run_count:
            current_light_value = next(colors_iteration)
            if TrafficLight.prev_colors[current_light_value] != prev_color:
                raise ValueError("Нарушен порядок!!")
            print(f"Сейчас горит сигнал: {current_light_value}"
                  f" {TrafficLight.__colors[current_light_value]} сек."
                  f"(Предыдущий: {prev_color})")
            sleep(self.__colors[current_light_value])
            prev_color = current_light_value
            run_count -= 1

    def get_colors(self, keyword):
        if keyword == "секретный пароль":
            return  self.__colors
        else:
            ValueError("Ошибка авторизации")


traffic_light = TrafficLight()
traffic_light.running(5)
print(traffic_light.get_colors("секретный пароль"))

