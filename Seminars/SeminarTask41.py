# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,. приоритет операций стандартный.
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;


# form = input('Введите выражение ')
form ='223-22+6'
form1 = form.split('2')
print(form1)
array = []
text = str(form)
print(text)
for i in text:
    array.append(i)
print(array)
print(type(array))
result = ''
for k in range(len(array)-1):
    if array[k] == ("+" or "-"):
        print(k)
        for j in range(0, k):
            result += array[j]
print(result)





numbers = [i for i in form if i.isdigit]
print(numbers)
print(type(numbers))


import re

a = '1+6-88/3'

listNumb = re.split('\+|\-|\*|\/', form)

print(listNumb)
print(type(listNumb))