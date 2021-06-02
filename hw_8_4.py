"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""



"""
В класс скад добавить параметр максимальной вместительности, добавить поле наполненности на складе, сделать метод 
добавления объектов из офисэквипмента.
"""
from abc import ABC, abstractmethod




class Storage:
    def __init__(self):
        pass
in_storage = []


class OfficeEquipment(ABC):



    def __init__(self, type_eq, manufacturing, model, price):
        self.type_eq = type_eq
        self.manufacturing = manufacturing
        self.model = model
        self.price = price

    @abstractmethod
    def action(self):
        pass

    def getting(self):
        if OfficeEquipment:
            in_warehouse[f'{self.type_eq}'] = [self.manufacturing, self.model, self.price]


class Printer(OfficeEquipment):
    count_printer = 0

    def __init__(self, manufacturing, model, price, ink, type_eq="Printer", condition="new"):
        super(Printer, self).__init__(type_eq, manufacturing, model, price)
        self.ink = ink
        self.condition = condition
        self.__class__.count_printer += 1

    def action(self):
        print("print documents")


class Scanner(OfficeEquipment):

    def __init__(self, manufacturing, model, price, lamp, type_eq="Scanner", condition="new"):
        super(Scanner, self).__init__(type_eq, manufacturing, model, price)
        self.lamp = lamp
        self.condition = condition

    def action(self):
        print("scan documents")


class Copier(OfficeEquipment):
    def __init__(self, manufacturing, model, price, paper, type_eq="Copier", condition="new"):
        super(Copier, self).__init__(type_eq, manufacturing, model, price)
        self.paper = paper
        self.condition = condition

    def action(self):
        print("copy documents")


obj_1 = Printer("canon", "x1", 100, 1)
obj_1.get_in_storage()

for i in in_storage:
    print(i.price, i.model)

# for _ in range(3):
#     Printer("canon", "x1", 100, 1, 300)
#
# print(Printer.count_printer)

#print(obj_1.type_eq)
# obj_1.action()


# obj_2 = Scanner("Scanner", "hp", "205", 200, 1, 1)
# print(obj_2.lamp)
# obj_2.action()
#
# obj_3 = Copier("Copier", "xerox", "100", 150, 1, 100)
# print(obj_3.paper)
# obj_3.action()
