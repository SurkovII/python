# Напишите программу, удаляющую из текста все слова, содержащие "абв"

txt = 'абв абв2 абв авыпв абвб валпв аааа ыф'

def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

print(del_some_words(txt))

