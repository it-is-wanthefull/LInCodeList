from heapq import heapify, heappop, heappush
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    files_q = list(map(int, input().split()))
    heapify(files_q)
    ans = 0

    for _ in range(n-1):
        merged_file = heappop(files_q) + heappop(files_q)
        ans += merged_file
        heappush(files_q, merged_file)

    print(ans)