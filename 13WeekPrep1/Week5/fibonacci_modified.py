def fibonacciModified(t1, t2, n):
    # Write your code here

    dict = {1: t1, 2: t2}
    i = 3
    while n not in dict:
        dict[i] = dict[i - 1] ** 2 + dict[i - 2]
        i += 1

    return dict[n]


print(fibonacciModified(0, 1, 10))