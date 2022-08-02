# Задайте строку из набора чисел.Напишите программу, которая покажет большее и меньшее число. В качестве разделителя изп пробел

# n = '1 23 4 36 688 765'

# list = n.split(' ')

# for i in list:
#     i = int(i)
    
# print(list)
# max = max(list)
# min = min(list)

# print(list)
# print(f'max - {max} min - {min}')
# print(type(list[0]))

# Другое решение

n = '1 23 4 36 688 765'
list = [int(s) for s in n.split()]
print(list)
max = max(list)
min = min(list)

print(list)
print(f'max - {max} min - {min}')
print(type(list[0]))