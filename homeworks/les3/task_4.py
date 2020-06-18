def deg(x, y):
    return x ** y


def cycle_deg(x, y):
    y = abs(y)
    result = x
    for i in range(y - 1):
        result *= x
    return 1 / result


print(deg(5, -3))
print(cycle_deg(5, -3))