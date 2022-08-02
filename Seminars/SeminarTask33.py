# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен.
# Пример:
# k = 2 => 2*x2+ 4*x + 5 = 0

import random

step = int(input('Введите степень многочлена '))
def NewList(k):
    numbers = []
    for i in range(k+1):
        numbers.append(random.randint(0, 100))
    return numbers

print(NewList(step))

