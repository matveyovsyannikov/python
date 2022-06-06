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


def int_func2(string):
    words = string.split(' ')
    n_words = []
    for elm in words:
        if int_func(elm) == 'Type word only with small letters':
            return 'Type words only with small letters'
        else:
            n_words.append(int_func(elm))
    return ' '.join(n_words)


string = (input('Type words with small latin letters using space: '))
print(int_func2(string))