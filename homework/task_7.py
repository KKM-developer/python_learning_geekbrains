'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json

result = {}
with open('task_7.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        key, _, *value = line.split()
        result[key] = value
profit = {'average_profit': 0}
total = {}
for key in result:
    total[key] = int(result[key][0]) - int(result[key][1])
for key, value in total.items():
    profit['average_profit'] += int(value)

with open('task_7_result.json', 'w', encoding='UTF-8') as res_file:
    json.dump(total, res_file)
    json.dump(', ', res_file)
    json.dump(profit, res_file)