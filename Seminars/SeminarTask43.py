lst = list(map(int, input('Введите числа через пробел: \n').split()))
def return_uniq(lst):
    return [i for i in lst if lst.count(i) == 1 ]
print(return_uniq(lst))