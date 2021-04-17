"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников."""


"""Изначальный вариант"""
with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_3.txt", "r") as new_f:
    sum_salary = 0
    for staff in new_f.readlines():
        staff = list(staff.split(" "))
        sum_salary += int(staff[1])
        if int(staff[1]) < 20000:
            print(f"{staff[0]} has less then 20000 in a month")
        new_f.seek(0)
    average = sum_salary / len(new_f.readlines())
    print(f"Average salary in company is {average}")

"""Вариант преподавателя"""
incomes = []
with open(r"C:\Users\paaltukhov\PycharmProjects\Паша\test_hw_5_3.txt", "r") as new_f:
    lines = new_f.readlines()

    for line in lines:
        name, income = line.split(",")
        income = int(income)
        if income < 2000:
            print(name)
        print(sum(incomes) / len(incomes))

"""Вариант преподавателя не работает, т.к. исходный текст создан иначе"""