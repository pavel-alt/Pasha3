"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

with open("test_hw_5_7.json", "w") as new_j_f:
    with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_7.txt", "r", encoding="utf-8") as new_f:
        firms_profit = {}
        average_profit = {}
        success_profit = []
        res_list = [firms_profit, average_profit]
        for line in new_f.readlines():
            line_list = [el for el in line.split()]
            name = line_list[0]
            profit = int(line_list[2]) - int(line_list[3])

            # firms_profit.update({name: profit})
            firms_profit[name] = profit        # Вариант решения препода
            if profit > 0:
                success_profit.append(profit)
        average_profit.update({"average_profit": sum(success_profit) / len(success_profit)})

        print(average_profit)
        print(firms_profit)
        print(res_list)

    json.dump(res_list, new_j_f)



