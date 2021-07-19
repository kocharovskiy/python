"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл."""

import json
profit = {}
dict_1 = {}
prof = 0
average_profit = 0
i = 0
with open('task-7.txt', 'r') as f:
    for line in f:
        name, form, revenue, expenses = line.split()
        profit[name] = int(revenue) - int(expenses)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
        average_profit = prof / i

    dict_1 = {'Средняя прибыль': round(average_profit)}
    profit.update(dict_1)
    print(f'Прибыль каждой компании: {profit}')

with open('task-7.json', 'w') as j:
    json.dump(profit, j)

    js_str = json.dumps(profit)
    print(f'Файл json: {js_str}')