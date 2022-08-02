# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не зватает одного, чтобы выполнилось условие A[i]-1 = A[i-1]. Найдите это число



# data = open('file3.txt', 'r')
# lst = list(data.read().split())
# lst = [1, 2, 3, 6]
# print(list)

def func(line):
    new_list = []
    for i in range(1, len(lst)):
        if lst[i] - 1 != lst[i-1]:
            new_list.append(lst[i]-1)
    return new_list

lst = [i for i in range(20) if i%2!=0]
res = []
with open ('task35.txt', 'r') as f:
    for line in f:
        res.append(func(line))
# with open('result', 'a') 


# print(new_list)
