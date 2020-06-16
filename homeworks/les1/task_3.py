while True:
    user_number = str(input('Введите целое чило '))
    try:
        int(user_number)
        break
    except ValueError:
        print('Это не целое число')

number_2 = user_number * 2
number_3 = user_number * 3

answer = int(user_number) + int(number_2) + int(number_3)

print('Результат вычисления ', answer)
