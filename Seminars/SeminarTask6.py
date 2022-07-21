# Создать словарь и вывести в файл ответ
N = 5


def inisp(N):
    sp = []
    for i in range(1, N+1):
        sp.append(round((1+1/i)**i, 2))
    return sp


def inib(sp):
    bib = {}
    max = sp[0]
    idmax = 0
    min = sp[0]
    idmin = 0
    sum = 0
    for i in range(len(sp)):
        if (max < sp[i]):
            max = sp[i]
            idmax = i
        if (min > sp[i]):
            min = sp[i]
            idmin = i
        sum += sp[i]
    sred = sum/len(sp)
    bib['max'] = max
    bib['idmax'] = idmax
    bib['min'] = min
    bib['idmin'] = idmin
    bib['sred'] = sred
    return bib


spisok = inisp(N)
bibl = {}
print(spisok)
bibl = inib(spisok)
print(bibl)
file = open('file1.txt', 'a')
for a,b in bibl.items():
    file.write(f'{a} - {b} ')
file.write('\n')
file.close()
