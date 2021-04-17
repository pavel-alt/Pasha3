"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""


"""Изначальный вариант"""

new_f = open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_1.txt", "w")
while True:
    s = input("Введите строку: ")
    new_f.write(f"{s}\n")
    if s == "":
        new_f.close()
        break


"""Вариант преподавателя"""

with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_1.txt", "w") as new_f_1:
    while True:
        line = f'{input("Введите строку: ")}\n'
        if line == "\n":
            break
        new_f_1.write(line)
