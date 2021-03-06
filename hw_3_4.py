# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def easy_func(x, y):
    """
    Как эту задачу можно решить быстро. Надо добавить проверку /0
    """
    res = x ** y
    return res


print(easy_func(2, -2))


def my_func(x, y):
    """
    Как эту задачу можно решить долго с проверкой /0
    + в if можно дописать решение для положительных степеней
    """
    b_el = x
    while True:
        if y < 0:
            a = [x]
            b = a * abs(y)
            for i in range(len(b) - 1):
                b_el *= b[i]
                i += 1
        break
    res = 1 / b_el
    return res


try:
    print(my_func(2, -3))

except ZeroDivisionError as err:
    print("на ноль делить нельзя!")


def my_func_2(x, y):
    """
    Как эту задачу можно решить нормально. Решай нормально.
    """
    result = x
    for i in range(abs(y)-1):
        result *= x
    return 1 / result


print(my_func_2(3.8, -4))

