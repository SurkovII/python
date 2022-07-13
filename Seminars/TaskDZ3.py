# Напишите программу для проверки истинности утверждения ¬(X v Y v Z) = ¬X ^ ¬Y ^ ¬Z для всех значений предикат



def predict(x, y, z):
    if not (x or y or z) == ((not (x)) and (not (y)) and (not (z))):
        return(True)
    else:
        return(False)
x = input('Введите X ')
y = input('Введите Y ')
z = input('Введите Z ')

print(predict(x, y, z))