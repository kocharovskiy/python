"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка."""


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter: '))
                self.my_list.append(val)
                print(f'Текущий список: {self.my_list}')
            except:
                print(f"Ошибка! Введите только числа.")
                popitka = input(f'Для продолжения "Y", для выхода "N": ')

                if popitka == 'Y' or popitka == 'y' or popitka == 'н' or popitka == 'Н':
                    print(try_except.my_input())
                elif popitka == 'N' or popitka == 'n' or popitka == 'т' or popitka == 'Т':
                    return f'Конец'
                else:
                    return f'Конец'

try_except = Error(1)
print(try_except.my_input())