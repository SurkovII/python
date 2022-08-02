# задайте список из вещественных чисел. Напишите программу, которая найдет разницу между максимальным и минимальным значением дробной части элкментов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01]

input = [1.1, 1.2, 3.1, 10.01]

def fun(list):
    listNew = []
    for i in list:
        listNew.append(round(i-int(i),2))
    return max(listNew) - min(listNew)

print(fun(input))