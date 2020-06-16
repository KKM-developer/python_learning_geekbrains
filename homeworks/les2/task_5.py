list_numb = [7, 5, 3, 3, 2]

print(list_numb)

while True:
    user_add = input('Введите целое натуральное число ')
    try:
        user_add = abs(int(user_add))
        if user_add == 0:
            print(user_add, 'не натуральное число')
            continue
        else:
            list_numb.append(user_add)
            list_numb.sort()
            list_numb.reverse()
        break
    except ValueError:
        print('это не число')
        continue

print(list_numb)