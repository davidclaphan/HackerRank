import heapq

my_heap = [10, 7, 9, 15, 25, 100, 71, 19, 13, 41, 40, 72]
print(my_heap)

print("Heapify List")
heapq.heapify(my_heap)
print(my_heap)

def heapsort(heap):
    output = []
    for value in heap:
        heapq.heappush(output, value)
    return [heapq.heappop(output) for i in range(len(output))]


sorted_heap = heapsort((my_heap))
print("Heapsort?")
print(sorted_heap)

