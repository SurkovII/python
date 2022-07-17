# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def multiplicationN(number):
    print('[', end='')
    multi = 1
    for i in range(1, number+1):
        multi = multi*i
        print(multi, end='')
        if i != number:
            print(', ', end='')
    print(']')

try:
    number = int(input('Введите число N '))
    multiplicationN(number)
except:
    print('Ошибка! Необходимо ввести целое число')
