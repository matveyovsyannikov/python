def my_func(x, y):
    res = x**y
    return res


def my_func2(x, y):
    res = 1
    while y < 0:
        res = res/x
        y = y+1
    return res


print(my_func(2, -2))
print(my_func2(2, -2))
