# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не зватает одного, чтобы выполнилось условие A[i]-1 = A[i-1]. Найдите это число


data = open('file3.txt', 'r')
lst = list(data.read().split())
data.close()
print(type(lst))
print(lst)
# lst = [1, 2, 3, 6]

last = lst[len(lst)-1]
print(last)

lst2 = []
for i in range(1, (int(last)+1)):
    lst2.append(i)

print((lst2))

result = list(sorted(set(str(lst2)) - set(str(lst))))
print(result)
