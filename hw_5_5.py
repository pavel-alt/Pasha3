# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint


with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_5.txt", "w", encoding="utf-8") as new_f:
    new_f.writelines(' '.join([str(randint(1, 100)) for el in range(10)]))

with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_5.txt", "r", encoding="utf-8") as new_f:
    res = sum([int(el) for el in list(new_f.readline().split(" "))])

print(res)

