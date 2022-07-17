

import random
xComp = random.randint(1,3)
print(xComp)

xUser = input('Введите К или Н или Б ')
def userChoise(xUser):
    if xUser == "К":
        xUserNumber = 1
    elif xUser == "Н":
        xUserNumber = 2
    elif xUser == "Б":
        xUserNumber = 3
    return xUserNumber

print(userChoise(xUser))

