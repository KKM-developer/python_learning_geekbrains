while True:
    sec = str(input('Введите время в секундах '))

    try:
        int(sec)
        break
    except ValueError:
        print('Введите данные с помощью цифр')

hour = int(sec) // 3600
min = (int(sec) - hour * 3600) // 60
sec = int(sec) - hour * 3600 - min * 60
print(hour, ':', min, ':', sec)
