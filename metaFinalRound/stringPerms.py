

def perms(S: str, B: str):
    i = 0
    S_dict = {}
    output = []

    for val in S:
        if val in S_dict:
            S_dict[val] += 1
        else:
            S_dict[val] = 1

    while i < (len(B) - len(S)):
        sub = B[i: i + len(S)]
        perm = {}
        for j in sub:
            if j in perm:
                perm[j] += 1
            else:
                perm[j] = 1


        if perm == S_dict:
            output.append(sub)

        i += 1

    return output

S = 'abbc'
B = 'babcabcbebbacbabab'

print(perms(S, B))