var_int = 15
var_float = 1.25
var_str1 = 'Hello '
var_str2 = 'world'

print(var_str1 + var_str2)

print(type(var_int), var_int)
print(type(var_float), var_float)
print(type(var_str1), var_str1)

user_input = str(input('Введите переменную. "Строку", "Целое число", "Число с плавающей запятой" '))

try:
    int(user_input)
    print('Вы ввели целое число ', user_input)
except ValueError:
    try:
        float(user_input)
        print('Вы ввели число с плавающей запятой ', user_input)
    except ValueError:
        print('Вы ввели строку ', user_input)
