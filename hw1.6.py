revenue = int(input('Type your company revenue: '))
cost = int(input('Type your company cost: '))
result = revenue - cost
if result > 0:
    print('You have profit: ', result)
else:
    print('You have loss: ', result)
