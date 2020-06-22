""""
    1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу:
    (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
    значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

name_script, hour, rate, premium = argv
wage = 0
try:
    wage = int(hour) * int(rate) + int(premium)
    print(f'Сотрудник за {hour} часов работы, со ставкой {rate}руб/час, и премией {premium}руб., получит {wage}руб.')
except ValueError:
    print('Запустите скрипт еще раз и введите параметры цифрами\n1) Отработанное время, ч.\n2) Ставка, руб/час\n3) '
          'Премия, руб.')
