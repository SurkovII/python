# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import numbers


number = [1, 2, 3, 4, 4, 1, 0, 8, 5, 6, 7, 8, 0, 8, 4]
# unique_numbers = list(set(numbers))
# print(unique_numbers)
# result = []
# for i in number:
#     if number.count(i) ==1:

#         result.append(i)
# print(result)

def func(list):
    return [x for x in list if list.count(x) == 1]
print(func(number))

