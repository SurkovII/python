# Напишите программу, которая найдет произведение пар чисел списка. Парой считается первый и последний элемент, и тд
# Пример:
#     [2, 3, 4, 5, 6]  => [12, 15, 16]

inputList = [2, 3, 4, 5, 6, 8]
def multiNumbers(list):
    multi = []
    res = 0
    
    if len(list) % 2 == 0:
        for i in range(0, round(len(list)/2)):
            res = list[i]*list[len(list) - i - 1]
            multi.append(res)
    else:
        for i in range(0, round((len(list)/2))+1):
            res = list[i]*list[len(list) - i -1]
            multi.append(res)
    return multi

print(multiNumbers(inputList))
