def sansaXor(arr):
    n = len(arr)
    if n % 2 == 0:
        return 0
    res = 0
    for i in range(n):
        if i % 2 == 0:
            res = res ^ arr[i]
    return res