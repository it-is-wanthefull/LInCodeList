import sys
import heapq

max_heap = []
heapq.heapify(max_heap)

t = int(sys.stdin.readline().strip())

for i in range(t):
    command = int(sys.stdin.readline().strip())
    if command > 0:
        heapq.heappush(max_heap, command)
    else: #command == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(max_heap))