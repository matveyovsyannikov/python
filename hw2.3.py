period_dict = dict(Winter=[12, 1, 2],
                   Spring=[3, 4, 5],
                   Summer=[6, 7, 8],
                   Fall=[9, 10, 11])
num = int(input('Type month number: '))
for key, value in period_dict.items():
    if num in value:
        print(f"{num} - {key}")