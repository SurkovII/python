from math import sqrt


a = 5
b = 5
c = 1
discr = (b**2-4*a*c)
if discr > 0:
    x1 = (-b + sqrt(discr))/(2*a)
    x2 = (-b - sqrt(discr))/(2*a)
    print(f'x1 = {x1}, x2 = {x2}')
elif discr ==0:
    x = -b/(a*2)
    print(x)
else:
    print('Корней нет')

    