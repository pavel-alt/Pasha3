"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

В класс скад добавить параметр максимальной вместительности, добавить поле наполненности на складе, сделать метод
добавления объектов из офисэквипмента.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
на уроках по ООП.
"""

from abc import ABC, abstractmethod


class Storage:

    list_storage = []

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.list_object = []
        Storage.list_storage.append(self)

    def getting(self, obj):
        if len(self.list_object) < self.capacity:
            if issubclass(type(obj), OfficeEquipment):
                self.list_object.append(obj)
                print("Object in storage")
            else:
                print("Zobery eto")
        else:
            print("Storage is full")

    def take_away(self, obj):
        if obj in self.list_object:
            self.list_object.remove(obj)
            print("Object deleted")

    @staticmethod
    def audit(storage):
        printer, scanner, copier = 0, 0, 0
        for obj in storage.list_object:
            if isinstance(obj, Printer):
                printer += 1
            if isinstance(obj, Scanner):
                scanner += 1
            if isinstance(obj, Copier):
                copier += 1

        in_storage = {'Printer': printer, 'Scanner': scanner, 'copier': copier}
        print(in_storage)


class OfficeEquipment(ABC):
    def __init__(self, firm='canon'):
        self.firm = firm

    @abstractmethod
    def action(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, firm='Canon', ink='full'):
        super(Printer, self).__init__(firm)
        self.ink = ink

    def action(self):
        print("Printing documents")


class Scanner(OfficeEquipment):

    def __init__(self, firm='Canon', lamp='new'):
        super(Scanner, self).__init__(firm)
        self.lamp = lamp

    def action(self):
        print("Scanning documents")


class Copier(OfficeEquipment):

    def __init__(self, firm='Canon', paper='full'):
        super(Copier, self).__init__(firm)
        self.paper = paper

    def action(self):
        print("Coping documents")


storage1 = Storage("storage1", 10)
storage2 = Storage("storage2", 10)

while True:
    user_answer = input("What kind of equipment do you need? Printer, Scanner or Copier?: ").title()
    if user_answer in [i.__name__ for i in OfficeEquipment.__subclasses__()]:
        equipment = [i for i in OfficeEquipment.__subclasses__() if i.__name__ == user_answer][0]
        break
while True:
    user_answer = input(f'What storage do you need? You can choose {[i.name for i in Storage.list_storage]}: ')
    if user_answer in [i.name for i in Storage.list_storage]:
        storage = [i for i in Storage.list_storage if i.name == user_answer][0]
        break
while True:
    try:
        user_answer = int(input(f'How mach {equipment.__name__}s du you need ?: '))
        break
    except ValueError as err:
        print("Please enter the number only")

for i in range(user_answer):
    equipment1 = equipment()
    storage.getting(equipment1)

Storage.audit(storage)
