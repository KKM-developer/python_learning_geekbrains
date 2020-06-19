user_input = input('Введите список данных, разделя значения пробелом ')

user_list = []
for i in user_input.split(' '):
    b = i.strip()
    if len(b) > 11:
        user_list.append(b[:10])
    else:
        user_list.append(b)

print(user_list)

for ind, el in enumerate(user_list, 1):
    print(ind, el)
