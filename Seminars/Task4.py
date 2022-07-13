# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

def firstFloatNumber(x):
    result = abs(x*10)
    result = int(result)
    result = result % 10
    return result


number = input('Введите число ')
try:
    number = float(number)
    print(firstFloatNumber(number))
except:
    print('Введите дробное число')
    