def int_func(st):
    letters = []
    for el in st:
        if 96 < ord(el) < 123:
            letters.append(el)
        else:
            return 'Type word only with small letters'
    if len(letters) == len(st):
        letters[0] = chr(ord(letters[0])-32)
        return ''.join(letters)


st = input('Type word with small latin letters: ')
print(int_func(st))
