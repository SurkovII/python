# Задайте список из N элементов, заполненых числами из промежутка [-N, N]. Сохраните список в формате json.

import json

a = int(input('Введите число N '))


def Nprint(x):
    lis = list(range(-x, x+1))
    return lis


Nprint(a)

with open('Task17.json', 'w', encoding='utf_8') as fh:  # Открываем файл на запись
    # Преобразуем словарь data в unicode-строку и записываем в файл
    fh.write(json.dumps(Nprint(a), ensure_ascii=False))
print('файл json успешно записан')
file = open('Task17.txt', 'w')
file.write(str(Nprint(a)))
file.write('\n')
file.close()
print('файл txt успешно записан')
