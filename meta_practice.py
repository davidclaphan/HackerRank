from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    additional_diners = 0

    for i in range(1, N + 1):

        if i in S:
            continue

        left = True
        right = True

        # check left
        for l in range(i - K, i):
            if l < 1:
                continue

            if l in S:
                left = False
                break

        # check right
        for r in range(i + 1, i + K + 1):
            if r > N:
                break

            if r in S:
                right = False
                break

        if left is True and right is True:
            additional_diners += 1
            S.append(i)

    print(S)
    return additional_diners


N = 10
K = 1
M = 2
S = [2, 6]

print(getMaxAdditionalDinersCount(N, K, M, S))

N = 15
K = 2
M = 3
S = [11, 6, 14]

print(getMaxAdditionalDinersCount(N, K, M, S))