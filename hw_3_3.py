# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
# сумму наибольших двух аргументов. Функция sum - читерство.


def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    s = my_list[0] + my_list[1]
    return s


print(my_func(10, 20, 30))
