

def mystery(a, b):
    x = a
    y = b

    while x != y:
        if x > y:
            x = x-y

        if x < y:
            y = y-x

    return x



print(mystery(2437, 875))