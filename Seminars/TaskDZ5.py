# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A(3, 6); B(2, 1) -> 5,09
# A(7, -5); B(1, -1) -> 7,21


from turtle import distance


def fillKoord(x):
    xy = ['X', 'Y']
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f'Введите координату по {xy[i]}: '))
                a.append(number)
                is_OK = True
            except:
                print('Необходимо ввести целое число')
    return a

def calculateLength(a, b):
    lengthAB = ((b[0] - a[0])**2 + (b[1] - a[1])**2)**(0.5)
    return lengthAB

print('Введите координат точки А ')
pointA = fillKoord(2)
print('Введите координат точки B ')
pointB = fillKoord(2)
distance = int(calculateLength(pointA, pointB)*100)/100
print(f'Длина отрезка {distance}')