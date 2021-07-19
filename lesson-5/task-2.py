"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""


with open('task-2.txt', 'r') as f:
    my_list = f.readlines()
print(f'Количество строк в файле {len(my_list)}\n')

with open('task-2.txt', 'r') as f:
    my_list = f.readlines()
    for i in range(len(my_list)):
        list_1 = my_list[i].split()
        print(f'В {i + 1}-ой строке {len(list_1)} слова')