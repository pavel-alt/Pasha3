"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def str_2_int(cls, string):
        res = [int(el) for el in string.split("-")]
        print(len(res))
        return res

    @staticmethod
    def validation(res):
        if len(res) == 3:
            if res[0] in range(1, 31):
                if res[1] in range(1, 12):
                    if res[2] > 0:
                        return res
        print("ERROR")


user_str = input("Input date string like 'day-month-year': ")
c = 1


print(Date.str_2_int(user_str))
print(Date.validation(user_str))
