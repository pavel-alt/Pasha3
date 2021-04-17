"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
строк, количества слов в каждой строке.
"""

"""Изначальный вариант"""

# with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_2.txt", "r") as new_f:
#     print(f"The number of strings is - {len(new_f.readlines())}")
#     new_f.seek(0)
#     for s in new_f.readlines():
#         w = len(s.split(" "))
#         print(f"The number of words in string - {w}")

"""Вариант преподавателя"""

with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_2.txt", "r") as new_f:
    lines = new_f.readlines()
    print(f"Всего строк: {len(lines)}")
    for line in lines:
        print(f"'{line[:-1]}' слов в строке - {len(line)}")

"""Вариант преподавателя не соответствует заданию, т.к. считает кол-во символов в строке, а не количество слов"""
