'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('task_3.txt', 'r', encoding='UTF-8') as file:
    line = file.readlines()
    line = [l.rstrip() for l in line]
    print(line)
    average = 0
    people_count = 0
    for i in line:
        people = i.split(' ')
        if int(people[1]) < 20000:
            print(f'{people[0]} получает меньше 20 000 руб')
        average += int(people[1])
        people_count += 1
    result = average / people_count
    print(f'Средняя величина дохода сотрудников равна {result}')

