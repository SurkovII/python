# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# Пример
# 45 -> 101101

def decimalToBin(n):
    listBin = []
    while n > 0:
        listBin.append(n % 2)
        n //= 2
    return listBin[::-1]       #reverse

srt = str(decimalToBin(6)).replace(',', "").replace(' ', "").replace('[', "").replace(']', "")
print(srt)
