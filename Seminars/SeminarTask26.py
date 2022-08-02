from random import *


sp = [1, 6.8, 8, 11, 'sdgdf', True]


def shuffle(sp):
    for i in range(25):
        buff = 0
        x = randint(0, len(sp)-1)
        y = randint(0, len(sp)-1)
        buff = sp[x]
        sp[x] = sp[y]
        sp[y] = buff
    return sp

shuffled = shuffle(sp)
print(shuffled)