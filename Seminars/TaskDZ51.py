# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
# то в итоге будет, 3*x^3 + 12*x^2+10*x+66

data = open('TaskDZ51_1.txt', 'r')
lst = (data.read().split('+'))
data.close()

data2 = open('TaskDZ51_2.txt', 'r')
lst2 = (data2.read().split('+'))
data2.close()
result = (list(lst2)) + list(lst)

def listPolynomials(result):
    for i in range(len(result)):
        if 'x' in result[i] and '^' not in result[i] and '*' not in result[i]:
            result[i] = '1*x^1'
        elif 'x' in result[i] and '^' not in result[i]:
            result[i] = result[i].replace('x', 'x^1')
        elif 'x^' in result[i] and '*' not in result[i]:
            result[i] = result[i].replace('x', '1*x')
        elif 'x' not in result[i]:
            result[i] = f'{result[i]}*x^0'
    return result

def polynomOut(sum):
    index = []
    row = []
    for i in sum:
        if 'x^' in i:
            index.append(i[:i.find("*x^")])
            row.append(i[i.find("^")+1:])
    row1 = int(max(row))
    result = 0
    INu = []
    j = 0
    while j <= row1:
        for i in range(0, len(row)):
            if int(row[i]) == row1:
                result += int(index[i])
        INu.append(f'{result}*x^{row1}')
        result = 0
        row1 -= 1
    return INu
       
def outPolinom(Out):
    return " + ".join(Out) + " = 0"

Out = polynomOut(listPolynomials(result))
text = outPolinom(Out).replace('*x^0', '').replace('1*x', 'x').replace('x^1', 'x')

data3 = open('TaskDZ51_3.txt', 'w')
data3.writelines(text)
data3.close()