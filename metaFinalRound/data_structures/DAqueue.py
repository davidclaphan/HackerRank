
class QUEUE:
    def __init__(self):
        self._queue = []
        self._size = 0

    def push(self, value) -> None:
        """

        :param value:
        :return:
        """
        self._queue.append(value)
        self._size += 1

    def pop(self) -> any:
        popped_val = self._queue.pop()
        self._size -= 1
        return popped_val

    def peek(self) -> any:
        """

        :return:
        """
        return self._queue[-1]

    def is_empty(self) -> bool:
        """

        :return:
        """
        if self._size == 0:
            return True

        else:
            return False

    def find(self, value) -> bool:
        for ele in self._queue:
            if ele == value:
                return True

        return False

    def get_size(self) -> int:
        """

        :return:
        """
        return self._size

    def print_queue(self) -> None:
        for i in range(-1, (self._size + 1) * -1, -1):
            print(self._queue[i])


if __name__ == "__main__":

    my_queue = QUEUE()

    my_queue.push(10)
    my_queue.push(12)
    print("Size should be 2:")
    print(my_queue.get_size())
    print()
    print("Look at the queue")
    my_queue.print_queue()
    print()

    print("Value should be 12:")
    print(my_queue.peek())
    print()
    print("Add some Values...")
    my_queue.push(88)
    my_queue.push(71)
    my_queue.push(93)
    my_queue.push(17)
    print()
    print("Look at the queue")
    my_queue.print_queue()

    print()
    print("Size should be 6:")
    print(my_queue.get_size())
    print()

    print("Pop a value...")
    print()
    my_queue.pop()
    print("Top value should be 93:")
    print(my_queue.peek())
    print()
    print("Size should be 5:")
    print(my_queue.get_size())
