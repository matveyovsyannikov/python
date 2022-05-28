my_list = [7, 5, 3, 3, 2]
new_el = int(input('Type new rating: '))
i = 0
for el in my_list:
    if el < new_el:
        my_list.insert(i, new_el)
        print(my_list)
        break
    elif new_el <= my_list[-1]:
        my_list.append(new_el)
        print(my_list)
        break
    else:
        i = i+1
