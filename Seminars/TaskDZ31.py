# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

x = str(input('Введите искомый элемент '))

sp = list(input('Введите список ').split())
def searchElement(x, sp):
    if x in sp:
        return 'Есть'
    else:
        return 'Искомого числа в списке нет'
print(sp)
print(searchElement(x, sp))

