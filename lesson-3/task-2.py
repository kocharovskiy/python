"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

def inf(name, surname, year, city, email, phone):
    return [name, surname, year, city, email, phone]

print(inf(name='Denis', surname='Koch', year='1990', city='Moscow', email='mail@mail.ru', phone='12345'))