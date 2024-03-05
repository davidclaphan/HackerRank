from llist import sllist

llst = sllist()

# appendleft == enqueue
llst.appendleft(8)
print(llst.first.value)
llst.appendleft(15)
print(llst.first.value)
llst.appendleft(100)
print(llst.first.value)

print(llst)

# pop == dequeue
first_up = llst.pop()
print(first_up)

print(llst)

llst.append(15)
llst.append(175)
second_up = llst.pop()

llst.append(10)
