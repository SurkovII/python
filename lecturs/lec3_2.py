# В файле хранятся числа, нужно выбрать четные и составить список пар(число, квадрат числа)


from platform import libc_ver


path = 'F:/python/lecturs/file.txt'
f = open(path, 'r')
data = f.read() + ' '  # разделили пробелом
f.close
print(data)
numbers = []

while data != '':
    spase_pos = data.index(' ')
    numbers.append(int(data[:spase_pos]))
    data = data[spase_pos+1:]

out = []

for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)
print()




def select(f, col):                 #Функция преобразования в инт
    return [f(x) for x in col]


def where(f, col):                  #Функция для фильтрации по условию
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x**2), res)
print(res)
print()

# Функция map

li = [x for x in range(1,20)]
print(li)
li = list(map(lambda x:x+10, li))     #Необходимо преобразовать в лист
print(li)

#data = list(map(int, input().split()))  #(',')

data = list(map(int, '1 2 5 7 8'.split()))

for e in data:
    print(e)

print('--')     # Повторится, если будет стоять лист 52 строка
     
for e in data:
    print(e)


# Без селекта

def where(f, col):                  #Функция для фильтрации по условию
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
print()



# Фуенкция фильтр

data = [x for x in range(10)]

res = list(filter(lambda x: not x%2, data))
print(res)


# Без where

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
print()

#Функция zip
# Применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных

zip ([1, 2, 3], ['o', 'p', 'f'], ['п', 'л', 'д'])
print(list(zip([1, 2, 3], ['o', 'p', 'f'], ['п', 'л', 'д'])))

#Обрабатывает по минимальному набору

# Функция enumerate - пронумерует все элементы и выдаст кортежи

users = ['User1', 'User2', 'User3', 'User4','User5']

print(list(enumerate(users)))