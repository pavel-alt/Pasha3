# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

new_f = open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_1.txt", "w")
while True:
    s = input("Введите строку: ")
    new_f.write(f"{s}\n")
    if s == "":
        new_f.close()
        break


