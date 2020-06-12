chek_max = 0

user_numb = input('Введите число  ')
while not user_numb.isdigit():
    print('Это не число')
    user_numb = input('Введите число  ')

for i in user_numb:
    i = int(i)
    if i > chek_max:
        chek_max = i

result = 'Максимальное число в числе {} это {}'.format(user_numb, chek_max)

print(result)