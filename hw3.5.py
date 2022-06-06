def calc():
    res = 0
    while True:
        st = input('Type numbers with space(for end type q): ')
        li = st.split(' ')
        for el in li:
            if el == 'q':
                return print(res)
            try:
                res = res + int(el)
            except ValueError:
                print('use only numbers or q')
        print(f'Result: {res}')


calc()

