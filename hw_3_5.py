# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.
import q as q

sum_list = 0

while True:

    user_answer = input("Введите числа через пробел: ").split()
    if "q" in user_answer:
        # user_answer = map(int, user_answer[0: user_answer.index("q")])
        # print(f"сумма элементов введенного массива {sum(user_answer)}")
        sum_list += sum(map(int, user_answer[: user_answer.index("q")]))
        print(f"сумма элементов результирующего массива {sum_list}")
        break
    else:
        print(f"сумма элементов введенного массива {sum(map(int, user_answer))}")
        sum_list += sum(map(int, user_answer))
        print(f"сумма элементов результирующего массива {sum_list}")

"""
Решение преподавателя
"""
def summator():
    total_sum = 0
    while True:
        num_list = input("Enter numbers: ")
        stopper = num_list.count("q")
        if stopper:
            total_sum += sum(map(int, num_list[:num_list.index("q") - 1].split()))
            break
        total_sum += sum(map(int, num_list.split()))
        print(f"Temporary sum value: {total_sum}")
    return total_sum


print(summator())

