'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
with open('task_5.txt', 'w', encoding='UTF-8') as file:
    file.write('29 52 92 257 51 26 2 361 24 628')

with open('task_5.txt', 'r', encoding='UTF-8') as r_file:
    numbers = r_file.read()
    numbers = numbers.split(' ')
    print(numbers)
    result = 0
    for number in numbers:
        result += int(number)
    print(result)
