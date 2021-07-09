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