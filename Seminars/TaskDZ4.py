#  Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)


numberQuarted = input('Введите номер четверти ')


def searchDiapazon(number):
    if number == 1:
        print(f'В четверти {number} x > 0, y > 0')
    elif number == 2:
        print(f'В четверти {number} x < 0, y > 0')
    elif number == 3:
        print(f'В четверти {number} x < 0, y < 0')
    elif number == 4:
        print(f'В четверти {number} x > 0, y < 0')
    else:
        print('Четвертей всего 4')


try:
    numberQuarted = int(numberQuarted)
    searchDiapazon(numberQuarted)
except:
    print('Необходимо ввести целое число')
