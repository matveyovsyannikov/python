def div_func(a, b):
    try:
        res = a/b
    except ZeroDivisionError:
        return 'b should not be 0'
    return res


a = int(input('Type a: '))
b = int(input('Type b: '))
print(div_func(a, b))
