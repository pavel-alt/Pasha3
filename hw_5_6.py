# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_6.txt", "r", encoding="utf-8") as new_f:
    new_dict = {}
    for line in new_f.readlines():
        name, hours_1 = line.split(":")
        res_hours = sum(list(map(int, ("".join([el for el in hours_1 if el.isdigit() or el == " "])).split())))
        new_dict.update({name: res_hours})
    print(new_dict)


