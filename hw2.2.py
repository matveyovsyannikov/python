li = list(input('Type new list: '))
i = 0
while i < len(li)-1:
    li[i], li[i+1] = li[i+1], li[i]
    i = i+2
print(li)
