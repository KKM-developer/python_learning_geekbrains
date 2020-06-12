profit = input('Введите выручку  ')
loss = input('Введите издержки ')
while not (profit.isdigit() and loss.isdigit()):
    print('Вы ввели не число')
    profit = input('Введите выручку  ')
    loss = input('Введите издержки ')
profit = int(profit)
loss = int(loss)
if profit > loss:
    print('Компания работает в плюс')
    rent = (profit - loss) / profit
    print('Рентабельность фирмы ', rent)
    employee = input('Введите количество сотрудников ')
    while not employee.isdigit():
        print('Вы ввели не число')
        employee = input('Введите количество сотрудников ')
    employee = int(employee)
    result = profit / employee
    print('Прибыль фирмы в расчете на одного сотрудника ', result)
elif profit == loss:
    print('Компания работает в ноль')
else:
    print('Компания работает в убыток')