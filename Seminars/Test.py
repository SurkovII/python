def Factorial(value):
    print('[',end='')# За скобки прошу прощения, использовал чиcто для визуализации
    result=1
    if value==0 or value==1:
        return print('1',end=']')
    else:
        for i in range(1,(value+1)):
            result*=i
            print(f'{result}',end='')
            if i!=value: print(', ',end='')
    print(']',end='')
def PrintFactorial(value):
    print(' (',end='')
    printMulti=''
    if value==0: print('1',end='')
    for i in range(1,(value+1)):
        printMulti=f'{printMulti}*{i}'
        print(f'{printMulti[1:]}',end='')
        if i!=value: print(', ',end='')
    print(')',end='')
try:
    number=int(input('Введите число: '))
    print(f'Пусть N = {number}, тогда ',end='')
    Factorial(number)
    PrintFactorial(number)
except:
    print('Ощибка! Введено не целочисленное значение!')