"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

def summary():
    with open('task-5.txt', 'w+') as f:
        line = input('Введите цифры через пробел: ')
        f.writelines(line)
        my_numb = line.split()

        print(sum(map(int, my_numb)))

summary()