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