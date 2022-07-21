# Задайте список из n чисел ряда фибоначи выведите на экран ряд

# number = int(input('Введите число фибоначи '))

def fibonacci(number):
    if number in [1,2]:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)

# list = []
# print(fibonacci(number))
# for i in range(1, number+1):
#     list.append(fibonacci(i))
# print(list)

x = int(input('Введите число фибоначи '))
def fibolist(x):
    list = []
    for i in range(1, x+1):
        list.append(fibonacci(i))
    return list
print(fibolist(x))
