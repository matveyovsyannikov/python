num = int(input('Type positive number: '))
maxdigit = 0
while num > 0:
    digit = num % 10
    num = num//10
    if digit>maxdigit:
        maxdigit=digit
print('Max digit = ', maxdigit)
