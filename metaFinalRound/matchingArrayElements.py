

def matching_elements(array1: list, array2: list):
    values_1 = {}
    values_2 = {}
    counter = 0

    for val in array1:
        if val in values_1:
            values_1[val] += 1
        else:
            values_1[val] = 1

    for val in array2:
        if val in values_2:
            values_2[val] += 1
        else:
            values_2[val] = 1

    for val in array1:
        if val in values_1 and val in values_2:
            counter += 1

    return counter



list1 = [1, 3, 5, 17, 18, 19, 35, 60]
list2 = [3, 5, 6, 17, 30, 60]


print(matching_elements(list1, list2))
