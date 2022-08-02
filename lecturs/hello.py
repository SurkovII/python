# Типы данных справедливы
# int, float, boolean, str
# list и др


# value = None
# a = 123
# b = 1.23

# print(type(a))
# print(type(b))
# print(type(value))
# value = 123334

# print(type(value))

# s = "hello world"     # '""  \' использование ' в тексте  \n переход нановую строку

# print(s)    # Вывод стоки
# print(a,'-' , b, "-", s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a, b, s))
# f = True
# print(f)

# list = [1,2,3]
# print(list)
# list = ['1', '2', '3', 'hello world', 1, 2, True ]
# print(list)
# col = ['1', '2', '3', 'hello world', 1, 2, True ] # Нельзя допускать ненужный пробел
# print(col)

# print('Введите a')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print(f'{b} {a}')
# print('{} - {}'.format(a, b))
# print(a,' + ', b, ' =  ', a+b)

# print('Введите a')
# a = int (input())
# print('Введите b')
# b =int( input())
# print(a, b)
# print(f'{b} {a}')
# print('{} - {}'.format(a, b))
# print(a,' + ', b, ' =  ', a+b)

# print('Введите a')
# a = float (input())
# print('Введите b')
# b = float (input())
# print(a, b)
# print(f'{b} {a}')
# print('{} - {}'.format(a, b))
# print(a,' + ', b, ' =  ', a+b)



# a = 1.3
# b = 3
# c = a * b  # // целые числа  ** возведение в степень
# print(c)

# a = 1.313253
# b = 3
# c =round (a * b, 5)  
# print(c)

# a = 3
# a = a * 5     # a +=5  a *= 5
# print(a)

# # not and or не путать с & | ^
# # is, is not, in, not in

# a = 1 > 4 and 5>2
# print(a)

# a = 1 > 4 or 5>2
# print(a)

# a = 1 != 4 
# print(a)

# a = 'qwe'
# b = 'qwe'

# print(a==b)
# a = [1, 2]      #list
# b = [1, 2]

# print(a==b)

# a = 1 < 3 < 5 < 6 < 10
# print(a)

# func = 1
# T = 4
# x = 2

# print(func<T>x)

# f = 1>2 or 4<6
# print(f)

# f = [1,2,3,2]
# print(f)
# print(2 in f)

# f = [1,2,3,2]
# print(f)
# print(not 2 in f)

# is_Odd = not f[0] % 2   # is_Odd = f[0] % 2 ==0
# print(is_Odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)



# username = input('Ввыедите имя ')
# if username  == 'Маша':
#     print('Ура, это Маша')
# elif username == 'Марина':
#     print('Здарова, Марина!')
# elif username == 'Ильнар':
#     print('Илнарушка')
# else:
#     print('Привет,', username,'!')

# orig = 23
# inverted = 0

# while orig !=0:
#     inverted = inverted * 10 + (orig % 10)
#     orig //= 10
# print(inverted)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
