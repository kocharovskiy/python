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