# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def findWeekDay(number):
    if (number > 5 and number < 8):
        print('Да')
    elif (number >= 8 or number <= 0):
        print('Введите число от 1 до 7')
    else:
        print('Нет')


number = input('Введите цифру ')
try:
    number = int(number)
    findWeekDay(number)
except:
    print('Необходимо ввести целое число ')
