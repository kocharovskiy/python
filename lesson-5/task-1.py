"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

my_list = []
while True:
    line = input("Введите текст: ")
    if line == '':
        print(my_list)
        break
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("task_1.txt", "w") as f:
        f.writelines(my_list)