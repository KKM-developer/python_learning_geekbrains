user_list = []
user_inp = input('Введите элемент списка, если хотите выйти введите "Exit" ')
while True:
    if user_inp.lower() == 'exit':
        break
    else:
        user_list.append(user_inp)
        user_inp = input('Введите элемент списка, если хотите выйти введите "Exit" ')

print(user_list)
change_list = []
for i in range(len(user_list)):
    try:
        if i % 2 == 0:
            change_list.append(user_list[i+1])
            change_list.append(user_list[i])
    except IndexError:
        change_list.append(i+1)


print(change_list)