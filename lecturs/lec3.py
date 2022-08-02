# Анонимные, lambda функции
def sum(x):     #sum = lambda x: x+10
 return x+10
def mult(x):    #mult = lambda x: x**2
 return x**2
sum(mult(2))    
def sum1(x):    #sum1 = lambda x: x+22
 return x+22
def mult2(x):   #mult2 = lambda x: x**3
 return x**3
sum1(mult2(2))
def sum3(x):    #sum4 = lambda x: x+242
 return x+242
def mult4(x):   #mult4 = lambda x: x**5
 return x**5
sum3(mult2(2))



# f(g(x))
def h(f, g, x): return f(g(x))h = lambda f, g, x: f(g(x))
h(sum, mult, 5)
h(lambda x: x+10, lambda x: x**2, 5)
