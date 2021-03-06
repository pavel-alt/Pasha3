# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_data(name, surname, yb, city, mail, phone):
    return f"{name} {surname} {yb} {city} {mail} {phone}"


print(user_data(name="Pavel", surname="Altukhov", yb="1986", city="SPb", mail="jfv@hmgc.ru", phone="89315822159"))
