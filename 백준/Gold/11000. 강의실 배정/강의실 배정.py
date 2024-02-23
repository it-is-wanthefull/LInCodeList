from heapq import heapify, heappop, heappush
from sys import stdin
input = stdin.readline

class_list = []
class_q = []
heapify(class_q)

n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    class_list.append([start, end])
class_list.sort()

for i in range(n):
    start, end = class_list[i]
    if len(class_q) == 0:
        heappush(class_q, [end, start])
        continue

    popped = heappop(class_q)
    if popped[0] <= start:
        heappush(class_q, [end, start])
    else:
        heappush(class_q, [end, start])
        heappush(class_q, popped)

print(len(class_q))