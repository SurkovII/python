sp = [5,11,2,3,4,8,157,555]
def max_aver(sp):
    sr = 0
    max = sp[0]
    for i in sp:
        if i > max:
            max = i
        sr +=i
    sr = sr/len(sp)     #Список


    # print(max, sr)
    rez = {}            #Словарь
    rez['максимальный элемент'] = max
    rez['Среднее арифм'] = sr   

    k = (max, sr, rez)       #Кортеж
    return k
    
    
res = max_aver(sp)

print(res)
print(res[2])
for x,y in res[2].items():
    print(x,y)


# print(k[0])
# print(rez)
# print(len(rez))

# for x,y in rez.items():
#     print(x,y)
