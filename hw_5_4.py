# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

from translate import Translator



""" Решение при помощи библиотеки translate"""

# with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_4.txt", "r", encoding="utf-8") as new_f:
#     with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_4_1.txt", "w", encoding="utf-8") as new_f_1:
#         for line in new_f.readlines():
#             line = list(line.split(" "))
#             translator = Translator(to_lang="Russian")
#             line[0] = translator.translate(line[0])
#             line = " ".join(line)
#             print(line)
#             new_f_1.writelines(line)


"""Решение при помощи словаря"""
numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_4.txt", "r", encoding="utf-8") as new_f:
    with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_4_1.txt", "w", encoding="utf-8") as new_f_1:
        for line in new_f.readlines():
            line = list(line.split(" "))
            # print(line)
            line[0] = numbers[line[0]]
            print(line)
            new_f_1.writelines(line)