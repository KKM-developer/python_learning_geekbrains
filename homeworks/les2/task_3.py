month = input('Введите месяц ')
while not month.isdigit():
    print('Введите числом')
    month = input('Введите месяц ')
time_year = ['зима', 'весна', 'лето', 'осень']
month = int(month)
if month == 12 or month < 3:
    print('сейчас', time_year[0])
elif 2 < month < 6:
    print('сейчас', time_year[1])
elif 5 < month < 9:
    print('сейчас', time_year[2])
elif 8 < month < 12:
    print('сейчас', time_year[3])

time_year_dict = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}
for name_time in time_year_dict.keys():
    if month in time_year_dict[name_time]:
        print('сейчас', name_time)



