
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.head = None
        self.size = 0


    def insert(self, node):

        if self.head is None:
            self.head = node

        else:
            prev = None
            current = self.head
            while current is not None:

                # move left
                if node.value < current.value:
                    prev = current
                    current = current.left

                # move right
                elif node.value > current.value:
                    prev = current
                    current = current.right

            node.parent = prev
            if node.parent.value < node.value:
                node.parent.right = node

            else:
                node.parent.left = node

            self.size += 1


def preOrder(node):
    if node is not None:
        print(node.value)
        preOrder(node.left)
        preOrder(node.right)


def inOrder(node):
    if node is not None:
        inOrder(node.left)
        print(node.value)
        inOrder(node.right)

def postOrder(node):
    if node is not None:
        postOrder(node.left)
        postOrder(node.right)
        print(node.value)


def inOrderPlusOne(node):
    if node is not None:
        inOrderPlusOne(node.left)
        node.value += 1
        inOrderPlusOne(node.right)


node1 = Node(64)
node2 = Node(32)
node3 = Node(80)
node4 = Node(48)
node5 = Node(16)
node6 = Node(72)
node7 = Node(88)
nodeList = [node1, node2, node3, node4, node5, node6, node7, Node(56), Node(84), Node(96)]
myTree = BST()
for node in nodeList:
    myTree.insert(node)

print("Start In-Order")
inOrder(myTree.head)

print("\nStart Pre-Order")
preOrder(myTree.head)

print("\nStart Post-Order")
postOrder(myTree.head)

print("\nLet's add 1 to each node")
inOrderPlusOne(myTree.head)
inOrder(myTree.head)