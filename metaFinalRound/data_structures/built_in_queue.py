import queue
from collections import deque

my_queue = queue.Queue(maxsize=10)

my_queue.put(19)
my_queue.put(13)
my_queue.put(40)
my_queue.put(88)
my_queue.put(71)
print(my_queue)

print(my_queue.get())
print(my_queue.get())



my_queue = deque()
my_queue.append(19)
my_queue.append(13)
my_queue.append(40)
my_queue.append(88)
my_queue.append(71)
print(my_queue)

first = my_queue.popleft()
print(first)
