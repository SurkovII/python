# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = (input('Введите натуральное число N '))

def search(N):
    sp = []
    minNum =2
    while N > 1:
        if (N % minNum == 0):
            sp.append(minNum)
            N = (N/minNum)
        else:
            minNum +=1 
    return sp


try:
    N = int(N)
    print(search(N))

except:
    print('Необходимо ввести натуральное число ')