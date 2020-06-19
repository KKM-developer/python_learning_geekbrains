def max_summ(a, b, c):
    list_numb = [a, b, c]
    list_numb.sort()
    return list_numb[1] + list_numb[2]


print(max_summ(5, 337, 8))