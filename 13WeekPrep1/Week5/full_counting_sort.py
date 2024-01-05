def countSort(arr):
    # Write your code here
    result_set = len({sublist[0] for sublist in arr})
    lst = [[] for _ in range(result_set + 1)]

    for i in range(len(arr) // 2):
        arr[i][1] = '-'

    for i in range(len(arr)):
        item = arr[i]
        lst[int(item[0])].append(item[1])

    res = [word for row in lst for word in row]

    print(' '.join(res))