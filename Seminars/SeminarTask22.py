# Задайте число. Составьте список Фибоначи, в том числе для отрицательных индексов.
# Пример:
# для к = 8 список [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, ...]

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n == -1:
#         return -1
#     else:
#         return (fibonacci(n+1)+ fibonacci(n+2))

# for i in range(-8, 1):
#     print(f'{fibonacci(i)}', end=' ')

def fibo(n):
    fibo_list = list()
    fibo_list.append(0)
    fibo_list.append(1)

    for i in range(2, n+1):
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2])

    fibo_list.insert(0, 1)
    fibo_list.insert(0, -1)

    for i in range(0, n-2):
        fibo_list.insert(0, (fibo_list[1] - fibo_list[0]))
    return fibo_list


print(fibo(10))
