min_dinst = input('Сколько километров Вы можете пробежать в первый день? ')
improve = input('На сколько процентов Вы можете улучшать свой пезультат каждый день? ')
max_dinst = input('Какого результата Вы хотите достичь? ')


while not (min_dinst.isdigit() and improve.isdigit() and max_dinst.isdigit()):
    print('Где-то Вы ошиблись. Вы должны вводить числы')
    min_dinst = input('Сколько километров Вы можете пробежать в первый день? ')
    improve = input('На сколько процентов Вы можете улучшать свой пезультат каждый день? ')
    max_dinst = input('Какого результата Вы хотите достичь? ')

day = 1
min_dinst = float(min_dinst)
max_dinst = float(max_dinst)
improve = float(improve)
result = '{}-й день Вы пробежите {} километров'.format(day, min_dinst)
print(result)
while min_dinst <= max_dinst:
    day += 1
    min_dinst = round(min_dinst + (min_dinst * (improve / 100)), 2)
    result = '{}-й день Вы пробежите {} километров'.format(day, min_dinst)
    print(result)