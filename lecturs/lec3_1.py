# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(g(4))
# print(f(4))


# def calc(x):
#     return x*10
# print(calc(10))

# def math(op, x):    # op -  Операция
#     print(op(x))


# math(calc, 20)



from ast import comprehension


def sum(x, y):
    return x+y

#f = sum
f = lambda q, w: q+w

def mylt(x, y):
    return x*y

def calc(op, a, b):
    print(op(a,b))
    
calc(f, 4, 5)

calc(lambda q, w: q+w, 5, 6)

# list comprehension

list = []
for i in range(1,101):
    if (i%2==0):
        list.append(i)

print(list)

list = [i for i in range(1,21) if i%2==0]
print(list)

def f(x):
    return x**3

list = [(f(i), i) for i in range(1,21) if i%2==0]
print(list)

