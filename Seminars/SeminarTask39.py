text = 'dddddddddddkfffpfffffp'

def sets(text):
    lists = [text[i] for i in range(len(text))]
    analyse = ''
    count = 1
    for i in range(len(lists)-1):
        if lists[i] == lists[i+1]:
            count +=1
        else:
            analyse += str(count) + lists[i]
            count = 1
    if count > 1 or (lists[len(lists)-2] != lists[-1]):
        analyse += str(count) + lists[-1]
    return analyse
print(sets(text))