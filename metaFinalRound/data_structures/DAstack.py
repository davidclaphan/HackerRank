class DAStack:
    def __init__(self):
        self._stack = []
        self._size = 0

    def push(self, value) -> None:
        """

        :param value:
        :return:
        """
        self._stack.append(value)
        self._size += 1

    def pop(self) -> None:
        """

        :return:
        """
        self._stack.pop()
        self._size -= 1

    def peek(self) -> None:
        """

        :return:
        """
        return self._stack[-1]

    def size(self) -> int:
        """

        :return:
        """
        return self._size

    def is_empty(self) -> bool:
        """

        :return:
        """
        if self._size == 0:
            return True
        else:
            return False

    def find_value(self, value) -> bool:
        """

        :param value:
        :return:
        """
        for node in self._stack:
            if node == value:
                return True

        return False

    def print_stack(self) -> None:
        """
        :return:
        """
        print("-- TOP OF STACK --")
        for i in range(-1, ((self._size + 1) * -1), -1):
            print(self._stack[i])
        print("-- BOTTOM OF STACK -- \n")


if __name__ == "__main__":
    print("***********START TESTS***********\n")

    llStack = DAStack()
    print("ADD 9")
    llStack.push(9)
    llStack.print_stack()
    print("ADD 6")
    llStack.push(6)
    llStack.print_stack()
    print("The size should be 2:")
    print(llStack.size(), "\n")

    print("ADD 11")
    llStack.push(11)

    llStack.print_stack()

    print("Peek the top value, should be 11:")
    print(llStack.peek(), "\n")
    llStack.pop()

    print("The size should be 2:")
    print(llStack.size(), "\n")

    print("Peek the top value, should be 6:")
    print(llStack.peek(), "\n")

    print("***********END TESTS***********")