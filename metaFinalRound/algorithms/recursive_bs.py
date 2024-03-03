import random

def binary_search(arr, target, low, high):

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)

        else:
            return binary_search(arr, target, mid + 1, high)

    return -1

test_list = [2, 3, 4, 10, 40, 45, 60, 100, 120, 123, 190, 500, 545, 1000, 1234, 1521]

print("@ Index:", binary_search(test_list, 10, 0, len(test_list) - 1))
print("@ Index:", binary_search(test_list, 25, 0, len(test_list) - 1))
print("@ Index:", binary_search(test_list, 1234, 0, len(test_list) - 1))
print("@ Index:", binary_search(test_list, 101, 0, len(test_list) - 1))

print("Test for 192 in random lists:")
tests = 1
outcome = -1
while outcome == -1:
    mylist = [random.randint(1, 99999) for i in range(100)]
    mylist.sort()
    outcome = binary_search(mylist, 192, 0, len(mylist) - 1)
    tests += 1

    if tests % 100 == 0:
        print("100 tests and counting...")

print("Number 192 found after", tests, "tests!")