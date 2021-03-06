#  Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#  Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
#  элемента — номер товара и словарь с параметрами (характеристиками товара: название,
#  цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
#  запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
# ключ — характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.

# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
'''
from copy import deepcopy

base = []
count = 0
char_of_product = []
product = {}

final_val = []
final_final_dict = {}
final_dict = {}

while True:
    keys = input("Введите характеристику товара: ")
    if keys == "0":
        break
    char_of_product.append(keys)

while True:
    agree = input("Вы хотите заполнить данные базы? Y/N: ")
    if agree == "N":
        break
    elif agree == "Y":
        count += 1
        for i in char_of_product:
            val = input(f"Введи значение {i}: ")
            product.update({i: val})
            # final_val.append(product.get(i))
            # final_dict = {i: final_val}
        tuple_tuple = (count, product)
        base.append(tuple_tuple)
        # final_final_dict.update(final_dict)



    else:
        print("Не сюда тебе надо...")

print(base)
#print(final_final_dict)
'''

'''
goods = []
features = {"название": "", "цена": "", "количество": "", "удиница измерений": ""}
analitics = {"название": [], "цена": [], "количество": [], "удиница измерений": []}
num = 0
while True:
    if input("Для выхода введите Q -> Enter, для продолжения - Enter").upper() == "Q":
        break
    num += 1
    for f in features.keys():
        fet = input(f"Введите значение свойства '{f}': ")  # Ввод свойства
        features[f] = int(fet) if f in {"цена", "количество"} else fet # меняем тип
        analitics[f].append(features[f]) # Добавляем свойство в список товаров
    goods.append((num, deepcopy(features)))
    print(f"\n Текущая структура товаров: \т {'*' * 30}")
    for good in goods:
        print(good)
    print(f"\n Текущая аналитика по товарам: \т {'*' * 30}")
    for key, value in analitics.items():
        print(f"{key[:25]:>30}:{value}")
    print("*" * 30)

'''

products = []
index = 0
name_spec = input("Введите через пробел, какие характиристики товаров вы будете указывать: ").split()
specifications = dict()

while True:
    user_answer = input("Чтобы создать новый товар введите + \nЧтобы перейти к аналитике введите 'Q': ")
    if user_answer == '+':
        for i in range(len(name_spec)):
            specifications.update({name_spec[i]: input(f"Введите {name_spec[i]} товара: ")})
    elif user_answer == 'Q':
        break
    index += 1
    new_product = (index, specifications)
    products.append(new_product)

analytics = {}
for product in products:
    for key, value in product[1].items():
        if key in analytics:
            analytics[key].append(value)
        else:
            analytics[key] = [value]

while True:
    user_answer = input(f"Чтобы закончить работу введите Q \n Введите характеристику товара, по которой вы хотите увидеть данные {name_spec}: ")
    if user_answer == 'Q':
        print("Работа окончена")
        break
    user_answer = user_answer.lower()
    print(user_answer, analytics.get(user_answer))