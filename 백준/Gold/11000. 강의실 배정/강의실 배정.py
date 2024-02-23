from heapq import heapify, heappop, heappush
from sys import stdin
input = stdin.readline


n = int(input())
class_list = [list(map(int, input().split())) for _ in range(n)]
class_list.sort()
class_q = []
heapify(class_q)

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