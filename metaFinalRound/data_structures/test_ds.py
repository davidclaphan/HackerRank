

list = [1, 2, 3, 4, 1, 6, 7, 8, 1]

for val in list:
    new_list = list[:]
    new_list.remove(val)
    print(val)
    print(new_list)