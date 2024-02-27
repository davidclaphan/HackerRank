

my_stack = []

want_to_stack = [3, 6, 10, 1, 7, 2, 5]


for val in want_to_stack:
    my_stack.append(val)
    print("The stack is growing:", my_stack)


print("The stack is full:", my_stack, "\n")

while len(my_stack) > 0:
    my_stack.pop()
    print("Popped a value:", my_stack)
