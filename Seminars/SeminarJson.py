from encodings import utf_8_sig
import json

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

with open('data.json' , 'w', encoding='utf_8') as fh:   #Открываем файл на запись
            fh.write(json.dumps(res, ensure_ascii=False))   # Преобразуем словарь data в unicode-строку и записываем в файл
print('БД успешно сохранена')

with open('data.json' , 'r', encoding='utf_8') as fh:   #Открываем файл для чтения
            BD = json.load(fh)   # Загружаем данные из файла
print('БД успешно сохранена2')
print(BD)