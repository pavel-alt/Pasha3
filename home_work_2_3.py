# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# 1 ВАРИАНТ
winter = (12, 1, 2)
spring = (3, 4, 5)
summer = (6, 7, 8)
autumn = (9, 10, 11)

year = {winter: "зима", spring: "весна", summer: "лето", autumn: "осень"}


try:
    user_qwestion = int(input("Введите номер месяца от 1 до 12: "))
except ValueError as err:
    print(f"В следующий раз постарайся и введи именно число от 1 до 12, а пока {err}")


if user_qwestion in winter:
    print(year.get(winter))
elif user_qwestion in spring:
    print(year.get(spring))
elif user_qwestion in summer:
    print(year.get(summer))
else:
    print(year.get(autumn))


# 2 ВАРИАНТ
year = {12: "зима", 1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень", 10: "осень", 11: "осень"}

try:
    user_qwestion = int(input("Введите номер месяца от 1 до 12: "))
except ValueError as err:
    print(f"В следующий раз постарайся и введи именно число от 1 до 12, а пока {err}")

print(year.get(user_qwestion))

# 3 ВАРИАНТ

year = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]

while True:
    try:
        user_qwestion = int(input("Введите номер месяца от 1 до 12: "))
        if user_qwestion < 1 or user_qwestion > 12:
            print(f"В следующий раз постарайся и введи именно число от 1 до 12")
        else:
            break
    except ValueError as err:
        print(f"В следующий раз постарайся и введи именно число от 1 до 12, а пока {err}")

print(year[user_qwestion - 1])