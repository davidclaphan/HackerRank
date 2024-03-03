from collections import deque


my_stack = deque()

my_stack.append(1)
my_stack.append(7)
my_stack.append(10)

print(my_stack.pop())  # 10
print(my_stack.pop())  # 7