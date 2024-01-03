"""
Query: 1 x y
Let idx = ((x^last_answer) % n)
Append the integer y to arr[idx]

Query: 2 x y
Let idx = ((x^last_answer) % n)
Assign the value arr[idx][y % size(arr[idx])] to last_answer
Store the new value of last_answer to an answers array.
"""

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    n = n
    last_answer = 0
    answers = []
    for query in queries:
        x = query[1]
        y = query[2]

        idx = ((x ^ last_answer) % n)

        if query[0] == 1:
            arr[idx].append(y)

        else:
            last_answer = arr[idx][y % len(arr[idx])]
            answers.append(last_answer)

    return answers




input = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]

print(dynamicArray(2, input))