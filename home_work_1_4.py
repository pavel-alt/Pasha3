# Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические операции.

num_init = int(input("Введите целое положительное число: "))
max_d = 0
num = num_init

while num > 0:
    digit = num % 10
    if digit > max_d:
        max_d = digit
        if max_d == 9:
            break
    num = num // 10

print(max_d)

# Надо научиться так думать