funk = input('Введите выражение через пробел ')


def calculator(funk):
    arr = funk.split(" ")
    x1 = float(arr[0])
    x2 = arr[1]
    x3 = float(arr[2])
    if x2 == '+':
        return (x1 + x3)
    elif x2 == '-':
        return (x1 - x3)
    elif x2 == '/':
        if x3 != 0:
            return (x1 / x3)
        else:
            return ("Ошибка, делить на 0 нельзя")
    elif x2 == '*':
        return (x1 * x3)
    elif x2 == 'mod':
        return (x1 % x3)
    elif x2 == 'pov':
        return (x1 ** x3)
    elif x2 == 'div':
        return (x1 // x3)

print(calculator(funk))