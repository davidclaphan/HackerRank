import llist


class LLStack:
    def __init__(self, single_or_double):
        if single_or_double == "single":
            self._linked_list = llist.sllist([])
        else:
            self._linked_list = llist.dllist([])

        self._size = 0

    def push(self, value) -> None:
        """

        :param value:
        :return:
        """
        self._linked_list.appendleft(value)
        self._size += 1

    def pop(self) -> None:
        """

        :return:
        """
        self._linked_list.popleft()
        self._size -= 1

    def peek(self) -> None:
        """

        :return:
        """
        return self._linked_list.first()

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
        for node in self._linked_list:
            if node == value:
                return True

        return False

    def print_stack(self) -> None:
        """
        :return:
        """
        print("-- TOP OF STACK --")
        for node in self._linked_list:
            print(node)
        print("-- BOTTOM OF STACK -- \n")


if __name__ == "__main__":
    print("***********START TESTS***********\n")

    llStack = LLStack("single")
    print("ADD 7")
    llStack.push(7)
    llStack.print_stack()
    print("ADD 5")
    llStack.push(5)
    llStack.print_stack()
    print("The size should be 2:")
    print(llStack.size(), "\n")

    print("ADD 4")
    llStack.push(4)

    llStack.print_stack()

    print("Peek the top value, should be 4:")
    print(llStack.peek(), "\n")
    llStack.pop()

    print("Peek the top value, should be 5:")
    print(llStack.peek(), "\n")

    print("***********END TESTS***********")


