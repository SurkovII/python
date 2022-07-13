# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
# Примеры:
# 1, 4, 6, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

'''
def maxNumber(a):
    maximum = a[0]
    for i in a:
        if (maximum < i):
            maximum = i
    return maximum

ls = list(input('Введите массив - '))
print (f'{maxNumber(ls)}')
'''
x1 = input('Введите первое число ')

try:
    x1 =(int (x1))
except:
    print('Необходимо ввести целое число')