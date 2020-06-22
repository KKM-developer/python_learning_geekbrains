"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from sys import argv
from itertools import count, cycle

tools = argv[1]

if tools == 'a':
    try:
        numb_count = argv[2]
        user_list = []
        for el in count(int(numb_count)):
            if el > 15:
                break
            else:
                user_list.append(el)
        print(user_list)
    except IndexError:
        print('Нет параметра')

if tools == 'b':
    try:
        numb_cycle = argv[2]
        user_list = []
        cyc_count = 0
        for el in cycle('123'):
            if cyc_count > int(numb_cycle):
                break
            user_list.append(el)
            cyc_count += 1
        print(user_list)
    except IndexError:
        print('Нет параметра')