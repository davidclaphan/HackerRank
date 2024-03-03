import random
mylist = [random.randint(1,10000) for i in range(1000)]
mylist.sort()

test_list = [2, 3, 4, 10, 40, 45, 60, 100, 120, 123, 190, 500, 545, 1000, 1234, 1521]


def binary_search(arr, value):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (high + low) // 2

        # if target is greater, ignore left half
        if arr[mid] < value:
            low = mid + 1

        # if target is smaller, ignore right half
        elif arr[mid] > value:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    return -1



print("@ Index:", binary_search(test_list, 10))
print("@ Index:", binary_search(test_list, 25))
print("@ Index:", binary_search(test_list, 1234))
print("@ Index:", binary_search(test_list, 101))

print("Test for 192 in random lists:")
tests = 1
outcome = -1
while outcome == -1:
    mylist = [random.randint(1, 99999) for i in range(100)]
    mylist.sort()
    outcome = binary_search(mylist, 192)
    tests += 1

    if tests % 100 == 0:
        print("100 tests and counting...")

print("Number 192 found after", tests, "tests!")
