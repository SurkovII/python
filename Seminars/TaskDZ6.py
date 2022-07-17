# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите вещественное число ')


def sum(number):
    summ = 0
    for i in number:
        if (i != '.' and i != '-'):
            summ = summ + int(i)
    return summ


print(sum(number))
