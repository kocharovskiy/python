# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print('Task 1')
list_1 = [1, 'строка', 'true', 4.0]
print(f'Мой список: {list_1}')

for i in list_1:
    print(f'Элемент "{i}" имеет тип данных: {type(i)}')

print('_________________________________')

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('Task 2')
list_1 = []
list_1 = input("Введите значение списка, разделённых пробелом: ").split()
if len(list_1) % 2 == 0:
    i = 0
    while i < len(list_1):
        el = list_1[i]
        list_1[i] = list_1[i+1]
        list_1[i+1] = el
        i += 2
else:
    i = 0
    while i < len(list_1) - 1:
        el = list_1[i]
        list_1[i] = list_1[i + 1]
        list_1[i + 1] = el
        i += 2
print(list_1)

print('_________________________________')

#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

print('Task 3')
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

mth = int(input('Введите месяц в виде числа от 1 до 12: '))

if mth ==1 or mth == 12 or mth == 2:
        print(season_dict.get(1))
        print(season_list[0])
elif mth ==3 or mth == 4 or mth == 5:
        print(season_dict.get(2))
        print(season_list[1])
elif mth ==5 or mth == 7 or mth == 8:
        print(season_dict.get(3))
        print(season_list[2])
elif mth ==9 or mth == 10 or mth == 11:
        print(season_dict.get(4))
        print(season_list[3])

print('_________________________________')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

print('Task 4')
str_1 = input('Введите несколько слов через пробел: ')
for i, el in enumerate(str_1.split(' '), 1):
    if len(el) > 10:
        el = el[0:10]
    print(i, el)

print('_________________________________')

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

print('Task 5')
my_list = [7, 4, 3, 2]

number = int(input("Введите номер рейтинга: "))
a = my_list.count(number)
for el in my_list:
    if a > 0:
        i = my_list.index(number)
        my_list.insert(i+a, number)
        break
    else:
        if number > el:
            b = my_list.index(el)
            my_list.insert(b, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

print('_________________________________')

#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.

print('Task 6')
goods = []
while True:
    number = input("Введите номер товара. Для выхода - '0': ")
    if number == '0':
        break
    prod_inf = {}
    while input("Для заполнения информации по товару нажмите '1', для ввода номера товара '0' ") == '1':
        prod_name = input("Введите название товара: ")
        prod_price = input("Введите цену товара: ")
        prod_inf[prod_name] = prod_price
    goods.append(tuple([number, prod_inf]))

print(goods)

analitica = {}
for good in goods:
    for prod_name, prod_price in good[1].items():
        if prod_name in analitica:
            analitica[prod_name].append(prod_price)
        else:
         analitica[prod_name] = [prod_price]

print(analitica)

print('_________________________________')
