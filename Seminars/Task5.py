# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30

def multiplicity(number):
    if ((number % 5 == 0 and number % 10 == 0) or (number % 15 == 0)) and not number % 30 == 0:
        print('Да')
    else:
        print('Нет')


number = input('Введите число ')
try:
    number = int(number)
    print(multiplicity(number))
except:
    print('Введите целое число')
 