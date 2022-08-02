# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # a запись, w перезапись, r считать 
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()

# import hello

# print(hello.f(1))


# import hello as h

# print(h.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5))
# print(new_string('!')) # Возьмет по умолчанию
# print(new_string(4))


# def concatenatio(*params):
#     res: str = ""           # Строка
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1'))


# def concatenatio(*params):
#     res: int = 0        # res = 0          # Число
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1, 5, 6, 8))

    
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n -2)
    
# list = []
# for e in range(1, 10):
#     list.append(fib(e))

# print(list)

# Картеж - неизменяемый список. Обязательна запятая

# a = (3, 4)
# print(a)
# print(a[1])
# # a[0] = 12 Нельзя

# a = (2, 4, 6)
# for item in a:
#     print(item)
    
    
# t= tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print(type(t))
# print('r: {} g: {} b: {}'.format(red, green, blue))


# Словари

# dictionary = {}
# dictionary = \
#     {
#         'up': 'W',
#         'left': '<',
#         'down': 's',
#         'right': '>'
#     }
    
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys():
#     print(k)
# for k in dictionary.values():
#     print(k)
# for v in dictionary:
#     print(dictionary[v])

# dictionary['up'] = 'up'
# print(dictionary)

# dictionary['back'] = 'op'
# print(dictionary)

# del dictionary['left']
# print(dictionary)

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
    
# Множества

# colors = {'red', 'green', 'blue'}

# print(type(colors))
# print(colors)

# colors.add('red')
# print(colors)
# colors.add('grey')
# print(colors)

# colors.remove('blue')   # Если элемента нет, будет ошибка
# print(colors)

# colors.discard('red')   # Если элемента нет, все будет ок
# print(colors)

# colors.clear()
# print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# c = a.copy()            # c = {1, 2, 3, 5, 8}
# u = a.union(b)          # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)   # i = {8, 2, 5}
# dl = a.difference(b)    # dl = {1, 2}
# dr = b.difference(a)    # dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
    
# print(q)    # q = {1, 21, 3, 13}


# s = frozenset(a)  # НЕизменяемое множесто

# Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# # for e in list1:
# #     print(e)
    
# # print()

# # for e in list2:
# #     print(e)
    
# list1[0] = 121
# list2[2] = 33

# for e in list1:
#     print(e)
    
# print()

# for e in list2:
#     print(e)

list1 = [1, 2, 3, 4, 5]


print(len(list1))
print(list1.pop())  # Удаление последнего аргумента
print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)

list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1.pop(2))  # Удаление выбранного аргумента
print(list1)

list1 = [1, 2, 3, 4, 5]
print(list1)
list1.insert(2, 11) # Вставка выбранного аргумента по индексу
print(list1)

list1 = [1, 2, 3, 4, 5]
print(list1)
list1.append(11)
print(list1)