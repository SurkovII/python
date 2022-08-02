# Задайте два числа. Напишите программу, которая найдет НОК(наименьшее общее кратное) этих двух чисел

# import numbers
# import math

# number1, number2 = int(input('Введите первое число ')), int(
#     input('Введите второе число '))
# print(math.lcm(number1, number2))


# def lcm2(a, b):
#     m = a*b
#     while a != 0 and b != 0:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#     return m//(a+b)


# try:
#     print('Введите два числа ')
#     num1 = float(input())
#     num2 = float(input())
#     print(lcm2(num1, num2))

# except:
#     print('Ошибка! Повторите ввод! ')


a= int(input('Введите первое число '))
b= int(input('Введите второе число '))

def gcd(a, b):
    if (a < b):
        (a, b) = (b, a)
    return gcd(b, a%b) if b != 0 else a

def lcm2(a,b):
    return a/gcd(a,b)*b

print(lcm2(a, b))