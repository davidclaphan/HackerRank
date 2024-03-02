import llist

llst = llist.sllist()

# appendleft == enqueue
llst.appendleft(8)
print(llst.first)
llst.appendleft(15)
print(llst.first)
llst.appendleft(100)
print(llst.first)

print(llst)

# pop == dequeue
first_up = llst.pop()
print(first_up)

print(llst)

llst.append(15)
llst.append(175)
second_up = llst.pop()

llst.append(10)
