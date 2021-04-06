# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.

with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_2.txt", "r") as new_f:
    print(f"The number of strings is - {len(new_f.readlines())}")
    new_f.seek(0)
    for s in new_f.readlines():
        w = len(s.split(" "))
        print(f"The number of words in string - {w}")

