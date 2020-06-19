def dell(div, split):
    return div / split


a = input('Введите дилимое ')
b = input('Введите делитель ')

try:
    a = float(a)
    b = float(b)
    print(dell(a, b))
except ValueError:
    print('Вы ввели не число')
except ZeroDivisionError:
    print('На 0 делить нельзя')