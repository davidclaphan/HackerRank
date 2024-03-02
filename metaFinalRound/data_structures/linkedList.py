from llist import sllist, sllistnode, dllist, dllistnode

lst = dllist()

node1 = dllistnode(1)
node2 = dllistnode(2)
node3 = dllistnode(5)

lst.append(node1)
lst.append(node2)
lst.append(node3)


lst.append(7)
print("Here is the dlist:", lst)
print("The head is:", lst.first)
print("The tail is:", lst.last, "\n")

node = lst.first
while node is not None:
    print("Next node:", node.next)
    print("Previous node:", node.prev)
    node = node.next


print("This is the end of the file.")