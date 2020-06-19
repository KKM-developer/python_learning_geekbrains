import sys


def summ_numb(numbers):
    res_summ = 0
    list_numb = numbers.split(' ')
    try:
        list_numb = list(map(int, list_numb))
        print(list_numb)
        for i in list_numb:
            res_summ += i
    except ValueError:
        if list_numb[-1] == 'q':
            try:
                list_numb = list(map(int, list_numb[:-1]))
                print(list_numb)
                for i in list_numb:
                    res_summ += i
                print(last_summ + res_summ)
                sys.exit()
            except ValueError:
                print('где-то вы ошиблись')
        else:
            print('где-то вы ошиблись')

    return res_summ


last_summ = 0
while True:
    user_numb = input('Введите числа для суммирования, разделяя их пробелами, для выхода введите "q" ')
    if user_numb == 'q':
        break
    else:
        result = summ_numb(user_numb)
        print(last_summ + result)
        last_summ += result
