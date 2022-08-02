# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# Крестики нолики




def func():
    UserMsg = 'Ошибка! Введите число "0" или "x": '
    add = (input('Ходите: '))
    if add =='0' or add == 'x':
        return add
    else:
        print(UserMsg, end='')
        return func

def NameUser(userNum = ''):
    User = input(userNum+'Введите свое имя: ')
    return User
User1 = NameUser('Игрок 1 ')
User2 = NameUser('Игрок 2 ')
print(User1)
print(User2)

# print('Введите координаты: ')
# a,b = map(int(input(), input()))
# def func2(a, b):
#     pole = ['', '', ''],['', '', ''],['', '', '']
#     for i in range(0, len(pole)):
#         for i2 in range(0, len(pole[i])):

