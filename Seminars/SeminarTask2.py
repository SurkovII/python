N = int(input('Введите размер последовательности'))

def Row(a):
    for i in range(0, a):
        b = (-3)**i
        print(b, end = " ")

Row(N)
print()
