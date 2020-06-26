'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

with open('task_4.txt', 'r', encoding='UTF-8') as file:
    line = file.readlines()
    line = [l.rstrip() for l in line]
    with open('task_4_ru.txt', 'w', encoding='UTF-8') as ru_file:
        for i in line:
            words = i.split(' ')
            if words[0] == 'One':
                ru_file.write(f'Один {words[1]} {words[2]} \n')
            elif words[0] == 'Two':
                ru_file.write(f'Два {words[1]} {words[2]}\n')
            elif words[0] == 'Three':
                ru_file.write(f'Три {words[1]} {words[2]}\n')
            elif words[0] == 'Four':
                ru_file.write(f'Четыре {words[1]} {words[2]}')
